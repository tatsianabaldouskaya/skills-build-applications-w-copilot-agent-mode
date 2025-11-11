from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        Activity.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Create users
        users = [
            User(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User(name='Captain America', email='cap@marvel.com', team=marvel),
            User(name='Batman', email='batman@dc.com', team=dc),
            User(name='Superman', email='superman@dc.com', team=dc),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
        ]
        User.objects.bulk_create(users)

        # Create activities
        for user in User.objects.all():
            Activity.objects.create(user=user, type='Running', duration=30, date='2025-11-11')
            Activity.objects.create(user=user, type='Swimming', duration=45, date='2025-11-10')

        # Create workouts
        workout1 = Workout.objects.create(name='Hero Training', description='Intense workout for heroes')
        workout2 = Workout.objects.create(name='Power Session', description='Strength and endurance')
        workout1.suggested_for.set([marvel, dc])
        workout2.suggested_for.set([dc])

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=300)
        Leaderboard.objects.create(team=dc, points=250)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully!'))
