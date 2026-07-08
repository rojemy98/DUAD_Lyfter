from base_repository import BaseRepository
from models import Address

class AdressRepository(BaseRepository):

    model = Address

    REQUIRED_FIELDS = {
        "street",
        "city",
        "country",
        "user_id"
    }

    ALLOWED_FIELDS = {
        "street",
        "city",
        "country",
        "user_id"
    }

    def create_adress(self, data):

        self._validate_dict(data)

        self._validate_required_fields(data, self.REQUIRED_FIELDS)

        self._validate_allowed_fields(data, self.ALLOWED_FIELDS)

        new_entity = self.model(**data)

        self.session.add(new_entity)

        self._commit()

        self._refresh(new_entity)

        return new_entity
    
    def update_adress(self, adress_id, data):

        self._validate_dict(data)

        self._validate_allowed_fields(data, self.ALLOWED_FIELDS)

        adress = self._get_by_id(adress_id)

        for key, value in data.items():
            setattr(adress, key, value)

        self._commit()

        self._refresh(adress)

        return adress
    
    def delete_adress(self, adress_id):

        adress = self._get_by_id(adress_id)

        self.session.delete(adress)

        self._commit()