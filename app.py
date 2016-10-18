import web
from model import Model

urls = (
    '/chat/(.*)', 'bella_chat'
)

app = web.application(urls, globals())

class bella_chat:
    def __init__(self):
        self.m = Model("bella_loss_9.99984147247/")

    def GET(self, first_char):
        return self.m.sample_char(first_char)


if __name__ == "__main__":
    app.run()