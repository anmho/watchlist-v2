import logging
from requests import Session, codes
from requests.exceptions import RequestException, Timeout, HTTPError
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
from src.config import Config

class GoogleOAuthService:
    def __init__(self, client_id: str, client_secret: str, redirect_uri: str):
        self.sess = Session()
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri

        retries = Retry(
            total=3,
            backoff_factor=0.1,
            status_forcelist=[502, 503, 504],
            allowed_methods={"POST"},
        )
        # Exponential Backoff with factor of 0.1
        self.sess.mount('http://', HTTPAdapter(max_retries=retries))
        self.sess.mount('https://', HTTPAdapter(max_retries=retries))


    def fetch_tokens(self, code: str):
        # Exchange authorization code for access token
        data = {
            'code': code,
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'redirect_uri': self.redirect_uri,
            'grant_type': 'authorization_code'
        }

        access_token = None
        refresh_token = None

        try:
            r = self.sess.post(
                Config.GOOGLE_TOKEN_URL,
                data=data,
                timeout=5
            )
            r.raise_for_status()  # Raise exception for non-successful status codes (4xx, 5xx)

            if r.ok: # status code is < 400, 500 (200 codes)
                token_data = r.json()
                access_token = token_data['access_token']
                refresh_token = token_data['refresh_token']
            else:
                # Handle specific error cases or raise an exception
                # based on the response status code or content
                pass

        except Exception as e:
            raise


        # except Timeout as e:
        #     logging.error("Request timed out: %s", e)
        #     raise
        # except HTTPError as e:
        #     logging.error("HTTP Error: %s", e)
        #     raise
        # except RequestException as e:
        #     logging.error("Request Exception: %s", e)
        #     raise

        return access_token, refresh_token


    def get_user_info(self, access_token: str):
        # Get user info
        headers = {'Authorization': f'Bearer {access_token}'}
        r = self.sess.get(
            'https://www.googleapis.com/oauth2/v2/userinfo', headers=headers
        )
        user_info = r.json()
        return user_info

