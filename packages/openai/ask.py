#--web true
#--param OPENAI_API_HOST $OPENAI_API_HOST
#--param OPENAI_API_KEY $OPENAI_API_KEY
#--kind python:default

from openai import AzureOpenAI

class Chatbot:

    ROLE = "You are an helpful assistant."
    MODEL = "gpt-35-turbo"

    def __init__(self, args):
        # accesso parametri
        key = args.get("OPENAI_API_KEY")
        host = args.get("OPENAI_API_HOST")
        # accesso alla ai
        ai = AzureOpenAI(api_version="2023-12-01-preview", api_key=key, azure_endpoint=host)
        self.ai = ai

    def ask(self, inp, role=ROLE):
        system = {"role": "system", "content": role}
        user = {"role": "user", "content": inp}
        request = [system, user]
        ai = self.ai
        comp = ai.chat.completions.create(model=self.MODEL, messages=request)
        if len(comp.choices) >0:
            return comp.choices[0].message.content
        return "I do not understand."


def main(args):
    chat = Chatbot(args)
    # read input
    inp = args.get("input")
    # produce output
    out = chat.ask(inp)
    # prepare res
    res = {
        "output": out
    }
    # adding html
    res['html'] = f"<h1>{inp}</h1><p>{out}</p>"
    #res['message'] = out
    return {
        "body": res
    }
