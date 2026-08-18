class BaseRepository:

    model = None

    def __init__(self, session):
        self.session = session

    def _validate_dict(self, data: dict):

        if not isinstance(data, dict):
            raise TypeError(
                "Data must be a dictionary."
            )
        
    def _validate_required_fields(self, data: dict, required_fields: set):

        missing_fields = required_fields - data.keys()

        if missing_fields:
            raise ValueError(
                f"Missing required fields: {missing_fields}"
            )
        
    def _validate_allowed_fields(self, data: dict, allowed_fields: set):

        invalid_fields = data.keys() - allowed_fields

        if invalid_fields:
            raise ValueError(
                f"Invalid fields: {invalid_fields}"
            )
        
    def _get_by_id(self, id: int):

        entity = self.session.get(self.model, id)

        if entity is None:
            raise LookupError(
                f"{self.model.__name__} {id} not found."
            )

        return entity
    
    def _commit(self):

        try:

            self.session.commit()

        except Exception:

            self.session.rollback()

            raise

    def _refresh(self, entity):

        self.session.refresh(entity)