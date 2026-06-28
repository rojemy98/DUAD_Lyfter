import traceback


def rollback(db_manager):
    """
    Rolls back the current database transaction and logs
    the exception traceback.

    Args:
        db_manager: Database manager instance.

    Returns:
        None
    """

    db_manager.rollback()

    traceback.print_exc()

    return None


def format_results(results, formatter):
    """
    Formats a list of database records using the provided
    formatter function.

    Args:
        results (list): Raw records returned from the database.
        formatter (callable): Function used to format each record.

    Returns:
        list: Formatted records.
    """

    return [
        formatter(result)
        for result in results
    ]