**Infrastructure Automation with Shell + Docker Compose**

Step 1: created Dockerfile inside app folder

step 2: Docker-compose file

Network:
    All services are attached to a custom bridge network named docker_network, which creates internal DNS-based communication using the Docker network stack.

Volumes:
    jenkins_home - used by jenkins to store the plugins, jobs to keep persistent.
    redis_data  - used by redis to store the data of redis on disk

Services:
    1) Jenkins:
        - Configured with URL path prefix (/jenkins) so the UI is accessible as http://localhost/jenkins as it is accessible only through nginx.
        - Uses a healthcheck to verify the login page before dependent services start.

    2) Redis:
        - redis-server --appendonly yes to make the data peristent
        - checking health of redis by using Ping and ensure that app starts after it is healthy

    3) Python App
        - Built locally using a Dockerfile inside ./app.
        - Waits for Redis to be healthy using

        depends_on:
            redis:
                condition: service_healthy

        - Connects to Redis by passing the Redis config through environment variables.

    4) nginx:
        - Exposes public port 80:80 so the stack can be accessed externally through Nginx only.
        - Starts only after both Jenkins & Python app pass their healthchecks.
        - mounted a custom config to the /etc/nginx/nginx.conf
        - so python app and jenkins are serving through nginx via path based routing

            localhost routes to python app
![alt text](images/image-1.png)

            localhost/jenkins routes to Jenkins

![alt text](images/image.png)

Step 3: shell script to check the whether docker exists if not install it and bring the containers up by running 
        docker compose --build -d