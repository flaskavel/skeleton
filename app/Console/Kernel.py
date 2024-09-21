from flaskavel.lab.beaker.scheduling.schedule import Schedule
from flaskavel.lab.nucleus.console.kernel import Kernel as ConsoleKernel

class Kernel(ConsoleKernel):

    def schedule(self, schedule: Schedule) -> None:
        schedule.command('app:water', {'framework':'flaskavel','version' : 1}).everySeconds(3)

        # schedule.command('app:water').everySecond()                 # Schedule the task to run every second.
        # schedule.command('app:water').everyTwoSeconds()             # Schedule the task to run every two seconds.
        # schedule.command('app:water').everyFiveSeconds()            # Schedule the task to run every five seconds.
        # schedule.command('app:water').everyTenSeconds()             # Schedule the task to run every ten seconds.
        # schedule.command('app:water').everyFifteenSeconds()         # Schedule the task to run every fifteen seconds.
        # schedule.command('app:water').everyTwentySeconds()          # Schedule the task to run every twenty seconds.
        # schedule.command('app:water').everyThirtySeconds()          # Schedule the task to run every thirty seconds.
        # schedule.command('app:water').everyMinutes(3)               # Schedule the task to run every 3 minutes.
        # schedule.command('app:water').everyMinute()                 # Schedule the task to run every minute.
        # schedule.command('app:water').everyTwoMinutes()             # Schedule the task to run every two minutes.
        # schedule.command('app:water').everyThreeMinutes()           # Schedule the task to run every three minutes.
        # schedule.command('app:water').everyFourMinutes()            # Schedule the task to run every four minutes.
        # schedule.command('app:water').everyFiveMinutes()            # Schedule the task to run every five minutes.
        # schedule.command('app:water').everyTenMinutes()             # Schedule the task to run every ten minutes.
        # schedule.command('app:water').everyFifteenMinutes()         # Schedule the task to run every fifteen minutes.
        # schedule.command('app:water').everyThirtyMinutes()          # Schedule the task to run every thirty minutes.
        # schedule.command('app:water').everyOddHour()                # Schedule the task to run every odd hour.
        # schedule.command('app:water').everyTwoHours()               # Schedule the task to run every two hours.
        # schedule.command('app:water').everyThreeHours()             # Schedule the task to run every three hours.
        # schedule.command('app:water').everyFourHours()              # Schedule the task to run every four hours.
        # schedule.command('app:water').everySixHours()               # Schedule the task to run every six hours.
        # schedule.command('app:water').days(4)                       # Schedule the task to run every 4 days.
        # schedule.command('app:water').daily()                       # Schedule the task to run daily at midnight.
        # schedule.command('app:water').dailyAt('12:00')              # Schedule the task to run daily at 12:00.
        # schedule.command('app:water').twiceDaily(1, 13)             # Schedule the task to run at 1:00 and 13:00 daily.
        # schedule.command('app:water').twiceDailyAt(1, 13, 15)       # Schedule the task to run at 1:15 and 13:15 daily.
        # schedule.command('app:water').monday()                      # Schedule the task to run every Monday at 00:00.
        # schedule.command('app:water').tuesday()                     # Schedule the task to run every Tuesday at 00:00.
        # schedule.command('app:water').wednesday()                   # Schedule the task to run every Wednesday at 00:00.
        # schedule.command('app:water').thursday()                    # Schedule the task to run every Thursday at 00:00.
        # schedule.command('app:water').friday()                      # Schedule the task to run every Friday at 00:00.
        # schedule.command('app:water').saturday()                    # Schedule the task to run every Saturday at 00:00.
        # schedule.command('app:water').sunday()                      # Schedule the task to run every Sunday at 00:00.
        # schedule.command('app:water').weekly()                      # Schedule the task to run every Sunday at 00:00.

    def commands(self) -> None:
        self.load(__file__, '/Commands')
