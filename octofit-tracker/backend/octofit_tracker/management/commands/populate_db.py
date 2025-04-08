from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = "Populate the database with test data"

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Populate users
        users = [
            {"name": "Alice", "email": "alice@example.com"},
            {"name": "Bob", "email": "bob@example.com"},
        ]
        for user_data in users:
            User.objects.create(**user_data)

        # Populate teams
        teams = [
            {"name": "Team A", "description": "Fitness enthusiasts"},
            {"name": "Team B", "description": "Competitive athletes"},
        ]
        for team_data in teams:
            Team.objects.create(**team_data)

        # Populate activities
        activities = [
            {"user": User.objects.first(), "type": "Running", "duration": 30},
            {"user": User.objects.last(), "type": "Cycling", "duration": 45},
        ]
        for activity_data in activities:
            Activity.objects.create(**activity_data)

        # Populate leaderboard
        leaderboard_entries = [
            {"user": User.objects.first(), "score": 100},
            {"user": User.objects.last(), "score": 150},
        ]
        for entry_data in leaderboard_entries:
            Leaderboard.objects.create(**entry_data)

        # Populate workouts
        workouts = [
            {"name": "Morning Run", "description": "5km run", "duration": 30},
            {"name": "Evening Yoga", "description": "Relaxing yoga session", "duration": 60},
        ]
        for workout_data in workouts:
            Workout.objects.create(**workout_data)

        self.stdout.write(self.style.SUCCESS("Database populated with test data."))
