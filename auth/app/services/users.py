import sqlalchemy
from app.models.users.tables import User
from app.models.database import Session
from app.utils.logger import LoggerFactory
from sqlalchemy.orm import sessionmaker


class UserService:
    logger = LoggerFactory.create("UserService")

    with Session() as session:
        session.get

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
            session.rollback()
            raise
        except Exception as e:
            session.rollback()
            raise

    def get_user_by_id(id, session) -> User:
        user = session.get
        return user

    def get_user_by_email(email: str, session: Session) -> User:
        user: User = session.query(User).filter_by(email=email).first()
        return user
