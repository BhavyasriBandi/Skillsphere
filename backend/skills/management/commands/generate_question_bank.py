
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from skills.models import Skill, AssessmentQuestion
from skills.ai_service import (
    generate_assessment_questions,
    questions_are_similar,
)


DIFFICULTIES = [
    "beginner",
    "intermediate",
    "advanced",
]

BATCH_SIZE = 10
DEFAULT_TARGET = 30


class Command(BaseCommand):
    help = (
        "Generate AI assessment questions for every skill "
        "and difficulty and save them in the database."
    )

    def add_arguments(self, parser):
        parser.add_argument(
            "--skill",
            type=str,
            help="Generate questions for one specific skill.",
        )

        parser.add_argument(
            "--target",
            type=int,
            default=DEFAULT_TARGET,
            help="Target number of questions per difficulty.",
        )

    def handle(self, *args, **options):
        skill_name = options.get("skill")
        target = options["target"]

        if target < 10:
            raise CommandError(
                "Target must be at least 10 questions."
            )

        skills = Skill.objects.filter(
            is_active=True
        ).order_by("name")

        if skill_name:
            skills = skills.filter(name__iexact=skill_name.strip())

        if not skills.exists():
            raise CommandError(
                "No matching active skills were found."
            )

        self.stdout.write(
            self.style.SUCCESS(
                f"Starting AI question-bank generation. "
                f"Target: {target} questions per difficulty."
            )
        )

        for skill in skills:
            self.generate_for_skill(skill, target)

        self.stdout.write(
            self.style.SUCCESS(
                "Question-bank generation completed."
            )
        )

    def generate_for_skill(self, skill, target):
        self.stdout.write(
            self.style.MIGRATE_HEADING(
                f"\nSkill: {skill.name}"
            )
        )

        for difficulty in DIFFICULTIES:
            self.generate_for_difficulty(
                skill,
                difficulty,
                target,
            )

    def generate_for_difficulty(
        self,
        skill,
        difficulty,
        target,
    ):
        existing = list(
            AssessmentQuestion.objects.filter(
                skill=skill,
                difficulty=difficulty,
                is_active=True,
            ).order_by("id")
        )

        existing_questions = [
            question.question_text
            for question in existing
        ]

        remaining = target - len(existing)

        if remaining <= 0:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{difficulty}: Already has "
                    f"{len(existing)} questions. Skipping."
                )
            )
            return

        self.stdout.write(
            f"{difficulty}: {len(existing)} available, "
            f"{remaining} more needed."
        )

        generated_count = 0
        batch_number = 0
        max_batches = max(3, (remaining // BATCH_SIZE) + 3)

        while generated_count < remaining:
            batch_number += 1

            if batch_number > max_batches:
                raise CommandError(
                    f"Could not reach the target for "
                    f"{skill.name} - {difficulty}. "
                    f"Generated {generated_count} new questions."
                )

            self.stdout.write(
                f"Generating batch {batch_number} "
                f"for {skill.name} - {difficulty}..."
            )

            try:
                generated_questions = generate_assessment_questions(
                    skill_name=skill.name,
                    difficulty=difficulty,
                    previous_questions=existing_questions,
                )

            except Exception as error:
                raise CommandError(
                    f"AI generation failed for "
                    f"{skill.name} - {difficulty}: {error}"
                ) from error

            batch_saved = 0

            for item in generated_questions:
                question_text = item["question_text"]

                duplicate = any(
                    questions_are_similar(
                        question_text,
                        previous,
                    )
                    for previous in existing_questions
                )

                if duplicate:
                    self.stdout.write(
                        self.style.WARNING(
                            "Skipped a duplicate question."
                        )
                    )
                    continue

                question = AssessmentQuestion(
                    skill=skill,
                    question_text=question_text,
                    options=item["options"],
                    correct_answer=item["correct_answer"],
                    explanation=item["explanation"],
                    difficulty=difficulty,
                    is_active=True,
                )

                try:
                    question.full_clean()

                    with transaction.atomic():
                        question.save()

                except Exception as error:
                    self.stdout.write(
                        self.style.WARNING(
                            f"Question rejected: {error}"
                        )
                    )
                    continue

                existing_questions.append(question_text)
                generated_count += 1
                batch_saved += 1

                if generated_count >= remaining:
                    break

            self.stdout.write(
                self.style.SUCCESS(
                    f"Saved {batch_saved} questions "
                    f"in this batch."
                )
            )

            if batch_saved == 0:
                raise CommandError(
                    f"No valid new questions were saved for "
                    f"{skill.name} - {difficulty}. "
                    "Check the Ollama output and logs."
                )

        final_count = AssessmentQuestion.objects.filter(
            skill=skill,
            difficulty=difficulty,
            is_active=True,
        ).count()

        self.stdout.write(
            self.style.SUCCESS(
                f"{difficulty}: Question bank now has "
                f"{final_count} active questions."
            )
        )
