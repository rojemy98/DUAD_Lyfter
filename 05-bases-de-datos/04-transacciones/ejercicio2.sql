DO $$
DECLARE
    v_user_id INTEGER := 1;  -- purchasing user
    v_bill_id INTEGER;
    
    -- Product 1
    v_product1_id INTEGER := 1;
    v_qty1 INTEGER := 2;
    v_stock1 INTEGER;

    -- Product 2
    v_product2_id INTEGER := 2;
    v_qty2 INTEGER := 1;
    v_stock2 INTEGER;

BEGIN
    -- 1. Verify that the user exists
    IF NOT EXISTS (SELECT 1 FROM users WHERE id = v_user_id) THEN
        RAISE EXCEPTION 'User does not exist';
    END IF;

    -- 2. Validate stock for product 1
    SELECT stock INTO v_stock1
    FROM products
    WHERE id = v_product1_id;

    IF v_stock1 IS NULL OR v_stock1 < v_qty1 THEN
        RAISE EXCEPTION 'Insufficient stock for product %', v_product1_id;
    END IF;

    -- 3. Validate stock for product 2
    SELECT stock INTO v_stock2
    FROM products
    WHERE id = v_product2_id;

    IF v_stock2 IS NULL OR v_stock2 < v_qty2 THEN
        RAISE EXCEPTION 'Insufficient stock for product %', v_product2_id;
    END IF;

    -- 4. Create invoice
    INSERT INTO bills (user_id, bill_date)
    VALUES (v_user_id, NOW())
    RETURNING id INTO v_bill_id;

    -- 5. Insert invoice detail for product 1
    INSERT INTO bill_details (
        bill_id, product_id, quantity, unit_price, subtotal
    )
    SELECT
        v_bill_id,
        id,
        v_qty1,
        price,
        price * v_qty1
    FROM products
    WHERE id = v_product1_id;

    -- 6. Reduce stock for product 1
    UPDATE products
    SET stock = stock - v_qty1
    WHERE id = v_product1_id;

    -- 7. Insert invoice detail for product 2
    INSERT INTO bill_details (
        bill_id, product_id, quantity, unit_price, subtotal
    )
    SELECT
        v_bill_id,
        id,
        v_qty2,
        price,
        price * v_qty2
    FROM products
    WHERE id = v_product2_id;

    -- 8. Reduce stock for product 2
    UPDATE products
    SET stock = stock - v_qty2
    WHERE id = v_product2_id;

    RAISE NOTICE 'Purchase completed successfully. Invoice ID: %', v_bill_id;

END;
$$ LANGUAGE plpgsql;