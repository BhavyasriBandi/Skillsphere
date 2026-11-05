
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from skills.models import Skill, AssessmentQuestion


QUESTIONS = [
    {
        "question_text": "Which of the following is used to store a value in a Python variable?",
        "options": ["=", "==", "!=", ":="],
        "correct_answer": 0,
        "explanation": "The assignment operator (=) assigns a value to a variable."
    },
    {
        "question_text": "What is the data type of the value 25 in Python?",
        "options": ["str", "int", "float", "bool"],
        "correct_answer": 1,
        "explanation": "An integer value without a decimal point has the int data type."
    },
    {
        "question_text": "What is the output of print(type(3.14))?",
        "options": ["<class 'int'>", "<class 'str'>", "<class 'float'>", "<class 'bool'>"],
        "correct_answer": 2,
        "explanation": "A number containing a decimal point is a float."
    },
    {
        "question_text": "Which function is used to display output in Python?",
        "options": ["input()", "display()", "print()", "show()"],
        "correct_answer": 2,
        "explanation": "The print() function displays output on the screen."
    },
    {
        "question_text": "What is the result of 10 // 3 in Python?",
        "options": ["3", "3.33", "1", "0"],
        "correct_answer": 0,
        "explanation": "The floor division operator // returns the quotient rounded down."
    },
    {
        "question_text": "What is the result of 10 % 3?",
        "options": ["3", "1", "0", "10"],
        "correct_answer": 1,
        "explanation": "The modulo operator returns the remainder. The remainder of 10 divided by 3 is 1."
    },
    {
        "question_text": "Which operator checks whether two values are equal?",
        "options": ["=", "==", ">=", "!="],
        "correct_answer": 1,
        "explanation": "The == operator compares two values for equality."
    },
    {
        "question_text": "Which keyword is used to make a decision in Python?",
        "options": ["for", "while", "if", "def"],
        "correct_answer": 2,
        "explanation": "The if keyword executes a block when its condition is true."
    },
    {
        "question_text": "What is the output of this code? x = 5; if x > 3: print('Yes')",
        "options": ["No", "Yes", "5", "Error"],
        "correct_answer": 1,
        "explanation": "Since 5 is greater than 3, the if condition is true and Yes is printed."
    },
    {
        "question_text": "Which keyword is used as an alternative condition after if?",
        "options": ["else if", "elseif", "elif", "otherwise"],
        "correct_answer": 2,
        "explanation": "Python uses elif to check another condition when the previous if condition is false."
    },
    {
        "question_text": "Which loop is commonly used to iterate over a sequence?",
        "options": ["for", "switch", "if", "def"],
        "correct_answer": 0,
        "explanation": "A for loop iterates over items in a sequence such as a list or string."
    },
    {
        "question_text": "How many times does this loop execute? for i in range(4): print(i)",
        "options": ["3", "4", "5", "0"],
        "correct_answer": 1,
        "explanation": "range(4) produces 0, 1, 2 and 3, so the loop executes four times."
    },
    {
        "question_text": "Which keyword immediately exits a loop?",
        "options": ["skip", "stop", "break", "exitloop"],
        "correct_answer": 2,
        "explanation": "The break statement terminates the nearest enclosing loop."
    },
    {
        "question_text": "Which keyword skips the current iteration and continues with the next one?",
        "options": ["pass", "continue", "break", "return"],
        "correct_answer": 1,
        "explanation": "The continue statement skips the remaining statements in the current iteration."
    },
    {
        "question_text": "Which keyword is used to define a function in Python?",
        "options": ["function", "define", "fun", "def"],
        "correct_answer": 3,
        "explanation": "The def keyword defines a function in Python."
    },
    {
        "question_text": "What does the return statement do in a function?",
        "options": ["Repeats the function", "Sends a value back to the caller", "Prints a value automatically", "Defines a variable"],
        "correct_answer": 1,
        "explanation": "The return statement sends a result back to the code that called the function."
    },
    {
        "question_text": "What is the output of len([10, 20, 30])?",
        "options": ["2", "3", "10", "30"],
        "correct_answer": 1,
        "explanation": "The len() function returns the number of elements in the list, which is three."
    },
    {
        "question_text": "Which method adds an element to the end of a Python list?",
        "options": ["add()", "insert_end()", "append()", "push()"],
        "correct_answer": 2,
        "explanation": "The append() method adds one element to the end of a list."
    },
    {
        "question_text": "What is the output of [10, 20, 30][1]?",
        "options": ["10", "20", "30", "1"],
        "correct_answer": 1,
        "explanation": "Python indexing starts at zero, so index 1 refers to the second element."
    },
    {
        "question_text": "Which data structure stores an ordered collection that cannot be modified?",
        "options": ["List", "Dictionary", "Set", "Tuple"],
        "correct_answer": 3,
        "explanation": "A tuple is ordered and immutable, meaning its elements cannot be reassigned."
    },
    {
        "question_text": "How do you create an empty dictionary in Python?",
        "options": ["[]", "()", "{}", "set()"],
        "correct_answer": 2,
        "explanation": "Empty curly braces create an empty dictionary."
    },
    {
        "question_text": "Which method returns the value associated with a dictionary key?",
        "options": ["get()", "append()", "add()", "push()"],
        "correct_answer": 0,
        "explanation": "The get() method retrieves the value associated with a dictionary key."
    },
    {
        "question_text": "Which collection automatically removes duplicate elements?",
        "options": ["List", "Tuple", "Set", "String"],
        "correct_answer": 2,
        "explanation": "A set stores unique elements and removes duplicates."
    },
    {
        "question_text": "What is the output of len(set([1, 2, 2, 3]))?",
        "options": ["4", "3", "2", "1"],
        "correct_answer": 1,
        "explanation": "The set contains only 1, 2 and 3 because duplicate values are removed."
    },
    {
        "question_text": "Which keyword is used to handle exceptions in Python?",
        "options": ["catch", "error", "try", "handle"],
        "correct_answer": 2,
        "explanation": "The try block contains code that may raise an exception."
    },
    {
        "question_text": "Which block executes when an exception occurs in a try block and is caught?",
        "options": ["finally", "except", "else", "def"],
        "correct_answer": 1,
        "explanation": "The except block handles exceptions raised inside the corresponding try block."
    },
    {
        "question_text": "What is the output of bool(0)?",
        "options": ["True", "False", "0", "None"],
        "correct_answer": 1,
        "explanation": "Zero is a falsy numeric value in Python, so bool(0) returns False."
    },
    {
        "question_text": "Which function converts a numeric string such as '25' into an integer?",
        "options": ["str()", "float()", "int()", "bool()"],
        "correct_answer": 2,
        "explanation": "The int() function converts a valid integer string into an integer."
    },
    {
        "question_text": "What is the output of 'Python'[0]?",
        "options": ["P", "y", "n", "Python"],
        "correct_answer": 0,
        "explanation": "String indexing starts at zero, so index 0 returns the first character P."
    },
    {
        "question_text": "Which statement correctly checks whether 5 is greater than 2?",
        "options": ["5 = 2", "5 < 2", "5 > 2", "5 == 2"],
        "correct_answer": 2,
        "explanation": "The greater-than operator > evaluates whether the left value is greater than the right value."
    },
]


