from flask import Flask
import redis
import os

app = Flask(__name__)

# Connect using Docker Compose service DNS "redis"
r = redis.Redis(
    host=os.getenv("REDIS_HOST", "redis"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    decode_responses=True
)

@app.route("/")
def home():
    hits = r.incr("hits")
    return f"Hello from Python! Redis hits: {hits}"

if __name__ == "__main__":
    # Flask must listen on 0.0.0.0 so healthcheck & nginx can reach it
    app.run(host="0.0.0.0", port=8000)
