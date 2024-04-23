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
        r = self.client.request("PROPFIND", f"/remote.php/dav/files/{self.user_name}/", auth=self.auth)
        print(r.text)

    @task(5)
    def verify_authentication(self):
        response = self.client.head("/remote.php/dav", auth=self.auth)

    @task(5)
    def read_file(self):
        self.client.get(f"/remote.php/dav/files/{self.user_name}/Readme.md", auth=self.auth)
        
    @task(1)
    def upload_file_1gb(self):
        remote_path = f"/remote.php/dav/files/{self.user_name}/1gb_file_{random.randrange(0, 9)}"
        with open("/Users/emanuele/desktop/cloud/testdata/file1GB", "rb") as file:
            self.client.put(remote_path, data=file, auth=self.auth)

    @task(10)
    def upload_file_1kb(self):
        remote_path = f"/remote.php/dav/files/{self.user_name}/1kb_file_{random.randrange(0, 9)}"
        with open("/Users/emanuele/desktop/cloud/testdata/file1KB", "rb") as file:
            self.client.put(remote_path, data=file, auth=self.auth)

    @task(5)
    def upload_file_1mb(self):
        remote_path = f"/remote.php/dav/files/{self.user_name}/1mb_file_{random.randrange(0, 9)}"
        with open("/Users/emanuele/desktop/cloud/testdata/file1MB", "rb") as file:
            self.client.put(remote_path, data=file, auth=self.auth)

    @task(2)
    def upload_file_jpg(self):
        remote_path = f"/remote.php/dav/files/{self.user_name}/example_{random.randrange(0, 9)}.jpg"
        with open("/Users/emanuele/desktop/cloud/testdata/locusta.jpg", "rb") as file:
            self.client.put(remote_path, data=file, auth=self.auth)
