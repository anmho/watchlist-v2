from uuid import UUID
from sqlalchemy import Uuid
from app.config import Config
from datetime import datetime, timedelta
from app.utils.logger import LoggerFactory
from authlib.jose import jwt, JWTClaims


class TokenService:
    _secret = Config.SECRET_KEY
    logger = LoggerFactory.create("TokenService")

    assert _secret is not None

    @classmethod
    def _create_token(cls, sub, token_type, expires_in) -> str:
        if token_type not in ("access", "refresh"):
            raise TypeError(f"invalid token type {token_type}")

        if not sub:
            raise ValueError("sub must be provided")

        if type(sub) is not str:
            cls.logger.info(type(sub))
            raise TypeError("sub must be a string")

        expires_at = datetime.utcnow() + timedelta(seconds=expires_in)

        header = {
            "alg": "HS256",
            "typ": "JWT"
        }

        payload = {
            "sub": sub,
            "exp": expires_at,
            "token_type": token_type
        }

        token = jwt.encode(header=header, payload=payload,
                           key=cls._secret, check=True).decode("utf-8")

        return token

    @classmethod
    def create_access(cls, sub, expires_in=36000) -> str:
        # iss, aud, scope, token_type

        return cls._create_token(sub, "access", expires_in)

    @classmethod
    def create_refresh(cls, sub, expires_in=86400) -> str:
        return cls._create_token(sub, "refresh", expires_in)

    @classmethod
    def check_token(cls, token) -> bool:
        try:
            claims = jwt.decode(token, cls._secret)
        except Exception as e:
            cls.logger.error(e)

            return False
        return True

    @classmethod
    def decode(cls, token) -> JWTClaims:
        claims: JWTClaims = jwt.decode(token, cls._secret)
        return claims
