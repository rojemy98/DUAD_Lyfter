DO $$
DECLARE
    v_user_id INTEGER := 1;
    v_bill_id INTEGER;

    rec RECORD;
BEGIN

    -- Verify user exists
    IF NOT EXISTS (
        SELECT 1
        FROM users
        WHERE id = v_user_id
    ) THEN
        RAISE EXCEPTION 'User % does not exist', v_user_id;
    END IF;

    -- Validate stock for all requested products
    FOR rec IN
        SELECT *
        FROM (
            VALUES
                (1, 2),  -- product_id, quantity
                (2, 3),
                (3, 1)
        ) AS purchase_items(product_id, quantity)
    LOOP

        IF NOT EXISTS (
            SELECT 1
            FROM products
            WHERE id = rec.product_id
              AND stock >= rec.quantity
        ) THEN
            RAISE EXCEPTION
                'Insufficient stock for product %',
                rec.product_id;
        END IF;

    END LOOP;

    -- Create invoice
    INSERT INTO bills (
        user_id,
        bill_date,
        status
    )
    VALUES (
        v_user_id,
        NOW(),
        'Completed'
    )
    RETURNING id INTO v_bill_id;

    -- Insert invoice details and update stock
    FOR rec IN
        SELECT *
        FROM (
            VALUES
                (1, 2),
                (2, 3),
                (3, 1)
        ) AS purchase_items(product_id, quantity)
    LOOP

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

        UPDATE products
        SET stock = stock - rec.quantity
        WHERE id = rec.product_id;

    END LOOP;

    RAISE NOTICE
        'Purchase completed successfully. Invoice ID: %',
        v_bill_id;

EXCEPTION
    WHEN OTHERS THEN
        RAISE EXCEPTION
            'Transaction failed. All changes have been rolled back. Error: %',
            SQLERRM;
END;
$$ LANGUAGE plpgsql;