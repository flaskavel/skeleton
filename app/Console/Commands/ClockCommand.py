import datetime
from flaskavel.lab.beaker.console.reactor import reactor
from flaskavel.lab.beaker.console.command import Command

@reactor.register
class CubicCommand(Command):

    """
    Flaskavel Example Command
    Attributes:
        signature (str): Unique name for the command to register.
        description (str): Brief description of its functionality.
    """

    signature = 'app:clock'
    description = 'Muestra un reloj por consola'

    def handle(self) -> None:

        """
        Command execution logic
        """

        self.uniqueLine(datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S"))
