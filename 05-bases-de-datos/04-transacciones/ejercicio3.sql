DO $$
DECLARE
    v_bill_id INTEGER := 1;      -- Invoice to be returned
    v_status VARCHAR(20);        -- Current invoice status

    rec RECORD;                  -- Variable used to iterate through invoice items

BEGIN

    -- Retrieve invoice status
    SELECT status
    INTO v_status
    FROM bills
    WHERE id = v_bill_id;

    -- Verify that the invoice exists
    IF v_status IS NULL THEN
        RAISE EXCEPTION
            'Invoice % does not exist',
            v_bill_id;
    END IF;

    -- Verify that the invoice has not already
    -- been returned
    IF v_status = 'Returned' THEN
        RAISE EXCEPTION
            'Invoice % has already been returned',
            v_bill_id;
    END IF;

    -- Restore stock for each product included
    -- in the invoice
    FOR rec IN
        SELECT
            product_id,
            quantity
        FROM bill_details
        WHERE bill_id = v_bill_id
    LOOP

        UPDATE products
        SET stock = stock + rec.quantity
        WHERE id = rec.product_id;

    END LOOP;

    -- Update invoice status
    UPDATE bills
    SET status = 'Returned'
    WHERE id = v_bill_id;

    -- Display success message
    RAISE NOTICE
        'Return processed successfully for invoice %',
        v_bill_id;

END;
$$ LANGUAGE plpgsql;