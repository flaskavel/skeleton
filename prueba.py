from orionis.luminate.facades.commands.commands_facade import Command
from orionis.luminate.app_context import app_context

with app_context() as cx:
    Command.call('schedule:work')
