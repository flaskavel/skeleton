import datetime
from flaskavel.lab.beaker.console.command import Command
from flaskavel.lab.beaker.console.reactor import reactor

@reactor.register
class CubicCommand(Command):
    """
    Example of a Flaskavel Command.

    This class demonstrates how to define a custom command in Flaskavel.
    The command displays the current date and time in the console.

    Attributes:
        signature (str): The unique name used to register the command.
        description (str): A brief description of the command's functionality.
    """

    # The signature of the command used to register it
    signature = 'app:clock'

    # A short description explaining what the command does
    description = 'Displays the current date and time in the console'

    def handle(self) -> None:
        """
        Command execution logic.

        This method is executed when the command is called. It retrieves
        the current date and time and prints it in the format "dd/mm/yy HH:MM:SS".
        """

        # Printing the current date and time in the specified format
        self.uniqueLine(datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S"))
