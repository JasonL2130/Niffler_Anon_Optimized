# Establish Redis Connection

import redis

def get_redis_connection():
    redis_host = 'redis-13158.c10.us-east-1-2.ec2.cloud.redislabs.com'
    redis_port = 13158
    redis_password = '3JrZyJpJxxTT1Cu8NxIe6JPoibu8ZqwZ'  # If your Redis instance has a password, provide it here

    try:
        # Create a connection to the Redis server
        redis_conn = redis.StrictRedis(
            host=redis_host,
            port=redis_port,
            password=redis_password,
            decode_responses=True
        )
 
        # If the ping is successful, the connection is established
        print('Connected to Redis successfully!')

        return redis_conn

    except redis.exceptions.ConnectionError as e:
        print(f'Error connecting to Redis: {e}')
        return None
