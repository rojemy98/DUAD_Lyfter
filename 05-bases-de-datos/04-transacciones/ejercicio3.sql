DO $$
DECLARE
    v_bill_id INTEGER := 1;
    v_status VARCHAR(20);
    v_exists BOOLEAN;
    rec RECORD;
BEGIN

    -- Verify invoice exists
    SELECT EXISTS (
        SELECT 1
        FROM bills
        WHERE id = v_bill_id
    )
    INTO v_exists;

    IF NOT v_exists THEN
        RAISE EXCEPTION 'Invoice % does not exist', v_bill_id;
    END IF;

    -- Verify invoice has not already been returned
    SELECT status
    INTO v_status
    FROM bills
    WHERE id = v_bill_id;

    IF v_status = 'Returned' THEN
        RAISE EXCEPTION 'Invoice % has already been returned', v_bill_id;
    END IF;

    -- Restore stock for all products in the invoice
    FOR rec IN
        SELECT product_id, quantity
        FROM bill_details
        WHERE bill_id = v_bill_id
    LOOP

        UPDATE products
        SET stock = stock + rec.quantity
        WHERE id = rec.product_id;

    END LOOP;

    -- Mark invoice as returned
    UPDATE bills
    SET status = 'Returned'
    WHERE id = v_bill_id;

    RAISE NOTICE 'Return processed successfully for invoice %', v_bill_id;

END;
$$ LANGUAGE plpgsql;