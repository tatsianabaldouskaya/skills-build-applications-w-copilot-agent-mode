from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')
        user1 = User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel)
        user2 = User.objects.create(name='Batman', email='batman@dc.com', team=dc)
        Activity.objects.create(user=user1, type='Running', duration=30, date='2025-11-11')
        Workout.objects.create(name='Hero Training', description='Intense workout for heroes')
        Leaderboard.objects.create(team=marvel, points=100)
        Leaderboard.objects.create(team=dc, points=90)

    def test_user_email_unique(self):
        marvel = Team.objects.get(name='Marvel')
        with self.assertRaises(Exception):
            User.objects.create(name='Duplicate', email='spiderman@marvel.com', team=marvel)

    def test_leaderboard_points(self):
        marvel = Team.objects.get(name='Marvel')
        leaderboard = Leaderboard.objects.get(team=marvel)
        self.assertEqual(leaderboard.points, 100)
