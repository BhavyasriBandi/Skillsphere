from django.core.management.base import BaseCommand
from assessments.models import AssessmentQuestion
from assessments.assessment_question_bank import RAW_QUESTIONS


class Command(BaseCommand):
    help = "Import the existing SkillSphere assessment questions."

    def handle(self, *args, **options):
        created_count = 0
        updated_count = 0

        for skill_name, rows in RAW_QUESTIONS.items():
            skill = (
                "C"
                if skill_name.strip().casefold() == "c"
                else skill_name.strip().title()
            )

            for question_id, question, answers, correct, explanation in rows:
                _, created = AssessmentQuestion.objects.update_or_create(
                    legacy_id=str(question_id),
                    defaults={
                        "skill": skill,
                        "question": question,
                        "options": answers,
                        "correct_answer": correct,
                        "explanation": explanation,
                        "is_active": True,
                    },
                )

                if created:
                    created_count += 1
                else:
                    updated_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Import completed! Created: {created_count}; "
                f"Updated: {updated_count}; "
                f"Total: {AssessmentQuestion.objects.count()}"
            )
        )