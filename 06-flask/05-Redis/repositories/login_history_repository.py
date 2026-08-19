from sqlalchemy import select

from repositories.base_repository import BaseRepository
from database.models import LoginHistory


class LoginHistoryRepository(BaseRepository):

    model = LoginHistory

    def insert_login_history(
        self,
        user_id: int | None,
        ip_address: str,
        success: bool
    ):

        login_history = LoginHistory(
            user_id=user_id,
            ip_address=ip_address,
            success=success
        )

        self.session.add(login_history)

        self._commit()
        self._refresh(login_history)

        return login_history

    def get_all_login_history(self):

        statement = (
            select(LoginHistory)
            .order_by(
                LoginHistory.login_date.desc()
            )
        )

        return self.session.scalars(statement).all()