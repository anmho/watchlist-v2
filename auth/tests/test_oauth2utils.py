# from src.
# from src.utils.oauth2utils import GoogleOAuth2Manager
# from src.config import Config
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from requests import codes
import requests
import webbrowser
import pytest



# @pytest.fixture
# def setup_and_teardown():
#     chrome_options = Options()
#     chrome_options.add_experimental_option('detach', True)
#     browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

#     yield browser

#     # browser.close()


# def test_fetch_tokens(setup_and_teardown):
#     browser: webdriver.Chrome = setup_and_teardown
#     browser.get("http://127.0.0.1:5000/")
#     login_button = browser.find_element(By.ID, 'login')
#     login_button.click()

#     email_input = browser.find_element(By.ID, "identifierId")

#     email_input.send_keys("andyminhtuanho@gmail.com")

#     # email_input.send_keys()


#     email_input.send_keys(Keys.ENTER)

# def test_fetch_tokens():
#     webbrowser.open("http://127.0.0.1:5000/auth/login")

#     response = requests.get("http://127.0.0.1:5000/auth/login")

#     print(response.status_code)
#     assert response.status_code == codes.ok



#     assert response.headers.get('Content-Type') == 'application/json'
#     assert 'access_token' in response.json()
#     assert 'refresh_token' in response.json()







    





#     # manager = GoogleOAuth2Manager(
#     #     Config.GOOGLE_CLIENT_ID, 
#     #     Config.GOOGLE_CLIENT_SECRET, 
#     #     "http://127.0.0.1:5000/auth/authorize/google"
#     # )


#     # authorization_url = requests.get()


#     # manager.fetch_tokens()

    









#     # manager.fetch_tokens()
    