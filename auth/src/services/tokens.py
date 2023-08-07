from datetime import datetime, timedelta
from abc import ABC, abstractmethod
from math import floor
import jwt
from typing import Dict, Tuple
from src.config import Config
from datetime import datetime
from redis import Redis
from src.app import redis

class Blacklist:
    def __init__(
            self,
            redis: Redis, 
            name: str
        ):
        self.redis = redis
        self.name = name

    def add(self, item: str) -> int:
        num_added = redis.sadd(self.name, item)

        return num_added
    def remove(self, item: str) -> int:
        num_removed = redis.srem(self.name, item)
        return num_removed

class Token:
    def __init__(
            self, 
            email: str, 
            duration: timedelta = timedelta(minutes=15)
        ):
        if not email:
            raise ValueError("Missing required argument 'email' of type str")
        
        if not isinstance(duration, timedelta):
            raise TypeError("Argument 'duration' must ")
        
        if duration <= timedelta(0):
            raise ValueError("duration must be a positive value")
        
        now = datetime.utcnow()
        expiry = now + duration
        expiry = expiry.timestamp()
        expiry = floor(expiry)

        self.iat = now
        self.expiry = expiry

        payload = {
            "email": email,
            "iat": now,
            "exp": expiry
        }
        
        # Generate the token
        self.value = jwt.encode(
            payload=payload,
            key=Config.SECRET_KEY,
            algorithm="HS256"
        )

    def _now(self) -> datetime.timestamp:
        return datetime.utcnow().timestamp()

    def is_expired(self) -> bool:
        return self._now() <= self.expiry

    def parse_from_token(self, token: str) -> None:
        claims = jwt.api_jwt.decode(
            token,
            key=Config.SECRET_KEY,
            algorithms=["HS256"],
            options={

            }
        )

    @property
    def claims(self) -> Dict[str, str]:
        result = jwt.decode(
            self.value, 
            key=Config.SECRET_KEY, 
            algorithms=["HS256"],
            options={

            }
        )
        return result
    
    @property
    def full_decode(self):
        if not self.value:
            raise ValueError("Must initialize token values by calling parse_from_token or passing initial values")

    def is_expired(self):
        return self.expiry > self._now()

class RefreshToken(Token):
    def __init__(
            self, 
            email, 
            duration, 
            blacklist: Blacklist
        ):
        super().__init__(email, duration)
        self.blacklist = blacklist
    
    def invalidate(self):
        # Add this token to redis blacklist
        self.blacklist.add(self.value)