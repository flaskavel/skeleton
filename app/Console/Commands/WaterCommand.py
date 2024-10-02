import time
from flaskavel.lab.beaker.console.reactor import reactor
from flaskavel.lab.beaker.console.command import Command

@reactor.register
class WaterCommand(Command):

    """
    Flaskavel Example Command
    Attributes:
        signature (str): Unique name for the command to register.
        description (str): Brief description of its functionality.
    """

    signature = 'app:cubic'
    description = 'Example usage of Flaskavel CLI, calculates the cubic meters of an element.'

    def arguments(self):
        """
        These are the expected arguments when calling the command
        """
        return [
            ('--height', {'type': int, 'required': True, 'help': 'Height of the area'}),
            ('--length', {'type': int, 'required': True, 'help': 'Length of the area'}),
            ('--width', {'type': int, 'required': True, 'help': 'Width of the area'}),
            ('--name', {'type': str, 'required': False, 'help': 'Name of the measured object'})
        ]

    def handle(self) -> None:

        """
        Command execution logic
        """

        # Read the arguments
        height = self.argument('height')
        length = self.argument('length')
        width = self.argument('width')
        name = self.argument('name', 'Cube')

        # Print a line
        self.line(f"Cubic Meters Calculation: Object Name: {name}, Height: {height} - Width: {width} - Length: {length}")

        # Print an informational message
        self.info(f"Dimensions: Height: {height} - Width: {width} - Length: {length}")

        # Ask how many objects
        quantity = self.ask("How many objects are there?")

        # Ensure it's numeric
        if not str(quantity).isnumeric():
            # Print an error message
            self.error("The value is not numeric.")
            self.exit()

        # Request confirmation
        result = self.confirm("Would you like to know the mathematical formula?")
        if result:
            self.line(f"fx = ({height}*{width}*{length})*{quantity}")

        # Ask for secret input
        secret = self.secret("To ensure you're not a robot, enter the value [1234]")
        if str(secret).strip() != "1234":
            # Print a failure message
            self.fail("Robot validation failed.")
            self.exit()

        # Anticipate input (autocomplete)
        anticipate_option = self.anticipate(
            question='What state of matter is the object in:',
            options=['Solid', 'Liquid', 'Gas', 'Plasma'],
            default='Solid'
        )
        self.line(f"Object state: {anticipate_option}")

        # Print a newline
        self.newLine()

        # Choose from a list
        measurement = self.choice('In which units are the dimensions:', ['Meters', 'Inches', 'Centimeters'])

        # Print multiple newlines
        self.newLine(2)

        # Generate a table with supplied data
        self.table(
            ['Concept', 'Value'],
            [
                ['Object Name', name],
                ['Length', length],
                ['Width', width],
                ['Quantity', quantity],
                ['Measurement Unit', measurement],
            ]
        )

        # Print a newline
        self.newLine()

        # Generate a progress bar simulating the process
        bar = self.createProgressBar(total=100, width=100, inline=False)
        bar.start()

        # Simulate progress
        for i in range(3):
            time.sleep(1)
            bar.advance(25)

        # Finish the progress bar
        bar.finish()

        # Final message
        volume = (int(height) * int(width) * int(length)) * int(quantity)
        self.info(f"The total volume is: {str(volume)} {measurement}")