class Command(BaseCommand):
    help = "Populate Python beginner assessment question bank."

    def handle(self, *args, **options):

        try:
            skill = Skill.objects.get(
                name__iexact="python",
                is_active=True
            )
        except Skill.DoesNotExist:
            raise CommandError(
                "Active Python skill was not found."
            )
        except Skill.MultipleObjectsReturned:
            raise CommandError(
                "Multiple active Python skills were found."
            )

        saved_count = 0
        skipped_count = 0

        with transaction.atomic():

            for item in QUESTIONS:

                question_text = item["question_text"]

                existing = AssessmentQuestion.objects.filter(
                    skill=skill,
                    difficulty="beginner",
                    question_text__iexact=question_text
                ).exists()

                if existing:
                    skipped_count += 1
                    continue

                question = AssessmentQuestion(
                    skill=skill,
                    question_text=question_text,
                    options=item["options"],
                    correct_answer=item["correct_answer"],
                    explanation=item["explanation"],
                    difficulty="beginner",
                    is_active=True
                )

                question.full_clean()
                question.save()

                saved_count += 1

        total_count = AssessmentQuestion.objects.filter(
            skill=skill,
            difficulty="beginner",
            is_active=True
        ).count()

        self.stdout.write("")
        self.stdout.write(
            self.style.SUCCESS(
                f"Saved questions: {saved_count}"
            )
        )
        self.stdout.write(
            self.style.WARNING(
                f"Skipped existing questions: {skipped_count}"
            )
        )
        self.stdout.write(
            self.style.SUCCESS(
                f"Total Python beginner questions: {total_count}"
            )
        )
