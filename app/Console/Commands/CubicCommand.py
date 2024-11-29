import time
from flaskavel.lab.beaker.console.command import Command
from flaskavel.lab.beaker.console.reactor import reactor

@reactor.register
class CubicCommand(Command):

    """
    Flaskavel Example Command

    This command calculates the cubic meters of an object based on user-provided dimensions
    (height, length, and width) and the number of objects. It also allows for further
    interactive steps like input validation, displaying mathematical formulas, and selecting
    units of measurement.

    Attributes:
        signature (str): The unique name for the command used to register it.
        description (str): A brief description of the command's functionality.
    """

    # The unique signature used to register the command
    signature = 'app:cubic'

    # A brief description of what the command does
    description = 'Example usage of Flaskavel CLI, calculates the cubic meters of an element.'

    def arguments(self):
        """
        Defines the expected arguments when calling the command.

        Returns:
            list: List of tuples with argument names and their properties (e.g., type, required, help text).
        """
        return [
            ('--height', {'type': int, 'required': True, 'help': 'Height of the area'}),
            ('--length', {'type': int, 'required': True, 'help': 'Length of the area'}),
            ('--width', {'type': int, 'required': True, 'help': 'Width of the area'}),
            ('--name', {'type': str, 'required': False, 'help': 'Name of the measured object'})
        ]

    def handle(self) -> None:

        """
        Command execution logic.

        Retrieves user inputs, calculates the cubic meters, and provides additional interactions
        like displaying the formula, confirming values, and providing a progress bar.
        """

        # Retrieve arguments passed to the command
        height = self.argument('height')
        length = self.argument('length')
        width = self.argument('width')
        name = self.argument('name', 'Cube')

        # Display the cubic meters calculation header
        self.line(f"Cubic Meters Calculation: Object Name: {name}, Height: {height} - Width: {width} - Length: {length}")

        # Show dimensions
        self.info(f"Dimensions: Height: {height} - Width: {width} - Length: {length}")

        # Ask the user how many objects they are calculating for
        quantity = self.ask("How many objects are there?")

        # Validate that the quantity is numeric
        if not str(quantity).isnumeric():
            self.error("The value is not numeric.")
            self.exit()

        # Ask for confirmation to show the mathematical formula
        result = self.confirm("Would you like to know the mathematical formula?")
        if result:
            self.line(f"fx = ({height}*{width}*{length})*{quantity}")

        # Request a secret input to verify user identity
        secret = self.secret("To ensure you're not a robot, enter the value [1234]")
        if str(secret).strip() != "1234":
            # Print a failure message
            self.fail("Robot validation failed.")
            self.exit()

        # Anticipate user's response with options for the state of matter
        anticipate_option = self.anticipate(
            question='What state of matter is the object in:',
            options=['Solid', 'Liquid', 'Gas', 'Plasma'],
            default='Solid'
        )
        self.line(f"Object state: {anticipate_option}")

        # Add a newline for clarity
        self.newLine()

        # Ask the user to choose the measurement units
        measurement = self.choice('In which units are the dimensions:', ['Meters', 'Inches', 'Centimeters'])

        # Add more newlines for formatting
        self.newLine(2)

        # Display the data in a table format
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

        # Add a final newline
        self.newLine()

        # Start a progress bar to simulate a task
        bar = self.createProgressBar(total=100, width=100, inline=False)
        bar.start()

        # Simulate progress in the task
        for i in range(3):
            time.sleep(1)
            bar.advance(25)

        # Finish the progress bar after the simulation
        bar.finish()

        # Final output: calculate and display the total volume
        volume = (int(height) * int(width) * int(length)) * int(quantity)
        self.info(f"The total volume is: {str(volume)} {measurement}")
