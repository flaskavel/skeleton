from flaskavel.lab.beaker.scheduling.schedule import Schedule
from flaskavel.lab.nucleus.console.kernel import Kernel as ConsoleKernel

class Kernel(ConsoleKernel):

    def schedule(self, schedule: Schedule) -> None:

        schedule.command('app:cubic', {
            'height':3,
            'length':2,
            'width':1,
        }).everyMinutes(3)

        # schedule.command('app:?').everySecond()                 # Schedule the task to run every second.
        # schedule.command('app:?').everyTwoSeconds()             # Schedule the task to run every two seconds.
        # schedule.command('app:?').everyFiveSeconds()            # Schedule the task to run every five seconds.
        # schedule.command('app:?').everyTenSeconds()             # Schedule the task to run every ten seconds.
        # schedule.command('app:?').everyFifteenSeconds()         # Schedule the task to run every fifteen seconds.
        # schedule.command('app:?').everyTwentySeconds()          # Schedule the task to run every twenty seconds.
        # schedule.command('app:?').everyThirtySeconds()          # Schedule the task to run every thirty seconds.
        # schedule.command('app:?').everyMinutes(3)               # Schedule the task to run every 3 minutes.
        # schedule.command('app:?').everyMinute()                 # Schedule the task to run every minute.
        # schedule.command('app:?').everyTwoMinutes()             # Schedule the task to run every two minutes.
        # schedule.command('app:?').everyThreeMinutes()           # Schedule the task to run every three minutes.
        # schedule.command('app:?').everyFourMinutes()            # Schedule the task to run every four minutes.
        # schedule.command('app:?').everyFiveMinutes()            # Schedule the task to run every five minutes.
        # schedule.command('app:?').everyTenMinutes()             # Schedule the task to run every ten minutes.
        # schedule.command('app:?').everyFifteenMinutes()         # Schedule the task to run every fifteen minutes.
        # schedule.command('app:?').everyThirtyMinutes()          # Schedule the task to run every thirty minutes.
        # schedule.command('app:?').everyOddHour()                # Schedule the task to run every odd hour.
        # schedule.command('app:?').everyTwoHours()               # Schedule the task to run every two hours.
        # schedule.command('app:?').everyThreeHours()             # Schedule the task to run every three hours.
        # schedule.command('app:?').everyFourHours()              # Schedule the task to run every four hours.
        # schedule.command('app:?').everySixHours()               # Schedule the task to run every six hours.
        # schedule.command('app:?').days(4)                       # Schedule the task to run every 4 days.
        # schedule.command('app:?').daily()                       # Schedule the task to run daily at midnight.
        # schedule.command('app:?').dailyAt('12:00')              # Schedule the task to run daily at 12:00.
        # schedule.command('app:?').twiceDaily(1, 13)             # Schedule the task to run at 1:00 and 13:00 daily.
        # schedule.command('app:?').twiceDailyAt(1, 13, 15)       # Schedule the task to run at 1:15 and 13:15 daily.
        # schedule.command('app:?').monday()                      # Schedule the task to run every Monday at 00:00.
        # schedule.command('app:?').tuesday()                     # Schedule the task to run every Tuesday at 00:00.
        # schedule.command('app:?').wednesday()                   # Schedule the task to run every Wednesday at 00:00.
        # schedule.command('app:?').thursday()                    # Schedule the task to run every Thursday at 00:00.
        # schedule.command('app:?').friday()                      # Schedule the task to run every Friday at 00:00.
        # schedule.command('app:?').saturday()                    # Schedule the task to run every Saturday at 00:00.
        # schedule.command('app:?').sunday()                      # Schedule the task to run every Sunday at 00:00.
        # schedule.command('app:?').weekly()                      # Schedule the task to run every Sunday at 00:00.

    def commands(self) -> None:
        self.load(__file__, '/Commands')
