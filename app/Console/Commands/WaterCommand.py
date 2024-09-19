from flaskavel.lab.beaker.commands.reactor import reactor
from flaskavel.lab.beaker.commands.command import Command
import time

@reactor.register
class WaterCommand(Command):

    """
    Command to display the technical components of H2O (water) and demonstrate the use of various console methods.
    """

    signature = 'app:water'
    description = 'Print the technical components of H2O and demonstrate various console methods.'

    def handle(self, *args, **kwargs) -> None:
        # Informative message
        self.info("Starting the water component analysis...")

        # Error message (simulated example)
        self.error("This is a simulated error message.")

        # Failure message (simulated example)
        self.fail("This is a simulated failure message.")

        # Ask for user's name and greet them
        name = self.ask("What is your name?")
        self.info(f"Hello, {name}!")

        # Confirm if the user is sure
        result = self.confirm("Are you sure you want to proceed?")
        self.info(f"User confirmed: {result}")

        # Ask for a secret (like a password)
        password = self.secret("Please enter a secret password:")
        self.info(f"Password entered: {password}")

        # Anticipate input (autocomplete)
        component = self.anticipate(
            question='What is the main component of water?',
            options=['Hydrogen', 'Oxygen', 'Nitrogen', 'Carbon'],
            default='Hydrogen'
        )
        self.info(f"Anticipated component: {component}")

        # Choice from a list
        choice = self.choice('Choose the form of water:', ['liquid', 'ice', 'steam'])
        self.info(f"Chosen form of water: {choice}")

        # Print a line of text
        self.line("Processing complete. Here's a summary:")

        # Print multiple new lines for clarity
        self.newLine(2)

        # Print a detailed table
        self.table(
            ['Component', 'Quantity'],
            [['Hydrogen', '2 atoms'], ['Oxygen', '1 atom']]
        )

        # Create and use a progress bar
        bar = self.createProgressBar(total=100, width=100, inline=False)
        bar.start()

        # Simulate progress
        for i in range(0, 101, 10):
            time.sleep(1)  # Simulate work
            bar.advance(10)

        bar.finish()

        # Final message
        self.info("Technical components of H2O (water) are: 2 hydrogen atoms and 1 oxygen atom.")
