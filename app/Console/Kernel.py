from flaskavel.lab.beaker.iterations.loops import Loops
from flaskavel.lab.beaker.scheduling.schedule import Schedule
from flaskavel.lab.nucleus.console.kernel import Kernel as ConsoleKernel

class Kernel(ConsoleKernel):

    def schedule(self, schedule: Schedule) -> None:
        """
        You can schedule the execution of your commands here based on the predefined options available in Flaskavel.
        """

        # Schedule the task to run every ten minutes.
        schedule.command('app:cubic', {'height':3, 'length':2, 'width':1}).everyTenMinutes()

        # Examples:
        # schedule.command('app:?').everySeconds(seconds=7)                                   # Schedule the task to run every  seconds.
        # schedule.command('app:?').everySecond()                                             # Schedule the task to run every second.
        # schedule.command('app:?').everyTwoSeconds()                                         # Schedule the task to run every two seconds.
        # schedule.command('app:?').everyFiveSeconds()                                        # Schedule the task to run every five seconds.
        # schedule.command('app:?').everyTenSeconds()                                         # Schedule the task to run every ten seconds.
        # schedule.command('app:?').everyFifteenSeconds()                                     # Schedule the task to run every fifteen seconds.
        # schedule.command('app:?').everyTwentySeconds()                                      # Schedule the task to run every twenty seconds.
        # schedule.command('app:?').everyThirtySeconds()                                      # Schedule the task to run every thirty seconds.
        # schedule.command('app:?').everyMinutes(minutes=7)                                   # Schedule the task to run every 7 minutes.
        # schedule.command('app:?').everyMinute()                                             # Schedule the task to run every minute.
        # schedule.command('app:?').everyTwoMinutes()                                         # Schedule the task to run every two minutes.
        # schedule.command('app:?').everyThreeMinutes()                                       # Schedule the task to run every three minutes.
        # schedule.command('app:?').everyFourMinutes()                                        # Schedule the task to run every four minutes
        # schedule.command('app:?').everyFiveMinutes()                                        # Schedule the task to run every five minutes.
        # schedule.command('app:?').everyTenMinutes()                                         # Schedule the task to run every ten minutes.
        # schedule.command('app:?').everyFifteenMinutes()                                     # Schedule the task to run every fifteen minutes.
        # schedule.command('app:?').everyThirtyMinutes()                                      # Schedule the task to run every thirty minutes.
        # schedule.command('app:?').hours(hours=7)                                            # Schedule the task to run every 7 hours.
        # schedule.command('app:?').hourly()                                                  # Schedule the task to run every hour.
        # schedule.command('app:?').hourlyAt(minute=45)                                       # Schedule the task to run hourly at a specific minute.
        # schedule.command('app:?').everyOddHour(minutes=45)                                  # Schedule the task to run every odd hour.
        # schedule.command('app:?').everyTwoHours(minutes=45)                                 # Schedule the task to run every two hours.
        # schedule.command('app:?').everyThreeHours(minutes=45)                               # Schedule the task to run every Three hours.
        # schedule.command('app:?').everyFourHours(minutes=45)                                # Schedule the task to run Four two hours.
        # schedule.command('app:?').everySixHours(minutes=45)                                 # Schedule the task to run every two hours
        # schedule.command('app:?').days(days=3)                                              # Schedule the task to run every 3 days.
        # schedule.command('app:?').daily()                                                   # Schedule the task to run daily at midnight.
        # schedule.command('app:?').dailyAt(time:'13:17')                                     # Schedule the task to run daily at a specific time.
        # schedule.command('app:?').twiceDaily(first_hour=6, second_hour=12)                  # Schedule the task twice a day.
        # schedule.command('app:?').twiceDailyAt(first_hour=6, second_hour=6, minutes=45)     # Schedule the task twice a day with minutes.
        # schedule.command('app:?').monday(at='00:00')                                        # Schedule the task to run every monday at 00:00.
        # schedule.command('app:?').tuesday(at='00:00')                                       # Schedule the task to run every tuesday at 00:00.
        # schedule.command('app:?').wednesday(at='00:00')                                     # Schedule the task to run every wednesday at 00:00.
        # schedule.command('app:?').thursday(at='00:00')                                      # Schedule the task to run every thursday at 00:00.
        # schedule.command('app:?').friday(at='00:00')                                        # Schedule the task to run every friday at 00:00.
        # schedule.command('app:?').saturday(at='00:00')                                      # Schedule the task to run every saturday at 00:00.
        # schedule.command('app:?').sunday(at='00:00')                                        # Schedule the task to run every sunday at 00:00.
        # schedule.command('app:?').weekly()                                                  # Schedule the task to run every sunday at 00:00.

    def loops(self, loop: Loops) -> None:
        """
        Manages continuous execution of a command in a loop, ensuring sequential processing
        to prevent multiple instances of the same command from overlapping.

        Args:
            loop (Loops): An instance of the Loops class that manages the loop execution.

        Usage:
            - command (str): Specifies the name of the command to be executed in a loop. This is required.
            - intervals (sleep: int): Defines the interval in seconds between each loop execution.
            This is a required parameter.
            - timer (optional: int): Specifies the maximum duration in seconds for the loop execution.
            When this time is reached, the loop stops. If not defined, the loop will run indefinitely.
            Use caution to avoid excessive or inefficient memory and CPU usage.
            - daemon (optional: bool): If set to `True`, runs the loop in a background daemon thread.
            Daemon threads run in the background and exit automatically when the main program finishes.
            If not set, the thread will continue running until its job is done, even if the main program exits.

        Example:
            # Running the loop with a specific command and intervals
            loop.command('app:clock').intervals(sleep=1, timer=10)

            # Running the loop as a daemon thread
            loop.command('app:clock').daemon().intervals(sleep=1, timer=10)

            # Running the loop without daemon (non-background thread)
            loop.command('app:clock').daemon(False).intervals(sleep=1, timer=10)
        """

        loop.command('app:clock').intervals(sleep=1, timer=10)

    def commands(self) -> None:
        """
        If you want to organize your commands in different locations, you can register here where to load them from.
        """

        self.load(__file__, '/Commands')