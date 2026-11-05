
from django.core.management.base import BaseCommand
from django.core.exceptions import ValidationError

from skills.models import AssessmentQuestion, Skill


# ============================================================
# PYTHON QUESTION BANKS
# ============================================================

from skills.question_bank import QUESTION_BANK
from skills.question_bank_extra import QUESTION_BANK_EXTRA
from skills.question_bank_extra2 import QUESTION_BANK_EXTRA2
from skills.question_bank_extra3 import QUESTION_BANK_EXTRA3

from skills.question_bank_python_beginner1 import QUESTION_BANK_PYTHON_BEGINNER1
from skills.question_bank_python_intermediate1 import QUESTION_BANK_PYTHON_INTERMEDIATE1
from skills.question_bank_python_advanced1 import QUESTION_BANK_PYTHON_ADVANCED1


# ============================================================
# DATA STRUCTURES QUESTION BANKS
# ============================================================

from skills.question_bank_ds_intermediate import QUESTION_BANK_DS_INTERMEDIATE
from skills.question_bank_ds_intermediate3 import QUESTION_BANK_DS_INTERMEDIATE3
from skills.question_bank_ds_intermediate4 import QUESTION_BANK_DS_INTERMEDIATE4
from skills.question_bank_ds_advanced1 import QUESTION_BANK_DS_ADVANCED1
from skills.question_bank_ds_advanced2 import QUESTION_BANK_DS_ADVANCED2


# ============================================================
# DJANGO QUESTION BANKS
# ============================================================

from skills.question_bank_django_beginner1 import QUESTION_BANK_DJANGO_BEGINNER1
from skills.question_bank_django_beginner2 import QUESTION_BANK_DJANGO_BEGINNER2
from skills.question_bank_django_intermediate1 import QUESTION_BANK_DJANGO_INTERMEDIATE1
from skills.question_bank_django_intermediate2 import QUESTION_BANK_DJANGO_INTERMEDIATE2
from skills.question_bank_django_advanced1 import QUESTION_BANK_DJANGO_ADVANCED1
from skills.question_bank_django_advanced2 import QUESTION_BANK_DJANGO_ADVANCED2


# ============================================================
# GIT & GITHUB QUESTION BANKS
# ============================================================

from skills.question_bank_git_beginner1 import QUESTION_BANK_GIT_BEGINNER1
from skills.question_bank_git_beginner2 import QUESTION_BANK_GIT_BEGINNER2
from skills.question_bank_git_intermediate1 import QUESTION_BANK_GIT_INTERMEDIATE1
from skills.question_bank_git_intermediate2 import QUESTION_BANK_GIT_INTERMEDIATE2
from skills.question_bank_git_advanced1 import QUESTION_BANK_GIT_ADVANCED1
from skills.question_bank_git_advanced2 import QUESTION_BANK_GIT_ADVANCED2


# ============================================================
# JAVA QUESTION BANKS
# ============================================================

from skills.question_bank_java_beginner1 import QUESTION_BANK_JAVA_BEGINNER1
from skills.question_bank_java_intermediate1 import QUESTION_BANK_JAVA_INTERMEDIATE1
from skills.question_bank_java_advanced1 import QUESTION_BANK_JAVA_ADVANCED1


# ============================================================
# C PROGRAMMING QUESTION BANKS
# ============================================================

from skills.question_bank_c_beginner1 import QUESTION_BANK_C_BEGINNER1
from skills.question_bank_c_intermediate1 import QUESTION_BANK_C_INTERMEDIATE1
from skills.question_bank_c_advanced1 import QUESTION_BANK_C_ADVANCED1


# ============================================================
# SQL & DATABASES QUESTION BANKS
# ============================================================

from skills.question_bank_sql_beginner1 import QUESTION_BANK_SQL_BEGINNER1
from skills.question_bank_sql_intermediate1 import QUESTION_BANK_SQL_INTERMEDIATE1
from skills.question_bank_sql_advanced1 import QUESTION_BANK_SQL_ADVANCED1


# ============================================================
# WEB TECHNOLOGIES QUESTION BANKS
# ============================================================

from skills.question_bank_web_beginner1 import QUESTION_BANK_WEB_BEGINNER1
from skills.question_bank_web_intermediate1 import QUESTION_BANK_WEB_INTERMEDIATE1
from skills.question_bank_web_advanced1 import QUESTION_BANK_WEB_ADVANCED1


# ============================================================
# ALL QUESTION BANKS
# ============================================================

ALL_QUESTION_BANKS = [

    # Python
    QUESTION_BANK,
    QUESTION_BANK_EXTRA,
    QUESTION_BANK_EXTRA2,
    QUESTION_BANK_EXTRA3,
    QUESTION_BANK_PYTHON_BEGINNER1,
    QUESTION_BANK_PYTHON_INTERMEDIATE1,
    QUESTION_BANK_PYTHON_ADVANCED1,

    # Data Structures
    QUESTION_BANK_DS_INTERMEDIATE,
    QUESTION_BANK_DS_INTERMEDIATE3,
    QUESTION_BANK_DS_INTERMEDIATE4,
    QUESTION_BANK_DS_ADVANCED1,
    QUESTION_BANK_DS_ADVANCED2,

    # Django
    QUESTION_BANK_DJANGO_BEGINNER1,
    QUESTION_BANK_DJANGO_BEGINNER2,
    QUESTION_BANK_DJANGO_INTERMEDIATE1,
    QUESTION_BANK_DJANGO_INTERMEDIATE2,
    QUESTION_BANK_DJANGO_ADVANCED1,
    QUESTION_BANK_DJANGO_ADVANCED2,

    # Git & GitHub
    QUESTION_BANK_GIT_BEGINNER1,
    QUESTION_BANK_GIT_BEGINNER2,
    QUESTION_BANK_GIT_INTERMEDIATE1,
    QUESTION_BANK_GIT_INTERMEDIATE2,
    QUESTION_BANK_GIT_ADVANCED1,
    QUESTION_BANK_GIT_ADVANCED2,

    # Java
    QUESTION_BANK_JAVA_BEGINNER1,
    QUESTION_BANK_JAVA_INTERMEDIATE1,
    QUESTION_BANK_JAVA_ADVANCED1,

    # C Programming
    QUESTION_BANK_C_BEGINNER1,
    QUESTION_BANK_C_INTERMEDIATE1,
    QUESTION_BANK_C_ADVANCED1,

    # SQL & Databases
    QUESTION_BANK_SQL_BEGINNER1,
    QUESTION_BANK_SQL_INTERMEDIATE1,
    QUESTION_BANK_SQL_ADVANCED1,

    # Web Technologies
    QUESTION_BANK_WEB_BEGINNER1,
    QUESTION_BANK_WEB_INTERMEDIATE1,
    QUESTION_BANK_WEB_ADVANCED1,
]


