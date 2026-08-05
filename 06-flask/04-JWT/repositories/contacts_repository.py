from sqlalchemy import select
from sqlalchemy.orm import selectinload
from repositories.base_repository import BaseRepository
from database.models import Contact

class ContactsRepository(BaseRepository):

    model = Contact

    REQUIRED_FIELDS = {
        "name",
        "phone",
        "email"
    }

    ALLOWED_FIELDS = {
        "name",
        "phone",
        "email",
        "entry_date"
    }


    def insert_contact(self, data: dict):

        try:

            self._validate_dict(data)
            self._validate_required_fields(data, self.REQUIRED_FIELDS)
            self._validate_allowed_fields(data, self.ALLOWED_FIELDS)

            contact = Contact(**data)

            self.session.add(contact)
            self._commit()
            self._refresh(contact)

            return contact
        
        except Exception:
            raise

    def get_contacts_by_user(self, user_id: int):
        statement = (
            select(Contact)
            .where(Contact.user_id == user_id)
            .order_by(Contact.entry_date.desc())
        )

        return self.session.scalars(statement).all()

    def get_contact_by_id(self, contact_id: int):

        try:

            return self._get_by_id(contact_id)

        except Exception:
            raise


    def update_contact(self, contact_id: int, data: dict):

        self._validate_dict(data)

        self._validate_allowed_fields(
            data,
            self.ALLOWED_FIELDS
        )

        contact = self._get_by_id(contact_id)

        for field, value in data.items():
            setattr(contact, field, value)

        self._commit()

        self._refresh(contact)

        return contact

    def delete_contact(self, contact_id: int):

        contact = self._get_by_id(contact_id)

        self.session.delete(contact)

        self._commit()

        return {
            "message": f"Contact '{contact.name}' deleted successfully."
        }

    def get_all_contacts(self):

        statement = (
            select(Contact)
            .order_by(Contact.id)
        )

        return self.session.scalars(statement).all()