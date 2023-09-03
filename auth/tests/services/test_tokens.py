# from app.services.tokens import TokenService
from uuid import uuid4

import pytest
from app.services.tokens import TokenService
from authlib.jose import jwt





class TestTokenService:
    def test_create_access(self):

        user_id = "1"

        token = TokenService.create_access(sub=user_id)

        with pytest.raises():
            

        decoded = jwt.decode(token, "asdf")

        assert True

    def test_create_refresh(self):
        assert True

    def test_check_token(self):
        assert True
