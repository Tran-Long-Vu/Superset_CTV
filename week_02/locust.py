# locust testing http request example: 
# when running locust, the following will be load tested: 
#
#
#
from locust import HttpUser, between, task

# post request login task from user.
class WebsiteUser(HttpUser):
    wait_time = between(5, 15)
    # start test: load test post request: /login.
    def on_start(self):
        self.client.post("/login", {
            "username": "test_user",
            "password": ""
        })
    # after login: load test get request: //assets
    @task
    def index(self):
        self.client.get("/")
        self.client.get("/static/assets.js")
    # load test get request: /about
    @task
    def about(self):
        self.client.get("/about/")