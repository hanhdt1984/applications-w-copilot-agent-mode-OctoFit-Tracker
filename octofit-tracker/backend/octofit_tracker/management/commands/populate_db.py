from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = "Populate the database with test data for the OctoFit tracker app"

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Populate users
        users = [
            {"name": "John Doe", "email": "john.doe@example.com"},
            {"name": "Jane Smith", "email": "jane.smith@example.com"},
        ]
        user_instances = [User.objects.create(**user_data) for user_data in users]

        # Populate teams
        teams = [
            {"name": "Team Alpha", "description": "A team of fitness enthusiasts"},
            {"name": "Team Beta", "description": "A team of competitive athletes"},
        ]
        team_instances = [Team.objects.create(**team_data) for team_data in teams]

        # Populate activities
        activities = [
            {"user": user_instances[0], "type": "Running", "duration": 30},
            {"user": user_instances[1], "type": "Cycling", "duration": 45},
        ]
        [Activity.objects.create(**activity_data) for activity_data in activities]

        # Populate leaderboard
        leaderboard_entries = [
            {"user": user_instances[0], "score": 120},
            {"user": user_instances[1], "score": 150},
        ]
        [Leaderboard.objects.create(**entry_data) for entry_data in leaderboard_entries]

        # Populate workouts
        workouts = [
            {"name": "Morning Run", "description": "5km run", "duration": 30},
            {"name": "Evening Yoga", "description": "Relaxing yoga session", "duration": 60},
        ]
        [Workout.objects.create(**workout_data) for workout_data in workouts]

        self.stdout.write(self.style.SUCCESS("Database populated with test data for OctoFit tracker."))
