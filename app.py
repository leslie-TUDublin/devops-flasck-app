import redis
from flask import Flask
app = Flask(__name__)
r = redis.Redis(host='the-redis-server', port=6379, decode_responses=True)

@app.route('/')
def hello():
    return "<h1>Today is Friday the 13th. Yesterday I was 49, I was born at midnight between Nov 12 and 13. Last night there was a global Microsoft outage.</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
