Title: Load testing with Locust
Date: 2017-02-27 12:10
Category: Tools
Tags: python, github, load-testing, programming

I have recently been looking into load testing after playing around with [Bombardier]({filename}/bombardier.md), and I remembered my days as an intern running JMeter, recording scenarios under Windows. Those were dark days. Anyway, after some digging, I found [Locust](https://github.com/locustio/locust), I installed it and tried it locally. I thought it was pretty cool, so I decided to write up something about it.

## Load testing with Locust

[Locust](https://github.com/locustio/locust) is a command-line/web HTTP load testing tool written in python and hosted on github. I like how you can write python code to describe your scenarios, launch the tool from command line, and have a nice web UI to launch the actual load testing and get reports in real time.

## Installation

Because I use [Antergos](https://antergos.com/), I have python 3.6 installed by default, therefore I will detail the installation using this version of python.

```
pip install locustio==0.8a2
```

Because locust seems to have [some issues with python >= 3.4](https://github.com/locustio/locust/issues/310), we need to temporarily install this version until 0.8.0 is officially released, which should come soon.

## Usage

To use `locust`, you need first to write your scenario using python, there is a simple API to define your tasks and make some HTTP calls (the `locust` http client is actually wrapping [requests](http://docs.python-requests.org/en/master/))

This is a minimal example, taken shamefully from the [quickstart example](http://docs.locust.io/en/latest/quickstart.html), which I highly recommend to read:

```py
from locust import HttpLocust, TaskSet, task
import json

# This is a TaskSet, it defines a scenario
class PayingUserBehaviour(TaskSet):

    # This is called ONCE when the scenario is started
    def on_start(self):
        # The TaskSet has an HTTP client, which is using requests
        self.client.get('/products/')

    # The task annotation is defining the 'weight' of the task. It is
    # a way to define how often this task should be called proportionally
    # to the other tasks. This tasks is triggered once every 2 payment_put
    @task(1)
    def payment_get(self):
        self.client.get('/payment/')

    # You can give any name to your task functions, as long as you set
    # a task annotation with a weight
    @task(2)
    def payment_put(self):
        payload = {'product_id': 'e202103a-f819-4996-b168-40b068ed804b', 'quantity': 1}
        self.client.post('/payment/', data=json.dumps(payload))

# This is the class that defines the scenarios to run and various
# configurations for the tasks.
class DesktopWebsiteUser(HttpLocust):
    # Which scenario to run
    task_set = PayingUserBehaviour

    # Time between the execution of tasks
    min_wait = 5000
    max_wait = 9000
```

Once you finished writing your scenario as `locustfile.py`, you can run the following in the same directory:

```
locust --host=http://example.com
```

At this point, a web app (written in flask), will be available on at the following url: http://localhost:8089

You will be ask to set:

 * Number of users to simulate (concurrent users)
 * Hatch rate (number of users to spawn every seconds)

 By clicking on Start swarming, you will trigger the load testing which will run the scenario you wrote just before. Statistics will be updated in real time with the requests that succeeded or failed, and you can export those numbers as csv files.

 Locust also has a very interesting feature I did not tested though: [running locust distributed](http://docs.locust.io/en/latest/running-locust-distributed.html). In case you need to massively do load testing on your application, you can create a master instance and multiple slaves, each of them should have the locust script, and you will need ZeroMQ for the nodes to communicate between each others.

## My two cents

Locust has become my favourite tool for load testing, not only because I love python, but because it offers a very user friendly API to write your own scenarios, backed with a powerful and familiar HTTP library which is requests. It has a simple but complete UI in the webapp, where you can easily run tests, reset stats, get __real time__ stats and export them in a common format (csv) for your convenience. A nice improvement would be to have an actual chart (using d3.js or anything else) to display stats on the fly in a graphic way.
