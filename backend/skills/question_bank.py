
QUESTION_BANK = [
    {
        "skill": "python",
        "difficulty": "intermediate",
        "questions": [
            {
                "question_text": "What is the output of [x * 2 for x in range(3)]?",
                "options": ["[0, 1, 2]", "[0, 2, 4]", "[2, 4, 6]", "[1, 2, 3]"],
                "correct_answer": 1,
                "explanation": "The list comprehension multiplies each value by 2."
            },
            {
                "question_text": "Which keyword is used to handle exceptions in Python?",
                "options": ["catch", "handle", "except", "error"],
                "correct_answer": 2,
                "explanation": "The except block handles exceptions raised inside a try block."
            },
            {
                "question_text": "What does enumerate() return?",
                "options": ["Only values", "Index-value pairs", "Only indexes", "A dictionary"],
                "correct_answer": 1,
                "explanation": "enumerate() produces index and value pairs."
            },
            {
                "question_text": "Which collection does not allow duplicate elements?",
                "options": ["List", "Tuple", "Set", "Dictionary"],
                "correct_answer": 2,
                "explanation": "A set stores unique elements."
            },
            {
                "question_text": "What is the purpose of __init__()?",
                "options": ["Destroy an object", "Initialize an object", "Import a module", "Define a loop"],
                "correct_answer": 1,
                "explanation": "__init__ initializes an object's attributes."
            },
            {
                "question_text": "What is len({'a': 1, 'b': 2})?",
                "options": ["1", "2", "3", "4"],
                "correct_answer": 1,
                "explanation": "The dictionary contains two key-value pairs."
            },
            {
                "question_text": "Which keyword creates an anonymous function?",
                "options": ["def", "lambda", "anonymous", "func"],
                "correct_answer": 1,
                "explanation": "lambda creates a small anonymous function."
            },
            {
                "question_text": "What does zip() do?",
                "options": ["Sorts a list", "Combines corresponding iterable elements", "Removes duplicates", "Reverses a sequence"],
                "correct_answer": 1,
                "explanation": "zip() groups corresponding elements from multiple iterables."
            },
            {
                "question_text": "Which file mode appends data without deleting existing content?",
                "options": ["r", "w", "a", "x"],
                "correct_answer": 2,
                "explanation": "The a mode opens a file for appending."
            },
            {
                "question_text": "What is bool([])?",
                "options": ["True", "False", "None", "Error"],
                "correct_answer": 1,
                "explanation": "An empty list is considered false."
            },
            {
                "question_text": "What is list(map(lambda x: x + 1, [1, 2, 3]))?",
                "options": ["[1, 2, 3]", "[2, 3, 4]", "[3, 4, 5]", "[2, 4, 6]"],
                "correct_answer": 1,
                "explanation": "map() applies the lambda function to every element."
            },
            {
                "question_text": "Which dictionary method safely retrieves a value?",
                "options": ["get()", "find()", "value()", "search()"],
                "correct_answer": 0,
                "explanation": "get() safely retrieves a value and can return a default."
            },
            {
                "question_text": "What does a finally block do?",
                "options": ["Runs only on exceptions", "Runs only without exceptions", "Normally runs in either case", "Stops execution"],
                "correct_answer": 2,
                "explanation": "finally normally executes whether an exception occurs or not."
            },
            {
                "question_text": "Which operator checks object identity?",
                "options": ["==", "is", "in", "!"],
                "correct_answer": 1,
                "explanation": "is checks whether two references point to the same object."
            },
            {
                "question_text": "What is 'python'.upper()?",
                "options": ["Python", "PYTHON", "python", "PyThOn"],
                "correct_answer": 1,
                "explanation": "upper() converts letters to uppercase."
            },
            {
                "question_text": "Which keyword accesses a variable in an enclosing function scope?",
                "options": ["global", "static", "nonlocal", "outer"],
                "correct_answer": 2,
                "explanation": "nonlocal allows assignment to an enclosing function's variable."
            },
            {
                "question_text": "What is sorted([3, 1, 2])?",
                "options": ["[3, 2, 1]", "[1, 2, 3]", "[2, 1, 3]", "None"],
                "correct_answer": 1,
                "explanation": "sorted() returns a new list in ascending order."
            },
            {
                "question_text": "Which module provides regular expression operations?",
                "options": ["math", "random", "re", "os"],
                "correct_answer": 2,
                "explanation": "The re module provides regular expression operations."
            },
            {
                "question_text": "What does *args collect?",
                "options": ["Extra positional arguments", "Only keyword arguments", "Return values", "Global variables"],
                "correct_answer": 0,
                "explanation": "*args collects extra positional arguments into a tuple."
            },
            {
                "question_text": "What is isinstance(10, int)?",
                "options": ["True", "False", "10", "None"],
                "correct_answer": 0,
                "explanation": "10 is an instance of int."
            },
            {
                "question_text": "What is the output of [1, 2, 3][1:]?",
                "options": ["[1, 2]", "[2, 3]", "[1, 2, 3]", "[3]"],
                "correct_answer": 1,
                "explanation": "Slicing from index 1 returns elements at indexes 1 and 2."
            },
            {
                "question_text": "Which method removes and returns the last element of a list by default?",
                "options": ["remove()", "delete()", "pop()", "clear()"],
                "correct_answer": 2,
                "explanation": "pop() removes and returns the last list element by default."
            },
            {
                "question_text": "What is the output of 'hello'.replace('l', 'x')?",
                "options": ["hexxo", "hexlo", "hello", "hxxxo"],
                "correct_answer": 0,
                "explanation": "replace() replaces every occurrence of l with x."
            },
            {
                "question_text": "Which statement imports only sqrt from math?",
                "options": ["import sqrt", "from math import sqrt", "include math.sqrt", "using math.sqrt"],
                "correct_answer": 1,
                "explanation": "from math import sqrt imports only the sqrt function."
            },
            {
                "question_text": "What does a Python generator function use to produce values?",
                "options": ["return", "yield", "break", "continue"],
                "correct_answer": 1,
                "explanation": "yield produces values while preserving the generator's execution state."
            },
            {
                "question_text": "What is bool('False')?",
                "options": ["True", "False", "None", "Error"],
                "correct_answer": 0,
                "explanation": "Every non-empty string is truthy, including the string 'False'."
            },
            {
                "question_text": "Which method adds all elements from another iterable to a list?",
                "options": ["append()", "extend()", "insert()", "add()"],
                "correct_answer": 1,
                "explanation": "extend() adds each element from the supplied iterable."
            },
            {
                "question_text": "What is the purpose of the with statement when working with files?",
                "options": ["Automatically close the file", "Delete the file", "Rename the file", "Encrypt the file"],
                "correct_answer": 0,
                "explanation": "A file context manager automatically closes the file when the block exits."
            },
            {
                "question_text": "Which built-in function returns the largest item in an iterable?",
                "options": ["high()", "largest()", "max()", "top()"],
                "correct_answer": 2,
                "explanation": "max() returns the largest item in an iterable."
            },
            {
                "question_text": "What does the @property decorator allow?",
                "options": ["Accessing a method like an attribute", "Creating a loop", "Importing a class", "Deleting an object"],
                "correct_answer": 0,
                "explanation": "@property allows a method to be accessed using attribute syntax."
            },
            {
                "question_text": "What is the output of isinstance(True, int)?",
                "options": ["True", "False", "None", "Error"],
                "correct_answer": 0,
                "explanation": "bool is a subclass of int in Python."
            },
            {
                "question_text": "Which method returns the index of the first matching item in a list?",
                "options": ["find()", "index()", "position()", "locate()"],
                "correct_answer": 1,
                "explanation": "The list index() method returns the index of the first matching item."
            },
            {
                "question_text": "What is the result of set([1, 2, 2, 3])?",
                "options": ["{1, 2, 2, 3}", "{1, 2, 3}", "[1, 2, 3]", "(1, 2, 3)"],
                "correct_answer": 1,
                "explanation": "Creating a set removes duplicate elements."
            },
            {
                "question_text": "Which method checks whether a string starts with a specified prefix?",
                "options": ["begins()", "startswith()", "start()", "prefix()"],
                "correct_answer": 1,
                "explanation": "startswith() checks whether a string begins with the specified prefix."
            },
            {
                "question_text": "What is the output of divmod(17, 5)?",
                "options": ["(3, 2)", "(2, 3)", "(3, 5)", "(2, 2)"],
                "correct_answer": 0,
                "explanation": "divmod() returns the quotient and remainder as a tuple."
            },
            {
                "question_text": "Which method creates a shallow copy of a list?",
                "options": ["copy()", "clone()", "duplicate()", "replicate()"],
                "correct_answer": 0,
                "explanation": "The list copy() method creates a shallow copy."
            },
            {
                "question_text": "What is the output of all([True, 1, 'yes'])?",
                "options": ["True", "False", "None", "Error"],
                "correct_answer": 0,
                "explanation": "All three values are truthy, so all() returns True."
            },
            {
                "question_text": "Which built-in function pairs iterable elements with their indexes?",
                "options": ["zip()", "enumerate()", "map()", "filter()"],
                "correct_answer": 1,
                "explanation": "enumerate() provides an index and value for each element."
            },
            {
                "question_text": "What does the __str__() method define?",
                "options": ["Object's readable string representation", "Object's memory address", "Object's data type", "Object's constructor"],
                "correct_answer": 0,
                "explanation": "__str__() defines the human-readable string representation of an object."
            },
            {
                "question_text": "Which function filters elements using a condition?",
                "options": ["map()", "filter()", "reduce()", "sort()"],
                "correct_answer": 1,
                "explanation": "filter() selects elements for which the supplied function returns True."
            },
            {
                "question_text": "What is the output of any([0, '', 5])?",
                "options": ["True", "False", "None", "Error"],
                "correct_answer": 0,
                "explanation": "any() returns True because 5 is truthy."
            },
            {
                "question_text": "Which operator performs floor division in Python?",
                "options": ["/", "//", "%", "**"],
                "correct_answer": 1,
                "explanation": "The // operator performs floor division."
            },
            {
                "question_text": "What is the output of '  hello  '.strip()?",
                "options": ["hello", "  hello", "hello  ", "  hello  "],
                "correct_answer": 0,
                "explanation": "strip() removes leading and trailing whitespace."
            },
            {
                "question_text": "Which built-in function converts an iterable into an iterator?",
                "options": ["iter()", "next()", "list()", "range()"],
                "correct_answer": 0,
                "explanation": "iter() returns an iterator from an iterable object."
            },
            {
                "question_text": "What does the super() function help access?",
                "options": ["Parent class methods", "Private variables only", "Global functions", "Built-in modules"],
                "correct_answer": 0,
                "explanation": "super() provides access to methods in a parent or next class in the method resolution order."
            },
            {
                "question_text": "What is the output of sum([2, 4, 6])?",
                "options": ["10", "12", "14", "24"],
                "correct_answer": 1,
                "explanation": "sum() adds all elements, producing 12."
            },
            {
                "question_text": "Which dictionary method returns all key-value pairs?",
                "options": ["keys()", "values()", "items()", "pairs()"],
                "correct_answer": 2,
                "explanation": "items() returns a view of dictionary key-value pairs."
            },
            {
                "question_text": "What is the result of 2 ** 3 ** 2 in Python?",
                "options": ["64", "512", "256", "36"],
                "correct_answer": 1,
                "explanation": "Exponentiation is right-associative, so 2 ** (3 ** 2) equals 512."
            },
            {
                "question_text": "Which method splits a string into a list using whitespace by default?",
                "options": ["divide()", "split()", "partition()", "separate()"],
                "correct_answer": 1,
                "explanation": "split() separates a string into a list of substrings."
            },
            {
                "question_text": "What does the isinstance() function check?",
                "options": ["Object type membership", "Variable length", "Object equality", "Memory size"],
                "correct_answer": 0,
                "explanation": "isinstance() checks whether an object belongs to a specified class or its subclasses."
            },
            {
                "question_text": "What is the output of list(reversed([1, 2, 3]))?",
                "options": ["[1, 2, 3]", "[3, 2, 1]", "[2, 1, 3]", "None"],
                "correct_answer": 1,
                "explanation": "reversed() produces an iterator in reverse order, and list() converts it to a list."
            },
            {
                "question_text": "Which exception occurs when accessing a dictionary key that does not exist using square brackets?",
                "options": ["IndexError", "KeyError", "ValueError", "TypeError"],
                "correct_answer": 1,
                "explanation": "Accessing a missing dictionary key with square brackets raises KeyError."
            },
            {
                "question_text": "What does the @staticmethod decorator indicate?",
                "options": ["A method that receives no automatic self or cls argument", "A method that must modify the class", "A method that creates an object", "A method that runs only once"],
                "correct_answer": 0,
                "explanation": "A static method does not receive an automatic instance or class argument."
            },
            {
                "question_text": "Which expression creates a dictionary containing squares of numbers from 1 to 3?",
                "options": ["{x: x*x for x in range(1, 4)}", "[x: x*x for x in range(1, 4)]", "(x: x*x for x in range(1, 4))", "{x*x for x in range(1, 4)}"],
                "correct_answer": 0,
                "explanation": "A dictionary comprehension uses key:value expressions inside curly braces."
            },
            {
                "question_text": "What is the output of 'banana'.count('a')?",
                "options": ["1", "2", "3", "4"],
                "correct_answer": 2,
                "explanation": "The character a appears three times in banana."
            },
            {
                "question_text": "Which built-in function returns the smallest item in an iterable?",
                "options": ["low()", "minimum()", "min()", "small()"],
                "correct_answer": 2,
                "explanation": "min() returns the smallest item."
            },
            {
                "question_text": "What is the output of round(3.14159, 2)?",
                "options": ["3.1", "3.14", "3.15", "3.141"],
                "correct_answer": 1,
                "explanation": "round() rounds the number to two decimal places."
            },
            {
                "question_text": "Which method checks whether all characters in a string are digits?",
                "options": ["isnumber()", "isdigit()", "isnumericstring()", "isint()"],
                "correct_answer": 1,
                "explanation": "isdigit() returns True when all characters are digits."
            },
            {
                "question_text": "What does the __repr__() method provide?",
                "options": ["An official or developer-oriented object representation", "A list of object attributes only", "A memory cleanup operation", "A class inheritance list"],
                "correct_answer": 0,
                "explanation": "__repr__() provides an unambiguous developer-oriented representation of an object."
            },
            {
                "question_text": "Which function can combine two lists element by element into tuples?",
                "options": ["merge()", "zip()", "join()", "append()"],
                "correct_answer": 1,
                "explanation": "zip() pairs elements from corresponding positions in the input iterables."
            },
            {
                "question_text": "What is the output of 'abc'.isalpha()?",
                "options": ["True", "False", "None", "Error"],
                "correct_answer": 0,
                "explanation": "isalpha() returns True because every character is an alphabetic letter."
            },
            {
                "question_text": "Which statement raises an exception manually?",
                "options": ["throw", "raise", "except", "assert"],
                "correct_answer": 1,
                "explanation": "The raise statement explicitly raises an exception."
            },
            {
                "question_text": "What is the output of list(filter(None, [0, 1, '', 'hi']))?",
                "options": ["[0, 1, '', 'hi']", "[1, 'hi']", "[0, '']", "[]"],
                "correct_answer": 1,
                "explanation": "filter(None, iterable) keeps truthy elements and removes falsy ones."
            },
            {
                "question_text": "Which method returns a new string with all occurrences of a substring replaced?",
                "options": ["replace()", "substitute()", "change()", "modify()"],
                "correct_answer": 0,
                "explanation": "The string replace() method returns a new string with replacements."
            },
            {
                "question_text": "What is the output of isinstance([], list)?",
                "options": ["True", "False", "None", "Error"],
                "correct_answer": 0,
                "explanation": "An empty list is an instance of the list class."
            },
            {
                "question_text": "Which method removes all elements from a list?",
                "options": ["remove()", "pop()", "clear()", "delete()"],
                "correct_answer": 2,
                "explanation": "clear() removes all items from a list."
            },
            {
                "question_text": "What is the result of 10 % 3?",
                "options": ["3", "1", "0", "3.33"],
                "correct_answer": 1,
                "explanation": "The modulo operator returns the remainder, which is 1."
            },
            {
                "question_text": "Which keyword is used to define a class in Python?",
                "options": ["object", "class", "struct", "define"],
                "correct_answer": 1,
                "explanation": "The class keyword begins a class definition."
            },
            {
                "question_text": "What does the hasattr() function check?",
                "options": ["Whether an object has a named attribute", "Whether two objects are equal", "Whether an object is iterable", "Whether a variable is global"],
                "correct_answer": 0,
                "explanation": "hasattr() checks whether an object has the specified attribute."
            },
            {
                "question_text": "Which method converts a string to lowercase?",
                "options": ["lower()", "casefolded()", "small()", "downcase()"],
                "correct_answer": 0,
                "explanation": "lower() returns a lowercase version of a string."
            },
            {
                "question_text": "What is the output of len({1, 1, 2, 3})?",
                "options": ["4", "3", "2", "1"],
                "correct_answer": 1,
                "explanation": "A set removes duplicates, leaving three unique elements."
            },
            {
                "question_text": "Which function returns an object's memory identity?",
                "options": ["type()", "id()", "hash()", "repr()"],
                "correct_answer": 1,
                "explanation": "id() returns an object's identity, which is unique during its lifetime."
            },
            {
                "question_text": "What is the output of 'a,b,c'.split(',')?",
                "options": ["['a,b,c']", "['a', 'b', 'c']", "('a', 'b', 'c')", "['abc']"],
                "correct_answer": 1,
                "explanation": "split(',') divides the string at each comma."
            },
            {
                "question_text": "Which built-in function checks whether every element satisfies a condition?",
                "options": ["any()", "all()", "each()", "every()"],
                "correct_answer": 1,
                "explanation": "all() returns True when all elements are truthy."
            },
            {
                "question_text": "What is the result of tuple([1, 2, 3])?",
                "options": ["[1, 2, 3]", "(1, 2, 3)", "{1, 2, 3}", "None"],
                "correct_answer": 1,
                "explanation": "tuple() converts an iterable into a tuple."
            },
            {
                "question_text": "Which method can add an element at a particular list position?",
                "options": ["append()", "extend()", "insert()", "place()"],
                "correct_answer": 2,
                "explanation": "insert(index, value) adds an item at the specified position."
            },
            {
                "question_text": "What does callable(obj) check?",
                "options": ["Whether obj can be called like a function", "Whether obj is a string", "Whether obj is empty", "Whether obj is immutable"],
                "correct_answer": 0,
                "explanation": "callable() checks whether an object appears callable."
            },
            {
                "question_text": "What is the output of 'python'.find('th')?",
                "options": ["1", "2", "3", "-1"],
                "correct_answer": 1,
                "explanation": "The substring th begins at index 2."
            },
            {
                "question_text": "Which built-in type is mutable?",
                "options": ["tuple", "str", "list", "int"],
                "correct_answer": 2,
                "explanation": "Lists are mutable, meaning their contents can be changed."
            },
            {
                "question_text": "What does the @classmethod decorator pass automatically to a method?",
                "options": ["self", "cls", "args", "None"],
                "correct_answer": 1,
                "explanation": "A class method receives the class as its first argument, conventionally named cls."
            },
            {
                "question_text": "What is the output of abs(-15)?",
                "options": ["-15", "15", "0", "Error"],
                "correct_answer": 1,
                "explanation": "abs() returns the absolute value of a number."
            },
            {
                "question_text": "Which module provides tools for working with dates and times?",
                "options": ["datetime", "calendar_only", "timeformat", "dateutil_builtin"],
                "correct_answer": 0,
                "explanation": "The datetime module provides date and time classes."
            },
            {
                "question_text": "What is the output of 'hello'.capitalize()?",
                "options": ["HELLO", "Hello", "hello", "hELLO"],
                "correct_answer": 1,
                "explanation": "capitalize() makes the first character uppercase and the remaining characters lowercase."
            },
            {
                "question_text": "Which function can retrieve the next item from an iterator?",
                "options": ["iter()", "next()", "advance()", "following()"],
                "correct_answer": 1,
                "explanation": "next() retrieves the next item from an iterator."
            },
            {
                "question_text": "What does dict.fromkeys(['a', 'b'], 0) create?",
                "options": ["{'a': 0, 'b': 0}", "{0: 'a', 0: 'b'}", "['a', 'b', 0]", "{'a': 'b'}"],
                "correct_answer": 0,
                "explanation": "fromkeys() creates a dictionary with the given keys and a shared default value."
            },
            {
                "question_text": "What is the output of 5 // 2?",
                "options": ["2.5", "2", "3", "1"],
                "correct_answer": 1,
                "explanation": "Floor division rounds the quotient down to 2."
            },
            {
                "question_text": "Which exception is raised when converting 'abc' to an integer?",
                "options": ["TypeError", "ValueError", "KeyError", "IndexError"],
                "correct_answer": 1,
                "explanation": "int('abc') raises ValueError because the string is not a valid integer representation."
            },
            {
                "question_text": "Which method checks whether a string ends with a specified suffix?",
                "options": ["endswith()", "finish()", "end()", "suffix()"],
                "correct_answer": 0,
                "explanation": "endswith() checks the ending of a string."
            },
            {
                "question_text": "What is the output of len(range(2, 10, 2))?",
                "options": ["3", "4", "5", "8"],
                "correct_answer": 1,
                "explanation": "The range produces 2, 4, 6 and 8, which contains four values."
            },
            {
                "question_text": "Which keyword skips the current loop iteration and continues with the next one?",
                "options": ["break", "pass", "continue", "skip"],
                "correct_answer": 2,
                "explanation": "continue skips the remaining statements in the current iteration."
            },
            {
                "question_text": "What is the output of 'abc' * 2?",
                "options": ["abc2", "abcabc", "aabbcc", "Error"],
                "correct_answer": 1,
                "explanation": "String multiplication repeats the string the specified number of times."
            },
            {
                "question_text": "Which function converts an integer into a string?",
                "options": ["str()", "int()", "repr_int()", "text()"],
                "correct_answer": 0,
                "explanation": "str() converts an object to its string representation."
            },
            {
                "question_text": "What does the del statement do when used with a list index?",
                "options": ["Deletes the selected item", "Returns the selected item", "Sorts the list", "Copies the list"],
                "correct_answer": 0,
                "explanation": "del removes the item at the specified index."
            },
            {
                "question_text": "Which operator tests whether a value belongs to a sequence or collection?",
                "options": ["is", "in", "==", "not"],
                "correct_answer": 1,
                "explanation": "The in operator checks membership."
            },
            {
                "question_text": "What is the output of min([8, 3, 6])?",
                "options": ["8", "3", "6", "17"],
                "correct_answer": 1,
                "explanation": "min() returns the smallest value, which is 3."
            },
            {
                "question_text": "Which function converts a string representation of a number into a floating-point value?",
                "options": ["int()", "float()", "str()", "complex_only()"],
                "correct_answer": 1,
                "explanation": "float() converts a compatible numeric string into a floating-point value."
            },
            {
                "question_text": "What is the output of 'a' in 'cat'?",
                "options": ["True", "False", "None", "Error"],
                "correct_answer": 0,
                "explanation": "The character a is present in the string cat."
            },
            {
                "question_text": "Which method returns a list of dictionary keys?",
                "options": ["keys()", "items()", "values()", "get()"],
                "correct_answer": 0,
                "explanation": "keys() returns a view of the dictionary's keys."
            },
            {
                "question_text": "What does the isinstance() function return?",
                "options": ["A Boolean value", "A string", "An integer count", "A list"],
                "correct_answer": 0,
                "explanation": "isinstance() returns True or False."
            },
            {
                "question_text": "What is the output of round(8.765, 1)?",
                "options": ["8.7", "8.8", "8.76", "9.0"],
                "correct_answer": 1,
                "explanation": "Rounding 8.765 to one decimal place gives 8.8."
            },
            {
                "question_text": "Which statement is used to provide an alternative branch when an if condition is false?",
                "options": ["otherwise", "else", "elifonly", "default"],
                "correct_answer": 1,
                "explanation": "The else block runs when the preceding if condition is false."
            },
            {
                "question_text": "What is the output of bool(0)?",
                "options": ["True", "False", "None", "Error"],
                "correct_answer": 1,
                "explanation": "Numeric zero is a falsy value in Python."
            },
            {
                "question_text": "Which built-in function creates an iterable sequence of numbers?",
                "options": ["range()", "sequence()", "numbers()", "loop()"],
                "correct_answer": 0,
                "explanation": "range() produces an immutable sequence of integers."
            },
            {
                "question_text": "What does the assert statement do?",
                "options": ["Checks a condition and raises AssertionError if false", "Always stops the program", "Creates a variable", "Handles every exception"],
                "correct_answer": 0,
                "explanation": "assert checks a condition and raises AssertionError when it is false."
            },
            {
                "question_text": "Which function returns the type of an object?",
                "options": ["typeof()", "type()", "classof()", "kind()"],
                "correct_answer": 1,
                "explanation": "type() returns the object's type."
            },
            {
                "question_text": "What is the output of 'PYTHON'.lower()?",
                "options": ["Python", "python", "PYTHON", "pYTHON"],
                "correct_answer": 1,
                "explanation": "lower() converts all alphabetic characters to lowercase."
            },
            {
                "question_text": "Which collection uses key-value pairs?",
                "options": ["List", "Tuple", "Dictionary", "Set"],
                "correct_answer": 2,
                "explanation": "A dictionary stores values associated with unique keys."
            },
            {
                "question_text": "What does the set intersection operator & return?",
                "options": ["Union", "Common elements", "Difference", "Symmetric difference"],
                "correct_answer": 1,
                "explanation": "The & operator returns elements common to both sets."
            },
            {
                "question_text": "Which method removes a specified key and returns its value from a dictionary?",
                "options": ["remove()", "pop()", "clear()", "discard()"],
                "correct_answer": 1,
                "explanation": "Dictionary pop() removes the specified key and returns its value."
            },
            {
                "question_text": "What is the output of list(range(1, 5))?",
                "options": ["[1, 2, 3, 4]", "[1, 2, 3, 4, 5]", "[0, 1, 2, 3, 4]", "[2, 3, 4, 5]"],
                "correct_answer": 0,
                "explanation": "The stop value 5 is excluded from range()."
            },
            {
                "question_text": "Which special method is called when an object is created?",
                "options": ["__start__", "__init__", "__create__", "__newclass__"],
                "correct_answer": 1,
                "explanation": "__init__ initializes the new instance after it has been created."
            },
            {
                "question_text": "What is the output of 'hello world'.title()?",
                "options": ["HELLO WORLD", "Hello World", "hello world", "Hello world"],
                "correct_answer": 1,
                "explanation": "title() capitalizes the first letter of each word."
            },
            {
                "question_text": "Which built-in function returns the number of elements in an object?",
                "options": ["count()", "size()", "len()", "length()"],
                "correct_answer": 2,
                "explanation": "len() returns the number of elements in a supported object."
            },
            {
                "question_text": "What is the output of 3 != 4?",
                "options": ["True", "False", "None", "Error"],
                "correct_answer": 0,
                "explanation": "The values 3 and 4 are not equal."
            },
            {
                "question_text": "Which function opens a file in Python?",
                "options": ["file()", "open()", "readfile()", "load()"],
                "correct_answer": 1,
                "explanation": "open() opens a file and returns a file object."
            },
            {
                "question_text": "What is the output of 'python'[0]?",
                "options": ["p", "y", "n", "python"],
                "correct_answer": 0,
                "explanation": "Python sequences use zero-based indexing, so index 0 is p."
            },
            {
                "question_text": "Which method checks whether a string contains only whitespace characters?",
                "options": ["isspace()", "isblank()", "isempty()", "whitespace()"],
                "correct_answer": 0,
                "explanation": "isspace() returns True when the string is non-empty and all characters are whitespace."
            },
            {
                "question_text": "What does the break statement do inside a loop?",
                "options": ["Skips one iteration", "Terminates the nearest loop", "Restarts the loop", "Does nothing"],
                "correct_answer": 1,
                "explanation": "break immediately terminates the nearest enclosing loop."
            },
            {
                "question_text": "Which operator is used for exponentiation?",
                "options": ["^", "**", "//", "%%"],
                "correct_answer": 1,
                "explanation": "The ** operator performs exponentiation."
            },
            {
                "question_text": "What is the output of bool(None)?",
                "options": ["True", "False", "None", "Error"],
                "correct_answer": 1,
                "explanation": "None is a falsy value in Python."
            },
            {
                "question_text": "Which function can convert a sequence of key-value pairs into a dictionary?",
                "options": ["dict()", "set()", "tuple()", "pairs()"],
                "correct_answer": 0,
                "explanation": "dict() can construct a dictionary from key-value pairs."
            },
            {
                "question_text": "What is the output of 'banana'.startswith('ban')?",
                "options": ["True", "False", "None", "Error"],
                "correct_answer": 0,
                "explanation": "The string banana begins with ban."
            },
            {
                "question_text": "Which method returns the values in a dictionary?",
                "options": ["keys()", "items()", "values()", "get()"],
                "correct_answer": 2,
                "explanation": "values() returns a view of dictionary values."
            },
            {
                "question_text": "What does the list comprehension [x for x in range(5) if x % 2 == 0] produce?",
                "options": ["[1, 3]", "[0, 2, 4]", "[0, 1, 2, 3, 4]", "[2, 4]"],
                "correct_answer": 1,
                "explanation": "The condition selects the even numbers 0, 2 and 4."
            },
            {
                "question_text": "Which exception is raised when a list index is outside its valid range?",
                "options": ["KeyError", "IndexError", "ValueError", "NameError"],
                "correct_answer": 1,
                "explanation": "Accessing a list index outside its valid range raises IndexError."
            },
            {
                "question_text": "What is the output of 'hello'.endswith('lo')?",
                "options": ["True", "False", "None", "Error"],
                "correct_answer": 0,
                "explanation": "The string hello ends with lo."
            },
            {
                "question_text": "Which built-in function can combine an iterable into a string using a separator?",
                "options": ["split()", "join()", "merge()", "concat()"],
                "correct_answer": 1,
                "explanation": "join() combines strings from an iterable using the separator string."
            },
            {
                "question_text": "What does the copy module's deepcopy() function do?",
                "options": ["Creates a deep copy of an object", "Creates a reference only", "Deletes nested values", "Converts an object to a string"],
                "correct_answer": 0,
                "explanation": "deepcopy() recursively copies nested objects rather than sharing their references."
            },
            {
                "question_text": "What is the output of 7 / 2?",
                "options": ["3", "3.5", "4", "2"],
                "correct_answer": 1,
                "explanation": "The / operator performs true division and returns 3.5."
            },
            {
                "question_text": "Which function returns the hash value of a hashable object?",
                "options": ["id()", "hash()", "key()", "digest()"],
                "correct_answer": 1,
                "explanation": "hash() returns an object's hash value when it is hashable."
            },
            {
                "question_text": "What is the output of 'abc'.upper().lower()?",
                "options": ["ABC", "abc", "Abc", "Error"],
                "correct_answer": 1,
                "explanation": "upper() creates ABC and lower() converts it back to abc."
            },
            {
                "question_text": "Which method adds a single element to a set?",
                "options": ["append()", "insert()", "add()", "extend()"],
                "correct_answer": 2,
                "explanation": "The set add() method inserts one element."
            },
            {
                "question_text": "What is the output of list(range(5, 0, -2))?",
                "options": ["[5, 3, 1]", "[5, 4, 3, 2, 1]", "[1, 3, 5]", "[5, 3]"],
                "correct_answer": 0,
                "explanation": "The negative step generates 5, 3 and 1 before reaching the stop boundary."
            },
            {
                "question_text": "Which built-in function returns True if at least one element is truthy?",
                "options": ["all()", "any()", "bool()", "filter()"],
                "correct_answer": 1,
                "explanation": "any() returns True when at least one element is truthy."
            },
            {
                "question_text": "What is the output of 'hello'.find('z')?",
                "options": ["0", "None", "-1", "Error"],
                "correct_answer": 2,
                "explanation": "find() returns -1 when the requested substring is not found."
            },
            {
                "question_text": "Which statement is correct about Python tuples?",
                "options": ["They are mutable", "They are immutable", "They only store numbers", "They cannot be indexed"],
                "correct_answer": 1,
                "explanation": "Tuples are immutable sequences."
            },
            {
                "question_text": "What is the output of 4 in [1, 2, 3, 4]?",
                "options": ["True", "False", "4", "Error"],
                "correct_answer": 0,
                "explanation": "The value 4 is present in the list."
            },
            {
                "question_text": "Which built-in function can return both the largest and smallest values separately?",
                "options": ["minmax()", "maxmin()", "min() and max()", "range()"],
                "correct_answer": 2,
                "explanation": "min() and max() return the smallest and largest values respectively."
            },
            {
                "question_text": "What does the __len__() special method support?",
                "options": ["The len() operation", "String conversion only", "Object creation", "Exception handling"],
                "correct_answer": 0,
                "explanation": "Defining __len__() allows len() to work on custom objects."
            },
            {
                "question_text": "Which method can update a dictionary with key-value pairs from another mapping?",
                "options": ["merge()", "update()", "append()", "extend()"],
                "correct_answer": 1,
                "explanation": "update() adds or replaces dictionary entries from another mapping or iterable."
            },
            {
                "question_text": "What is the output of 'hello world'.split()[1]?",
                "options": ["hello", "world", "h", "Error"],
                "correct_answer": 1,
                "explanation": "split() creates ['hello', 'world']; index 1 is world."
            },
            {
                "question_text": "Which keyword is used to create a function that returns a value?",
                "options": ["function", "def", "return", "yield"],
                "correct_answer": 1,
                "explanation": "def defines a function; return is used inside it to send back a value."
            },
            {
                "question_text": "What is the output of 2 + 3 * 4?",
                "options": ["20", "14", "24", "9"],
                "correct_answer": 1,
                "explanation": "Multiplication is evaluated before addition, so the result is 14."
            },
            {
                "question_text": "Which method returns a new string with leading zeros added to reach a specified width?",
                "options": ["zfill()", "fillzero()", "pad()", "zeroes()"],
                "correct_answer": 0,
                "explanation": "zfill() pads a string on the left with zeros to the requested width."
            },
            {
                "question_text": "What is the output of list(zip([1, 2], ['a', 'b']))?",
                "options": ["[(1, 'a'), (2, 'b')]", "[1, 2, 'a', 'b']", "{1: 'a', 2: 'b'}", "[(1, 2), ('a', 'b')]"],
                "correct_answer": 0,
                "explanation": "zip() pairs elements at corresponding positions."
            },
            {
                "question_text": "Which built-in function can check whether an object is callable?",
                "options": ["isfunction()", "callable()", "function()", "hascall()"],
                "correct_answer": 1,
                "explanation": "callable() returns whether an object can be called."
            },
            {
                "question_text": "What is the output of 'abc'.replace('b', 'x')?",
                "options": ["axc", "xbc", "abx", "abcx"],
                "correct_answer": 0,
                "explanation": "replace() substitutes b with x."
            },
            {
                "question_text": "Which operator performs set union?",
                "options": ["&", "|", "-", "^"],
                "correct_answer": 1,
                "explanation": "The | operator returns elements present in either set."
            },
            {
                "question_text": "What is the output of bool({})?",
                "options": ["True", "False", "None", "Error"],
                "correct_answer": 1,
                "explanation": "An empty dictionary is falsy."
            },
            {
                "question_text": "Which module is commonly used to generate pseudo-random numbers?",
                "options": ["random", "numbers", "math", "choice"],
                "correct_answer": 0,
                "explanation": "The random module provides functions for pseudo-random values and selections."
            },
            {
                "question_text": "What is the output of 'banana'.find('na')?",
                "options": ["1", "2", "3", "-1"],
                "correct_answer": 1,
                "explanation": "The first occurrence of na begins at index 2."
            },
            {
                "question_text": "Which statement about Python dictionaries is correct?",
                "options": ["Keys must be unique", "Values must be unique", "Keys must be lists", "Dictionaries cannot be changed"],
                "correct_answer": 0,
                "explanation": "Dictionary keys are unique; assigning an existing key replaces its value."
            },
            {
                "question_text": "What is the output of list(enumerate(['x', 'y'], start=1))?",
                "options": ["[(0, 'x'), (1, 'y')]", "[(1, 'x'), (2, 'y')]", "['x', 'y']", "[(1, 2), ('x', 'y')]"],
                "correct_answer": 1,
                "explanation": "The start argument sets the first index to 1."
            },
            {
                "question_text": "Which exception is the base class for most built-in non-system-exiting exceptions?",
                "options": ["BaseException", "Exception", "RuntimeError", "Error"],
                "correct_answer": 1,
                "explanation": "Exception is the base class for most built-in application exceptions."
            },
            {
                "question_text": "What is the output of '  Python  '.strip().lower()?",
                "options": ["python", "  python  ", "PYTHON", "Python"],
                "correct_answer": 0,
                "explanation": "strip() removes surrounding whitespace and lower() converts the text to lowercase."
            },
            {
                "question_text": "Which method can remove an arbitrary element from a set and raise KeyError if it is missing?",
                "options": ["discard()", "remove()", "popitem()", "delete()"],
                "correct_answer": 1,
                "explanation": "set.remove() raises KeyError when the specified element is absent."
            },
            {
                "question_text": "What is the output of pow(2, 4)?",
                "options": ["6", "8", "16", "24"],
                "correct_answer": 2,
                "explanation": "pow(2, 4) calculates 2 raised to the power of 4."
            },
            {
                "question_text": "Which built-in function can return an iterator that applies a function to multiple iterables?",
                "options": ["filter()", "map()", "zip()", "iter()"],
                "correct_answer": 1,
                "explanation": "map() applies a function to corresponding items from one or more iterables."
            },
            {
                "question_text": "What is the output of 'hello'.center(9, '-')?",
                "options": ["--hello--", "---hello-", "-hello---", "hello----"],
                "correct_answer": 0,
                "explanation": "center() pads the string on both sides to the requested width."
            },
            {
                "question_text": "Which special method supports the + operator for custom objects?",
                "options": ["__add__()", "__plus__()", "__sum__()", "__concat__()"],
                "correct_answer": 0,
                "explanation": "__add__() implements addition behavior for custom objects."
            },
            {
                "question_text": "What is the output of list(range(3))?",
                "options": ["[1, 2, 3]", "[0, 1, 2]", "[0, 1, 2, 3]", "[3]"],
                "correct_answer": 1,
                "explanation": "range(3) produces 0, 1 and 2."
            },
            {
                "question_text": "Which string method removes a specified prefix if it is present?",
                "options": ["removeprefix()", "strip()", "replaceall()", "cutprefix()"],
                "correct_answer": 0,
                "explanation": "removeprefix() returns a copy without the specified leading prefix when present."
            },
            {
                "question_text": "What is the output of {'a': 1}.get('b', 5)?",
                "options": ["None", "1", "5", "KeyError"],
                "correct_answer": 2,
                "explanation": "get() returns the supplied default value 5 because key b is absent."
            },
            {
                "question_text": "Which function can test whether a value is an instance of a class or its subclass?",
                "options": ["type()", "isinstance()", "issubclass()", "id()"],
                "correct_answer": 1,
                "explanation": "isinstance() checks an object's membership in a class hierarchy."
            },
            {
                "question_text": "What is the output of 'a-b-c'.partition('-')?",
                "options": ["('a', '-', 'b-c')", "['a', 'b', 'c']", "('a-b', '-', 'c')", "('a-b-c', '', '')"],
                "correct_answer": 0,
                "explanation": "partition() splits at the first separator and returns three strings."
            },
            {
                "question_text": "Which built-in function returns a Boolean indicating whether an object has an attribute?",
                "options": ["getattr()", "hasattr()", "setattr()", "delattr()"],
                "correct_answer": 1,
                "explanation": "hasattr() checks for the existence of an attribute."
            },
            {
                "question_text": "What is the output of 9 ** 0?",
                "options": ["0", "1", "9", "Error"],
                "correct_answer": 1,
                "explanation": "Any nonzero number raised to the power zero equals 1."
            },
            {
                "question_text": "Which method can return a formatted string by substituting named placeholders?",
                "options": ["format()", "replace()", "join()", "sub()"],
                "correct_answer": 0,
                "explanation": "str.format() replaces placeholders with supplied values."
            },
            {
                "question_text": "What is the output of list(dict.fromkeys([1, 2, 1, 3]))?",
                "options": ["[1, 2, 1, 3]", "[1, 2, 3]", "[2, 1, 3]", "Error"],
                "correct_answer": 1,
                "explanation": "Dictionary keys are unique and preserve insertion order."
            },
            {
                "question_text": "Which keyword is used to create a context manager block?",
                "options": ["with", "using", "context", "manage"],
                "correct_answer": 0,
                "explanation": "The with statement manages entry to and exit from a context manager."
            },
            {
                "question_text": "What is the output of 'python'.endswith(('on', 'py'))?",
                "options": ["True", "False", "None", "Error"],
                "correct_answer": 0,
                "explanation": "endswith() accepts a tuple of suffixes; python ends with on."
            },
            {
                "question_text": "Which built-in function can convert a sequence into an iterator?",
                "options": ["next()", "iter()", "enumerate()", "range()"],
                "correct_answer": 1,
                "explanation": "iter() obtains an iterator from an iterable."
            },
            {
                "question_text": "What is the output of '  hi  '.lstrip()?",
                "options": ["hi  ", "  hi", "hi", "  hi  "],
                "correct_answer": 0,
                "explanation": "lstrip() removes whitespace from the left side only."
            },
            {
                "question_text": "Which built-in function returns the absolute value of a number?",
                "options": ["round()", "abs()", "fabsint()", "positive()"],
                "correct_answer": 1,
                "explanation": "abs() returns a number's absolute value."
            },
            {
                "question_text": "What is the output of 'hello'.isupper()?",
                "options": ["True", "False", "None", "Error"],
                "correct_answer": 1,
                "explanation": "The letters in hello are lowercase, so isupper() returns False."
            },
            {
                "question_text": "Which method can retrieve a dictionary value and remove its key?",
                "options": ["get()", "pop()", "values()", "items()"],
                "correct_answer": 1,
                "explanation": "pop() returns the value for a key while removing that entry."
            },
            {
                "question_text": "What is the output of list(range(10, 4, -2))?",
                "options": ["[10, 8, 6]", "[10, 8, 6, 4]", "[4, 6, 8, 10]", "[10, 6, 2]"],
                "correct_answer": 0,
                "explanation": "The stop value 4 is excluded, so the sequence is 10, 8, 6."
            },
            {
                "question_text": "Which method checks whether a string contains only lowercase alphabetic characters?",
                "options": ["islower()", "isalpha()", "isupper()", "isdecimal()"],
                "correct_answer": 0,
                "explanation": "islower() returns True when cased characters are lowercase and at least one cased character exists."
            },
            {
                "question_text": "What is the output of 'one,two,three'.rsplit(',', 1)?",
                "options": ["['one', 'two', 'three']", "['one,two', 'three']", "['one', 'two,three']", "['one,two,three']"],
                "correct_answer": 1,
                "explanation": "rsplit() splits from the right, at most once here."
            },
            {
                "question_text": "Which method returns a new set containing elements that are in either set but not both?",
                "options": ["union()", "intersection()", "symmetric_difference()", "difference()"],
                "correct_answer": 2,
                "explanation": "symmetric_difference() returns elements belonging to exactly one of the two sets."
            },
            {
                "question_text": "What is the output of sum(range(1, 4))?",
                "options": ["3", "6", "10", "4"],
                "correct_answer": 1,
                "explanation": "The range produces 1, 2 and 3; their sum is 6."
            },
            {
                "question_text": "Which built-in function retrieves an attribute value by name?",
                "options": ["hasattr()", "getattr()", "setattr()", "delattr()"],
                "correct_answer": 1,
                "explanation": "getattr() retrieves a named attribute from an object."
            },
            {
                "question_text": "What is the output of 'python'.index('y')?",
                "options": ["0", "1", "2", "-1"],
                "correct_answer": 1,
                "explanation": "The character y is at index 1."
            },
            {
                "question_text": "Which method removes and returns an arbitrary element from a set?",
                "options": ["pop()", "remove()", "discard()", "clear()"],
                "correct_answer": 0,
                "explanation": "set.pop() removes and returns an arbitrary element."
            },
            {
                "question_text": "What is the output of 5 ** 2?",
                "options": ["10", "25", "7", "32"],
                "correct_answer": 1,
                "explanation": "5 raised to the power 2 equals 25."
            },
            {
                "question_text": "Which built-in function can create a sorted list from an iterable?",
                "options": ["sort()", "sorted()", "order()", "arrange()"],
                "correct_answer": 1,
                "explanation": "sorted() returns a new sorted list from an iterable."
            },
            {
                "question_text": "What is the output of 'hello'.rfind('l')?",
                "options": ["2", "3", "4", "-1"],
                "correct_answer": 2,
                "explanation": "rfind() returns the highest index of the substring, which is 3? In hello, l occurs at indexes 2 and 3, so the correct result is 3."
            },
            {
                "question_text": "Which special method is used to implement equality comparison with ==?",
                "options": ["__eq__()", "__cmp__()", "__same__()", "__equal__()"],
                "correct_answer": 0,
                "explanation": "__eq__() implements equality comparison."
            },
            {
                "question_text": "What is the output of 'hello'.count('l', 0, 3)?",
                "options": ["1", "2", "3", "0"],
                "correct_answer": 0,
                "explanation": "The slice from index 0 up to but excluding 3 contains one l."
            },
            {
                "question_text": "Which built-in function returns a new list containing an iterable's elements in reverse order?",
                "options": ["reverse()", "reversed()", "backward()", "invert()"],
                "correct_answer": 1,
                "explanation": "reversed() returns an iterator in reverse order; list() can convert it to a list."
            },
            {
                "question_text": "What is the output of '42'.isdigit()?",
                "options": ["True", "False", "None", "Error"],
                "correct_answer": 0,
                "explanation": "Both characters are digits, so isdigit() returns True."
            },
            {
                "question_text": "Which operator checks whether two sets have no common elements?",
                "options": ["isdisjoint()", "&", "|", "issubset()"],
                "correct_answer": 0,
                "explanation": "isdisjoint() returns True when two sets share no elements."
            },
            {
                "question_text": "What is the output of 'abc'.ljust(5, '-')?",
                "options": ["abc--", "--abc", "-abc-", "abc"],
                "correct_answer": 0,
                "explanation": "ljust() left-aligns the string and fills the remaining width on the right."
            },
            {
                "question_text": "Which function can return a default value when an attribute is missing?",
                "options": ["getattr()", "setattr()", "hasattr()", "delattr()"],
                "correct_answer": 0,
                "explanation": "getattr(object, name, default) returns the default when the attribute is absent."
            },
            {
                "question_text": "What is the output of 'a' * 3?",
                "options": ["aaa", "a3", "3a", "Error"],
                "correct_answer": 0,
                "explanation": "Multiplying a string by 3 repeats it three times."
            },
            {
                "question_text": "Which list method sorts the list in place?",
                "options": ["sorted()", "sort()", "order()", "arrange()"],
                "correct_answer": 1,
                "explanation": "list.sort() modifies the existing list in place."
            },
            {
                "question_text": "What is the output of 11 % 4?",
                "options": ["2", "3", "4", "2.75"],
                "correct_answer": 1,
                "explanation": "The remainder after dividing 11 by 4 is 3."
            },
            {
                "question_text": "Which method returns a copy of a dictionary with updated values?",
                "options": ["copy()", "update()", "fromkeys()", "pop()"],
                "correct_answer": 0,
                "explanation": "copy() creates a shallow copy; update() changes the existing dictionary."
            },
            {
                "question_text": "What is the output of 'hello'.isalpha()?",
                "options": ["True", "False", "None", "Error"],
                "correct_answer": 0,
                "explanation": "All characters in hello are alphabetic."
            },
            {
                "question_text": "Which function can test whether a class is a subclass of another class?",
                "options": ["isinstance()", "issubclass()", "hasattr()", "type()"],
                "correct_answer": 1,
                "explanation": "issubclass() checks the inheritance relationship between classes."
            },
            {
                "question_text": "What is the output of 'python'.partition('t')?",
                "options": ["('py', 't', 'hon')", "('pyt', '', 'hon')", "['py', 'hon']", "('python', '', '')"],
                "correct_answer": 0,
                "explanation": "partition() returns the part before, the separator, and the part after its first occurrence."
            },
            {
                "question_text": "Which built-in function returns an object's attributes and methods in a list?",
                "options": ["dir()", "vars()", "id()", "type()"],
                "correct_answer": 0,
                "explanation": "dir() returns a list of names available on an object."
            },
            {
                "question_text": "What is the output of 6 / 3?",
                "options": ["2", "2.0", "3", "1.5"],
                "correct_answer": 1,
                "explanation": "True division with / returns a floating-point result."
            },
            {
                "question_text": "Which method removes leading whitespace only?",
                "options": ["strip()", "rstrip()", "lstrip()", "trim()"],
                "correct_answer": 2,
                "explanation": "lstrip() removes leading whitespace."
            },
            {
                "question_text": "What is the output of 'abc'.isnumeric()?",
                "options": ["True", "False", "None", "Error"],
                "correct_answer": 1,
                "explanation": "The letters a, b and c are not numeric characters."
            },
            {
                "question_text": "Which function can return the next value from an iterator with a fallback value?",
                "options": ["next(iterator, default)", "iter(iterator, default)", "first(iterator)", "getnext(iterator)"],
                "correct_answer": 0,
                "explanation": "next() accepts an optional default returned when the iterator is exhausted."
            },
            {
                "question_text": "What is the output of 'Hello'.swapcase()?",
                "options": ["HELLO", "hello", "hELLO", "Hello"],
                "correct_answer": 2,
                "explanation": "swapcase() changes uppercase letters to lowercase and lowercase letters to uppercase."
            },
            {
                "question_text": "Which built-in function creates a sequence of indexes and values from an iterable?",
                "options": ["enumerate()", "zip()", "map()", "filter()"],
                "correct_answer": 0,
                "explanation": "enumerate() yields index-value pairs."
            },
            {
                "question_text": "What is the output of '  abc  '.rstrip()?",
                "options": ["  abc", "abc  ", "abc", "  abc  "],
                "correct_answer": 0,
                "explanation": "rstrip() removes trailing whitespace but preserves leading whitespace."
            },
            {
                "question_text": "Which method checks whether a string contains only decimal characters?",
                "options": ["isdecimal()", "isalpha()", "islower()", "isidentifier()"],
                "correct_answer": 0,
                "explanation": "isdecimal() returns True if all characters are decimal characters and the string is non-empty."
            },
            {
                "question_text": "What is the output of 'a,b,c'.count(',')?",
                "options": ["1", "2", "3", "0"],
                "correct_answer": 1,
                "explanation": "There are two commas in the string."
            },
            {
                "question_text": "Which method checks whether a string is a valid Python identifier?",
                "options": ["isidentifier()", "isname()", "isvariable()", "isvalid()"],
                "correct_answer": 0,
                "explanation": "isidentifier() checks whether a string is a valid identifier."
            },
            {
                "question_text": "What is the output of 'hello'.ljust(7, '*')?",
                "options": ["hello**", "**hello", "*hello*", "hello"],
                "correct_answer": 0,
                "explanation": "ljust() pads the right side to reach the requested width."
            },
            {
                "question_text": "Which built-in function returns the Boolean negation of a value?",
                "options": ["not()", "bool()", "operator.not_()", "invert()"],
                "correct_answer": 2,
                "explanation": "operator.not_() returns the logical negation of its argument."
            },
            {
                "question_text": "What is the output of 'abc'.zfill(5)?",
                "options": ["00abc", "abc00", "0abc0", "abc"],
                "correct_answer": 0,
                "explanation": "zfill() adds zeros on the left until the string reaches the requested width."
            },
            {
                "question_text": "Which method returns a list of a dictionary's key-value pairs?",
                "options": ["items()", "keys()", "values()", "pairs()"],
                "correct_answer": 0,
                "explanation": "items() returns a view of the dictionary's key-value pairs."
            },
            {
                "question_text": "What is the output of 'hello'.rjust(7, '-')?",
                "options": ["--hello", "hello--", "-hello-", "hello"],
                "correct_answer": 0,
                "explanation": "rjust() right-aligns the string and pads the left side."
            },
            {
                "question_text": "Which function returns the number of occurrences of an item in a list?",
                "options": ["index()", "count()", "find()", "length()"],
                "correct_answer": 1,
                "explanation": "The list count() method returns the number of matching items."
            },
            {
                "question_text": "What is the output of 'abc'.isalnum()?",
                "options": ["True", "False", "None", "Error"],
                "correct_answer": 0,
                "explanation": "All characters are alphanumeric letters."
            },
            {
                "question_text": "Which built-in function returns a Boolean indicating whether a value is truthy?",
                "options": ["bool()", "truth()", "isTrue()", "any()"],
                "correct_answer": 0,
                "explanation": "bool() converts a value to its truth value."
            },
            {
                "question_text": "What is the output of 'hello'.removesuffix('lo')?",
                "options": ["hel", "hello", "lo", "Error"],
                "correct_answer": 0,
                "explanation": "removesuffix() removes the specified ending when present."
            },
            {
                "question_text": "Which set method adds elements from an iterable?",
                "options": ["add()", "update()", "append()", "extend()"],
                "correct_answer": 1,
                "explanation": "set.update() adds elements from one or more iterables."
            },
            {
                "question_text": "What is the output of 13 // 5?",
                "options": ["2", "3", "2.6", "1"],
                "correct_answer": 0,
                "explanation": "Floor division returns 2."
            },
            {
                "question_text": "Which method returns the number of times a substring occurs in a string?",
                "options": ["find()", "count()", "index()", "match()"],
                "correct_answer": 1,
                "explanation": "str.count() counts occurrences of a substring."
            },
            {
                "question_text": "What is the output of 'abc'.isprintable()?",
                "options": ["True", "False", "None", "Error"],
                "correct_answer": 0,
                "explanation": "All characters in abc are printable."
            },
            {
                "question_text": "Which function returns the quotient and remainder together?",
                "options": ["divmod()", "modulo()", "quotient()", "splitnum()"],
                "correct_answer": 0,
                "explanation": "divmod() returns a pair containing quotient and remainder."
            },
            {
                "question_text": "What is the output of 'hello'.removeprefix('he')?",
                "options": ["llo", "hello", "he", "Error"],
                "correct_answer": 0,
                "explanation": "removeprefix() removes the matching prefix."
            },
            {
                "question_text": "Which operator performs bitwise XOR?",
                "options": ["&", "|", "^", "~"],
                "correct_answer": 2,
                "explanation": "The ^ operator performs bitwise exclusive OR."
            },
            {
                "question_text": "What is the output of 5 & 3?",
                "options": ["1", "7", "6", "2"],
                "correct_answer": 0,
                "explanation": "Binary 0101 AND 0011 gives 0001."
            },
            {
                "question_text": "Which method returns a new list containing the elements of an iterable in reverse order?",
                "options": ["reversed()", "reverse()", "sort()", "back()"],
                "correct_answer": 0,
                "explanation": "reversed() returns an iterator that can be converted to a list."
            },
            {
                "question_text": "What is the output of 'a,b,c'.split(',', 1)?",
                "options": ["['a', 'b,c']", "['a', 'b', 'c']", "['a,b', 'c']", "['a,b,c']"],
                "correct_answer": 0,
                "explanation": "The maxsplit value 1 allows only one split."
            },
            {
                "question_text": "Which built-in function returns the Unicode code point of a character?",
                "options": ["ord()", "chr()", "ascii()", "code()"],
                "correct_answer": 0,
                "explanation": "ord() returns the Unicode code point of a one-character string."
            },
            {
                "question_text": "What is the output of chr(65)?",
                "options": ["A", "65", "a", "Error"],
                "correct_answer": 0,
                "explanation": "The Unicode code point 65 represents the character A."
            },
            {
                "question_text": "Which function can return a string representation suitable for debugging?",
                "options": ["str()", "repr()", "format()", "print()"],
                "correct_answer": 1,
                "explanation": "repr() aims to provide an unambiguous representation of an object."
            },
            {
                "question_text": "What is the output of 'abc'.center(7, '-')?",
                "options": ["--abc--", "---abc-", "-abc---", "abc----"],
                "correct_answer": 0,
                "explanation": "center() pads both sides to the requested width."
            },
            {
                "question_text": "Which method returns a new string with tabs expanded to spaces?",
                "options": ["expandtabs()", "tabspace()", "replace()", "split()"],
                "correct_answer": 0,
                "explanation": "expandtabs() replaces tab characters with spaces."
            },
            {
                "question_text": "What is the output of 'a\\tb'.expandtabs(4)?",
                "options": ["a   b", "a    b", "a b", "ab"],
                "correct_answer": 0,
                "explanation": "The tab advances to the next multiple-of-four column; after a, three spaces are needed."
            },
            {
                "question_text": "Which built-in function can return the sum of an iterable with an optional starting value?",
                "options": ["sum()", "add()", "total()", "reduce()"],
                "correct_answer": 0,
                "explanation": "sum(iterable, start) adds the iterable's values to the starting value."
            },
            {
                "question_text": "What is the output of sum([1, 2, 3], 10)?",
                "options": ["6", "10", "16", "13"],
                "correct_answer": 2,
                "explanation": "The start value 10 is added to the sum 6."
            },
            {
                "question_text": "Which operator performs bitwise left shift?",
                "options": [">>", "<<", "&", "^"],
                "correct_answer": 1,
                "explanation": "The << operator shifts bits to the left."
            },
            {
                "question_text": "What is the output of 3 << 2?",
                "options": ["6", "12", "9", "5"],
                "correct_answer": 1,
                "explanation": "Left shifting 3 by two positions multiplies it by four, giving 12."
            },
            {
                "question_text": "Which function can return the remainder of a floating-point division?",
                "options": ["math.remainder()", "math.mod()", "float.mod()", "divmod()"],
                "correct_answer": 0,
                "explanation": "math.remainder() returns the IEEE 754-style remainder."
            },
            {
                "question_text": "What is the output of 'python'.count('p')?",
                "options": ["0", "1", "2", "3"],
                "correct_answer": 1,
                "explanation": "The character p appears once."
            },
            {
                "question_text": "Which built-in function returns a new list of an iterable's elements sorted by a key function?",
                "options": ["sorted()", "sort()", "order()", "keysort()"],
                "correct_answer": 0,
                "explanation": "sorted() accepts a key function to determine sort order."
            },
            {
                "question_text": "Which method returns the number of items in a set?",
                "options": ["size()", "len()", "count()", "length()"],
                "correct_answer": 1,
                "explanation": "len() returns the number of unique elements in a set."
            },
            {
                "question_text": "What is the output of 'abc'.encode()?",
                "options": ["b'abc'", "'abc'", "[97, 98, 99]", "Error"],
                "correct_answer": 0,
                "explanation": "encode() converts a string to bytes using UTF-8 by default."
            },
            {
                "question_text": "Which method converts bytes into a string?",
                "options": ["encode()", "decode()", "convert()", "stringify()"],
                "correct_answer": 1,
                "explanation": "decode() converts bytes to a string using the selected encoding."
            },
            {
                "question_text": "What is the output of 'abc'.encode().decode()?",
                "options": ["b'abc'", "abc", "['a', 'b', 'c']", "Error"],
                "correct_answer": 1,
                "explanation": "Encoding creates bytes and decoding converts them back to a string."
            },
            {
                "question_text": "Which method can check whether a string is title-cased?",
                "options": ["istitle()", "istop()", "iscapitalized()", "istitlecase()"],
                "correct_answer": 0,
                "explanation": "istitle() checks whether each word follows title-case rules."
            },
            {
                "question_text": "What is the output of 'Hello World'.istitle()?",
                "options": ["True", "False", "None", "Error"],
                "correct_answer": 0,
                "explanation": "Both words begin with uppercase letters and have lowercase remaining letters."
            },
            {
                "question_text": "Which method returns a shallow copy of a set?",
                "options": ["copy()", "clone()", "duplicate()", "replicate()"],
                "correct_answer": 0,
                "explanation": "The set copy() method creates a shallow copy."
            },
            {
                "question_text": "What is the output of {1, 2}.issubset({1, 2, 3})?",
                "options": ["True", "False", "None", "Error"],
                "correct_answer": 0,
                "explanation": "Every element of the first set is present in the second set."
            },
            {
                "question_text": "Which method checks whether one set contains every element of another set?",
                "options": ["issubset()", "isdisjoint()", "intersection()", "difference()"],
                "correct_answer": 0,
                "explanation": "issubset() checks whether all elements of one set belong to another."
            },
            {
                "question_text": "What is the output of {1, 2, 3}.issuperset({2, 3})?",
                "options": ["True", "False", "None", "Error"],
                "correct_answer": 0,
                "explanation": "The first set contains every element of the second set."
            },
            {
                "question_text": "Which function can return a new dictionary with keys created from an iterable?",
                "options": ["dict.fromkeys()", "dict.keys()", "dict.items()", "dict.update()"],
                "correct_answer": 0,
                "explanation": "dict.fromkeys() creates a dictionary using the supplied keys and optional default value."
            },
            {
                "question_text": "What is the output of dict.fromkeys(['x', 'y'], 1)?",
                "options": ["{'x': 1, 'y': 1}", "{1: 'x', 1: 'y'}", "['x', 'y', 1]", "Error"],
                "correct_answer": 0,
                "explanation": "Each key receives the supplied default value 1."
            },
            {
                "question_text": "Which built-in function can return the number of items in a sequence?",
                "options": ["len()", "count()", "size()", "items()"],
                "correct_answer": 0,
                "explanation": "len() returns the number of items in a sequence."
            },
            {
                "question_text": "What is the output of 'abc'.__len__()?",
                "options": ["2", "3", "4", "Error"],
                "correct_answer": 1,
                "explanation": "The string contains three characters."
            },
            {
                "question_text": "Which function returns a Boolean indicating whether an object is an instance of a class?",
                "options": ["isinstance()", "issubclass()", "type()", "id()"],
                "correct_answer": 0,
                "explanation": "isinstance() checks object membership in a class or its subclasses."
            },
            {
                "question_text": "What is the output of 'hello'.partition('x')?",
                "options": ["('hello', '', '')", "('', 'x', 'hello')", "['hello']", "Error"],
                "correct_answer": 0,
                "explanation": "When the separator is absent, partition() returns the original string followed by two empty strings."
            },
            {
                "question_text": "Which method can remove a key from a dictionary without raising KeyError when the key is missing?",
                "options": ["pop(key, default)", "remove(key)", "delete(key)", "discard(key)"],
                "correct_answer": 0,
                "explanation": "Providing a default to dictionary pop() prevents KeyError for a missing key."
            },
            {
                "question_text": "What is the output of {'a': 1}.pop('b', 0)?",
                "options": ["1", "0", "None", "KeyError"],
                "correct_answer": 1,
                "explanation": "The key b is missing, so pop() returns the supplied default 0."
            },
            {
                "question_text": "Which built-in function can return a Boolean indicating whether an iterable contains a truthy value?",
                "options": ["any()", "all()", "bool()", "sum()"],
                "correct_answer": 0,
                "explanation": "any() returns True when at least one item is truthy."
            },
            {
                "question_text": "What is the output of any([0, '', False, 2])?",
                "options": ["True", "False", "None", "Error"],
                "correct_answer": 0,
                "explanation": "The value 2 is truthy, so any() returns True."
            },
            {
                "question_text": "Which function can return True only if every element in an iterable is truthy?",
                "options": ["any()", "all()", "every()", "each()"],
                "correct_answer": 1,
                "explanation": "all() returns True when every element is truthy."
            },
            {
                "question_text": "What is the output of all([1, 'x', True])?",
                "options": ["True", "False", "None", "Error"],
                "correct_answer": 0,
                "explanation": "All values in the list are truthy."
            },
            {
                "question_text": "Which method can remove all key-value pairs from a dictionary?",
                "options": ["clear()", "pop()", "remove()", "empty()"],
                "correct_answer": 0,
                "explanation": "clear() removes all entries from a dictionary."
            },
            {
                "question_text": "What is the output of {'a': 1}.clear()?",
                "options": ["{}", "None", "{'a': 1}", "Error"],
                "correct_answer": 1,
                "explanation": "clear() modifies the dictionary in place and returns None."
            },
            {
                "question_text": "Which method returns the first occurrence index of a substring and raises ValueError if absent?",
                "options": ["find()", "index()", "count()", "search()"],
                "correct_answer": 1,
                "explanation": "str.index() raises ValueError when the substring is not found."
            },
            {
                "question_text": "What is the output of 'banana'.index('na')?",
                "options": ["1", "2", "3", "4"],
                "correct_answer": 1,
                "explanation": "The first occurrence of na starts at index 2."
            },
            {
                "question_text": "Which string method returns a tuple containing the part before, separator, and part after the last occurrence?",
                "options": ["partition()", "rpartition()", "rsplit()", "split()"],
                "correct_answer": 1,
                "explanation": "rpartition() searches for the separator from the right."
            },
            {
                "question_text": "What is the output of 'a-b-c'.rpartition('-')?",
                "options": ["('a-b', '-', 'c')", "('a', '-', 'b-c')", "['a', 'b', 'c']", "('a-b-c', '', '')"],
                "correct_answer": 0,
                "explanation": "rpartition() splits at the last separator."
            },
            {
                "question_text": "Which method can remove a specified suffix from a string if present?",
                "options": ["removesuffix()", "rstrip()", "strip()", "replace()"],
                "correct_answer": 0,
                "explanation": "removesuffix() removes exactly the given suffix when present."
            },
            {
                "question_text": "What is the output of 'filename.py'.removesuffix('.py')?",
                "options": ["filename", "filename.py", ".py", "Error"],
                "correct_answer": 0,
                "explanation": "removesuffix() removes the .py ending."
            },
            {
                "question_text": "Which function can return the current working directory?",
                "options": ["os.getcwd()", "os.chdir()", "os.listdir()", "os.path()"],
                "correct_answer": 0,
                "explanation": "os.getcwd() returns the current working directory."
            },
            {
                "question_text": "Which function changes the current working directory?",
                "options": ["os.getcwd()", "os.chdir()", "os.listdir()", "os.rename()"],
                "correct_answer": 1,
                "explanation": "os.chdir() changes the current working directory."
            },
            {
                "question_text": "Which module provides access to operating-system dependent functionality?",
                "options": ["os", "math", "random", "string"],
                "correct_answer": 0,
                "explanation": "The os module provides operating-system interfaces."
            },
            {
                "question_text": "Which module provides functions for path manipulation?",
                "options": ["os.path", "sys.pathonly", "pathlib_only", "file.path"],
                "correct_answer": 0,
                "explanation": "os.path provides common path manipulation functions."
            },
            {
                "question_text": "What does os.path.exists(path) check?",
                "options": ["Whether a path exists", "Whether a file is open", "Whether a folder is empty", "Whether a path is writable"],
                "correct_answer": 0,
                "explanation": "exists() checks whether the given path exists."
            },
            {
                "question_text": "Which module provides access to command-line arguments?",
                "options": ["sys", "os", "argparse_only", "console"],
                "correct_answer": 0,
                "explanation": "sys.argv contains command-line arguments passed to a Python script."
            },
            {
                "question_text": "What is the first element of sys.argv typically?",
                "options": ["The script name", "The first argument after the script", "The Python version", "The current directory"],
                "correct_answer": 0,
                "explanation": "sys.argv[0] typically contains the script name or path."
            },
            {
                "question_text": "Which module can parse command-line options and arguments?",
                "options": ["argparse", "sys", "os", "input"],
                "correct_answer": 0,
                "explanation": "argparse provides command-line argument parsing."
            },
            {
                "question_text": "Which method of a file object reads the entire remaining content?",
                "options": ["read()", "readline()", "readlines()", "write()"],
                "correct_answer": 0,
                "explanation": "read() reads the remaining file content as a string by default."
            },
            {
                "question_text": "Which file method reads one line at a time?",
                "options": ["read()", "readline()", "readlines()", "nextline()"],
                "correct_answer": 1,
                "explanation": "readline() reads the next line from a file."
            },
            {
                "question_text": "What does the file object's tell() method return?",
                "options": ["Current file position", "File size only", "File name", "Number of lines"],
                "correct_answer": 0,
                "explanation": "tell() returns the current stream position."
            },
            {
                "question_text": "What does the file object's seek(0) do?",
                "options": ["Moves to the beginning of the file", "Moves to the end", "Deletes the file", "Closes the file"],
                "correct_answer": 0,
                "explanation": "seek(0) moves the file position to the beginning."
            },
            {
                "question_text": "Which file mode allows reading and writing without truncating an existing file?",
                "options": ["r+", "w", "a", "x"],
                "correct_answer": 0,
                "explanation": "r+ opens an existing file for both reading and writing without truncating it."
            },
            {
                "question_text": "Which method writes a string to a file object?",
                "options": ["write()", "read()", "append()", "printfile()"],
                "correct_answer": 0,
                "explanation": "write() writes a string to a file."
            },
            {
                "question_text": "What does the file method writelines() do?",
                "options": ["Writes an iterable of strings without adding separators automatically", "Reads every line", "Adds line numbers", "Closes a file"],
                "correct_answer": 0,
                "explanation": "writelines() writes each supplied string as-is and does not automatically add newline characters."
            },
            {
                "question_text": "Which module provides JSON encoding and decoding?",
                "options": ["json", "pickle", "csv", "marshal_only"],
                "correct_answer": 0,
                "explanation": "The json module provides JSON serialization and deserialization."
            },
            {
                "question_text": "Which function converts a Python object into a JSON-formatted string?",
                "options": ["json.loads()", "json.dumps()", "json.load()", "json.dumpfile()"],
                "correct_answer": 1,
                "explanation": "json.dumps() serializes a Python object to a JSON string."
            },
            {
                "question_text": "Which function parses a JSON-formatted string into a Python object?",
                "options": ["json.dumps()", "json.loads()", "json.dump()", "json.parsefile()"],
                "correct_answer": 1,
                "explanation": "json.loads() deserializes a JSON string into a Python object."
            },
            {
                "question_text": "Which module is commonly used to read and write CSV files?",
                "options": ["csv", "json", "re", "math"],
                "correct_answer": 0,
                "explanation": "The csv module supports reading and writing comma-separated values."
            },
            {
                "question_text": "Which function creates a CSV reader from a file object?",
                "options": ["csv.reader()", "csv.read()", "csv.open()", "csv.load()"],
                "correct_answer": 0,
                "explanation": "csv.reader() returns an iterator over rows in a CSV file."
            },
            {
                "question_text": "Which module is used to serialize Python objects into a binary format?",
                "options": ["pickle", "json", "csv", "text"],
                "correct_answer": 0,
                "explanation": "pickle serializes and deserializes Python objects in a Python-specific binary format."
            },
            {
                "question_text": "Which function in the pickle module serializes an object to a bytes object?",
                "options": ["pickle.dumps()", "pickle.loads()", "pickle.dumpfile()", "pickle.read()"],
                "correct_answer": 0,
                "explanation": "pickle.dumps() serializes an object into bytes."
            },
            {
                "question_text": "Which module provides a high-level interface for working with ZIP archives?",
                "options": ["zipfile", "tarfile", "shutil", "archive"],
                "correct_answer": 0,
                "explanation": "zipfile supports reading and writing ZIP archives."
            },
            {
                "question_text": "Which module provides high-level file operations such as copying and moving?",
                "options": ["shutil", "os.path", "sys", "copyfile_only"],
                "correct_answer": 0,
                "explanation": "shutil provides high-level file and directory operations."
            },
            {
                "question_text": "Which module provides a temporary directory or file facility?",
                "options": ["tempfile", "temporary", "os.temp", "shutil"],
                "correct_answer": 0,
                "explanation": "tempfile creates temporary files and directories."
            },
            {
                "question_text": "Which module provides object-oriented filesystem paths?",
                "options": ["pathlib", "os.path", "filelib", "sys"],
                "correct_answer": 0,
                "explanation": "pathlib provides the Path class for object-oriented path handling."
            },
            {
                "question_text": "Which Path method checks whether a path is a directory?",
                "options": ["is_dir()", "is_file()", "exists()", "is_path()"],
                "correct_answer": 0,
                "explanation": "Path.is_dir() checks whether the path points to a directory."
            },
            {
                "question_text": "Which Path method reads text content from a file?",
                "options": ["read_text()", "read_bytes()", "open_text()", "load_text()"],
                "correct_answer": 0,
                "explanation": "Path.read_text() reads the file's text content."
            },
            {
                "question_text": "Which module provides tools for matching patterns in strings?",
                "options": ["re", "fnmatch", "string", "pattern"],
                "correct_answer": 0,
                "explanation": "The re module supports regular expression matching."
            },
            {
                "question_text": "Which re function checks for a match only at the beginning of a string?",
                "options": ["re.match()", "re.search()", "re.findall()", "re.sub()"],
                "correct_answer": 0,
                "explanation": "re.match() attempts matching at the beginning of the string."
            },
            {
                "question_text": "Which re function searches for a pattern anywhere in a string?",
                "options": ["re.match()", "re.search()", "re.compile_only()", "re.escape()"],
                "correct_answer": 1,
                "explanation": "re.search() scans the string for the first matching location."
            },
            {
                "question_text": "Which re function returns all non-overlapping matches as a list?",
                "options": ["re.findall()", "re.match()", "re.search()", "re.splitonly()"],
                "correct_answer": 0,
                "explanation": "re.findall() returns all non-overlapping matches."
            },
            {
                "question_text": "Which re function replaces matched patterns with a replacement string?",
                "options": ["re.sub()", "re.find()", "re.match()", "re.replace()"],
                "correct_answer": 0,
                "explanation": "re.sub() substitutes occurrences of a regular expression pattern."
            },
            {
                "question_text": "Which module provides mathematical functions such as sin, cos and sqrt?",
                "options": ["math", "cmath_only", "numbers", "statistics"],
                "correct_answer": 0,
                "explanation": "The math module provides common mathematical functions."
            },
            {
                "question_text": "What does math.ceil(4.2) return?",
                "options": ["4", "5", "4.2", "6"],
                "correct_answer": 1,
                "explanation": "ceil() returns the smallest integer greater than or equal to the value."
            },
            {
                "question_text": "What does math.floor(4.8) return?",
                "options": ["4", "5", "4.8", "3"],
                "correct_answer": 0,
                "explanation": "floor() returns the greatest integer less than or equal to the value."
            },
            {
                "question_text": "Which module provides functions for calculating mean, median and mode?",
                "options": ["statistics", "math", "random", "numbers"],
                "correct_answer": 0,
                "explanation": "The statistics module provides descriptive statistical functions."
            },
            {
                "question_text": "What does statistics.mean([2, 4, 6]) return?",
                "options": ["3", "4", "6", "12"],
                "correct_answer": 1,
                "explanation": "The arithmetic mean is (2 + 4 + 6) / 3, which equals 4."
            },
            {
                "question_text": "Which function selects a random element from a non-empty sequence?",
                "options": ["random.choice()", "random.sample()", "random.shuffle()", "random.seed()"],
                "correct_answer": 0,
                "explanation": "random.choice() selects one element from a non-empty sequence."
            },
            {
                "question_text": "Which function shuffles a mutable sequence in place?",
                "options": ["random.choice()", "random.shuffle()", "random.sample()", "random.random()"],
                "correct_answer": 1,
                "explanation": "random.shuffle() rearranges a mutable sequence in place."
            },
            {
                "question_text": "Which function selects a specified number of unique items without replacement?",
                "options": ["random.sample()", "random.choice()", "random.shuffle()", "random.uniform()"],
                "correct_answer": 0,
                "explanation": "random.sample() selects unique population elements without replacement."
            },
            {
                "question_text": "Which module supports date and time arithmetic?",
                "options": ["datetime", "timeonly", "calendar_only", "clock"],
                "correct_answer": 0,
                "explanation": "datetime provides date, time and timedelta types."
            },
            {
                "question_text": "Which datetime type represents a duration between two dates or times?",
                "options": ["date", "time", "timedelta", "timezone"],
                "correct_answer": 2,
                "explanation": "timedelta represents a duration or difference between dates and times."
            },
            {
                "question_text": "Which method can format a datetime object as a string?",
                "options": ["strftime()", "strptime()", "formatdate()", "dateformat()"],
                "correct_answer": 0,
                "explanation": "strftime() formats a date or time according to a format string."
            },
            {
                "question_text": "Which method parses a date string into a datetime object?",
                "options": ["strftime()", "strptime()", "parseformat()", "datetime.parse()"],
                "correct_answer": 1,
                "explanation": "strptime() parses a string according to a specified format."
            },
            {
                "question_text": "Which module provides a counter and other specialized container types?",
                "options": ["collections", "container", "types", "itertools"],
                "correct_answer": 0,
                "explanation": "collections provides specialized container data types."
            },
            {
                "question_text": "Which collections class counts occurrences of hashable elements?",
                "options": ["Counter", "defaultdict", "deque", "namedtuple"],
                "correct_answer": 0,
                "explanation": "Counter is a dictionary subclass designed for counting hashable objects."
            },
            {
                "question_text": "Which collections class provides a dictionary with a default value factory?",
                "options": ["Counter", "defaultdict", "deque", "OrderedDict"],
                "correct_answer": 1,
                "explanation": "defaultdict creates missing values using its default factory."
            },
            {
                "question_text": "Which collections class supports efficient appends and pops from both ends?",
                "options": ["deque", "Counter", "defaultdict", "ChainMap"],
                "correct_answer": 0,
                "explanation": "deque supports efficient operations at both ends."
            },
            {
                "question_text": "Which itertools function creates an iterator that accumulates values?",
                "options": ["accumulate()", "chain()", "cycle()", "repeat()"],
                "correct_answer": 0,
                "explanation": "itertools.accumulate() returns accumulated results from an iterable."
            },
            {
                "question_text": "Which itertools function chains multiple iterables into one iterator?",
                "options": ["chain()", "cycle()", "repeat()", "product()"],
                "correct_answer": 0,
                "explanation": "chain() iterates over each iterable in sequence."
            },
            {
                "question_text": "Which itertools function produces the Cartesian product of input iterables?",
                "options": ["product()", "permutations()", "combinations()", "chain()"],
                "correct_answer": 0,
                "explanation": "product() produces Cartesian product tuples."
            },
            {
                "question_text": "Which itertools function generates ordered arrangements without replacement?",
                "options": ["permutations()", "combinations()", "product()", "cycle()"],
                "correct_answer": 0,
                "explanation": "permutations() generates ordered arrangements of elements."
            },
            {
                "question_text": "Which itertools function generates selections where order does not matter?",
                "options": ["permutations()", "combinations()", "product()", "accumulate()"],
                "correct_answer": 1,
                "explanation": "combinations() generates selections without regard to order."
            },
            {
                "question_text": "Which module provides tools for functional programming such as reduce()?",
                "options": ["functools", "itertools", "operator", "functions"],
                "correct_answer": 0,
                "explanation": "functools provides higher-order functions and callable-related tools."
            },
            {
                "question_text": "Which functools function applies a function cumulatively to an iterable?",
                "options": ["reduce()", "partial()", "wraps()", "lru_cache()"],
                "correct_answer": 0,
                "explanation": "reduce() applies a two-argument function cumulatively to iterable items."
            },
            {
                "question_text": "Which decorator can cache function results?",
                "options": ["functools.lru_cache", "staticmethod", "property", "classmethod"],
                "correct_answer": 0,
                "explanation": "lru_cache caches results from calls to a function."
            },
            {
                "question_text": "Which functools function creates a new callable with some arguments already supplied?",
                "options": ["partial()", "reduce()", "wraps()", "cache()"],
                "correct_answer": 0,
                "explanation": "partial() creates a callable with pre-filled arguments."
            },
            {
                "question_text": "Which module provides tools for working with function signatures and introspection?",
                "options": ["inspect", "types", "typing", "ast"],
                "correct_answer": 0,
                "explanation": "inspect provides tools for examining live objects, including functions and signatures."
            },
            {
                "question_text": "Which module provides abstract base classes and abstractmethod?",
                "options": ["abc", "abstract", "classes", "typing"],
                "correct_answer": 0,
                "explanation": "The abc module provides abstract base class support."
            },
            {
                "question_text": "Which decorator marks a method as abstract?",
                "options": ["@abstractmethod", "@classmethod", "@staticmethod", "@property"],
                "correct_answer": 0,
                "explanation": "@abstractmethod marks methods that concrete subclasses are expected to implement."
            },
            {
                "question_text": "Which module provides tools for defining and using enumerations?",
                "options": ["enum", "collections", "types", "constants"],
                "correct_answer": 0,
                "explanation": "The enum module provides support for enumerated constants."
            },
            {
                "question_text": "Which module provides a class decorator for automatically generating common methods?",
                "options": ["dataclasses", "classes", "attrs_builtin", "objecttools"],
                "correct_answer": 0,
                "explanation": "dataclasses.dataclass can generate methods such as __init__ and __repr__."
            },
            {
                "question_text": "Which decorator creates a class with generated initialization and representation methods?",
                "options": ["@dataclass", "@property", "@staticmethod", "@abstractmethod"],
                "correct_answer": 0,
                "explanation": "@dataclass generates common methods based on annotated fields."
            },
            {
                "question_text": "Which module provides type hints such as List, Optional and Union?",
                "options": ["typing", "types", "annotations", "hints"],
                "correct_answer": 0,
                "explanation": "The typing module provides constructs for type annotations."
            },
            {
                "question_text": "What does Optional[int] traditionally mean in Python type hints?",
                "options": ["An integer or None", "Only an integer", "A list of integers", "An optional argument of any type"],
                "correct_answer": 0,
                "explanation": "Optional[int] means int or None."
            },
            {
                "question_text": "Which syntax represents a union of int and str in modern Python?",
                "options": ["int | str", "int & str", "int + str", "int / str"],
                "correct_answer": 0,
                "explanation": "The | operator can express a union type in modern Python."
            },
            {
                "question_text": "Which module provides tools for parsing Python source code into an abstract syntax tree?",
                "options": ["ast", "tokenize", "inspect", "parser"],
                "correct_answer": 0,
                "explanation": "The ast module provides abstract syntax tree parsing and manipulation."
            },
            {
                "question_text": "Which module can tokenize Python source code?",
                "options": ["tokenize", "ast", "inspect", "compile"],
                "correct_answer": 0,
                "explanation": "The tokenize module provides a lexical scanner for Python source."
            },
            {
                "question_text": "Which built-in function compiles source code into a code object?",
                "options": ["compile()", "execfile()", "evalfile()", "parse()"],
                "correct_answer": 0,
                "explanation": "compile() produces a code object from source code."
            },
            {
                "question_text": "Which built-in function evaluates a Python expression from a string?",
                "options": ["eval()", "exec()", "compile()", "parse()"],
                "correct_answer": 0,
                "explanation": "eval() evaluates a Python expression; never use it with untrusted input."
            },
            {
                "question_text": "Which built-in function executes Python statements from a string?",
                "options": ["eval()", "exec()", "compileonly()", "run()"],
                "correct_answer": 1,
                "explanation": "exec() executes Python statements; never use it with untrusted input."
            },
            {
                "question_text": "Which module provides access to interpreter-specific variables and functions?",
                "options": ["sys", "os", "platform", "inspect"],
                "correct_answer": 0,
                "explanation": "sys provides access to interpreter-related information and functions."
            },
            {
                "question_text": "Which sys attribute contains the Python version information?",
                "options": ["sys.version", "sys.release", "sys.python", "sys.info"],
                "correct_answer": 0,
                "explanation": "sys.version contains a string describing the Python version."
            },
            {
                "question_text": "Which module can report the operating system platform?",
                "options": ["platform", "sys", "os.path", "computer"],
                "correct_answer": 0,
                "explanation": "The platform module provides access to platform identification information."
            },
            {
                "question_text": "Which module provides a portable way to create threads?",
                "options": ["threading", "multiprocessing", "asyncio", "concurrent"],
                "correct_answer": 0,
                "explanation": "threading provides thread-based parallel execution."
            },
            {
                "question_text": "Which module provides process-based parallelism?",
                "options": ["threading", "multiprocessing", "asyncio", "queue"],
                "correct_answer": 1,
                "explanation": "multiprocessing provides process-based parallel execution."
            },
            {
                "question_text": "Which module provides asynchronous event-loop functionality?",
                "options": ["asyncio", "threading", "multiprocessing", "sched"],
                "correct_answer": 0,
                "explanation": "asyncio supports asynchronous programming using event loops and coroutines."
            },
            {
                "question_text": "Which keyword declares an asynchronous function?",
                "options": ["async def", "await def", "async function", "coroutine"],
                "correct_answer": 0,
                "explanation": "async def defines a coroutine function."
            },
            {
                "question_text": "Which keyword suspends a coroutine until an awaitable completes?",
                "options": ["yield", "await", "pause", "wait"],
                "correct_answer": 1,
                "explanation": "await suspends the coroutine until the awaitable produces a result."
            },
            {
                "question_text": "Which concurrent.futures class manages a pool of worker threads?",
                "options": ["ThreadPoolExecutor", "ProcessPoolExecutor", "FutureThread", "ThreadManager"],
                "correct_answer": 0,
                "explanation": "ThreadPoolExecutor manages a pool of worker threads."
            },
            {
                "question_text": "Which concurrent.futures class manages a pool of worker processes?",
                "options": ["ThreadPoolExecutor", "ProcessPoolExecutor", "ProcessManager", "WorkerPool"],
                "correct_answer": 1,
                "explanation": "ProcessPoolExecutor manages a pool of worker processes."
            },
            {
                "question_text": "Which module provides a thread-safe queue implementation?",
                "options": ["queue", "collections", "list", "heapq"],
                "correct_answer": 0,
                "explanation": "The queue module provides synchronized queue classes."
            },
            {
                "question_text": "Which module provides a heap queue algorithm?",
                "options": ["heapq", "queue", "collections", "bisect"],
                "correct_answer": 0,
                "explanation": "heapq implements a min-heap priority queue algorithm."
            },
            {
                "question_text": "Which module provides efficient binary search operations on sorted lists?",
                "options": ["bisect", "heapq", "array", "search"],
                "correct_answer": 0,
                "explanation": "bisect provides binary-search-based insertion and lookup helpers."
            },
            {
                "question_text": "Which module provides compact arrays of numeric values?",
                "options": ["array", "list", "struct", "numbers"],
                "correct_answer": 0,
                "explanation": "The array module provides space-efficient arrays of basic numeric types."
            },
            {
                "question_text": "Which module packs and unpacks binary data?",
                "options": ["struct", "array", "pickle", "bytes"],
                "correct_answer": 0,
                "explanation": "struct converts between Python values and C-style binary structures."
            },
            {
                "question_text": "Which module provides cryptographic hash functions?",
                "options": ["hashlib", "random", "secrets", "hmac"],
                "correct_answer": 0,
                "explanation": "hashlib provides secure hash and message digest algorithms."
            },
            {
                "question_text": "Which module provides cryptographically strong random numbers for security-sensitive uses?",
                "options": ["random", "secrets", "math", "statistics"],
                "correct_answer": 1,
                "explanation": "secrets is designed for cryptographically strong random values."
            },
            {
                "question_text": "Which module provides keyed-hash message authentication codes?",
                "options": ["hmac", "hashlib", "secrets", "ssl"],
                "correct_answer": 0,
                "explanation": "hmac implements keyed-hash message authentication codes."
            },
            {
                "question_text": "Which module provides TLS and certificate-related functionality?",
                "options": ["ssl", "socket", "http", "urllib"],
                "correct_answer": 0,
                "explanation": "ssl provides TLS/SSL support for network sockets."
            },
            {
                "question_text": "Which module provides low-level networking interfaces?",
                "options": ["socket", "http", "urllib", "ssl"],
                "correct_answer": 0,
                "explanation": "socket provides low-level networking interfaces."
            },
            {
                "question_text": "Which module provides HTTP client functionality?",
                "options": ["http.client", "socketserver", "email", "ftplib"],
                "correct_answer": 0,
                "explanation": "http.client provides an HTTP client implementation."
            },
            {
                "question_text": "Which module can parse URLs and query strings?",
                "options": ["urllib.parse", "http.client", "socket", "urltools"],
                "correct_answer": 0,
                "explanation": "urllib.parse provides URL parsing and query-string utilities."
            },
            {
                "question_text": "Which module provides an SMTP client?",
                "options": ["smtplib", "imaplib", "poplib", "email"],
                "correct_answer": 0,
                "explanation": "smtplib provides an SMTP client for sending email."
            },
            {
                "question_text": "Which module provides an IMAP4 client?",
                "options": ["smtplib", "imaplib", "poplib", "mailbox"],
                "correct_answer": 1,
                "explanation": "imaplib provides an IMAP4 client implementation."
            },
            {
                "question_text": "Which module provides tools for parsing email messages?",
                "options": ["email", "smtplib", "imaplib", "mail"],
                "correct_answer": 0,
                "explanation": "The email package supports creating and parsing email messages."
            },
            {
                "question_text": "Which module provides a simple HTTP server implementation?",
                "options": ["http.server", "http.client", "socket", "wsgiref"],
                "correct_answer": 0,
                "explanation": "http.server provides basic HTTP server classes."
            },
            {
                "question_text": "Which module provides an FTP client?",
                "options": ["ftplib", "smtplib", "imaplib", "urllib"],
                "correct_answer": 0,
                "explanation": "ftplib implements an FTP client."
            },
            {
                "question_text": "Which module provides tools for working with HTML entities?",
                "options": ["html", "xml", "re", "urllib"],
                "correct_answer": 0,
                "explanation": "The html module provides utilities such as HTML entity escaping and unescaping."
            },
            {
                "question_text": "Which module provides XML parsing and processing tools?",
                "options": ["xml.etree.ElementTree", "json", "html", "csv"],
                "correct_answer": 0,
                "explanation": "xml.etree.ElementTree provides an API for parsing and creating XML."
            },
            {
                "question_text": "Which module provides tools for parsing and generating configuration files in INI format?",
                "options": ["configparser", "json", "tomllib", "csv"],
                "correct_answer": 0,
                "explanation": "configparser reads and writes INI-style configuration files."
            },
            {
                "question_text": "Which standard-library module reads TOML files?",
                "options": ["tomllib", "configparser", "json", "yaml"],
                "correct_answer": 0,
                "explanation": "tomllib parses TOML data; it is available in Python 3.11 and later."
            },
            {
                "question_text": "Which module provides logging facilities?",
                "options": ["logging", "warnings", "traceback", "sys"],
                "correct_answer": 0,
                "explanation": "The logging module provides flexible event logging."
            },
            {
                "question_text": "Which module provides warning message facilities?",
                "options": ["warnings", "logging", "traceback", "errors"],
                "correct_answer": 0,
                "explanation": "The warnings module supports issuing and controlling warning messages."
            },
            {
                "question_text": "Which module provides traceback formatting and printing utilities?",
                "options": ["traceback", "logging", "warnings", "inspect"],
                "correct_answer": 0,
                "explanation": "traceback provides utilities for extracting and formatting stack traces."
            },
            {
                "question_text": "Which module supports unit testing in the Python standard library?",
                "options": ["unittest", "pytest_builtin", "testcase", "doctestonly"],
                "correct_answer": 0,
                "explanation": "unittest provides a testing framework inspired by JUnit."
            },
            {
                "question_text": "Which module runs tests embedded in documentation strings?",
                "options": ["doctest", "unittest", "pydoc", "inspect"],
                "correct_answer": 0,
                "explanation": "doctest checks interactive examples in docstrings."
            },
            {
                "question_text": "Which module provides tools for measuring execution time?",
                "options": ["timeit", "datetime", "time", "profile"],
                "correct_answer": 0,
                "explanation": "timeit is designed to measure small code snippets."
            },
            {
                "question_text": "Which module provides deterministic profiling of Python programs?",
                "options": ["cProfile", "timeit", "pstats", "trace"],
                "correct_answer": 0,
                "explanation": "cProfile provides deterministic profiling of Python code."
            },
            {
                "question_text": "Which module can trace Python statements and execution events?",
                "options": ["trace", "logging", "inspect", "ast"],
                "correct_answer": 0,
                "explanation": "The trace module supports tracing program execution."
            },
            {
                "question_text": "Which module provides garbage collector interface tools?",
                "options": ["gc", "memory", "sys", "resource"],
                "correct_answer": 0,
                "explanation": "The gc module provides an interface to the cyclic garbage collector."
            },
            {
                "question_text": "Which module can report object reference counts in CPython?",
                "options": ["sys", "gc", "inspect", "types"],
                "correct_answer": 0,
                "explanation": "sys.getrefcount() reports a reference count in CPython, including a temporary reference from the call."
            },
            {
                "question_text": "Which module provides access to Python's built-in object types?",
                "options": ["types", "typing", "inspect", "builtins"],
                "correct_answer": 3,
                "explanation": "The builtins module contains names of built-in functions, exceptions and types."
            },
            {
                "question_text": "Which module provides access to built-in names such as len and print?",
                "options": ["builtins", "types", "sys", "inspect"],
                "correct_answer": 0,
                "explanation": "The builtins module contains built-in functions and types."
            },
            {
                "question_text": "Which module can create and manipulate function objects and code objects?",
                "options": ["types", "inspect", "ast", "compile"],
                "correct_answer": 0,
                "explanation": "The types module exposes names for many built-in interpreter types."
            },
            {
                "question_text": "Which module provides a lightweight way to create namespaces?",
                "options": ["types", "argparse", "collections", "namespace"],
                "correct_answer": 0,
                "explanation": "types.SimpleNamespace provides an attribute-accessible namespace."
            },
            {
                "question_text": "Which module provides tools for working with decimal floating-point arithmetic?",
                "options": ["decimal", "fractions", "math", "numbers"],
                "correct_answer": 0,
                "explanation": "decimal provides decimal arithmetic with configurable precision."
            },
            {
                "question_text": "Which module provides rational number arithmetic?",
                "options": ["fractions", "decimal", "math", "statistics"],
                "correct_answer": 0,
                "explanation": "fractions provides rational numbers through the Fraction class."
            },
            {
                "question_text": "What is the result of Fraction(1, 2) + Fraction(1, 3)?",
                "options": ["5/6", "2/5", "1/6", "3/6"],
                "correct_answer": 0,
                "explanation": "The sum of one-half and one-third is five-sixths."
            },
            {
                "question_text": "Which module provides exact decimal arithmetic?",
                "options": ["decimal", "math", "random", "fractions"],
                "correct_answer": 0,
                "explanation": "decimal supports decimal arithmetic with explicit precision and rounding contexts."
            },
            {
                "question_text": "Which module provides tools for working with binary and hexadecimal representations?",
                "options": ["builtins", "binascii", "struct", "All of these"],
                "correct_answer": 3,
                "explanation": "Python provides several built-in and standard-library tools for binary and hexadecimal conversions."
            },
            {
                "question_text": "What is the output of hex(255)?",
                "options": ["'0xff'", "'255'", "'ff00'", "'0b11111111'"],
                "correct_answer": 0,
                "explanation": "hex() returns the hexadecimal string representation with a 0x prefix."
            },
            {
                "question_text": "What is the output of bin(10)?",
                "options": ["'0b1010'", "'1010'", "'0x10'", "'10'"],
                "correct_answer": 0,
                "explanation": "bin() returns the binary string representation with a 0b prefix."
            },
            {
                "question_text": "Which built-in function converts an integer to an octal string?",
                "options": ["oct()", "hex()", "bin()", "formatbin()"],
                "correct_answer": 0,
                "explanation": "oct() returns the octal string representation with a 0o prefix."
            },
            {
                "question_text": "What is the output of oct(8)?",
                "options": ["'0o10'", "'0x8'", "'0b1000'", "'8'"],
                "correct_answer": 0,
                "explanation": "The octal representation of decimal 8 is 10, prefixed with 0o."
            },
            {
                "question_text": "Which built-in function returns a formatted representation of a value?",
                "options": ["format()", "repr()", "str()", "All of these"],
                "correct_answer": 3,
                "explanation": "format(), repr() and str() all produce string representations in different ways."
            },
            {
                "question_text": "What is the output of format(255, 'x')?",
                "options": ["'ff'", "'255'", "'0xff'", "'11111111'"],
                "correct_answer": 0,
                "explanation": "The x format specifier produces lowercase hexadecimal digits."
            },
            {
                "question_text": "Which method can return a string with a specified number of decimal places using f-string formatting?",
                "options": ["format()", "round()", "str()", "All of these"],
                "correct_answer": 3,
                "explanation": "Formatting, rounding and string conversion can all be used to present decimal values, with different behavior."
            },
            {
                "question_text": "What is the output of f'{3.14159:.2f}'?",
                "options": ["3.14", "3.15", "3.14159", "3.1"],
                "correct_answer": 0,
                "explanation": "The .2f format displays two digits after the decimal point."
            },
            {
                "question_text": "Which operator performs bitwise NOT?",
                "options": ["~", "!", "^", "&"],
                "correct_answer": 0,
                "explanation": "The ~ operator performs bitwise inversion."
            },
            {
                "question_text": "What is the output of ~5 in Python?",
                "options": ["-5", "-6", "6", "5"],
                "correct_answer": 1,
                "explanation": "For integers, ~x equals -(x + 1), so ~5 is -6."
            },
            {
                "question_text": "Which method checks whether a set is a superset of another set?",
                "options": ["issuperset()", "issubset()", "isdisjoint()", "intersection()"],
                "correct_answer": 0,
                "explanation": "issuperset() checks whether the set contains every element of another set."
            },
            {
                "question_text": "What is the output of {1, 2, 3}.isdisjoint({4, 5})?",
                "options": ["True", "False", "None", "Error"],
                "correct_answer": 0,
                "explanation": "The two sets have no common elements."
            },
            {
                "question_text": "Which dictionary method returns a view of its values?",
                "options": ["values()", "items()", "keys()", "get()"],
                "correct_answer": 0,
                "explanation": "values() returns a dynamic view of dictionary values."
            },
            {
                "question_text": "What is the output of list({'a': 1, 'b': 2})?",
                "options": ["['a', 'b']", "[1, 2]", "[('a', 1), ('b', 2)]", "Error"],
                "correct_answer": 0,
                "explanation": "Iterating over a dictionary yields its keys by default."
            },
            {
                "question_text": "Which expression creates a set containing the squares of 1, 2 and 3?",
                "options": ["{x*x for x in range(1, 4)}", "[x*x for x in range(1, 4)]", "(x*x for x in range(1, 4))", "{x: x*x for x in range(1, 4)}"],
                "correct_answer": 0,
                "explanation": "Set comprehensions use curly braces with an expression and for clause."
            },
            {
                "question_text": "What is the output of list({x for x in [1, 1, 2]})?",
                "options": ["[1, 1, 2]", "[1, 2]", "[2, 1]", "Error"],
                "correct_answer": 1,
                "explanation": "A set comprehension removes duplicate values; iteration order is not guaranteed."
            },
            {
                "question_text": "Which built-in function can convert an iterable into a list?",
                "options": ["list()", "tuple()", "set()", "All of these"],
                "correct_answer": 0,
                "explanation": "list() constructs a list from an iterable."
            },
            {
                "question_text": "What is the output of list('abc')?",
                "options": ["['a', 'b', 'c']", "['abc']", "('a', 'b', 'c')", "Error"],
                "correct_answer": 0,
                "explanation": "A string is iterable, so list() creates a list of its characters."
            },
            {
                "question_text": "Which built-in function converts an iterable into a tuple?",
                "options": ["tuple()", "list()", "set()", "dict()"],
                "correct_answer": 0,
                "explanation": "tuple() constructs a tuple from an iterable."
            },
            {
                "question_text": "What is the output of tuple('xy')?",
                "options": ["('x', 'y')", "['x', 'y']", "('xy')", "Error"],
                "correct_answer": 0,
                "explanation": "tuple() creates a tuple containing each character."
            },
            {
                "question_text": "Which function returns a new set from an iterable?",
                "options": ["set()", "dict()", "tuple()", "list()"],
                "correct_answer": 0,
                "explanation": "set() creates a set containing unique elements from an iterable."
            },
            {
                "question_text": "What is the output of set('aba')?",
                "options": ["{'a', 'b'}", "{'a', 'b', 'a'}", "['a', 'b']", "Error"],
                "correct_answer": 0,
                "explanation": "Sets retain unique characters; their iteration order is not guaranteed."
            },
            {
                "question_text": "Which built-in function creates a dictionary from keyword arguments?",
                "options": ["dict()", "list()", "set()", "tuple()"],
                "correct_answer": 0,
                "explanation": "dict() accepts keyword arguments to create dictionary entries."
            },
            {
                "question_text": "What is the output of dict(a=1, b=2)?",
                "options": ["{'a': 1, 'b': 2}", "['a', 'b']", "{1: 'a', 2: 'b'}", "Error"],
                "correct_answer": 0,
                "explanation": "Keyword arguments become string keys in the dictionary."
            },
            {
                "question_text": "Which method returns a list of tuples containing dictionary key-value pairs when converted to a list?",
                "options": ["items()", "keys()", "values()", "get()"],
                "correct_answer": 0,
                "explanation": "list(dictionary.items()) creates a list of key-value tuples."
            },
            {
                "question_text": "What is the output of list({'x': 1, 'y': 2}.items())?",
                "options": ["[('x', 1), ('y', 2)]", "['x', 'y']", "[1, 2]", "{'x': 1, 'y': 2}"],
                "correct_answer": 0,
                "explanation": "items() yields key-value pairs, which list() collects into a list."
            },
            {
                "question_text": "Which method can add a key-value pair to a dictionary?",
                "options": ["update()", "append()", "extend()", "insert()"],
                "correct_answer": 0,
                "explanation": "update() adds or replaces key-value pairs."
            },
            {
                "question_text": "What is the output of {'a': 1} | {'b': 2} in Python 3.9+?",
                "options": ["{'a': 1, 'b': 2}", "{'a': 1}", "{'b': 2}", "Error"],
                "correct_answer": 0,
                "explanation": "The dictionary union operator merges the two dictionaries."
            },
            {
                "question_text": "Which operator is used for dictionary union in Python 3.9 and later?",
                "options": ["|", "&", "+", "^"],
                "correct_answer": 0,
                "explanation": "The | operator creates a merged dictionary."
            },
            {
                "question_text": "What happens when two dictionaries have the same key during union?",
                "options": ["The right-hand value wins", "The left-hand value wins", "An error is always raised", "Both values are stored"],
                "correct_answer": 0,
                "explanation": "For duplicate keys, the value from the right-hand dictionary is used."
            },
            {
                "question_text": "Which method returns a dictionary value without removing the key?",
                "options": ["get()", "pop()", "popitem()", "clear()"],
                "correct_answer": 0,
                "explanation": "get() retrieves a value without modifying the dictionary."
            },
            {
                "question_text": "What is the output of {'x': 2}.get('x')?",
                "options": ["2", "'x'", "None", "KeyError"],
                "correct_answer": 0,
                "explanation": "The key x exists and its value is 2."
            },
            {
                "question_text": "Which method removes and returns the last inserted key-value pair from a dictionary?",
                "options": ["popitem()", "pop()", "remove()", "last()"],
                "correct_answer": 0,
                "explanation": "popitem() removes and returns the last inserted pair in modern Python dictionaries."
            },
            {
                "question_text": "What is the output of {'a': 1, 'b': 2}.popitem()?",
                "options": ["('b', 2)", "('a', 1)", "2", "None"],
                "correct_answer": 0,
                "explanation": "popitem() removes and returns the last inserted pair."
            },
            {
                "question_text": "Which list method removes the first matching value?",
                "options": ["remove()", "pop()", "clear()", "discard()"],
                "correct_answer": 0,
                "explanation": "remove(value) deletes the first matching value."
            },
            {
                "question_text": "What happens when list.remove() cannot find the specified value?",
                "options": ["Raises ValueError", "Returns None", "Raises KeyError", "Does nothing"],
                "correct_answer": 0,
                "explanation": "remove() raises ValueError if the value is not present."
            },
            {
                "question_text": "Which method removes and returns an item at a specified list index?",
                "options": ["pop()", "remove()", "clear()", "delete()"],
                "correct_answer": 0,
                "explanation": "pop(index) removes and returns the item at the given index."
            },
            {
                "question_text": "What is the output of [10, 20, 30].pop(1)?",
                "options": ["20", "10", "30", "[10, 30]"],
                "correct_answer": 0,
                "explanation": "pop(1) returns the item at index 1, which is 20."
            },
            {
                "question_text": "Which list method inserts an item at a specified index?",
                "options": ["insert()", "append()", "extend()", "add()"],
                "correct_answer": 0,
                "explanation": "insert(index, value) inserts an element at the requested position."
            },
            {
                "question_text": "What is the output of [1, 3].insert(1, 2)?",
                "options": ["None", "[1, 2, 3]", "[2, 1, 3]", "Error"],
                "correct_answer": 0,
                "explanation": "insert() modifies the list in place and returns None."
            },
            {
                "question_text": "Which list method returns None after sorting the list in place?",
                "options": ["sort()", "sorted()", "order()", "arrange()"],
                "correct_answer": 0,
                "explanation": "list.sort() modifies the list in place and returns None."
            },
            {
                "question_text": "What is the output of [3, 1, 2].sort()?",
                "options": ["None", "[1, 2, 3]", "[3, 2, 1]", "Error"],
                "correct_answer": 0,
                "explanation": "sort() changes the list in place and returns None."
            },
            {
                "question_text": "Which list method reverses the list in place?",
                "options": ["reverse()", "reversed()", "sort()", "invert()"],
                "correct_answer": 0,
                "explanation": "list.reverse() reverses the existing list in place."
            },
            {
                "question_text": "What is the output of [1, 2, 3].reverse()?",
                "options": ["None", "[3, 2, 1]", "[1, 2, 3]", "Error"],
                "correct_answer": 0,
                "explanation": "reverse() modifies the list in place and returns None."
            },
            {
                "question_text": "Which method returns the index of a specified element in a list?",
                "options": ["index()", "find()", "count()", "locate()"],
                "correct_answer": 0,
                "explanation": "index() returns the first matching position."
            },
            {
                "question_text": "What is the output of [5, 6, 5].count(5)?",
                "options": ["1", "2", "3", "0"],
                "correct_answer": 1,
                "explanation": "The value 5 appears twice."
            },
            {
                "question_text": "Which expression creates a list of even numbers from 0 through 8?",
                "options": ["[x for x in range(10) if x % 2 == 0]", "[x for x in range(10) if x % 2 == 1]", "[x for x in range(8)]", "[x * 2 for x in range(4)]"],
                "correct_answer": 0,
                "explanation": "The condition selects 0, 2, 4, 6 and 8."
            },
            {
                "question_text": "What is the output of [x + y for x in [1, 2] for y in [10, 20]]?",
                "options": ["[11, 21, 12, 22]", "[11, 12, 21, 22]", "[10, 20, 1, 2]", "[11, 22]"],
                "correct_answer": 0,
                "explanation": "The outer loop iterates x first, then the inner loop iterates y."
            },
            {
                "question_text": "Which expression creates a generator expression?",
                "options": ["(x * 2 for x in range(3))", "[x * 2 for x in range(3)]", "{x * 2 for x in range(3)}", "{x: x * 2 for x in range(3)}"],
                "correct_answer": 0,
                "explanation": "Parentheses around a comprehension expression create a generator expression."
            },
            {
                "question_text": "What is the output of sum(x for x in range(4))?",
                "options": ["6", "4", "10", "3"],
                "correct_answer": 0,
                "explanation": "The generated values are 0, 1, 2 and 3, whose sum is 6."
            },
            {
                "question_text": "Which statement about generator expressions is correct?",
                "options": ["They produce values lazily", "They always create a list", "They cannot be iterated", "They store all results immediately"],
                "correct_answer": 0,
                "explanation": "Generator expressions produce values on demand."
            },
            {
                "question_text": "Which method of a generator can send a value into a suspended generator?",
                "options": ["send()", "throw()", "close()", "next()"],
                "correct_answer": 0,
                "explanation": "send() resumes a generator and supplies a value to its suspended yield expression."
            },
            {
                "question_text": "Which generator method raises an exception at the suspension point?",
                "options": ["throw()", "send()", "close()", "raise()"],
                "correct_answer": 0,
                "explanation": "throw() raises the specified exception inside a suspended generator."
            },
            {
                "question_text": "Which generator method requests that a generator stop?",
                "options": ["close()", "stop()", "finish()", "end()"],
                "correct_answer": 0,
                "explanation": "close() raises GeneratorExit inside the generator."
            },
            {
                "question_text": "Which exception signals that an iterator has no more values?",
                "options": ["StopIteration", "IndexError", "EOFError", "RuntimeError"],
                "correct_answer": 0,
                "explanation": "StopIteration signals the end of an iterator."
            },
            {
                "question_text": "Which special method makes an object iterable using the iter() function?",
                "options": ["__iter__()", "__next__()", "__getitem__()", "__call__()"],
                "correct_answer": 0,
                "explanation": "__iter__() returns an iterator for an iterable object."
            },
            {
                "question_text": "Which special method retrieves the next item from an iterator?",
                "options": ["__next__()", "__iter__()", "__getitem__()", "__call__()"],
                "correct_answer": 0,
                "explanation": "__next__() returns the next item or raises StopIteration."
            },
            {
                "question_text": "What is the output of next(iter([4, 5, 6]))?",
                "options": ["4", "5", "6", "None"],
                "correct_answer": 0,
                "explanation": "A new iterator starts at the first element, which is 4."
            },
            {
                "question_text": "Which special method is used to support the len() function?",
                "options": ["__len__()", "__size__()", "__count__()", "__length__()"],
                "correct_answer": 0,
                "explanation": "__len__() defines the length behavior of an object."
            },
            {
                "question_text": "Which special method is used to support item lookup with square brackets?",
                "options": ["__getitem__()", "__getattr__()", "__index__()", "__lookup__()"],
                "correct_answer": 0,
                "explanation": "__getitem__() implements indexed and keyed item access."
            },
            {
                "question_text": "Which special method is used to support assignment with square brackets?",
                "options": ["__setitem__()", "__getitem__()", "__setattr__()", "__assign__()"],
                "correct_answer": 0,
                "explanation": "__setitem__() implements item assignment."
            },
            {
                "question_text": "Which special method is used to support the in operator for a custom object?",
                "options": ["__contains__()", "__iter__()", "__next__()", "__inside__()"],
                "correct_answer": 0,
                "explanation": "__contains__() implements membership testing."
            },
            {
                "question_text": "Which special method is called when an object is used in a for loop if it is an iterator?",
                "options": ["__next__()", "__iter__()", "__loop__()", "__for__()"],
                "correct_answer": 0,
                "explanation": "An iterator's __next__() supplies successive values during iteration."
            },
            {
                "question_text": "Which special method can define how an object behaves when called like a function?",
                "options": ["__call__()", "__func__()", "__invoke__()", "__run__()"],
                "correct_answer": 0,
                "explanation": "__call__() allows instances to be called as functions."
            },
            {
                "question_text": "Which special method is used to implement the less-than operator?",
                "options": ["__lt__()", "__le__()", "__gt__()", "__cmp__()"],
                "correct_answer": 0,
                "explanation": "__lt__() implements the < comparison."
            },
            {
                "question_text": "Which special method implements the greater-than-or-equal operator?",
                "options": ["__ge__()", "__gt__()", "__le__()", "__eq__()"],
                "correct_answer": 0,
                "explanation": "__ge__() implements the >= comparison."
            },
            {
                "question_text": "Which special method implements the multiplication operator?",
                "options": ["__mul__()", "__add__()", "__pow__()", "__div__()"],
                "correct_answer": 0,
                "explanation": "__mul__() implements multiplication with *."
            },
            {
                "question_text": "Which special method implements the modulo operator?",
                "options": ["__mod__()", "__divmod__()", "__floordiv__()", "__rem__()"],
                "correct_answer": 0,
                "explanation": "__mod__() implements the % operator."
            },
            {
                "question_text": "Which special method implements exponentiation?",
                "options": ["__pow__()", "__exp__()", "__mul__()", "__power__()"],
                "correct_answer": 0,
                "explanation": "__pow__() implements the ** operator."
            },
            {
                "question_text": "Which special method implements integer conversion using int()?",
                "options": ["__int__()", "__index__()", "__float__()", "__str__()"],
                "correct_answer": 0,
                "explanation": "__int__() defines integer conversion behavior."
            },
            {
                "question_text": "Which special method implements conversion to a floating-point value?",
                "options": ["__float__()", "__int__()", "__number__()", "__decimal__()"],
                "correct_answer": 0,
                "explanation": "__float__() defines conversion using float()."
            },
            {
                "question_text": "Which special method implements conversion to a string?",
                "options": ["__str__()", "__repr__()", "__text__()", "__format__()"],
                "correct_answer": 0,
                "explanation": "__str__() defines the string conversion behavior."
            },
            {
                "question_text": "Which special method supports formatted string conversion?",
                "options": ["__format__()", "__str__()", "__repr__()", "__formatstr__()"],
                "correct_answer": 0,
                "explanation": "__format__() implements format specification behavior."
            },
            {
                "question_text": "Which special method is called when an object is used in a context manager?",
                "options": ["__enter__()", "__start__()", "__open__()", "__begin__()"],
                "correct_answer": 0,
                "explanation": "__enter__() is called when entering a with block."
            },
            {
                "question_text": "Which special method is called when exiting a context manager?",
                "options": ["__exit__()", "__close__()", "__end__()", "__leave__()"],
                "correct_answer": 0,
                "explanation": "__exit__() is called when leaving a with block."
            },
            {
                "question_text": "Which decorator can create a property with a setter?",
                "options": ["@property_name.setter", "@setter", "@classmethod", "@staticmethod"],
                "correct_answer": 0,
                "explanation": "A property object's setter decorator defines assignment behavior for that property."
            },
            {
                "question_text": "Which built-in function retrieves an attribute and can use a default if it is missing?",
                "options": ["getattr()", "hasattr()", "setattr()", "delattr()"],
                "correct_answer": 0,
                "explanation": "getattr() accepts an optional default value."
            },
            {
                "question_text": "Which built-in function assigns a named attribute to an object?",
                "options": ["setattr()", "getattr()", "hasattr()", "delattr()"],
                "correct_answer": 0,
                "explanation": "setattr() assigns a named attribute."
            },
            {
                "question_text": "Which built-in function deletes a named attribute from an object?",
                "options": ["delattr()", "setattr()", "getattr()", "hasattr()"],
                "correct_answer": 0,
                "explanation": "delattr() deletes the named attribute."
            },
            {
                "question_text": "Which built-in function returns an iterator of an object's attributes and methods?",
                "options": ["dir()", "vars()", "id()", "type()"],
                "correct_answer": 0,
                "explanation": "dir() returns a list of names associated with an object."
            },
            {
                "question_text": "Which built-in function returns an object's __dict__ attribute when available?",
                "options": ["vars()", "dir()", "locals()", "globals()"],
                "correct_answer": 0,
                "explanation": "vars() without arguments returns the current local namespace; with an object, it returns its __dict__ when available."
            },
            {
                "question_text": "Which built-in function returns the current global symbol table as a dictionary?",
                "options": ["globals()", "locals()", "vars()", "dir()"],
                "correct_answer": 0,
                "explanation": "globals() returns the current global namespace dictionary."
            },
            {
                "question_text": "Which built-in function returns the current local symbol table as a dictionary?",
                "options": ["locals()", "globals()", "vars()", "dir()"],
                "correct_answer": 0,
                "explanation": "locals() returns the current local namespace mapping."
            },
            {
                "question_text": "Which built-in function returns the identity of an object?",
                "options": ["id()", "hash()", "type()", "repr()"],
                "correct_answer": 0,
                "explanation": "id() returns the identity value of an object."
            },
            {
                "question_text": "Which built-in function checks whether an object is an instance of a class?",
                "options": ["isinstance()", "issubclass()", "type()", "id()"],
                "correct_answer": 0,
                "explanation": "isinstance() tests an object's class membership."
            },
            {
                "question_text": "Which built-in function checks the inheritance relationship between two classes?",
                "options": ["issubclass()", "isinstance()", "hasattr()", "callable()"],
                "correct_answer": 0,
                "explanation": "issubclass() tests whether one class derives from another."
            },
            {
                "question_text": "Which built-in function can check whether an object supports calling?",
                "options": ["callable()", "hasattr()", "isinstance()", "type()"],
                "correct_answer": 0,
                "explanation": "callable() checks whether an object can be called."
            },
            {
                "question_text": "Which built-in function returns the hash value of a hashable object?",
                "options": ["hash()", "id()", "hex()", "ord()"],
                "correct_answer": 0,
                "explanation": "hash() returns the hash value used by hash-based collections."
            },
            {
                "question_text": "Which built-in function returns the Unicode code point of a character?",
                "options": ["ord()", "chr()", "ascii()", "bin()"],
                "correct_answer": 0,
                "explanation": "ord() returns the Unicode code point."
            },
            {
                "question_text": "Which built-in function converts a Unicode code point into a character?",
                "options": ["chr()", "ord()", "ascii()", "hex()"],
                "correct_answer": 0,
                "explanation": "chr() returns the character represented by the code point."
            },
            {
                "question_text": "Which built-in function returns the ASCII representation of an object?",
                "options": ["ascii()", "ord()", "chr()", "repr()"],
                "correct_answer": 0,
                "explanation": "ascii() returns a printable representation with non-ASCII characters escaped."
            },
            {
                "question_text": "What is the output of ascii('é')?",
                "options": ["'\\xe9'", "'é'", "'e'", "Error"],
                "correct_answer": 0,
                "explanation": "ascii() escapes non-ASCII characters in the returned representation."
            },
            {
                "question_text": "Which built-in function returns the length of an object?",
                "options": ["len()", "size()", "count()", "length()"],
                "correct_answer": 0,
                "explanation": "len() returns the number of items in a supported object."
            },
            {
                "question_text": "Which built-in function returns the type of an object?",
                "options": ["type()", "id()", "class()", "kind()"],
                "correct_answer": 0,
                "explanation": "type() returns the object's type."
            },
            {
                "question_text": "Which built-in function can create a new class dynamically?",
                "options": ["type()", "class()", "object()", "newclass()"],
                "correct_answer": 0,
                "explanation": "The three-argument form of type() creates a new class dynamically."
            },
            {
                "question_text": "Which built-in function returns a representation of an object as a string?",
                "options": ["repr()", "str()", "format()", "print()"],
                "correct_answer": 0,
                "explanation": "repr() returns the developer-oriented representation."
            },
            {
                "question_text": "Which built-in function returns a human-readable string representation?",
                "options": ["str()", "repr()", "id()", "hash()"],
                "correct_answer": 0,
                "explanation": "str() returns a readable string representation."
            },
            {
                "question_text": "Which built-in function can convert an iterable to a tuple?",
                "options": ["tuple()", "list()", "set()", "dict()"],
                "correct_answer": 0,
                "explanation": "tuple() constructs a tuple from an iterable."
            },
            {
                "question_text": "Which built-in function can convert an iterable to a set?",
                "options": ["set()", "tuple()", "list()", "dict()"],
                "correct_answer": 0,
                "explanation": "set() creates a set from an iterable."
            },
            {
                "question_text": "Which built-in function can convert an iterable to a list?",
                "options": ["list()", "tuple()", "set()", "dict()"],
                "correct_answer": 0,
                "explanation": "list() creates a list from an iterable."
            },
            {
                "question_text": "Which built-in function can construct a dictionary?",
                "options": ["dict()", "list()", "tuple()", "set()"],
                "correct_answer": 0,
                "explanation": "dict() constructs a dictionary from mappings or key-value pairs."
            },
            {
                "question_text": "Which built-in function can return a range object?",
                "options": ["range()", "list()", "iter()", "enumerate()"],
                "correct_answer": 0,
                "explanation": "range() creates an immutable sequence of integers."
            },
            {
                "question_text": "Which built-in function can return an iterator from an iterable?",
                "options": ["iter()", "next()", "range()", "enumerate()"],
                "correct_answer": 0,
                "explanation": "iter() returns an iterator from an iterable."
            },
            {
                "question_text": "Which built-in function retrieves the next item from an iterator?",
                "options": ["next()", "iter()", "first()", "advance()"],
                "correct_answer": 0,
                "explanation": "next() obtains the next value from an iterator."
            },
            {
                "question_text": "Which built-in function can return an iterator with index-value pairs?",
                "options": ["enumerate()", "zip()", "map()", "filter()"],
                "correct_answer": 0,
                "explanation": "enumerate() produces index-value pairs."
            },
            {
                "question_text": "Which built-in function applies a function to each item in one or more iterables?",
                "options": ["map()", "filter()", "reduce()", "zip()"],
                "correct_answer": 0,
                "explanation": "map() applies a function to corresponding iterable elements."
            },
            {
                "question_text": "Which built-in function selects items for which a predicate is true?",
                "options": ["filter()", "map()", "zip()", "enumerate()"],
                "correct_answer": 0,
                "explanation": "filter() retains elements for which the predicate returns True."
            },
            {
                "question_text": "Which built-in function combines corresponding elements from multiple iterables?",
                "options": ["zip()", "map()", "filter()", "enumerate()"],
                "correct_answer": 0,
                "explanation": "zip() pairs corresponding items from input iterables."
            },
            {
                "question_text": "Which built-in function returns the maximum value from an iterable?",
                "options": ["max()", "min()", "sum()", "sorted()"],
                "correct_answer": 0,
                "explanation": "max() returns the largest item."
            },
            {
                "question_text": "Which built-in function returns the minimum value from an iterable?",
                "options": ["min()", "max()", "sum()", "sorted()"],
                "correct_answer": 0,
                "explanation": "min() returns the smallest item."
            },
            {
                "question_text": "Which built-in function returns the sum of an iterable?",
                "options": ["sum()", "add()", "total()", "reduce()"],
                "correct_answer": 0,
                "explanation": "sum() adds the values in an iterable."
            },
            {
                "question_text": "Which built-in function returns a sorted list?",
                "options": ["sorted()", "sort()", "order()", "arrange()"],
                "correct_answer": 0,
                "explanation": "sorted() returns a new sorted list."
            },
            {
                "question_text": "Which built-in function returns the absolute value?",
                "options": ["abs()", "round()", "floor()", "ceil()"],
                "correct_answer": 0,
                "explanation": "abs() returns the magnitude of a number."
            },
            {
                "question_text": "Which built-in function rounds a number to a specified number of digits?",
                "options": ["round()", "abs()", "floor()", "ceil()"],
                "correct_answer": 0,
                "explanation": "round() rounds a number to the requested precision."
            },
            {
                "question_text": "Which built-in function returns the quotient and remainder of integer division?",
                "options": ["divmod()", "pow()", "round()", "abs()"],
                "correct_answer": 0,
                "explanation": "divmod() returns quotient and remainder together."
            },
            {
                "question_text": "Which built-in function performs exponentiation?",
                "options": ["pow()", "abs()", "round()", "divmod()"],
                "correct_answer": 0,
                "explanation": "pow() raises a number to a specified power."
            },
            {
                "question_text": "Which built-in function checks whether all values are true?",
                "options": ["all()", "any()", "bool()", "filter()"],
                "correct_answer": 0,
                "explanation": "all() returns True when every item is truthy."
            },
            {
                "question_text": "Which built-in function checks whether at least one value is true?",
                "options": ["any()", "all()", "bool()", "filter()"],
                "correct_answer": 0,
                "explanation": "any() returns True if at least one item is truthy."
            },
            {
                "question_text": "Which built-in function converts a value to a Boolean?",
                "options": ["bool()", "int()", "str()", "type()"],
                "correct_answer": 0,
                "explanation": "bool() returns the truth value of an object."
            },
            {
                "question_text": "Which built-in function converts a value to an integer?",
                "options": ["int()", "float()", "str()", "bool()"],
                "correct_answer": 0,
                "explanation": "int() converts compatible values to integers."
            },
            {
                "question_text": "Which built-in function converts a value to a floating-point number?",
                "options": ["float()", "int()", "str()", "complex()"],
                "correct_answer": 0,
                "explanation": "float() converts compatible values to floating-point numbers."
            },
            {
                "question_text": "Which built-in function converts a value to a string?",
                "options": ["str()", "repr()", "int()", "bytes()"],
                "correct_answer": 0,
                "explanation": "str() creates a string representation."
            },
            {
                "question_text": "Which built-in function creates a bytes object from an iterable of integers?",
                "options": ["bytes()", "bytearray()", "str()", "memoryview()"],
                "correct_answer": 0,
                "explanation": "bytes() creates an immutable bytes object."
            },
            {
                "question_text": "Which built-in type represents a mutable sequence of bytes?",
                "options": ["bytearray", "bytes", "str", "memoryview"],
                "correct_answer": 0,
                "explanation": "bytearray is a mutable sequence of integers representing bytes."
            },
            {
                "question_text": "Which built-in type provides a memory view of an object's buffer?",
                "options": ["memoryview", "bytearray", "bytes", "buffer"],
                "correct_answer": 0,
                "explanation": "memoryview allows access to buffer-protocol data without copying it."
            },
            {
                "question_text": "Which built-in function returns the Boolean inverse of a truth value?",
                "options": ["not", "bool()", "any()", "all()"],
                "correct_answer": 0,
                "explanation": "The not operator returns the logical negation of its operand."
            },
            {
                "question_text": "What is the output of not 0?",
                "options": ["True", "False", "0", "None"],
                "correct_answer": 0,
                "explanation": "Zero is falsy, so not 0 evaluates to True."
            },
            {
                "question_text": "What is the output of not 'hello'?",
                "options": ["True", "False", "hello", "None"],
                "correct_answer": 1,
                "explanation": "A non-empty string is truthy, so its negation is False."
            },
            {
                "question_text": "Which operator checks equality?",
                "options": ["==", "is", "!=", "="],
                "correct_answer": 0,
                "explanation": "== compares values for equality."
            },
            {
                "question_text": "Which operator checks inequality?",
                "options": ["!=", "==", "is", "<="],
                "correct_answer": 0,
                "explanation": "!= returns True when values are not equal."
            },
            {
                "question_text": "Which operator checks whether two references point to the same object?",
                "options": ["is", "==", "in", "!="],
                "correct_answer": 0,
                "explanation": "is tests object identity."
            },
            {
                "question_text": "Which operator checks membership in a sequence?",
                "options": ["in", "is", "==", "and"],
                "correct_answer": 0,
                "explanation": "in checks whether an element belongs to a collection."
            },
            {
                "question_text": "Which logical operator returns True only when both operands are truthy?",
                "options": ["and", "or", "not", "xor"],
                "correct_answer": 0,
                "explanation": "and evaluates to a truthy result only when both operands are truthy."
            },
            {
                "question_text": "Which logical operator returns a truthy result when at least one operand is truthy?",
                "options": ["or", "and", "not", "xor"],
                "correct_answer": 0,
                "explanation": "or returns a truthy operand when one is available."
            },
            {
                "question_text": "What is the output of True and False?",
                "options": ["True", "False", "None", "Error"],
                "correct_answer": 1,
                "explanation": "The and expression is false because the second operand is False."
            },
            {
                "question_text": "What is the output of False or True?",
                "options": ["True", "False", "None", "Error"],
                "correct_answer": 0,
                "explanation": "The or expression evaluates to True because the second operand is truthy."
            },
            {
                "question_text": "Which operator checks whether a value is not a member of a collection?",
                "options": ["not in", "is not", "!=", "not"],
                "correct_answer": 0,
                "explanation": "not in is the membership negation operator."
            },
            {
                "question_text": "Which operator checks that two objects are not identical?",
                "options": ["is not", "not in", "!=", "not"],
                "correct_answer": 0,
                "explanation": "is not returns True when two references do not identify the same object."
            },
            {
                "question_text": "What is the output of 5 > 3 and 2 < 4?",
                "options": ["True", "False", "None", "Error"],
                "correct_answer": 0,
                "explanation": "Both comparisons are true, so the and expression is True."
            },
            {
                "question_text": "What is the output of 5 < 3 or 2 < 4?",
                "options": ["True", "False", "None", "Error"],
                "correct_answer": 0,
                "explanation": "The second comparison is true, so the or expression is True."
            },
            {
                "question_text": "Which operator performs floor division?",
                "options": ["//", "/", "%", "**"],
                "correct_answer": 0,
                "explanation": "// performs floor division."
            },
            {
                "question_text": "Which operator returns the remainder of division?",
                "options": ["%", "//", "/", "**"],
                "correct_answer": 0,
                "explanation": "% returns the remainder."
            },
            {
                "question_text": "Which operator performs true division?",
                "options": ["/", "//", "%", "**"],
                "correct_answer": 0,
                "explanation": "/ performs true division and returns a floating-point result for numeric operands."
            },
            {
                "question_text": "Which operator performs exponentiation?",
                "options": ["**", "^", "//", "%"],
                "correct_answer": 0,
                "explanation": "** raises a number to a power."
            },
            {
                "question_text": "What is the output of 2 ** 3?",
                "options": ["6", "8", "9", "5"],
                "correct_answer": 1,
                "explanation": "2 raised to the third power is 8."
            },
            {
                "question_text": "What is the output of 10 // 3?",
                "options": ["3", "3.33", "1", "4"],
                "correct_answer": 0,
                "explanation": "Floor division returns 3."
            },
            {
                "question_text": "What is the output of 10 % 3?",
                "options": ["1", "3", "0", "3.33"],
                "correct_answer": 0,
                "explanation": "The remainder is 1."
            },
            {
                "question_text": "Which operator performs bitwise AND?",
                "options": ["&", "|", "^", "~"],
                "correct_answer": 0,
                "explanation": "& performs bitwise AND."
            },
            {
                "question_text": "Which operator performs bitwise OR?",
                "options": ["|", "&", "^", "~"],
                "correct_answer": 0,
                "explanation": "| performs bitwise OR."
            },
            {
                "question_text": "Which operator performs bitwise XOR?",
                "options": ["^", "&", "|", "~"],
                "correct_answer": 0,
                "explanation": "^ performs bitwise exclusive OR."
            },
            {
                "question_text": "Which operator performs bitwise inversion?",
                "options": ["~", "^", "&", "|"],
                "correct_answer": 0,
                "explanation": "~ inverts the bits of an integer."
            },
            {
                "question_text": "Which operator shifts bits to the right?",
                "options": [">>", "<<", "&", "|"],
                "correct_answer": 0,
                "explanation": ">> performs a right bit shift."
            },
            {
                "question_text": "What is the output of 8 >> 1?",
                "options": ["4", "16", "2", "8"],
                "correct_answer": 0,
                "explanation": "Right shifting 8 by one bit gives 4."
            },
            {
                "question_text": "What is the output of 2 << 3?",
                "options": ["16", "8", "6", "12"],
                "correct_answer": 0,
                "explanation": "Left shifting 2 by three bits gives 16."
            },
            {
                "question_text": "Which built-in function can return the quotient and remainder of a division?",
                "options": ["divmod()", "pow()", "round()", "abs()"],
                "correct_answer": 0,
                "explanation": "divmod() returns both values as a tuple."
            },
            {
                "question_text": "What is the output of divmod(20, 6)?",
                "options": ["(3, 2)", "(2, 3)", "(3, 1)", "(4, 2)"],
                "correct_answer": 0,
                "explanation": "20 divided by 6 has quotient 3 and remainder 2."
            },
            {
                "question_text": "Which operator is used for assignment?",
                "options": ["=", "==", "!=", ":="],
                "correct_answer": 0,
                "explanation": "= assigns a value to a variable."
            },
            {
                "question_text": "Which operator is used for equality comparison?",
                "options": ["==", "=", "!=", ":="],
                "correct_answer": 0,
                "explanation": "== compares two values."
            },
            {
                "question_text": "Which operator performs assignment expression in Python?",
                "options": [":=", "=", "==", "=>"],
                "correct_answer": 0,
                "explanation": ":= is the assignment expression operator, also called the walrus operator."
            },
            {
                "question_text": "Which operator is used to concatenate two strings?",
                "options": ["+", "*", "&", "|"],
                "correct_answer": 0,
                "explanation": "The + operator concatenates strings."
            },
            {
                "question_text": "What is the output of 'py' + 'thon'?",
                "options": ["python", "py thon", "python", "Error"],
                "correct_answer": 0,
                "explanation": "String concatenation joins the two strings."
            },
            {
                "question_text": "Which operator repeats a sequence?",
                "options": ["*", "+", "/", "%"],
                "correct_answer": 0,
                "explanation": "The * operator repeats sequences when multiplied by an integer."
            },
            {
                "question_text": "What is the output of [1, 2] * 2?",
                "options": ["[1, 2, 1, 2]", "[2, 4]", "[1, 2, 2]", "Error"],
                "correct_answer": 0,
                "explanation": "List multiplication repeats the list contents."
            },
            {
                "question_text": "Which operator is used to unpack an iterable into positional arguments?",
                "options": ["*", "**", "&", "|"],
                "correct_answer": 0,
                "explanation": "* unpacks an iterable into positional arguments."
            },
            {
                "question_text": "Which operator unpacks a dictionary into keyword arguments?",
                "options": ["**", "*", "&", "|"],
                "correct_answer": 0,
                "explanation": "** unpacks dictionary key-value pairs as keyword arguments."
            },
            {
                "question_text": "Which function can return a shallow copy of a list?",
                "options": ["copy()", "deepcopy()", "clone()", "duplicate()"],
                "correct_answer": 0,
                "explanation": "The list copy() method returns a shallow copy."
            },
            {
                "question_text": "Which module provides deep-copy functionality?",
                "options": ["copy", "collections", "types", "pickle"],
                "correct_answer": 0,
                "explanation": "The copy module provides copy() and deepcopy()."
            },
            {
                "question_text": "Which function creates a deep copy of an object?",
                "options": ["copy.deepcopy()", "copy.copy()", "list()", "repr()"],
                "correct_answer": 0,
                "explanation": "deepcopy() recursively copies nested objects."
            },
            {
                "question_text": "Which method can check whether a string starts with one of several possible prefixes?",
                "options": ["startswith()", "find()", "count()", "partition()"],
                "correct_answer": 0,
                "explanation": "startswith() accepts a tuple of prefixes."
            },
            {
                "question_text": "What is the output of 'python'.startswith(('py', 'ja'))?",
                "options": ["True", "False", "None", "Error"],
                "correct_answer": 0,
                "explanation": "The string begins with py, one of the supplied prefixes."
            },
            {
                "question_text": "Which method can remove a specified prefix from a string if it exists?",
                "options": ["removeprefix()", "strip()", "lstrip()", "replace()"],
                "correct_answer": 0,
                "explanation": "removeprefix() removes the exact matching prefix."
            },
            {
                "question_text": "Which method can remove a specified suffix from a string if it exists?",
                "options": ["removesuffix()", "rstrip()", "strip()", "replace()"],
                "correct_answer": 0,
                "explanation": "removesuffix() removes the exact matching suffix."
            },
            {
                "question_text": "What is the output of 'unhappy'.removeprefix('un')?",
                "options": ["happy", "unhappy", "un", "Error"],
                "correct_answer": 0,
                "explanation": "The prefix un is removed, leaving happy."
            },
            {
                "question_text": "What is the output of 'testing.py'.removesuffix('.py')?",
                "options": ["testing", "testing.py", ".py", "Error"],
                "correct_answer": 0,
                "explanation": "The suffix .py is removed."
            },
            {
                "question_text": "Which method returns the string with all occurrences of a substring replaced?",
                "options": ["replace()", "sub()", "change()", "swap()"],
                "correct_answer": 0,
                "explanation": "replace() returns a string with occurrences replaced."
            },
            {
                "question_text": "What is the output of 'aaa'.replace('a', 'b', 2)?",
                "options": ["bba", "bbb", "abb", "aaa"],
                "correct_answer": 0,
                "explanation": "The count argument limits replacement to the first two occurrences."
            },
            {
                "question_text": "Which string method removes leading and trailing characters from a specified set?",
                "options": ["strip()", "replace()", "split()", "partition()"],
                "correct_answer": 0,
                "explanation": "strip(chars) removes leading and trailing characters belonging to the supplied set."
            },
            {
                "question_text": "What is the output of 'xxhelloxx'.strip('x')?",
                "options": ["hello", "xxhello", "helloxx", "xhellox"],
                "correct_answer": 0,
                "explanation": "strip('x') removes x characters from both ends."
            },
            {
                "question_text": "Which method removes whitespace from the end of a string?",
                "options": ["rstrip()", "lstrip()", "strip()", "trimright()"],
                "correct_answer": 0,
                "explanation": "rstrip() removes trailing whitespace."
            },
            {
                "question_text": "Which method removes whitespace from the beginning of a string?",
                "options": ["lstrip()", "rstrip()", "strip()", "trimleft()"],
                "correct_answer": 0,
                "explanation": "lstrip() removes leading whitespace."
            },
            {
                "question_text": "Which method splits a string from the right side?",
                "options": ["rsplit()", "split()", "partition()", "rpartition()"],
                "correct_answer": 0,
                "explanation": "rsplit() splits starting from the right."
            },
            {
                "question_text": "Which method splits a string at the first occurrence of a separator?",
                "options": ["partition()", "split()", "rsplit()", "rpartition()"],
                "correct_answer": 0,
                "explanation": "partition() splits at the first separator occurrence."
            },
            {
                "question_text": "Which method splits a string at the last occurrence of a separator?",
                "options": ["rpartition()", "partition()", "split()", "rsplit()"],
                "correct_answer": 0,
                "explanation": "rpartition() splits at the last separator occurrence."
            },
            {
                "question_text": "What is the output of 'a:b:c'.partition(':')?",
                "options": ["('a', ':', 'b:c')", "('a:b', ':', 'c')", "['a', 'b', 'c']", "('a:b:c', '', '')"],
                "correct_answer": 0,
                "explanation": "partition() splits at the first colon."
            },
            {
                "question_text": "What is the output of 'a:b:c'.rpartition(':')?",
                "options": ["('a:b', ':', 'c')", "('a', ':', 'b:c')", "['a', 'b', 'c']", "('a:b:c', '', '')"],
                "correct_answer": 0,
                "explanation": "rpartition() splits at the last colon."
            },
            {
                "question_text": "Which method returns a new string with each word capitalized?",
                "options": ["title()", "capitalize()", "upper()", "casefold()"],
                "correct_answer": 0,
                "explanation": "title() applies title-case conversion."
            },
            {
                "question_text": "Which method capitalizes only the first character and lowercases the rest?",
                "options": ["capitalize()", "title()", "upper()", "casefold()"],
                "correct_answer": 0,
                "explanation": "capitalize() uppercases the first character and lowercases the remaining characters."
            },
            {
                "question_text": "Which method performs Unicode case folding for caseless matching?",
                "options": ["casefold()", "lower()", "upper()", "capitalize()"],
                "correct_answer": 0,
                "explanation": "casefold() is designed for caseless Unicode string matching."
            },
            {
                "question_text": "Which method checks whether all characters are lowercase?",
                "options": ["islower()", "isupper()", "istitle()", "isalpha()"],
                "correct_answer": 0,
                "explanation": "islower() checks lowercase status of cased characters."
            },
            {
                "question_text": "Which method checks whether all cased characters are uppercase?",
                "options": ["isupper()", "islower()", "istitle()", "isalpha()"],
                "correct_answer": 0,
                "explanation": "isupper() checks uppercase status of cased characters."
            },
            {
                "question_text": "Which method checks whether all characters are alphabetic?",
                "options": ["isalpha()", "isalnum()", "isdigit()", "isnumeric()"],
                "correct_answer": 0,
                "explanation": "isalpha() checks whether all characters are alphabetic."
            },
            {
                "question_text": "Which method checks whether all characters are alphanumeric?",
                "options": ["isalnum()", "isalpha()", "isdigit()", "isdecimal()"],
                "correct_answer": 0,
                "explanation": "isalnum() checks whether all characters are letters or numbers."
            },
            {
                "question_text": "Which method checks whether all characters are numeric?",
                "options": ["isnumeric()", "isalpha()", "islower()", "istitle()"],
                "correct_answer": 0,
                "explanation": "isnumeric() recognizes Unicode numeric characters."
            },
            {
                "question_text": "Which method checks whether all characters are decimal digits?",
                "options": ["isdecimal()", "isalpha()", "isspace()", "isidentifier()"],
                "correct_answer": 0,
                "explanation": "isdecimal() checks for decimal characters."
            },
            {
                "question_text": "Which method checks whether a string contains only digits?",
                "options": ["isdigit()", "isalpha()", "isupper()", "istitle()"],
                "correct_answer": 0,
                "explanation": "isdigit() checks for digit characters."
            },
            {
                "question_text": "Which method checks whether a string contains only whitespace characters?",
                "options": ["isspace()", "isalpha()", "isalnum()", "isdecimal()"],
                "correct_answer": 0,
                "explanation": "isspace() checks for whitespace characters."
            },
            {
                "question_text": "Which method checks whether a string is a valid identifier?",
                "options": ["isidentifier()", "isalpha()", "isalnum()", "iskeyword()"],
                "correct_answer": 0,
                "explanation": "isidentifier() checks identifier syntax, but not whether the name is a reserved keyword."
            },
            {
                "question_text": "Which module can check whether a string is a Python keyword?",
                "options": ["keyword", "tokenize", "ast", "inspect"],
                "correct_answer": 0,
                "explanation": "The keyword module provides iskeyword() and keyword lists."
            },
            {
                "question_text": "Which function checks whether a string is a reserved Python keyword?",
                "options": ["keyword.iskeyword()", "str.isidentifier()", "ast.parse()", "inspect.isclass()"],
                "correct_answer": 0,
                "explanation": "keyword.iskeyword() checks whether a string is a Python keyword."
            },
            {
                "question_text": "Which method expands tab characters into spaces?",
                "options": ["expandtabs()", "replace()", "split()", "join()"],
                "correct_answer": 0,
                "explanation": "expandtabs() replaces tab characters with spaces."
            },
            {
                "question_text": "Which method returns a centered string padded to a given width?",
                "options": ["center()", "ljust()", "rjust()", "zfill()"],
                "correct_answer": 0,
                "explanation": "center() centers the string within the requested width."
            },
            {
                "question_text": "Which method right-aligns a string within a given width?",
                "options": ["rjust()", "ljust()", "center()", "zfill()"],
                "correct_answer": 0,
                "explanation": "rjust() right-aligns the string."
            },
            {
                "question_text": "Which method left-aligns a string within a given width?",
                "options": ["ljust()", "rjust()", "center()", "zfill()"],
                "correct_answer": 0,
                "explanation": "ljust() left-aligns the string."
            },
            {
                "question_text": "Which method pads a numeric string with zeros on the left?",
                "options": ["zfill()", "ljust()", "rjust()", "center()"],
                "correct_answer": 0,
                "explanation": "zfill() pads a string on the left using zero characters."
            },
            {
                "question_text": "Which method joins an iterable of strings using a separator?",
                "options": ["join()", "split()", "partition()", "replace()"],
                "correct_answer": 0,
                "explanation": "join() combines strings with the calling string as separator."
            },
            {
                "question_text": "What is the output of '-'.join(['a', 'b', 'c'])?",
                "options": ["a-b-c", "abc", "['a', 'b', 'c']", "a,b,c"],
                "correct_answer": 0,
                "explanation": "The hyphen joins the three strings."
            },
            {
                "question_text": "Which method returns a list of substrings separated by whitespace by default?",
                "options": ["split()", "join()", "partition()", "replace()"],
                "correct_answer": 0,
                "explanation": "split() separates a string into a list."
            },
            {
                "question_text": "Which method returns the lowest index of a substring or -1 when absent?",
                "options": ["find()", "index()", "count()", "rfind()"],
                "correct_answer": 0,
                "explanation": "find() returns -1 if the substring is not found."
            },
            {
                "question_text": "Which method returns the highest index of a substring or -1 when absent?",
                "options": ["rfind()", "find()", "index()", "count()"],
                "correct_answer": 0,
                "explanation": "rfind() searches from the right and returns the highest matching index."
            },
            {
                "question_text": "Which method returns the lowest index of a substring and raises ValueError if absent?",
                "options": ["index()", "find()", "rfind()", "count()"],
                "correct_answer": 0,
                "explanation": "index() raises ValueError when the substring is missing."
            },
            {
                "question_text": "Which method returns the number of non-overlapping occurrences of a substring?",
                "options": ["count()", "find()", "index()", "rfind()"],
                "correct_answer": 0,
                "explanation": "count() counts non-overlapping occurrences."
            },
            {
                "question_text": "What is the output of 'aaaa'.count('aa')?",
                "options": ["2", "3", "4", "1"],
                "correct_answer": 0,
                "explanation": "count() counts non-overlapping matches, so the result is 2."
            },
            {
                "question_text": "Which method checks whether a string begins with a prefix?",
                "options": ["startswith()", "endswith()", "find()", "count()"],
                "correct_answer": 0,
                "explanation": "startswith() checks a string prefix."
            },
            {
                "question_text": "Which method checks whether a string ends with a suffix?",
                "options": ["endswith()", "startswith()", "find()", "count()"],
                "correct_answer": 0,
                "explanation": "endswith() checks a string suffix."
            },
            {
                "question_text": "Which method returns a copy of a string with a specified substring replaced?",
                "options": ["replace()", "remove()", "change()", "substitute()"],
                "correct_answer": 0,
                "explanation": "replace() returns a new string with the requested substitutions."
            },
            {
                "question_text": "Which method can limit the number of replacements?",
                "options": ["replace()", "split()", "join()", "partition()"],
                "correct_answer": 0,
                "explanation": "replace(old, new, count) limits the number of replacements."
            },
            {
                "question_text": "Which string method returns the original string if a prefix is absent?",
                "options": ["removeprefix()", "strip()", "replace()", "split()"],
                "correct_answer": 0,
                "explanation": "removeprefix() returns an unchanged copy when the prefix does not match."
            },
            {
                "question_text": "Which string method returns the original string if a suffix is absent?",
                "options": ["removesuffix()", "rstrip()", "replace()", "split()"],
                "correct_answer": 0,
                "explanation": "removesuffix() returns an unchanged copy when the suffix does not match."
            },
            {
                "question_text": "Which string method can return a tuple with three parts around the first separator?",
                "options": ["partition()", "split()", "rsplit()", "join()"],
                "correct_answer": 0,
                "explanation": "partition() returns a three-element tuple."
            },
            {
                "question_text": "Which string method can return a tuple with three parts around the last separator?",
                "options": ["rpartition()", "partition()", "split()", "rsplit()"],
                "correct_answer": 0,
                "explanation": "rpartition() returns a three-element tuple based on the last separator."
            },
            {
                "question_text": "Which method returns a copy of a string with the first character uppercase?",
                "options": ["capitalize()", "title()", "upper()", "casefold()"],
                "correct_answer": 0,
                "explanation": "capitalize() uppercases the first character and lowercases the rest."
            },
            {
                "question_text": "Which method returns a string with each word's first character uppercase?",
                "options": ["title()", "capitalize()", "upper()", "lower()"],
                "correct_answer": 0,
                "explanation": "title() applies title-case formatting."
            },
            {
                "question_text": "Which method converts all alphabetic characters to uppercase?",
                "options": ["upper()", "lower()", "capitalize()", "title()"],
                "correct_answer": 0,
                "explanation": "upper() returns an uppercase string."
            },
            {
                "question_text": "Which method converts all alphabetic characters to lowercase?",
                "options": ["lower()", "upper()", "capitalize()", "title()"],
                "correct_answer": 0,
                "explanation": "lower() returns a lowercase string."
            },
            {
                "question_text": "Which method changes the case of every cased character?",
                "options": ["swapcase()", "casefold()", "capitalize()", "title()"],
                "correct_answer": 0,
                "explanation": "swapcase() swaps uppercase and lowercase characters."
            },
            {
                "question_text": "Which method is most suitable for Unicode caseless comparison?",
                "options": ["casefold()", "lower()", "upper()", "title()"],
                "correct_answer": 0,
                "explanation": "casefold() is intended for caseless Unicode matching."
            },
            {
                "question_text": "Which method can check whether all characters are lowercase letters?",
                "options": ["islower()", "isupper()", "istitle()", "isnumeric()"],
                "correct_answer": 0,
                "explanation": "islower() checks whether cased characters are lowercase."
            },
            {
                "question_text": "Which method can check whether all characters are uppercase letters?",
                "options": ["isupper()", "islower()", "istitle()", "isnumeric()"],
                "correct_answer": 0,
                "explanation": "isupper() checks whether cased characters are uppercase."
            },
            {
                "question_text": "Which method checks whether a string is title-cased?",
                "options": ["istitle()", "isupper()", "islower()", "isalpha()"],
                "correct_answer": 0,
                "explanation": "istitle() checks title-case formatting."
            },
            {
                "question_text": "Which method checks whether all characters are alphabetic?",
                "options": ["isalpha()", "isalnum()", "isdigit()", "isspace()"],
                "correct_answer": 0,
                "explanation": "isalpha() checks for alphabetic characters."
            },
            {
                "question_text": "Which method checks whether all characters are alphanumeric?",
                "options": ["isalnum()", "isalpha()", "isdigit()", "isspace()"],
                "correct_answer": 0,
                "explanation": "isalnum() checks for letters and digits."
            },
            {
                "question_text": "Which method checks whether a string contains only whitespace?",
                "options": ["isspace()", "isalpha()", "isalnum()", "isdigit()"],
                "correct_answer": 0,
                "explanation": "isspace() checks whitespace characters."
            },
            {
                "question_text": "Which method checks whether all characters are decimal digits?",
                "options": ["isdecimal()", "isdigit()", "isnumeric()", "isalpha()"],
                "correct_answer": 0,
                "explanation": "isdecimal() checks decimal characters."
            },
            {
                "question_text": "Which method checks whether all characters are digits?",
                "options": ["isdigit()", "isdecimal()", "isnumeric()", "isalpha()"],
                "correct_answer": 0,
                "explanation": "isdigit() checks digit characters."
            },
            {
                "question_text": "Which method checks whether all characters are numeric?",
                "options": ["isnumeric()", "isdigit()", "isdecimal()", "isalpha()"],
                "correct_answer": 0,
                "explanation": "isnumeric() recognizes Unicode numeric characters."
            },
            {
                "question_text": "Which method checks whether a string is a valid identifier?",
                "options": ["isidentifier()", "isalpha()", "isalnum()", "isdigit()"],
                "correct_answer": 0,
                "explanation": "isidentifier() checks whether a string follows identifier syntax."
            },
            {
                "question_text": "Which module checks whether an identifier is a Python keyword?",
                "options": ["keyword", "tokenize", "ast", "inspect"],
                "correct_answer": 0,
                "explanation": "The keyword module provides keyword.iskeyword()."
            },
            {
                "question_text": "Which method returns a new string padded with zeros on the left?",
                "options": ["zfill()", "center()", "ljust()", "rjust()"],
                "correct_answer": 0,
                "explanation": "zfill() adds zeros on the left."
            },
            {
                "question_text": "Which method returns a centered string with padding?",
                "options": ["center()", "ljust()", "rjust()", "zfill()"],
                "correct_answer": 0,
                "explanation": "center() centers a string within the requested width."
            },
            {
                "question_text": "Which method returns a left-aligned string with padding?",
                "options": ["ljust()", "rjust()", "center()", "zfill()"],
                "correct_answer": 0,
                "explanation": "ljust() left-aligns a string."
            },
            {
                "question_text": "Which method returns a right-aligned string with padding?",
                "options": ["rjust()", "ljust()", "center()", "zfill()"],
                "correct_answer": 0,
                "explanation": "rjust() right-aligns a string."
            },
            {
                "question_text": "Which method replaces tab characters with spaces?",
                "options": ["expandtabs()", "replace()", "split()", "join()"],
                "correct_answer": 0,
                "explanation": "expandtabs() expands tab characters."
            },
            {
                "question_text": "Which method removes leading and trailing whitespace?",
                "options": ["strip()", "lstrip()", "rstrip()", "replace()"],
                "correct_answer": 0,
                "explanation": "strip() removes whitespace from both ends."
            },
            {
                "question_text": "Which method removes leading whitespace?",
                "options": ["lstrip()", "rstrip()", "strip()", "replace()"],
                "correct_answer": 0,
                "explanation": "lstrip() removes whitespace from the left."
            },
            {
                "question_text": "Which method removes trailing whitespace?",
                "options": ["rstrip()", "lstrip()", "strip()", "replace()"],
                "correct_answer": 0,
                "explanation": "rstrip() removes whitespace from the right."
            },
            {
                "question_text": "Which method combines strings using a separator?",
                "options": ["join()", "split()", "partition()", "replace()"],
                "correct_answer": 0,
                "explanation": "join() combines an iterable of strings."
            },
            {
                "question_text": "Which method splits a string into a list?",
                "options": ["split()", "join()", "replace()", "partition()"],
                "correct_answer": 0,
                "explanation": "split() returns a list of substrings."
            },
            {
                "question_text": "Which method splits from the right side?",
                "options": ["rsplit()", "split()", "partition()", "rpartition()"],
                "correct_answer": 0,
                "explanation": "rsplit() splits from the right."
            },
            {
                "question_text": "Which method finds the first occurrence of a substring?",
                "options": ["find()", "rfind()", "count()", "replace()"],
                "correct_answer": 0,
                "explanation": "find() returns the first matching index."
            },
            {
                "question_text": "Which method finds the last occurrence of a substring?",
                "options": ["rfind()", "find()", "count()", "replace()"],
                "correct_answer": 0,
                "explanation": "rfind() returns the highest matching index."
            },
            {
                "question_text": "Which method counts substring occurrences?",
                "options": ["count()", "find()", "index()", "replace()"],
                "correct_answer": 0,
                "explanation": "count() returns the number of non-overlapping occurrences."
            },
            {
                "question_text": "Which method checks a string's prefix?",
                "options": ["startswith()", "endswith()", "find()", "count()"],
                "correct_answer": 0,
                "explanation": "startswith() checks the beginning of a string."
            },
            {
                "question_text": "Which method checks a string's suffix?",
                "options": ["endswith()", "startswith()", "find()", "count()"],
                "correct_answer": 0,
                "explanation": "endswith() checks the ending of a string."
            },
            {
                "question_text": "Which method substitutes one substring with another?",
                "options": ["replace()", "split()", "join()", "partition()"],
                "correct_answer": 0,
                "explanation": "replace() returns a new string with substitutions."
            },
            {
                "question_text": "Which method returns three pieces around the first separator?",
                "options": ["partition()", "rpartition()", "split()", "rsplit()"],
                "correct_answer": 0,
                "explanation": "partition() splits at the first separator."
            },
            {
                "question_text": "Which method returns three pieces around the last separator?",
                "options": ["rpartition()", "partition()", "split()", "rsplit()"],
                "correct_answer": 0,
                "explanation": "rpartition() splits at the last separator."
            },
            {
                "question_text": "Which method removes a prefix if it matches?",
                "options": ["removeprefix()", "strip()", "lstrip()", "replace()"],
                "correct_answer": 0,
                "explanation": "removeprefix() removes the exact matching prefix."
            },
            {
                "question_text": "Which method removes a suffix if it matches?",
                "options": ["removesuffix()", "strip()", "rstrip()", "replace()"],
                "correct_answer": 0,
                "explanation": "removesuffix() removes the exact matching suffix."
            },
            {
                "question_text": "Which function can return the smallest element of an iterable?",
                "options": ["min()", "max()", "sum()", "sorted()"],
                "correct_answer": 0,
                "explanation": "min() returns the smallest element."
            },
            {
                "question_text": "Which function can return the largest element of an iterable?",
                "options": ["max()", "min()", "sum()", "sorted()"],
                "correct_answer": 0,
                "explanation": "max() returns the largest element."
            },
            {
                "question_text": "Which function returns a new sorted list?",
                "options": ["sorted()", "sort()", "reverse()", "order()"],
                "correct_answer": 0,
                "explanation": "sorted() returns a new sorted list."
            },
            {
                "question_text": "Which method sorts an existing list in place?",
                "options": ["sort()", "sorted()", "order()", "arrange()"],
                "correct_answer": 0,
                "explanation": "sort() modifies the existing list."
            },
            {
                "question_text": "Which method reverses an existing list in place?",
                "options": ["reverse()", "reversed()", "sort()", "invert()"],
                "correct_answer": 0,
                "explanation": "reverse() modifies the list order in place."
            },
            {
                "question_text": "Which built-in function returns a reverse iterator?",
                "options": ["reversed()", "reverse()", "sort()", "sorted()"],
                "correct_answer": 0,
                "explanation": "reversed() returns a reverse iterator."
            },
            {
                "question_text": "Which function can return an integer's binary representation?",
                "options": ["bin()", "hex()", "oct()", "formatint()"],
                "correct_answer": 0,
                "explanation": "bin() returns a binary string."
            },
            {
                "question_text": "Which function can return an integer's hexadecimal representation?",
                "options": ["hex()", "bin()", "oct()", "formatint()"],
                "correct_answer": 0,
                "explanation": "hex() returns a hexadecimal string."
            },
            {
                "question_text": "Which function can return an integer's octal representation?",
                "options": ["oct()", "bin()", "hex()", "formatint()"],
                "correct_answer": 0,
                "explanation": "oct() returns an octal string."
            },
            {
                "question_text": "Which function converts a Unicode code point to a character?",
                "options": ["chr()", "ord()", "ascii()", "repr()"],
                "correct_answer": 0,
                "explanation": "chr() converts an integer code point to a string character."
            },
            {
                "question_text": "Which function converts a character to its Unicode code point?",
                "options": ["ord()", "chr()", "ascii()", "repr()"],
                "correct_answer": 0,
                "explanation": "ord() returns the Unicode code point."
            },
            {
                "question_text": "Which built-in function returns the object's type?",
                "options": ["type()", "id()", "hash()", "repr()"],
                "correct_answer": 0,
                "explanation": "type() returns the object's type."
            },
            {
                "question_text": "Which built-in function returns the object's identity?",
                "options": ["id()", "type()", "hash()", "repr()"],
                "correct_answer": 0,
                "explanation": "id() returns the object's identity."
            },
            {
                "question_text": "Which built-in function returns a hash value?",
                "options": ["hash()", "id()", "type()", "repr()"],
                "correct_answer": 0,
                "explanation": "hash() returns a hash value for a hashable object."
            },
            {
                "question_text": "Which built-in function returns a string representation suitable for debugging?",
                "options": ["repr()", "str()", "print()", "format()"],
                "correct_answer": 0,
                "explanation": "repr() returns a developer-oriented representation."
            },
            {
                "question_text": "Which built-in function returns a readable string representation?",
                "options": ["str()", "repr()", "type()", "id()"],
                "correct_answer": 0,
                "explanation": "str() returns a human-readable representation."
            },
            {
                "question_text": "Which built-in function checks whether an object can be called?",
                "options": ["callable()", "hasattr()", "isinstance()", "issubclass()"],
                "correct_answer": 0,
                "explanation": "callable() checks whether an object can be called."
            },
            {
                "question_text": "Which built-in function checks whether an object has an attribute?",
                "options": ["hasattr()", "getattr()", "setattr()", "delattr()"],
                "correct_answer": 0,
                "explanation": "hasattr() checks attribute existence."
            },
            {
                "question_text": "Which built-in function retrieves an object's attribute?",
                "options": ["getattr()", "hasattr()", "setattr()", "delattr()"],
                "correct_answer": 0,
                "explanation": "getattr() retrieves a named attribute."
            },
            {
                "question_text": "Which built-in function assigns an object's attribute?",
                "options": ["setattr()", "getattr()", "hasattr()", "delattr()"],
                "correct_answer": 0,
                "explanation": "setattr() assigns a named attribute."
            },
            {
                "question_text": "Which built-in function deletes an object's attribute?",
                "options": ["delattr()", "setattr()", "getattr()", "hasattr()"],
                "correct_answer": 0,
                "explanation": "delattr() deletes a named attribute."
            },
            {
                "question_text": "Which built-in function returns a list of names in an object's scope?",
                "options": ["dir()", "vars()", "locals()", "globals()"],
                "correct_answer": 0,
                "explanation": "dir() returns names associated with an object."
            },
            {
                "question_text": "Which built-in function returns the current global namespace?",
                "options": ["globals()", "locals()", "vars()", "dir()"],
                "correct_answer": 0,
                "explanation": "globals() returns the global namespace dictionary."
            },
            {
                "question_text": "Which built-in function returns the current local namespace?",
                "options": ["locals()", "globals()", "vars()", "dir()"],
                "correct_answer": 0,
                "explanation": "locals() returns the local namespace mapping."
            },
            {
                "question_text": "Which built-in function checks whether a class is a subclass of another class?",
                "options": ["issubclass()", "isinstance()", "type()", "id()"],
                "correct_answer": 0,
                "explanation": "issubclass() checks class inheritance."
            },
            {
                "question_text": "Which built-in function checks whether an object belongs to a class hierarchy?",
                "options": ["isinstance()", "issubclass()", "type()", "id()"],
                "correct_answer": 0,
                "explanation": "isinstance() checks object membership in a class hierarchy."
            },
            {
                "question_text": "Which built-in function creates a complex number?",
                "options": ["complex()", "float()", "int()", "decimal()"],
                "correct_answer": 0,
                "explanation": "complex() creates a complex number."
            },
            {
                "question_text": "What is the output of complex(2, 3)?",
                "options": ["(2+3j)", "(2+3i)", "5", "2.3"],
                "correct_answer": 0,
                "explanation": "complex(2, 3) creates 2 + 3j."
            },
            {
                "question_text": "Which built-in function returns a bytearray?",
                "options": ["bytearray()", "bytes()", "memoryview()", "str()"],
                "correct_answer": 0,
                "explanation": "bytearray() creates a mutable bytes sequence."
            },
            {
                "question_text": "Which built-in function returns an immutable bytes object?",
                "options": ["bytes()", "bytearray()", "memoryview()", "str()"],
                "correct_answer": 0,
                "explanation": "bytes() creates an immutable bytes object."
            },
            {
                "question_text": "Which built-in function creates a memory view?",
                "options": ["memoryview()", "bytes()", "bytearray()", "buffer()"],
                "correct_answer": 0,
                "explanation": "memoryview() creates a view over an object's buffer."
            },
            {
                "question_text": "Which function can convert a binary string to an integer using base 2?",
                "options": ["int('101', 2)", "bin('101')", "hex('101')", "oct('101')"],
                "correct_answer": 0,
                "explanation": "int() accepts a base argument and converts the string using that base."
            },
            {
                "question_text": "What is the output of int('101', 2)?",
                "options": ["5", "101", "2", "4"],
                "correct_answer": 0,
                "explanation": "Binary 101 represents decimal 5."
            },
            {
                "question_text": "Which function can convert a hexadecimal string to an integer?",
                "options": ["int('ff', 16)", "hex('ff')", "bin('ff')", "oct('ff')"],
                "correct_answer": 0,
                "explanation": "int() with base 16 converts a hexadecimal string to an integer."
            },
            {
                "question_text": "What is the output of int('10', 8)?",
                "options": ["8", "10", "16", "2"],
                "correct_answer": 0,
                "explanation": "Octal 10 represents decimal 8."
            },
            {
                "question_text": "Which function formats a number using a specified format specifier?",
                "options": ["format()", "repr()", "str()", "print()"],
                "correct_answer": 0,
                "explanation": "format() applies a format specification to a value."
            },
            {
                "question_text": "What is the output of format(12.3456, '.2f')?",
                "options": ["12.35", "12.34", "12.3456", "12.3"],
                "correct_answer": 0,
                "explanation": "The .2f format rounds and displays two decimal places."
            },
            {
                "question_text": "Which module provides tools for decimal arithmetic?",
                "options": ["decimal", "fractions", "math", "statistics"],
                "correct_answer": 0,
                "explanation": "decimal supports decimal arithmetic with controlled precision."
            },
            {
                "question_text": "Which module provides rational number support?",
                "options": ["fractions", "decimal", "math", "numbers"],
                "correct_answer": 0,
                "explanation": "fractions provides the Fraction class."
            },
            {
                "question_text": "Which module provides common statistical calculations?",
                "options": ["statistics", "math", "random", "decimal"],
                "correct_answer": 0,
                "explanation": "statistics provides mean, median, mode and other calculations."
            },
            {
                "question_text": "Which module provides pseudo-random number generation?",
                "options": ["random", "secrets", "math", "statistics"],
                "correct_answer": 0,
                "explanation": "random provides pseudo-random generators."
            },
            {
                "question_text": "Which module provides secure random token generation?",
                "options": ["secrets", "random", "math", "statistics"],
                "correct_answer": 0,
                "explanation": "secrets is designed for secure random values."
            },
            {
                "question_text": "Which module provides hash algorithms such as SHA-256?",
                "options": ["hashlib", "hmac", "random", "ssl"],
                "correct_answer": 0,
                "explanation": "hashlib provides SHA-family and other hash algorithms."
            },
            {
                "question_text": "Which module provides keyed message authentication codes?",
                "options": ["hmac", "hashlib", "secrets", "ssl"],
                "correct_answer": 0,
                "explanation": "hmac provides keyed-hash message authentication."
            },
            {
                "question_text": "Which module provides date and time objects?",
                "options": ["datetime", "time", "calendar", "All of these"],
                "correct_answer": 3,
                "explanation": "datetime, time and calendar all provide date/time-related functionality."
            },
            {
                "question_text": "Which module provides time-related functions such as sleep()?",
                "options": ["time", "datetime", "calendar", "clock"],
                "correct_answer": 0,
                "explanation": "The time module provides sleep() and other time functions."
            },
            {
                "question_text": "Which module provides calendar-related calculations?",
                "options": ["calendar", "datetime", "time", "date"],
                "correct_answer": 0,
                "explanation": "The calendar module provides calendar calculations and formatting."
            },
            {
                "question_text": "Which module provides a counter for counting hashable items?",
                "options": ["collections", "itertools", "functools", "statistics"],
                "correct_answer": 0,
                "explanation": "collections.Counter counts hashable objects."
            },
            {
                "question_text": "Which module provides an ordered double-ended queue?",
                "options": ["collections", "queue", "heapq", "array"],
                "correct_answer": 0,
                "explanation": "collections.deque supports efficient operations at both ends."
            },
            {
                "question_text": "Which module provides a default dictionary?",
                "options": ["collections", "dict", "types", "functools"],
                "correct_answer": 0,
                "explanation": "collections.defaultdict supplies a default factory for missing keys."
            },
            {
                "question_text": "Which module provides tools for creating iterators?",
                "options": ["itertools", "functools", "collections", "operator"],
                "correct_answer": 0,
                "explanation": "itertools provides efficient iterator-building functions."
            },
            {
                "question_text": "Which module provides function tools such as partial application and caching?",
                "options": ["functools", "itertools", "collections", "operator"],
                "correct_answer": 0,
                "explanation": "functools provides partial(), caching decorators and other tools."
            },
            {
                "question_text": "Which module provides operators as functions?",
                "options": ["operator", "functools", "itertools", "types"],
                "correct_answer": 0,
                "explanation": "operator exposes many Python operators as callable functions."
            },
            {
                "question_text": "Which module provides tools for object inspection?",
                "options": ["inspect", "ast", "types", "sys"],
                "correct_answer": 0,
                "explanation": "inspect supports introspection of live objects."
            },
            {
                "question_text": "Which module provides abstract syntax tree tools?",
                "options": ["ast", "tokenize", "inspect", "compile"],
                "correct_answer": 0,
                "explanation": "ast provides abstract syntax tree operations."
            },
            {
                "question_text": "Which module provides tokenization of Python source code?",
                "options": ["tokenize", "ast", "inspect", "keyword"],
                "correct_answer": 0,
                "explanation": "tokenize generates tokens from Python source."
            },
            {
                "question_text": "Which module provides command-line argument parsing?",
                "options": ["argparse", "sys", "os", "getopt_only"],
                "correct_answer": 0,
                "explanation": "argparse provides a convenient command-line parsing interface."
            },
            {
                "question_text": "Which module provides logging functionality?",
                "options": ["logging", "warnings", "traceback", "inspect"],
                "correct_answer": 0,
                "explanation": "logging records application events."
            },
            {
                "question_text": "Which module provides warning control?",
                "options": ["warnings", "logging", "traceback", "sys"],
                "correct_answer": 0,
                "explanation": "warnings supports warning filters and messages."
            },
            {
                "question_text": "Which module provides unit testing support?",
                "options": ["unittest", "doctest", "timeit", "cProfile"],
                "correct_answer": 0,
                "explanation": "unittest is the standard-library unit testing framework."
            },
            {
                "question_text": "Which module tests examples embedded in docstrings?",
                "options": ["doctest", "unittest", "pydoc", "inspect"],
                "correct_answer": 0,
                "explanation": "doctest runs examples in documentation strings."
            },
            {
                "question_text": "Which module measures the execution time of small code snippets?",
                "options": ["timeit", "datetime", "time", "profile"],
                "correct_answer": 0,
                "explanation": "timeit is designed to time small code snippets."
            },
            {
                "question_text": "Which module provides deterministic profiling?",
                "options": ["cProfile", "timeit", "trace", "pstats"],
                "correct_answer": 0,
                "explanation": "cProfile profiles program execution."
            },
            {
                "question_text": "Which module provides thread-based concurrency?",
                "options": ["threading", "multiprocessing", "asyncio", "queue"],
                "correct_answer": 0,
                "explanation": "threading provides thread-based concurrency."
            },
            {
                "question_text": "Which module provides process-based concurrency?",
                "options": ["multiprocessing", "threading", "asyncio", "queue"],
                "correct_answer": 0,
                "explanation": "multiprocessing provides process-based concurrency."
            },
            {
                "question_text": "Which module provides asynchronous programming support?",
                "options": ["asyncio", "threading", "multiprocessing", "sched"],
                "correct_answer": 0,
                "explanation": "asyncio provides asynchronous event-loop support."
            },
            {
                "question_text": "Which module provides thread-safe queues?",
                "options": ["queue", "heapq", "collections", "array"],
                "correct_answer": 0,
                "explanation": "queue provides synchronized queue classes."
            },
            {
                "question_text": "Which module provides a priority queue based on a heap?",
                "options": ["heapq", "queue", "bisect", "array"],
                "correct_answer": 0,
                "explanation": "heapq implements a heap queue algorithm."
            },
            {
                "question_text": "Which module provides binary search insertion helpers?",
                "options": ["bisect", "heapq", "array", "struct"],
                "correct_answer": 0,
                "explanation": "bisect provides binary search operations on sorted lists."
            },
            {
                "question_text": "Which module provides compact numeric arrays?",
                "options": ["array", "struct", "bytes", "memoryview"],
                "correct_answer": 0,
                "explanation": "array provides compact arrays of basic numeric values."
            },
            {
                "question_text": "Which module packs values into binary data?",
                "options": ["struct", "pickle", "json", "array"],
                "correct_answer": 0,
                "explanation": "struct packs and unpacks binary data."
            },
            {
                "question_text": "Which module reads and writes JSON data?",
                "options": ["json", "csv", "pickle", "configparser"],
                "correct_answer": 0,
                "explanation": "json supports JSON serialization and parsing."
            },
            {
                "question_text": "Which module reads and writes CSV data?",
                "options": ["csv", "json", "pickle", "configparser"],
                "correct_answer": 0,
                "explanation": "csv supports comma-separated data."
            },
            {
                "question_text": "Which module reads and writes INI configuration files?",
                "options": ["configparser", "json", "csv", "tomllib"],
                "correct_answer": 0,
                "explanation": "configparser handles INI-style configuration."
            },
            {
                "question_text": "Which module parses TOML data?",
                "options": ["tomllib", "configparser", "json", "csv"],
                "correct_answer": 0,
                "explanation": "tomllib parses TOML documents in modern Python."
            },
            {
                "question_text": "Which module provides ZIP archive support?",
                "options": ["zipfile", "tarfile", "shutil", "gzip"],
                "correct_answer": 0,
                "explanation": "zipfile reads and writes ZIP archives."
            },
            {
                "question_text": "Which module provides TAR archive support?",
                "options": ["tarfile", "zipfile", "gzip", "shutil"],
                "correct_answer": 0,
                "explanation": "tarfile reads and writes TAR archives."
            },
            {
                "question_text": "Which module provides gzip compression support?",
                "options": ["gzip", "zipfile", "tarfile", "zlib"],
                "correct_answer": 0,
                "explanation": "gzip reads and writes gzip-compressed files."
            },
            {
                "question_text": "Which module provides low-level compression and decompression?",
                "options": ["zlib", "gzip", "zipfile", "tarfile"],
                "correct_answer": 0,
                "explanation": "zlib provides compression and decompression functions."
            },
            {
                "question_text": "Which module provides temporary files and directories?",
                "options": ["tempfile", "shutil", "os", "pathlib"],
                "correct_answer": 0,
                "explanation": "tempfile provides temporary file and directory creation."
            },
            {
                "question_text": "Which module provides high-level file operations?",
                "options": ["shutil", "os.path", "sys", "tempfile"],
                "correct_answer": 0,
                "explanation": "shutil provides high-level file and directory operations."
            },
            {
                "question_text": "Which module provides object-oriented paths?",
                "options": ["pathlib", "os.path", "sys", "file"],
                "correct_answer": 0,
                "explanation": "pathlib provides the Path class and related path operations."
            },
            {
                "question_text": "Which module provides URL parsing?",
                "options": ["urllib.parse", "http.client", "socket", "ssl"],
                "correct_answer": 0,
                "explanation": "urllib.parse provides URL parsing and query-string tools."
            },
            {
                "question_text": "Which module provides a basic HTTP server?",
                "options": ["http.server", "http.client", "socket", "urllib"],
                "correct_answer": 0,
                "explanation": "http.server provides basic HTTP server classes."
            },
            {
                "question_text": "Which module provides a basic HTTP client?",
                "options": ["http.client", "http.server", "socketserver", "ssl"],
                "correct_answer": 0,
                "explanation": "http.client provides HTTP client functionality."
            },
            {
                "question_text": "Which module provides SMTP email sending?",
                "options": ["smtplib", "imaplib", "poplib", "email"],
                "correct_answer": 0,
                "explanation": "smtplib provides SMTP client functionality."
            },
            {
                "question_text": "Which module provides POP3 email access?",
                "options": ["poplib", "imaplib", "smtplib", "email"],
                "correct_answer": 0,
                "explanation": "poplib provides a POP3 client."
            },
            {
                "question_text": "Which module provides IMAP email access?",
                "options": ["imaplib", "poplib", "smtplib", "email"],
                "correct_answer": 0,
                "explanation": "imaplib provides an IMAP client."
            },
            {
                "question_text": "Which module provides email message parsing and creation?",
                "options": ["email", "smtplib", "imaplib", "poplib"],
                "correct_answer": 0,
                "explanation": "email provides classes and utilities for email messages."
            },
            {
                "question_text": "Which module provides HTML escaping and unescaping?",
                "options": ["html", "xml", "re", "json"],
                "correct_answer": 0,
                "explanation": "html provides HTML entity escaping and unescaping utilities."
            },
            {
                "question_text": "Which module provides XML parsing tools?",
                "options": ["xml.etree.ElementTree", "json", "html", "csv"],
                "correct_answer": 0,
                "explanation": "ElementTree supports XML parsing and construction."
            },
            {
                "question_text": "Which module provides operating-system interfaces?",
                "options": ["os", "sys", "platform", "pathlib"],
                "correct_answer": 0,
                "explanation": "os provides operating-system dependent functionality."
            },
            {
                "question_text": "Which module provides interpreter-specific functionality?",
                "options": ["sys", "os", "platform", "inspect"],
                "correct_answer": 0,
                "explanation": "sys provides interpreter-specific variables and functions."
            },
            {
                "question_text": "Which module provides platform identification?",
                "options": ["platform", "os", "sys", "inspect"],
                "correct_answer": 0,
                "explanation": "platform reports details about the underlying platform."
            },
            {
                "question_text": "Which module provides garbage collection controls?",
                "options": ["gc", "sys", "resource", "memory"],
                "correct_answer": 0,
                "explanation": "gc exposes the cyclic garbage collector interface."
            },
            {
                "question_text": "Which module provides traceback utilities?",
                "options": ["traceback", "logging", "warnings", "inspect"],
                "correct_answer": 0,
                "explanation": "traceback formats and prints stack traces."
            },
            {
                "question_text": "Which module provides warning filters?",
                "options": ["warnings", "logging", "traceback", "sys"],
                "correct_answer": 0,
                "explanation": "warnings supports warning filters and message control."
            },
            {
                "question_text": "Which module provides a command-line parser?",
                "options": ["argparse", "sys", "os", "getopt"],
                "correct_answer": 0,
                "explanation": "argparse parses command-line options and arguments."
            },
            {
                "question_text": "Which module provides a shell-like pattern matching facility?",
                "options": ["fnmatch", "re", "glob", "pathlib"],
                "correct_answer": 0,
                "explanation": "fnmatch matches filenames using shell-style wildcard patterns."
            },
            {
                "question_text": "Which module finds pathnames matching a pattern?",
                "options": ["glob", "fnmatch", "re", "os.path"],
                "correct_answer": 0,
                "explanation": "glob finds pathnames matching shell-style patterns."
            },
            {
                "question_text": "Which module provides tools for manipulating file permissions and paths?",
                "options": ["os", "sys", "math", "random"],
                "correct_answer": 0,
                "explanation": "os exposes filesystem and operating-system operations."
            },
            {
                "question_text": "Which module provides a portable way to work with filesystem paths?",
                "options": ["pathlib", "sys", "inspect", "types"],
                "correct_answer": 0,
                "explanation": "pathlib provides object-oriented filesystem paths."
            },
            {
                "question_text": "Which module provides a class for representing a path?",
                "options": ["pathlib.Path", "os.Path", "sys.Path", "file.Path"],
                "correct_answer": 0,
                "explanation": "pathlib.Path represents filesystem paths."
            },
            {
                "question_text": "Which method checks whether a Path points to a regular file?",
                "options": ["is_file()", "is_dir()", "exists()", "is_path()"],
                "correct_answer": 0,
                "explanation": "Path.is_file() checks whether the path is a file."
            },
            {
                "question_text": "Which method checks whether a Path exists?",
                "options": ["exists()", "is_file()", "is_dir()", "is_valid()"],
                "correct_answer": 0,
                "explanation": "Path.exists() checks path existence."
            },
            {
                "question_text": "Which method creates a directory using pathlib?",
                "options": ["mkdir()", "makedir()", "create()", "newdir()"],
                "correct_answer": 0,
                "explanation": "Path.mkdir() creates a directory."
            },
            {
                "question_text": "Which method deletes a file using pathlib?",
                "options": ["unlink()", "rmdir()", "remove()", "delete()"],
                "correct_answer": 0,
                "explanation": "Path.unlink() removes a file or symbolic link."
            },
            {
                "question_text": "Which method removes an empty directory using pathlib?",
                "options": ["rmdir()", "unlink()", "remove()", "delete()"],
                "correct_answer": 0,
                "explanation": "Path.rmdir() removes an empty directory."
            },
            {
                "question_text": "Which method returns the file name including its suffix?",
                "options": ["name", "stem", "suffix", "parent"],
                "correct_answer": 0,
                "explanation": "Path.name returns the final component including its suffix."
            },
            {
                "question_text": "Which Path attribute returns the file name without its suffix?",
                "options": ["stem", "name", "suffix", "parent"],
                "correct_answer": 0,
                "explanation": "Path.stem returns the final path component without its suffix."
            },
            {
                "question_text": "Which Path attribute returns the file extension including the dot?",
                "options": ["suffix", "stem", "name", "parent"],
                "correct_answer": 0,
                "explanation": "Path.suffix returns the final extension including the dot."
            },
            {
                "question_text": "Which Path attribute returns the parent directory?",
                "options": ["parent", "name", "stem", "suffix"],
                "correct_answer": 0,
                "explanation": "Path.parent returns the logical parent path."
            },
            {
                "question_text": "Which method reads a file as bytes using pathlib?",
                "options": ["read_bytes()", "read_text()", "write_bytes()", "open()"],
                "correct_answer": 0,
                "explanation": "Path.read_bytes() reads file content as bytes."
            },
            {
                "question_text": "Which method writes text to a file using pathlib?",
                "options": ["write_text()", "read_text()", "write_bytes()", "save_text()"],
                "correct_answer": 0,
                "explanation": "Path.write_text() writes a string to a file."
            },
            {
                "question_text": "Which method writes bytes to a file using pathlib?",
                "options": ["write_bytes()", "write_text()", "read_bytes()", "save_bytes()"],
                "correct_answer": 0,
                "explanation": "Path.write_bytes() writes bytes to a file."
            },
            {
                "question_text": "Which method can rename a path using pathlib?",
                "options": ["rename()", "replace()", "move()", "change()"],
                "correct_answer": 0,
                "explanation": "Path.rename() renames a file or directory."
            },
            {
                "question_text": "Which method can replace an existing path using pathlib?",
                "options": ["replace()", "rename()", "move()", "swap()"],
                "correct_answer": 0,
                "explanation": "Path.replace() replaces the destination path."
            },
            {
                "question_text": "Which method can resolve a path to an absolute path?",
                "options": ["resolve()", "absolute()", "expand()", "normalize()"],
                "correct_answer": 0,
                "explanation": "Path.resolve() resolves a path to an absolute path."
            },
            {
                "question_text": "Which method can expand a user home directory marker in a path?",
                "options": ["expanduser()", "resolve()", "absolute()", "normalize()"],
                "correct_answer": 0,
                "explanation": "Path.expanduser() expands a tilde to the user's home directory."
            },
            {
                "question_text": "Which method returns the relative path from one path to another?",
                "options": ["relative_to()", "resolve()", "joinpath()", "with_name()"],
                "correct_answer": 0,
                "explanation": "relative_to() computes a path relative to another path when possible."
            },
            {
                "question_text": "Which method joins a path with another path component?",
                "options": ["joinpath()", "relative_to()", "resolve()", "with_suffix()"],
                "correct_answer": 0,
                "explanation": "joinpath() combines path components."
            },
            {
                "question_text": "Which method returns a path with a new suffix?",
                "options": ["with_suffix()", "with_name()", "with_stem()", "replace()"],
                "correct_answer": 0,
                "explanation": "with_suffix() returns a path with a changed suffix."
            },
            {
                "question_text": "Which method returns a path with a new final name?",
                "options": ["with_name()", "with_suffix()", "with_stem()", "rename()"],
                "correct_answer": 0,
                "explanation": "with_name() returns a path with a new final component."
            },
            {
                "question_text": "Which method returns a path with a changed stem?",
                "options": ["with_stem()", "with_name()", "with_suffix()", "rename()"],
                "correct_answer": 0,
                "explanation": "with_stem() returns a path with a new stem."
            },
            {
                "question_text": "Which method returns matching paths for a glob pattern?",
                "options": ["glob()", "rglob()", "match()", "search()"],
                "correct_answer": 0,
                "explanation": "Path.glob() yields matching paths in a directory."
            },
            {
                "question_text": "Which method searches recursively for matching paths?",
                "options": ["rglob()", "glob()", "match()", "search()"],
                "correct_answer": 0,
                "explanation": "Path.rglob() searches recursively."
            },
            {
                "question_text": "Which method checks whether a path matches a glob pattern?",
                "options": ["match()", "glob()", "rglob()", "search()"],
                "correct_answer": 0,
                "explanation": "Path.match() checks a path against a glob-style pattern."
            },
            {
                "question_text": "Which method returns the first matching path from a glob iterator?",
                "options": ["next()", "first()", "find()", "match()"],
                "correct_answer": 0,
                "explanation": "The iterator can be passed to next() to retrieve its first result."
            },
            {
                "question_text": "Which method can return a file's last modification time?",
                "options": ["stat()", "resolve()", "exists()", "is_file()"],
                "correct_answer": 0,
                "explanation": "Path.stat() returns file status information including modification time."
            },
            {
                "question_text": "Which property of stat results stores the file size in bytes?",
                "options": ["st_size", "st_mode", "st_mtime", "st_uid"],
                "correct_answer": 0,
                "explanation": "st_size stores the file size in bytes."
            },
            {
                "question_text": "Which property of stat results stores the last modification time?",
                "options": ["st_mtime", "st_size", "st_mode", "st_uid"],
                "correct_answer": 0,
                "explanation": "st_mtime stores the last modification time as a timestamp."
            },
            {
                "question_text": "Which function can return a file's absolute path?",
                "options": ["os.path.abspath()", "os.path.basename()", "os.path.dirname()", "os.path.splitext()"],
                "correct_answer": 0,
                "explanation": "os.path.abspath() returns an absolute normalized path."
            },
            {
                "question_text": "Which function returns the final component of a path?",
                "options": ["os.path.basename()", "os.path.dirname()", "os.path.abspath()", "os.path.splitext()"],
                "correct_answer": 0,
                "explanation": "os.path.basename() returns the final path component."
            },
            {
                "question_text": "Which function returns the directory portion of a path?",
                "options": ["os.path.dirname()", "os.path.basename()", "os.path.abspath()", "os.path.splitext()"],
                "correct_answer": 0,
                "explanation": "os.path.dirname() returns the directory component."
            },
            {
                "question_text": "Which function splits a path into its root and extension?",
                "options": ["os.path.splitext()", "os.path.basename()", "os.path.dirname()", "os.path.join()"],
                "correct_answer": 0,
                "explanation": "os.path.splitext() separates the final extension."
            },
            {
                "question_text": "Which function joins path components using the platform's path separator?",
                "options": ["os.path.join()", "os.path.split()", "os.path.basename()", "os.path.dirname()"],
                "correct_answer": 0,
                "explanation": "os.path.join() combines path components."
            },
            {
                "question_text": "Which function checks whether a path points to a directory?",
                "options": ["os.path.isdir()", "os.path.isfile()", "os.path.exists()", "os.path.islink()"],
                "correct_answer": 0,
                "explanation": "os.path.isdir() checks for a directory."
            },
            {
                "question_text": "Which function checks whether a path points to a regular file?",
                "options": ["os.path.isfile()", "os.path.isdir()", "os.path.exists()", "os.path.islink()"],
                "correct_answer": 0,
                "explanation": "os.path.isfile() checks for a regular file."
            },
            {
                "question_text": "Which function checks whether a path is a symbolic link?",
                "options": ["os.path.islink()", "os.path.isfile()", "os.path.isdir()", "os.path.exists()"],
                "correct_answer": 0,
                "explanation": "os.path.islink() checks whether a path is a symbolic link."
            },
            {
                "question_text": "Which function checks whether two paths refer to the same file?",
                "options": ["os.path.samefile()", "os.path.samepath()", "os.path.identical()", "os.path.compare()"],
                "correct_answer": 0,
                "explanation": "os.path.samefile() checks whether paths identify the same file."
            },
            {
                "question_text": "Which function returns the size of a file in bytes?",
                "options": ["os.path.getsize()", "os.path.isdir()", "os.path.basename()", "os.path.abspath()"],
                "correct_answer": 0,
                "explanation": "os.path.getsize() returns the file size in bytes."
            },
            {
                "question_text": "Which function returns the modification time of a path?",
                "options": ["os.path.getmtime()", "os.path.getsize()", "os.path.getatime()", "os.path.getctime()"],
                "correct_answer": 0,
                "explanation": "os.path.getmtime() returns the last modification timestamp."
            },
            {
                "question_text": "Which function returns the access time of a path?",
                "options": ["os.path.getatime()", "os.path.getmtime()", "os.path.getctime()", "os.path.getsize()"],
                "correct_answer": 0,
                "explanation": "os.path.getatime() returns the last access timestamp."
            },
            {
                "question_text": "Which function returns the creation or metadata-change time depending on the platform?",
                "options": ["os.path.getctime()", "os.path.getmtime()", "os.path.getatime()", "os.path.getsize()"],
                "correct_answer": 0,
                "explanation": "getctime() returns creation time on Windows and metadata-change time on many Unix systems."
            },
            {
                "question_text": "Which module provides a way to create and manage subprocesses?",
                "options": ["subprocess", "os", "sys", "threading"],
                "correct_answer": 0,
                "explanation": "subprocess allows Python to spawn and manage external processes."
            },
            {
                "question_text": "Which subprocess function runs a command and waits for it to complete?",
                "options": ["subprocess.run()", "subprocess.Popen()", "subprocess.callonly()", "subprocess.start()"],
                "correct_answer": 0,
                "explanation": "subprocess.run() executes a command and waits for completion."
            },
            {
                "question_text": "Which subprocess class provides more advanced process control?",
                "options": ["Popen", "Run", "Process", "Command"],
                "correct_answer": 0,
                "explanation": "Popen provides advanced control over spawned processes."
            },
            {
                "question_text": "Which subprocess option captures standard output?",
                "options": ["capture_output=True", "stdout=False", "output=True", "capture=True"],
                "correct_answer": 0,
                "explanation": "capture_output=True captures stdout and stderr."
            },
            {
                "question_text": "Which subprocess option raises CalledProcessError when a command exits with a non-zero status?",
                "options": ["check=True", "raise=True", "error=True", "strict=True"],
                "correct_answer": 0,
                "explanation": "check=True raises CalledProcessError for a non-zero return code."
            },
            {
                "question_text": "Which exception is raised by subprocess.run(check=True) for a non-zero return code?",
                "options": ["CalledProcessError", "FileNotFoundError", "ValueError", "TimeoutError"],
                "correct_answer": 0,
                "explanation": "CalledProcessError represents a process that returned a non-zero exit status."
            },
            {
                "question_text": "Which subprocess option sets a maximum time for a command to complete?",
                "options": ["timeout", "max_time", "limit", "duration"],
                "correct_answer": 0,
                "explanation": "The timeout argument limits how long the process can run."
            },
            {
                "question_text": "Which exception can be raised when a subprocess exceeds its timeout?",
                "options": ["TimeoutExpired", "CalledProcessError", "RuntimeError", "ProcessError"],
                "correct_answer": 0,
                "explanation": "subprocess.TimeoutExpired indicates the process exceeded its timeout."
            },
            {
                "question_text": "Which module provides a way to create and manage environment variables?",
                "options": ["os", "sys", "platform", "subprocess"],
                "correct_answer": 0,
                "explanation": "os.environ exposes the process environment variables."
            },
            {
                "question_text": "Which object provides access to environment variables?",
                "options": ["os.environ", "sys.environ", "os.env", "environment.variables"],
                "correct_answer": 0,
                "explanation": "os.environ is a mapping of environment variables."
            },
            {
                "question_text": "Which function can retrieve an environment variable with a default?",
                "options": ["os.getenv()", "os.setenv()", "sys.getenv()", "os.get()"],
                "correct_answer": 0,
                "explanation": "os.getenv() returns the value or a supplied default."
            },
            {
                "question_text": "Which function changes the current working directory?",
                "options": ["os.chdir()", "os.getcwd()", "os.listdir()", "os.mkdir()"],
                "correct_answer": 0,
                "explanation": "os.chdir() changes the current working directory."
            },
            {
                "question_text": "Which function returns the current working directory?",
                "options": ["os.getcwd()", "os.chdir()", "os.listdir()", "os.mkdir()"],
                "correct_answer": 0,
                "explanation": "os.getcwd() returns the current working directory."
            }
        ]
    },

    {
        "skill": "Data Structures",
        "difficulty": "beginner",
        "questions": [
            {
                "question_text": "Which data structure follows the Last In, First Out (LIFO) principle?",
                "options": ["Queue", "Stack", "Array", "Linked List"],
                "correct_answer": 1,
                "explanation": "A stack follows LIFO, meaning the last inserted element is removed first."
            },
            {
                "question_text": "Which data structure follows the First In, First Out (FIFO) principle?",
                "options": ["Stack", "Tree", "Queue", "Graph"],
                "correct_answer": 2,
                "explanation": "A queue follows FIFO, meaning the first inserted element is removed first."
            },
            {
                "question_text": "Which data structure stores elements in contiguous memory locations?",
                "options": ["Linked List", "Array", "Tree", "Graph"],
                "correct_answer": 1,
                "explanation": "An array stores its elements in contiguous memory locations."
            },
            {
                "question_text": "What is the index of the first element in a typical zero-indexed array?",
                "options": ["1", "-1", "0", "2"],
                "correct_answer": 2,
                "explanation": "Zero-indexed arrays begin at index 0."
            },
            {
                "question_text": "Which operation adds an element to the top of a stack?",
                "options": ["Pop", "Push", "Dequeue", "Search"],
                "correct_answer": 1,
                "explanation": "Push inserts an element at the top of a stack."
            },
            {
                "question_text": "Which operation removes the top element from a stack?",
                "options": ["Push", "Insert", "Pop", "Enqueue"],
                "correct_answer": 2,
                "explanation": "Pop removes the top element from a stack."
            },
            {
                "question_text": "Which operation inserts an element into a queue?",
                "options": ["Push", "Pop", "Enqueue", "Dequeue"],
                "correct_answer": 2,
                "explanation": "Enqueue adds an element to the rear of a queue."
            },
            {
                "question_text": "Which operation removes an element from the front of a queue?",
                "options": ["Enqueue", "Dequeue", "Push", "Peek"],
                "correct_answer": 1,
                "explanation": "Dequeue removes an element from the front of a queue."
            },
            {
                "question_text": "Which data structure consists of nodes connected using links?",
                "options": ["Array", "Linked List", "Stack", "Matrix"],
                "correct_answer": 1,
                "explanation": "A linked list consists of nodes connected through references or links."
            },
            {
                "question_text": "What does a node in a singly linked list typically contain?",
                "options": ["Only an index", "Data and a next pointer", "Only a previous pointer", "Two arrays"],
                "correct_answer": 1,
                "explanation": "A singly linked list node stores data and a reference to the next node."
            },
            {
                "question_text": "Which data structure represents hierarchical relationships?",
                "options": ["Queue", "Stack", "Tree", "Array"],
                "correct_answer": 2,
                "explanation": "A tree represents hierarchical relationships using parent and child nodes."
            },
            {
                "question_text": "What is the topmost node of a tree called?",
                "options": ["Leaf", "Root", "Edge", "Sibling"],
                "correct_answer": 1,
                "explanation": "The root is the topmost node of a tree."
            },
            {
                "question_text": "What is a node with no children in a tree called?",
                "options": ["Root", "Parent", "Leaf", "Edge"],
                "correct_answer": 2,
                "explanation": "A leaf node has no child nodes."
            },
            {
                "question_text": "Which data structure is commonly used to implement recursion?",
                "options": ["Queue", "Stack", "Graph", "Hash Table"],
                "correct_answer": 1,
                "explanation": "Function calls are managed using the call stack."
            },
            {
                "question_text": "Which data structure stores data as key-value pairs?",
                "options": ["Stack", "Queue", "Hash Table", "Linked List"],
                "correct_answer": 2,
                "explanation": "A hash table stores values associated with keys."
            },
            {
                "question_text": "Which data structure is commonly used to represent a network of connected locations?",
                "options": ["Stack", "Graph", "Array", "Queue"],
                "correct_answer": 1,
                "explanation": "A graph represents entities as vertices and their connections as edges."
            },
            {
                "question_text": "What is the time complexity of accessing an array element by index?",
                "options": ["O(n)", "O(log n)", "O(1)", "O(n²)"],
                "correct_answer": 2,
                "explanation": "Array indexing provides constant-time access."
            },
            {
                "question_text": "Which data structure is best suited for processing items in arrival order?",
                "options": ["Stack", "Queue", "Tree", "Hash Table"],
                "correct_answer": 1,
                "explanation": "A queue processes elements in FIFO order."
            },
            {
                "question_text": "What is the maximum number of children a binary tree node can have?",
                "options": ["One", "Two", "Three", "Unlimited"],
                "correct_answer": 1,
                "explanation": "A binary tree node can have at most two children."
            },
            {
                "question_text": "Which traversal visits the left subtree, root, and then right subtree?",
                "options": ["Preorder", "Postorder", "Inorder", "Level order"],
                "correct_answer": 2,
                "explanation": "Inorder traversal follows Left, Root, Right."
            }
                      

        ]
    }
]
        
    


