DO $$
DECLARE
    v_product_id INTEGER := 1;
    v_qty INTEGER := 1;

    v_stock INTEGER;
    v_version INTEGER;
    v_new_version INTEGER;
BEGIN

    -- 1. Leer stock y versión actual
    SELECT stock, version
    INTO v_stock, v_version
    FROM products
    WHERE id = v_product_id;

    -- 2. Validar stock suficiente
    IF v_stock < v_qty THEN
        RAISE EXCEPTION 'Insufficient stock for product %', v_product_id;
    END IF;

    -- 3. Intentar actualizar SOLO si la versión no cambió
    UPDATE products
    SET stock = stock - v_qty,
        version = version + 1
    WHERE id = v_product_id
      AND version = v_version
    RETURNING version INTO v_new_version;

    -- 4. Si no se actualizó ninguna fila → alguien lo modificó
    IF NOT FOUND THEN
        RAISE EXCEPTION
            'Concurrency conflict: product % was modified by another transaction',
            v_product_id;
    END IF;

    RAISE NOTICE
        'Purchase successful. New stock updated safely. Product %',
        v_product_id;

END;
$$ LANGUAGE plpgsql;