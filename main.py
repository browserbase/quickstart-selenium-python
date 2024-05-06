from selenium import webdriver
from selenium.webdriver.remote.remote_connection import RemoteConnection
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import requests
import os

def create_session():
    url = 'https://www.browserbase.com/v1/sessions'
    headers = {'Content-Type': 'application/json', 'x-bb-api-key': os.environ["BROWSERBASE_API_KEY"]}
    response = requests.post(url, json={ "projectId": os.environ["BROWSERBASE_PROJECT_ID"] }, headers=headers)
    return response.json()['id']


class CustomRemoteConnection(RemoteConnection):
    _session_id = None

    def __init__(self, remote_server_addr: str, session_id: str):
        super().__init__(remote_server_addr)
        self._session_id = session_id

    def get_remote_connection_headers(self, parsed_url, keep_alive=False):
        headers = super().get_remote_connection_headers(parsed_url, keep_alive)
        headers.update({'x-bb-api-key': os.environ["BROWSERBASE_API_KEY"]})
        headers.update({'session-id': self._session_id})
        return headers


def run():
    session_id = create_session()
    custom_conn = CustomRemoteConnection('http://connect.browserbase.com/webdriver', session_id)
    options = webdriver.ChromeOptions()
    options.debugger_address = "localhost:9223"
    driver = webdriver.Remote(custom_conn, options=options)
    driver.get("https://www.browserbase.com")
    get_title = driver.title
    print(get_title)
    # Make sure to quit the driver so your session is ended!
    driver.quit()

run()
