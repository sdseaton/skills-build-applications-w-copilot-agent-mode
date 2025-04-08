import os
import django

# Ensure Django settings are loaded
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

from django.core.management.base import BaseCommand
from octofit_tracker.tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import date

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        users = [
            User(email='thundergod@mhigh.edu', name='Thor', password='password123'),
            User(email='metalgeek@mhigh.edu', name='Tony Stark', password='password123'),
            User(email='zerocool@mhigh.edu', name='Elliot Alderson', password='password123'),
            User(email='crashoverride@mhigh.edu', name='Dade Murphy', password='password123'),
            User(email='sleeptoken@mhigh.edu', name='Sleep Token', password='password123'),
        ]
        User.objects.bulk_create(users)

        # Create teams
        teams = [
            Team(name='Blue Team', members=[users[0], users[1]]),
            Team(name='Gold Team', members=[users[2], users[3], users[4]]),
        ]
        Team.objects.bulk_create(teams)

        # Create activities
        activities = [
            Activity(user=users[0], type='Cycling', duration=60, date=date(2025, 4, 1)),
            Activity(user=users[1], type='Crossfit', duration=120, date=date(2025, 4, 2)),
            Activity(user=users[2], type='Running', duration=90, date=date(2025, 4, 3)),
            Activity(user=users[3], type='Strength', duration=30, date=date(2025, 4, 4)),
            Activity(user=users[4], type='Swimming', duration=75, date=date(2025, 4, 5)),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(team=teams[0], points=100),
            Leaderboard(team=teams[1], points=90),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(name='Cycling Training', description='Training for a road cycling event'),
            Workout(name='Crossfit', description='Training for a crossfit competition'),
            Workout(name='Running Training', description='Training for a marathon'),
            Workout(name='Strength Training', description='Training for strength'),
            Workout(name='Swimming Training', description='Training for a swimming competition'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))