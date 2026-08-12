from sqlalchemy import select
from database.models import Contact
from repositories.base_repository import BaseRepository


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
        "email"
    }

    def insert_contact(self, user_id: int, data: dict):

        self._validate_dict(data)

        self._validate_required_fields(
            data,
            self.REQUIRED_FIELDS
        )

        self._validate_allowed_fields(
            data,
            self.ALLOWED_FIELDS
        )

        contact = Contact(
            user_id=user_id,
            **data
        )

        self.session.add(contact)

        self._commit()
        self._refresh(contact)

        return contact

    def get_contacts_by_user(self, user_id: int):

        statement = (
            select(Contact)
            .where(Contact.user_id == user_id)
            .order_by(Contact.id)
        )

        return self.session.scalars(statement).all()

    def get_contact_by_id(self, contact_id: int):

        return self._get_by_id(contact_id)

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

    def update_contact_by_user(
    self,
    contact_id: int,
    user_id: int,
    data: dict
    ):
        self._validate_dict(data)

        self._validate_allowed_fields(
            data,
            self.ALLOWED_FIELDS
        )

        statement = (
            select(Contact)
            .where(
                Contact.id == contact_id,
                Contact.user_id == user_id
            )
        )

        contact = self.session.scalar(statement)

        if contact is None:
            raise LookupError(
                f"Contact {contact_id} not found."
            )

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

    def delete_contact_by_user(self, contact_id: int, user_id: int):

        statement = (
            select(Contact)
            .where(
                Contact.id == contact_id,
                Contact.user_id == user_id
            )
        )

        contact = self.session.scalar(statement)

        if contact is None:
            raise LookupError(
                f"Contact {contact_id} not found."
            )

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