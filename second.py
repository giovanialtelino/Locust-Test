import time
from locust import task, between
from locust.contrib.fasthttp import FastHttpUser
import locust.stats

class QuickStartUser(FastHttpUser):
    wait_time = between(1, 3)

    @task
    def project_page(self):
        self.client.get("/project")
        
    @task
    def my_journey(self):
        self.client.get("/about/about")

    @task
    def hacker_news_graphql(self):
        self.client.get("/project/hacker-news-graphql")

    @task
    def whatsapp_monitor(self):
        self.client.get("/project/whatsapp-monitor")

    @task
    def automation(self):
        self.client.get("/post/automation")

    @task
    def covid_api(self):
        self.client.get("/project/covid-api")

    @task
    def this_blog(self):
        self.client.get("/post/this-blog")