from flask_script import Command


class runserver(Command):

    def __init__(self, app):
        super().__init__()
        self.app = app

    def run(self):
        self.app.run()