# ============================================================
# FLATTEN QUESTION BANKS
# ============================================================

def flatten_question_bank(bank):

    if not isinstance(bank, (list, tuple)):
        return

    for item in bank:

        if not isinstance(item, dict):
            continue

        questions = item.get("questions")

        if isinstance(questions, list):

            parent_data = {
                key: value
                for key, value in item.items()
                if key != "questions"
            }

            for question in questions:

                if not isinstance(question, dict):
                    continue

                merged_question = {
                    **parent_data,
                    **question,
                }

                yield merged_question

        else:
            yield item


# ============================================================
# MANAGEMENT COMMAND
# ============================================================

class Command(BaseCommand):

    help = "Import all prewritten SkillSphere assessment questions"

    def handle(self, *args, **options):

        self.stdout.write(
            self.style.SUCCESS(
                "\nStarting SkillSphere Question Bank Import...\n"
            )
        )

        created_count = 0
        duplicate_count = 0
        invalid_count = 0
        missing_skill_count = 0
        checked_count = 0

        skill_cache = {}

        # ----------------------------------------------------
        # PROCESS ALL QUESTION BANKS
        # ----------------------------------------------------

        for bank in ALL_QUESTION_BANKS:

            for item in flatten_question_bank(bank):

                checked_count += 1

                skill_name = item.get("skill")
                difficulty = item.get("difficulty")

                question_text = (
                    item.get("question_text")
                    or item.get("question")
                )

                question_options = item.get("options")
                correct_answer = item.get("correct_answer")
                explanation = item.get("explanation", "")

                # --------------------------------------------
                # REQUIRED FIELD VALIDATION
                # --------------------------------------------

                if not skill_name or not difficulty or not question_text:
                    invalid_count += 1
                    continue

                skill_name = str(skill_name).strip()
                difficulty = str(difficulty).strip().lower()
                question_text = str(question_text).strip()

                if difficulty not in [
                    "beginner",
                    "intermediate",
                    "advanced",
                ]:
                    invalid_count += 1
                    continue

                if not isinstance(question_options, list):
                    invalid_count += 1
                    continue

                if len(question_options) != 4:
                    invalid_count += 1
                    continue

                if not all(
                    isinstance(option, str) and option.strip()
                    for option in question_options
                ):
                    invalid_count += 1
                    continue

                if (
                    not isinstance(correct_answer, int)
                    or isinstance(correct_answer, bool)
                    or correct_answer not in range(4)
                ):
                    invalid_count += 1
                    continue

                # --------------------------------------------
                # GET SKILL
                # --------------------------------------------

                skill_key = skill_name.lower()

                if skill_key not in skill_cache:

                    skill_cache[skill_key] = Skill.objects.filter(
                        name__iexact=skill_name
                    ).first()

                skill = skill_cache[skill_key]

                if skill is None or not skill.is_active:
                    missing_skill_count += 1
                    continue

                # --------------------------------------------
                # DUPLICATE CHECK
                # --------------------------------------------

                duplicate_exists = AssessmentQuestion.objects.filter(
                    skill=skill,
                    difficulty=difficulty,
                    question_text__iexact=question_text,
                ).exists()

                if duplicate_exists:
                    duplicate_count += 1
                    continue

                # --------------------------------------------
                # CREATE QUESTION
                # --------------------------------------------

                question = AssessmentQuestion(
                    skill=skill,
                    question_text=question_text,
                    options=question_options,
                    correct_answer=correct_answer,
                    explanation=explanation,
                    difficulty=difficulty,
                    is_active=True,
                )

                try:

                    question.full_clean()
                    question.save()

                    created_count += 1

                except ValidationError:
                    invalid_count += 1

        # ====================================================
        # FINAL SUMMARY
        # ====================================================

        self.stdout.write("\n")

        self.stdout.write(
            self.style.SUCCESS(
                "QUESTION BANK IMPORT COMPLETED"
            )
        )

        self.stdout.write("-----------------------------------")

        self.stdout.write(
            f"Total questions checked : {checked_count}"
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"New questions created   : {created_count}"
            )
        )

        self.stdout.write(
            f"Duplicates skipped      : {duplicate_count}"
        )

        self.stdout.write(
            f"Invalid questions       : {invalid_count}"
        )

        self.stdout.write(
            f"Missing skills          : {missing_skill_count}"
        )

        self.stdout.write("-----------------------------------")

        self.stdout.write(
            self.style.SUCCESS(
                "\nExisting database questions were preserved."
            )
        )
