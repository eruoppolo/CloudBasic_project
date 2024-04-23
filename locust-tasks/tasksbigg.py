import os
import random
from locust import HttpUser, task, between
from requests.auth import HTTPBasicAuth

class NextcloudUser(HttpUser):
    auth = None
    user_name = None
    wait_time = between(2, 5)

    # users to test this with.
    def on_start(self): 
        user_idx = random.randrange(0, 89)
        self.user_name = f'locust_user{user_idx}'
        self.auth = HTTPBasicAuth(self.user_name, 'test_password1234!')

    @task(5)
    def propfind(self):
        r = self.client.request("PROPFIND", f"/remote.php/dav", auth=self.auth)
        print(r.text)

    @task(3)
    def verify_authentication(self):
        response = self.client.head("/remote.php/dav", auth=self.auth)

    @task(5)
    def read_file(self):
        self.client.get(f"/remote.php/dav/files/{self.user_name}/Readme.md", auth=self.auth, name="/remote.php/dav/files/[user]/Readme.txt")
        
    @task(6)
    def upload_file_1mb(self):
        remote_path = f"/remote.php/dav/files/{self.user_name}/1mb_file"
        with open("/Users/emanuele/desktop/cloud/testdata/file1MB", "rb") as file:
            self.client.put(remote_path, data=file, auth=self.auth, name="/remote.php/dav/files/[user]/1mb_file")
        self.client.delete(remote_path, auth=self.auth, name="/remote.php/dav/files/[user]/1mb_file")



   
