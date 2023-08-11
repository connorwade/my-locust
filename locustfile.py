from locust import between, events, tag, task, HttpUser
import common.user_agents
import random
import logging

# @events.init.add_listener
# def on_locust_init(evironment, **_kwargs):

primary_urls = [
    "services",
    "solutions",
    "why-hoodoo",
    "success-stories",
    "webinars",
    "blog",
]

secondary_urls = [
    "adobe-experience-manager-sites",
    "adobe-analytics",
    "adobe-sign",
    "experience-design",
    "fastly",
]


class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    @tag("home_page")
    @task(3)
    def home_page(self):
        user_agent = common.user_agents.get_random_agent()
        logging.info(f"user agent is: {user_agent}")
        self.client.headers["User-Agent"] = user_agent
        with self.client.get("/", catch_response=True) as response:
            if response.status_code != 200:
                response.failure(
                    f"Got wrong response, Status code: {response.status_code}"
                )

    @tag("primary_urls")
    @task(10)
    def primary_urls(self):
        user_agent = common.user_agents.get_random_agent()
        logging.info(f"user agent is: {user_agent}")
        self.client.headers["User-Agent"] = user_agent
        with self.client.get(
            f"/{random.choice(primary_urls)}", catch_response=True
        ) as response:
            if response.status_code != 200:
                response.failure(f"Got wrong response")

    @tag("secondary_urls")
    @task(1)
    def secondary_urls(self):
        user_agent = common.user_agents.get_random_agent()
        logging.info(f"user agent is: {user_agent}")
        self.client.headers["User-Agent"] = user_agent
        with self.client.get(
            f"/{random.choice(secondary_urls)}", catch_response=True
        ) as response:
            if response.status_code != 200:
                response.failure(f"Got wrong response")

    def on_start(self):
        print("New user was spawned")
