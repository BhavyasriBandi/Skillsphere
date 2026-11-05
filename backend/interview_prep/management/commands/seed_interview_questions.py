
from django.core.management.base import BaseCommand
from interview_prep.models import InterviewQuestion


QUESTIONS = [
    {
        "category": "Python",
        "difficulty": "Beginner",
        "question": "What is Python?",
        "suggested_answer": "Python is a high-level, interpreted, general-purpose programming language known for its readable syntax and broad ecosystem.",
        "keywords": ["high-level", "interpreted", "readable syntax"],
    },
    {
        "category": "Python",
        "difficulty": "Beginner",
        "question": "What are Python's main features?",
        "suggested_answer": "Python offers readable syntax, dynamic typing, automatic memory management, a large standard library, and support for multiple programming styles.",
        "keywords": ["readability", "dynamic typing", "standard library"],
    },
    {
        "category": "Python",
        "difficulty": "Beginner",
        "question": "What is the difference between a list and a tuple?",
        "suggested_answer": "A list is mutable, so its elements can be changed. A tuple is immutable, so its elements cannot be reassigned after creation.",
        "keywords": ["list", "tuple", "mutable", "immutable"],
    },
    {
        "category": "Python",
        "difficulty": "Intermediate",
        "question": "What is the difference between == and is in Python?",
        "suggested_answer": "The == operator compares values for equality, while is checks whether two references point to the same object.",
        "keywords": ["equality", "identity", "object"],
    },
    {
        "category": "Python",
        "difficulty": "Intermediate",
        "question": "What are decorators in Python?",
        "suggested_answer": "Decorators are callables that wrap or modify the behavior of another function or class without changing its original source code.",
        "keywords": ["decorator", "wrapper", "function"],
    },
    {
        "category": "Java",
        "difficulty": "Beginner",
        "question": "What is Java?",
        "suggested_answer": "Java is a high-level, class-based programming language that compiles to bytecode and runs on a Java Virtual Machine.",
        "keywords": ["JVM", "bytecode", "object-oriented"],
    },
    {
        "category": "Java",
        "difficulty": "Beginner",
        "question": "What is the JVM?",
        "suggested_answer": "The Java Virtual Machine executes Java bytecode and provides runtime services such as memory management.",
        "keywords": ["JVM", "bytecode", "runtime"],
    },
    {
        "category": "Java",
        "difficulty": "Beginner",
        "question": "What is the difference between JDK, JRE, and JVM?",
        "suggested_answer": "The JVM executes bytecode, the JRE provides the JVM and runtime libraries, and the JDK includes development tools as well as the runtime.",
        "keywords": ["JDK", "JRE", "JVM"],
    },
    {
        "category": "Java",
        "difficulty": "Intermediate",
        "question": "What is method overloading in Java?",
        "suggested_answer": "Method overloading means defining multiple methods with the same name but different parameter lists.",
        "keywords": ["overloading", "parameters", "compile-time"],
    },
    {
        "category": "Java",
        "difficulty": "Intermediate",
        "question": "What is the difference between an interface and an abstract class?",
        "suggested_answer": "An interface defines a contract that classes implement. An abstract class can provide shared state and implementation as well as abstract methods.",
        "keywords": ["interface", "abstract class", "implementation"],
    },
    {
        "category": "C",
        "difficulty": "Beginner",
        "question": "What is the C programming language?",
        "suggested_answer": "C is a procedural, general-purpose programming language commonly used for systems programming and applications requiring low-level control.",
        "keywords": ["procedural", "compiled", "systems programming"],
    },
    {
        "category": "C",
        "difficulty": "Beginner",
        "question": "What is a pointer in C?",
        "suggested_answer": "A pointer is a variable that stores the memory address of an object or function.",
        "keywords": ["pointer", "memory address", "dereference"],
    },
    {
        "category": "C",
        "difficulty": "Intermediate",
        "question": "What is the difference between malloc() and calloc()?",
        "suggested_answer": "Both allocate memory dynamically. malloc() leaves the allocated bytes uninitialized, while calloc() allocates space for multiple elements and initializes the bytes to zero.",
        "keywords": ["dynamic memory", "malloc", "calloc"],
    },
    {
        "category": "C",
        "difficulty": "Intermediate",
        "question": "What is the difference between a structure and a union in C?",
        "suggested_answer": "A structure allocates storage for each member separately. A union shares the same storage among its members.",
        "keywords": ["structure", "union", "memory"],
    },
    {
        "category": "SQL",
        "difficulty": "Beginner",
        "question": "What is SQL?",
        "suggested_answer": "SQL is a language used to define, query, and manipulate data in relational database systems.",
        "keywords": ["SQL", "database", "relational"],
    },
    {
        "category": "SQL",
        "difficulty": "Beginner",
        "question": "What is the difference between WHERE and HAVING?",
        "suggested_answer": "WHERE filters rows before grouping, while HAVING filters groups after GROUP BY is applied.",
        "keywords": ["WHERE", "HAVING", "GROUP BY"],
    },
    {
        "category": "SQL",
        "difficulty": "Intermediate",
        "question": "What is a JOIN in SQL?",
        "suggested_answer": "A JOIN combines rows from two or more tables based on a related column or join condition.",
        "keywords": ["JOIN", "tables", "join condition"],
    },
    {
        "category": "SQL",
        "difficulty": "Intermediate",
        "question": "What is the difference between a primary key and a foreign key?",
        "suggested_answer": "A primary key uniquely identifies a row in its table. A foreign key references a key in another table or the same table to enforce a relationship.",
        "keywords": ["primary key", "foreign key", "relationship"],
    },
    {
        "category": "React",
        "difficulty": "Beginner",
        "question": "What is React?",
        "suggested_answer": "React is a JavaScript library for building user interfaces using reusable components.",
        "keywords": ["React", "components", "user interface"],
    },
    {
        "category": "React",
        "difficulty": "Beginner",
        "question": "What are props in React?",
        "suggested_answer": "Props are read-only inputs passed from a parent component to a child component.",
        "keywords": ["props", "parent", "child"],
    },
    {
        "category": "React",
        "difficulty": "Intermediate",
        "question": "What is the useState hook?",
        "suggested_answer": "useState is a React hook that adds local state to a function component and provides a setter to update it.",
        "keywords": ["useState", "state", "setter"],
    },
    {
        "category": "Django",
        "difficulty": "Beginner",
        "question": "What is Django?",
        "suggested_answer": "Django is a Python web framework that provides tools for building secure, maintainable web applications.",
        "keywords": ["Django", "Python", "web framework"],
    },
    {
        "category": "Django",
        "difficulty": "Beginner",
        "question": "What is Django ORM?",
        "suggested_answer": "Django's Object-Relational Mapper lets developers query and manipulate database records using Python objects and query methods.",
        "keywords": ["ORM", "models", "querysets"],
    },
    {
        "category": "Django",
        "difficulty": "Intermediate",
        "question": "What is the difference between a project and an app in Django?",
        "suggested_answer": "A project contains the overall configuration and URL setup. An app is a modular component that implements a particular set of features.",
        "keywords": ["project", "app", "modularity"],
    },
    {
        "category": "Data Structures",
        "difficulty": "Beginner",
        "question": "What is a data structure?",
        "suggested_answer": "A data structure is a way to organize and store data so it can be accessed and modified efficiently.",
        "keywords": ["data organization", "access", "efficiency"],
    },
    {
        "category": "Data Structures",
        "difficulty": "Beginner",
        "question": "What is the difference between a stack and a queue?",
        "suggested_answer": "A stack follows last-in, first-out (LIFO), while a queue follows first-in, first-out (FIFO).",
        "keywords": ["stack", "queue", "LIFO", "FIFO"],
    },
    {
        "category": "Data Structures",
        "difficulty": "Intermediate",
        "question": "What is a linked list?",
        "suggested_answer": "A linked list is a collection of nodes where each node stores data and one or more links to other nodes.",
        "keywords": ["nodes", "links", "dynamic"],
    },
]


class Command(BaseCommand):
    help = "Seed the Interview Prep question bank."

    def handle(self, *args, **options):
        created_count = 0
        updated_count = 0

        for item in QUESTIONS:
            _, created = InterviewQuestion.objects.update_or_create(
                question=item["question"],
                defaults={
                    "category": item["category"],
                    "difficulty": item["difficulty"],
                    "suggested_answer": item["suggested_answer"],
                    "keywords": item["keywords"],
                    "explanation": "",
                    "is_active": True,
                },
            )

            if created:
                created_count += 1
            else:
                updated_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Interview Prep seeding complete. "
                f"Created: {created_count}; updated: {updated_count}; "
                f"total in this seed list: {len(QUESTIONS)}."
            )
        )
