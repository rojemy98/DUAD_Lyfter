DO $$
DECLARE
    v_bill_id INTEGER := 1;
    v_status VARCHAR(20);
    rec RECORD;
BEGIN

    -- Verify invoice exists
    IF NOT EXISTS (
        SELECT 1
        FROM bills
        WHERE id = v_bill_id
    ) THEN
        RAISE EXCEPTION 'Invoice % does not exist', v_bill_id;
    END IF;

    -- Verify invoice status
    SELECT status
    INTO v_status
    FROM bills
    WHERE id = v_bill_id;

    IF v_status <> 'Pending' THEN
        RAISE EXCEPTION
            'Invoice % cannot be cancelled because its status is %',
            v_bill_id,
            v_status;
    END IF;

    -- Restore stock only for products not delivered
    FOR rec IN
        SELECT product_id, quantity
        FROM bill_details
        WHERE bill_id = v_bill_id
          AND delivered = FALSE
    LOOP

        UPDATE products
        SET stock = stock + rec.quantity
        WHERE id = rec.product_id;

    END LOOP;

    -- Update invoice status
    UPDATE bills
    SET status = 'Cancelled'
    WHERE id = v_bill_id;

    RAISE NOTICE
        'Invoice % has been cancelled successfully',
        v_bill_id;

EXCEPTION
    WHEN OTHERS THEN
        RAISE EXCEPTION
            'Transaction failed. Cancellation rolled back. Error: %',
            SQLERRM;
END;
$$ LANGUAGE plpgsql;