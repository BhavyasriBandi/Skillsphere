
from django.core.management.base import BaseCommand

from achievements.models import Achievement


BADGES = [
    {
        "badge_key": "career-starter",
        "icon": "🎯",
        "title": "Career Starter",
        "description": "Set your first career goal.",
        "category": "Career",
        "requirement": "career",
        "target": 1,
        "points": 20,
        "tier": "bronze",
    },
    {
        "badge_key": "first-assessment",
        "icon": "🧠",
        "title": "First Assessment",
        "description": "Complete your first skill assessment.",
        "category": "Assessment",
        "requirement": "assessment",
        "target": 1,
        "points": 25,
        "tier": "bronze",
    },
    {
        "badge_key": "assessment-pro",
        "icon": "🌟",
        "title": "Assessment Pro",
        "description": "Complete five skill assessments.",
        "category": "Assessment",
        "requirement": "assessment",
        "target": 5,
        "points": 100,
        "tier": "gold",
    },
    {
        "badge_key": "high-scorer",
        "icon": "🏅",
        "title": "High Scorer",
        "description": "Score 80% or higher in an assessment.",
        "category": "Assessment",
        "requirement": "highScore",
        "target": 1,
        "points": 50,
        "tier": "silver",
    },
    {
        "badge_key": "first-project",
        "icon": "💻",
        "title": "Project Builder",
        "description": "Add your first project to your portfolio.",
        "category": "Projects",
        "requirement": "project",
        "target": 1,
        "points": 30,
        "tier": "bronze",
    },
    {
        "badge_key": "project-creator",
        "icon": "🚀",
        "title": "Project Creator",
        "description": "Add three projects to your portfolio.",
        "category": "Projects",
        "requirement": "project",
        "target": 3,
        "points": 75,
        "tier": "silver",
    },
    {
        "badge_key": "challenge-solver",
        "icon": "⚡",
        "title": "Challenge Solver",
        "description": "Complete five coding challenges.",
        "category": "Challenges",
        "requirement": "challenge",
        "target": 5,
        "points": 60,
        "tier": "silver",
    },
    {
        "badge_key": "learning-star",
        "icon": "📚",
        "title": "Learning Star",
        "description": "Complete five learning activities.",
        "category": "Learning",
        "requirement": "lesson",
        "target": 5,
        "points": 60,
        "tier": "silver",
    },
    {
        "badge_key": "interview-ready",
        "icon": "🎤",
        "title": "Interview Ready",
        "description": "Practise five interview questions.",
        "category": "Interview",
        "requirement": "interview",
        "target": 5,
        "points": 60,
        "tier": "silver",
    },
    {
        "badge_key": "skill-gap-master",
        "icon": "🧩",
        "title": "Skill Gap Master",
        "description": "Complete five skill-gap checklist items.",
        "category": "Skills",
        "requirement": "skillGap",
        "target": 5,
        "points": 75,
        "tier": "gold",
    },
    {
        "badge_key": "roadmap-explorer",
        "icon": "🗺️",
        "title": "Roadmap Explorer",
        "description": "Complete five roadmap items.",
        "category": "Roadmap",
        "requirement": "roadmap",
        "target": 5,
        "points": 75,
        "tier": "gold",
    },
    {
        "badge_key": "dedicated-learner",
        "icon": "👑",
        "title": "Dedicated Learner",
        "description": "Earn five different achievements.",
        "category": "Special",
        "requirement": "badges",
        "target": 5,
        "points": 100,
        "tier": "gold",
    },
]


class Command(BaseCommand):
    help = "Seed the SkillSphere achievement definitions."

    def handle(self, *args, **options):
        created_count = 0
        updated_count = 0

        for badge in BADGES:
            key = badge["badge_key"]
            defaults = {
                field: value
                for field, value in badge.items()
                if field != "badge_key"
            }

            _, created = Achievement.objects.update_or_create(
                badge_key=key,
                defaults=defaults,
            )

            if created:
                created_count += 1
            else:
                updated_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Created: {created_count}; updated: {updated_count}; "
                f"total in seed list: {len(BADGES)}."
            )
        )
