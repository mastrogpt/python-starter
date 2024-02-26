#--param REDIS_URL $REDIS_URL
#--param REDIS_PREFIX $REDIS_PREFIX
#--kind python:default

import redis

def main(args):    
    r = redis.from_url(args.get("REDIS_URL"))
    r.ping()

    p = args.get("REDIS_PREFIX")
    r.set(f"{p}hello", "world")
    name = r.get(f"{p}hello").decode()
    
    greeting = "Hello " + str(name) + "!"
    return {"body": greeting}