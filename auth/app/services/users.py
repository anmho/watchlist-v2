import sqlalchemy
from app.models.users.tables import User
from sqlalchemy.orm import Session
from app.utils.logger import LoggerFactory
from sqlalchemy.orm import sessionmaker


class UserService:
    logger = LoggerFactory.create("UserService")

    @classmethod
    def create_user(cls, email, password, session: sessionmaker[Session], registration_type="standard") -> User:
        try:
            user = User(email=email, registration_type=registration_type)
            session.add(user)
            user.set_password(password)
            session.add(user)
            session.commit()

            return user

        except sqlalchemy.exc.IntegrityError as e:
            cls.logger.error(e)
            session.rollback()
            raise
        except Exception as e:
            cls.logger.error(e)
            session.rollback()
            raise

    def get_user_by_id(id, session: Session) -> User:
        user = session.get(id)
        return user

    def get_user_by_email(email: str, session: Session) -> User:
        user: User = session.query(User).filter_by(email=email).first()
        return user
