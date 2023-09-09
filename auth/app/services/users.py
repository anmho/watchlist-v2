from enum import Enum
import sqlalchemy
from app.models.users.tables import User
from sqlalchemy.orm import Session
from app.utils.logger import LoggerFactory
from sqlalchemy.orm import sessionmaker


class UserCreationError(Exception):
    pass


class InvalidUserFieldsError(UserCreationError):
    pass


class UserUpdateError(Exception):
    pass


class RegistrationType(Enum):
    STANDARD = "standard"
    GOOGLE = "google"
    # ...
    # GITHUB = 3


class UserService:
    logger = LoggerFactory.create("UserService")

    @classmethod
    def get_users(cls, session: Session):
        try:
            users = session.query(User).all()
            return users
        except Exception as e:
            cls.logger.error(e)
            raise

    @classmethod
    def create_user(cls, email, password, session: sessionmaker[Session], registration_type: RegistrationType = RegistrationType.STANDARD) -> User:
        if registration_type == RegistrationType.STANDARD and password is None:
            raise ValueError("password required for standard registration")
        try:
            user = User(email=email, registration_type=registration_type.value)
            session.add(user)
            if registration_type == RegistrationType.STANDARD:
                user.set_password(password=password)
            session.add(user)
            session.commit()
            return user

        except sqlalchemy.exc.IntegrityError as e:
            cls.logger.error(e)
            session.rollback()
            raise InvalidUserFieldsError("Invalid fields") from e

        except Exception as e:
            cls.logger.error(e)
            session.rollback()
            raise UserCreationError() from e

    @classmethod
    def get_user_by_id(cls, id, session: Session) -> User:
        user = session.get(id)
        return user

    @classmethod
    def get_user_by_email(cls, email: str, session: Session) -> User:
        user: User = session.query(User).filter_by(email=email).first()
        return user
