-- Temporary table to simulate a shopping cart
CREATE TEMP TABLE temp_purchase_items (
    product_id INTEGER,
    quantity INTEGER
);

-- Sample products to purchase
INSERT INTO temp_purchase_items VALUES
(1, 2),
(2, 1),
(3, 4);

DO $$
DECLARE
    v_user_id INTEGER := 1;      -- Purchasing user
    v_bill_id INTEGER;           -- Generated invoice ID

    rec RECORD;                  -- Variable used to iterate through products
    v_stock INTEGER;             -- Available stock for each product

BEGIN


    -- Verify that the user exists
    IF NOT EXISTS (
        SELECT 1
        FROM users
        WHERE id = v_user_id
    ) THEN
        RAISE EXCEPTION 'User % does not exist', v_user_id;
    END IF;

    -- Validate stock for all requested products
    FOR rec IN
        SELECT product_id, quantity
        FROM temp_purchase_items
    LOOP

        SELECT stock
        INTO v_stock
        FROM products
        WHERE id = rec.product_id;

        -- Verify that the product exists
        IF v_stock IS NULL THEN
            RAISE EXCEPTION
                'Product % does not exist',
                rec.product_id;
        END IF;

        -- Verify sufficient stock
        IF v_stock < rec.quantity THEN
            RAISE EXCEPTION
                'Insufficient stock for product %. Available: %, Requested: %',
                rec.product_id,
                v_stock,
                rec.quantity;
        END IF;

    END LOOP;

    -- Create the invoice
    INSERT INTO bills (
        user_id,
        bill_date
    )
    VALUES (
        v_user_id,
        NOW()
    )
    RETURNING id INTO v_bill_id;

    -- Insert invoice details and reduce stock
    FOR rec IN
        SELECT product_id, quantity
        FROM temp_purchase_items
    LOOP

        -- Insert invoice detail
        INSERT INTO bill_details (
            bill_id,
            product_id,
            quantity,
            unit_price,
            subtotal
        )
        SELECT
            v_bill_id,
            p.id,
            rec.quantity,
            p.price,
            p.price * rec.quantity
        FROM products p
        WHERE p.id = rec.product_id;

        -- Update product stock
        UPDATE products
        SET stock = stock - rec.quantity
        WHERE id = rec.product_id;

    END LOOP;

    -- Display success message
    RAISE NOTICE
        'Purchase completed successfully. Invoice ID: %',
        v_bill_id;

END;
$$ LANGUAGE plpgsql;