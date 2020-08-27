from flask_script import Manager
from flask_migrate import MigrateCommand
from settings.create_app import FlaskApp
from settings.manage_commands import runserver

app = FlaskApp().create_app()

manager = Manager(app)

manager.add_command('db', MigrateCommand)
manager.add_command('runserver', runserver(app))

if __name__ == '__main__':
    manager.run()
