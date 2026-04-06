from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='dc', description='DC Superheroes')

        # Users
        users = [
            User(name='Iron Man', email='ironman@marvel.com', team='marvel'),
            User(name='Captain America', email='cap@marvel.com', team='marvel'),
            User(name='Spider-Man', email='spiderman@marvel.com', team='marvel'),
            User(name='Batman', email='batman@dc.com', team='dc'),
            User(name='Superman', email='superman@dc.com', team='dc'),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team='dc'),
        ]
        for user in users:
            user.save()

        # Activities
        activities = [
            Activity(user='Iron Man', type='run', duration=30, date=timezone.now().date()),
            Activity(user='Captain America', type='cycle', duration=45, date=timezone.now().date()),
            Activity(user='Spider-Man', type='swim', duration=25, date=timezone.now().date()),
            Activity(user='Batman', type='run', duration=40, date=timezone.now().date()),
            Activity(user='Superman', type='cycle', duration=60, date=timezone.now().date()),
            Activity(user='Wonder Woman', type='swim', duration=35, date=timezone.now().date()),
        ]
        for activity in activities:
            activity.save()

        # Leaderboard
        Leaderboard.objects.create(team='marvel', points=200)
        Leaderboard.objects.create(team='dc', points=180)

        # Workouts
        workouts = [
            Workout(name='Pushups', description='Do 20 pushups', difficulty='easy'),
            Workout(name='Situps', description='Do 30 situps', difficulty='easy'),
            Workout(name='Squats', description='Do 15 squats', difficulty='medium'),
            Workout(name='Plank', description='Hold plank for 1 min', difficulty='hard'),
        ]
        for workout in workouts:
            workout.save()

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
