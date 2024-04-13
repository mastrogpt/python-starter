#--kind python:default
#--web true

def main(args):
    print("hello")
    name = args.get("name", "world")
    greeting = "Hello " + name + "!"
    return {"body": greeting}
