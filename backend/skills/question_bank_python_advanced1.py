
def _q(question_text, options, correct_answer, explanation):
    return {
        "skill": "Python",
        "difficulty": "advanced",
        "question_text": question_text,
        "options": options,
        "correct_answer": correct_answer,
        "explanation": explanation,
    }


QUESTION_BANK_PYTHON_ADVANCED1 = [

    # 1–10: Advanced Python Internals

    _q("What is the Global Interpreter Lock (GIL) in CPython?",
       ["A lock that prevents all file operations", "A mechanism that allows only one thread to execute Python bytecode at a time in standard GIL-enabled CPython", "A database locking mechanism", "A memory allocation algorithm"],
       1, "The GIL protects interpreter state and limits simultaneous Python bytecode execution by threads in standard GIL-enabled CPython."),

    _q("What does the id() function return?",
       ["The object's memory size", "The object's identity as an integer", "The object's class name", "The object's hash only"],
       1, "id() returns an integer representing an object's identity during its lifetime."),

    _q("What is the difference between is and ==?",
       ["Both always compare values", "is compares identity, while == compares equality", "is compares types only", "== compares memory addresses"],
       1, "is checks whether two references point to the same object; == checks equality."),

    _q("What is interning in Python?",
       ["Automatically converting all objects into strings", "Reusing certain immutable objects to reduce memory usage", "Deleting unused variables", "Converting lists into tuples"],
       1, "Python may reuse certain immutable objects, such as some strings and small integers."),

    _q("What does sys.getsizeof() measure?",
       ["Total memory used by all referenced objects", "Shallow size of an object in bytes", "CPU execution time", "Number of references to an object"],
       1, "getsizeof() reports an object's shallow memory size, not the complete size of referenced objects."),

    _q("What is reference counting used for in CPython?",
       ["Tracking how many references point to an object", "Counting function arguments", "Tracking loop iterations", "Measuring CPU usage"],
       0, "CPython uses reference counting as a primary mechanism for reclaiming objects."),

    _q("Which module provides tools for tracking memory allocations in Python?",
       ["threading", "tracemalloc", "itertools", "inspect"],
       1, "tracemalloc tracks memory allocations made by Python."),

    _q("What is the purpose of the __slots__ attribute?",
       ["To create asynchronous functions", "To restrict instance attributes and potentially reduce memory usage", "To override every inherited method", "To enable multiple inheritance"],
       1, "__slots__ declares allowed instance attributes and can avoid a per-instance __dict__."),

    _q("What does the descriptor protocol primarily define?",
       ["How objects are serialized", "Attribute access behavior through __get__, __set__ and __delete__", "How loops are executed", "How modules are imported"],
       1, "Descriptors customize attribute access and are used by properties, methods and other Python features."),

    _q("What is the purpose of the __new__() method?",
       ["Initialize an already-created instance", "Create and return a new instance", "Delete an instance", "Convert an object to a string"],
       1, "__new__() creates an instance before __init__() initializes it."),

    # 11–20: Decorators and Closures

    _q("What is a decorator in Python?",
       ["A special type of loop", "A callable that modifies or extends another callable or class", "A database object", "A built-in exception"],
       1, "Decorators wrap or modify functions and classes without changing their original source definition."),

    _q("Which decorator preserves the wrapped function's metadata?",
       ["@property", "@staticmethod", "@functools.wraps", "@classmethod"],
       2, "functools.wraps preserves metadata such as the original function's name and documentation."),

    _q("What is a closure?",
       ["A function that remembers variables from its enclosing scope", "A function without arguments", "A class without methods", "A loop that never terminates"],
       0, "A closure retains access to variables from an enclosing lexical scope."),

    _q("Which keyword allows reassignment of a variable in an enclosing function scope?",
       ["global", "nonlocal", "static", "outer"],
       1, "nonlocal allows a nested function to rebind a variable in an enclosing function scope."),

    _q("What is the output of a function decorated with @property when accessed through an instance?",
       ["A function object", "The property's computed value", "A class object", "Always None"],
       1, "Accessing a property invokes its getter and returns the computed value."),

    _q("Which decorator defines a method that receives the class as its first argument?",
       ["@staticmethod", "@classmethod", "@property", "@abstractmethod"],
       1, "@classmethod passes the class as the first argument, conventionally named cls."),

    _q("What is the main difference between a class method and a static method?",
       ["A static method receives self automatically", "A class method receives cls automatically; a static method receives neither automatically", "A static method cannot be called on a class", "There is no difference"],
       1, "Class methods receive the class; static methods behave like regular functions placed in a class namespace."),

    _q("What does functools.lru_cache provide?",
       ["Automatic database backup", "Memoization of function results", "Thread creation", "Automatic type conversion"],
       1, "lru_cache stores results of previous calls and reuses them for matching arguments."),

    _q("What does a generator-based decorator need to preserve when wrapping a function?",
       ["Only the function's return type", "The wrapped function's call behavior and metadata where appropriate", "The operating system process ID", "The function's source file permissions"],
       1, "A well-designed decorator preserves the wrapped callable's behavior and commonly its metadata."),

    _q("What is the purpose of functools.partial()?",
       ["Create a generator", "Fix some arguments of a callable to create a new callable", "Delete function arguments", "Convert a function into a class"],
       1, "partial() creates a new callable with some arguments already supplied."),

    # 21–30: Iterators and Generators

    _q("Which method makes an object an iterator?",
       ["__call__()", "__iter__() and __next__()", "__getitem__() only", "__str__()"],
       1, "An iterator implements __iter__() and __next__()."),

    _q("What exception signals that an iterator has no more items?",
       ["IndexError", "StopIteration", "GeneratorExit", "EOFError"],
       1, "StopIteration signals the end of an iteration."),

    _q("What does yield do inside a function?",
       ["Terminates the Python interpreter", "Turns the function into a generator that can suspend and resume", "Creates a new operating system process", "Always returns a list"],
       1, "yield produces a value and suspends the generator's execution state."),

    _q("What is the purpose of yield from?",
       ["Import a module", "Delegate yielding to another iterable or generator", "Create a class", "Catch all exceptions"],
       1, "yield from delegates iteration to a sub-iterator."),

    _q("Which method sends a value into a suspended generator?",
       ["append()", "send()", "push()", "write()"],
       1, "send() resumes a generator and makes the supplied value the result of its suspended yield expression."),

    _q("What does generator.close() do?",
       ["Deletes the generator's source file", "Raises GeneratorExit inside the suspended generator", "Restarts the generator", "Converts it into a list"],
       1, "close() requests generator termination by raising GeneratorExit at its suspension point."),

    _q("Why are generators useful for large datasets?",
       ["They always run in parallel", "They produce values lazily without storing the entire result in memory", "They automatically use a database", "They eliminate all exceptions"],
       1, "Generators produce values on demand, often reducing memory usage."),

    _q("What does iter(callable, sentinel) do?",
       ["Calls a function once", "Creates an iterator that calls the callable until its result equals the sentinel", "Creates an infinite list", "Converts a callable into a class"],
       1, "The two-argument form of iter() repeatedly calls a callable until it returns the sentinel."),

    _q("What is a generator expression?",
       ["A list comprehension with square brackets", "A lazy expression that produces a generator", "A function declaration", "A dictionary declaration"],
       1, "Generator expressions use parentheses and produce values lazily."),

    _q("Can a generator be restarted after it is exhausted?",
       ["Yes, using next()", "No, a new generator must be created", "Yes, using close()", "Only when it has no arguments"],
       1, "An exhausted generator cannot produce values again."),

    # 31–40: Concurrency and Asynchronous Programming

    _q("Which Python module provides thread-based concurrency primitives?",
       ["multiprocessing", "threading", "subprocess", "socketserver"],
       1, "The threading module provides thread objects, locks and other synchronization tools."),

    _q("Which module is commonly used for process-based parallelism?",
       ["threading", "multiprocessing", "contextlib", "functools"],
       1, "multiprocessing provides separate processes that can execute Python code concurrently."),

    _q("What is the primary purpose of asyncio?",
       ["Manage asynchronous I/O using an event loop", "Compile Python into machine code", "Create database schemas", "Replace object-oriented programming"],
       0, "asyncio supports concurrent asynchronous programming, especially for I/O-bound workloads."),

    _q("Which keyword declares a coroutine function?",
       ["yield", "async def", "await def", "coroutine"],
       1, "A function declared with async def is a coroutine function."),

    _q("What does await do?",
       ["Starts a new operating system process", "Suspends a coroutine until an awaitable completes", "Terminates the event loop", "Converts a coroutine into a thread"],
       1, "await suspends the current coroutine while the awaited operation makes progress."),

    _q("Which function runs the top-level entry point of an asyncio program?",
       ["asyncio.start()", "asyncio.run()", "asyncio.execute()", "asyncio.main()"],
       1, "asyncio.run() creates and manages an event loop for the supplied coroutine."),

    _q("What is an asyncio.Task?",
       ["A database record", "A scheduled coroutine that runs on the event loop", "A separate operating system process", "A Python class decorator"],
       1, "A Task wraps a coroutine and schedules its execution on an event loop."),

    _q("Which synchronization primitive provides mutual exclusion between threads?",
       ["threading.Lock", "threading.Event", "threading.Timer", "threading.local"],
       0, "threading.Lock provides a basic mutual-exclusion lock."),

    _q("What is a race condition?",
       ["A syntax error in a loop", "A result that depends on the unpredictable timing of concurrent operations", "A memory allocation failure", "A failed import"],
       1, "Race conditions occur when concurrent operations access shared state without adequate coordination."),

    _q("Which approach is generally appropriate for CPU-bound parallel work in standard GIL-enabled CPython?",
       ["Using only one asyncio coroutine", "Using multiprocessing", "Using time.sleep()", "Using a single threading.Lock"],
       1, "Separate processes can execute CPU-bound Python code in parallel without sharing one interpreter GIL."),

    # 41–50: Object-Oriented Programming and Metaclasses

    _q("What is a metaclass?",
       ["A class whose instances are classes", "A class that cannot be inherited", "A function that creates lists", "A special exception"],
       0, "Metaclasses control class creation; type is the default metaclass."),

    _q("Which built-in object is the default metaclass in Python?",
       ["object", "type", "super", "classmethod"],
       1, "type is the default metaclass for most Python classes."),

    _q("What does super() commonly provide?",
       ["Direct access to private memory", "A proxy for calling methods in the method resolution order", "Automatic database connections", "A new interpreter"],
       1, "super() supports cooperative method calls following the class's method resolution order."),

    _q("What is the Method Resolution Order (MRO)?",
       ["The order in which modules are imported", "The order in which base classes are searched for an attribute or method", "The order in which variables are deleted", "The order of function arguments"],
       1, "MRO determines the lookup order for attributes and methods in inheritance hierarchies."),

    _q("Which method can customize attribute lookup when normal lookup fails?",
       ["__getattr__()", "__init__()", "__repr__()", "__del__()"],
       0, "__getattr__() is called when normal attribute lookup does not find the requested attribute."),

    _q("What is the difference between __getattribute__() and __getattr__()?",
       ["They are identical", "__getattribute__() handles every attribute lookup; __getattr__() handles missing attributes", "__getattr__() handles every lookup", "__getattribute__() is used only during deletion"],
       1, "__getattribute__() intercepts all attribute accesses, while __getattr__() is a fallback."),

    _q("Which special method controls the string representation intended for developers?",
       ["__str__()", "__repr__()", "__len__()", "__format__()"],
       1, "__repr__() provides an official or developer-oriented representation of an object."),

    _q("What is an abstract base class commonly used for?",
       ["Preventing all inheritance", "Defining interfaces and shared behavior for subclasses", "Creating global variables", "Replacing modules"],
       1, "Abstract base classes define required methods and common behavior for subclasses."),

    _q("Which module provides abstract base class support?",
       ["abc", "inspect", "types", "collections"],
       0, "The abc module provides ABC and abstractmethod."),

    _q("What does @abstractmethod indicate?",
       ["A method that must be implemented by a concrete subclass", "A method that runs only once", "A method that cannot be called", "A method that is automatically asynchronous"],
       0, "@abstractmethod marks methods that concrete subclasses are expected to implement."),

    # 51–60: Data Structures and Algorithms

    _q("What is the average time complexity of dictionary lookup by key?",
       ["O(1)", "O(n)", "O(log n)", "O(n log n)"],
       0, "Dictionary lookup is average-case O(1), although worst-case behavior can be slower."),

    _q("What is the average time complexity of checking membership in a Python set?",
       ["O(1)", "O(n)", "O(log n)", "O(n²)"],
       0, "Set membership is average-case O(1) because sets use hash tables."),

    _q("Which data structure is used internally by Python dictionaries?",
       ["Binary search tree", "Hash table", "Linked list only", "Stack"],
       1, "Python dictionaries use a hash-table-based implementation."),

    _q("Which module provides deque, a double-ended queue?",
       ["heapq", "collections", "bisect", "array"],
       1, "collections.deque supports efficient insertion and removal at both ends."),

    _q("Which module provides a heap-based priority queue implementation?",
       ["queue", "heapq", "itertools", "bisect"],
       1, "heapq provides functions for maintaining a heap-based priority queue."),

    _q("What is the time complexity of inserting an item into a heap using heapq.heappush()?",
       ["O(1)", "O(log n)", "O(n)", "O(n log n)"],
       1, "Heap insertion restores the heap property in O(log n) time."),

    _q("Which module provides efficient binary search operations on sorted lists?",
       ["bisect", "copy", "operator", "statistics"],
       0, "bisect provides binary-search-based insertion-point operations."),

    _q("What is the average time complexity of list append()?",
       ["O(1) amortized", "O(n) always", "O(log n)", "O(n²)"],
       0, "Appending to a Python list is amortized O(1), although occasional resizing takes longer."),

    _q("Which algorithmic technique solves a problem by breaking it into smaller subproblems?",
       ["Divide and conquer", "Linear scanning only", "Hashing only", "Serialization"],
       0, "Divide and conquer splits a problem into smaller subproblems, solves them and combines results."),

    _q("What is memoization?",
       ["Deleting cached values", "Caching function results to avoid repeated computation", "Sorting a dictionary", "Creating multiple processes"],
       1, "Memoization stores previously computed results for reuse."),

    # 61–70: Files, Serialization and Context Managers

    _q("Which special methods allow an object to work with the with statement?",
       ["__enter__() and __exit__()", "__open__() and __close__()", "__start__() and __stop__()", "__begin__() and __end__()"],
       0, "Context managers implement __enter__() and __exit__()."),

    _q("What is the main benefit of a context manager?",
       ["Automatic resource management", "Automatic code compilation", "Parallel execution", "Automatic type inference"],
       0, "Context managers help reliably acquire and release resources."),

    _q("Which module provides contextmanager for creating context managers using generators?",
       ["contextlib", "pickle", "marshal", "tempfile"],
       0, "contextlib.contextmanager converts a generator function into a context manager."),

    _q("Which module is commonly used to serialize Python objects into byte streams?",
       ["pickle", "csv", "pathlib", "logging"],
       0, "pickle serializes and deserializes Python objects."),

    _q("Why should untrusted pickle data not be loaded?",
       ["It cannot store numbers", "Unpickling can execute arbitrary code", "It always deletes files", "It cannot handle classes"],
       1, "Unpickling untrusted data can execute malicious code."),

    _q("Which module provides a platform-independent object-oriented filesystem path API?",
       ["pathlib", "socket", "subprocess", "argparse"],
       0, "pathlib provides Path objects for filesystem operations."),

    _q("Which module provides temporary files and directories?",
       ["tempfile", "shutil", "glob", "fnmatch"],
       0, "tempfile provides functions for creating temporary files and directories."),

    _q("Which module provides high-level file and directory operations such as copying and moving?",
       ["shutil", "inspect", "typing", "decimal"],
       0, "shutil provides high-level file operations."),

    _q("What is the purpose of the csv.DictReader class?",
       ["Read CSV rows as dictionaries", "Write JSON objects", "Compress CSV files", "Create database indexes"],
       0, "DictReader maps CSV fields to dictionary keys."),

    _q("Which module is designed for parsing and generating JSON data?",
       ["json", "pickle", "struct", "configparser"],
       0, "The json module supports JSON encoding and decoding."),

    # 71–80: Testing, Debugging and Logging

    _q("Which built-in module provides unit testing support?",
       ["unittest", "logging", "profile", "doctest only"],
       0, "unittest provides a framework for writing and running unit tests."),

    _q("Which statement is used to verify an expected condition in a test?",
       ["assert", "yield", "global", "pass"],
       0, "assert checks a condition and raises AssertionError if it is false."),

    _q("Which method in unittest checks whether two values are equal?",
       ["assertSame()", "assertEqual()", "assertMatch()", "assertCompare()"],
       1, "TestCase.assertEqual() checks equality between expected and actual values."),

    _q("What is mocking in software testing?",
       ["Replacing dependencies with controlled test objects", "Deleting all test cases", "Running tests only in production", "Converting tests into documentation"],
       0, "Mocking replaces real dependencies with controlled substitutes."),

    _q("Which standard library module supports mocking?",
       ["unittest.mock", "test.mocking", "mocktools", "pytest.mock"],
       0, "unittest.mock provides Mock, MagicMock and patch."),

    _q("Which module provides Python's standard logging framework?",
       ["logging", "warnings", "traceback", "pdb"],
       0, "The logging module supports configurable application logs."),

    _q("Which logging level is generally more severe: WARNING or ERROR?",
       ["WARNING", "ERROR", "They are equal", "Neither is a logging level"],
       1, "ERROR has a higher severity level than WARNING."),

    _q("Which module provides an interactive Python debugger?",
       ["pdb", "timeit", "dis", "ast"],
       0, "pdb provides an interactive source-code debugger."),

    _q("Which module can measure the execution time of small code snippets?",
       ["timeit", "datetime", "calendar", "secrets"],
       0, "timeit is designed to measure small code snippets reliably."),

    _q("What is code coverage?",
       ["The percentage of code exercised by tests", "The number of Python packages installed", "The amount of memory used", "The number of developers"],
       0, "Code coverage measures which parts of a codebase are executed during testing."),

    # 81–90: Networking, Security and APIs

    _q("Which standard library module provides HTTP client functionality?",
       ["http.client", "html.parser", "xml.etree", "email.mime"],
       0, "http.client provides low-level HTTP client functionality."),

    _q("Which module provides URL parsing and query-string utilities?",
       ["urllib.parse", "pathlib", "socketserver", "ftplib"],
       0, "urllib.parse provides URL parsing, quoting and query-string utilities."),

    _q("Which module provides low-level networking interfaces?",
       ["socket", "logging", "csv", "inspect"],
       0, "The socket module provides access to low-level network communication."),

    _q("Which module provides cryptographically strong random values for security-sensitive operations?",
       ["random", "secrets", "statistics", "math"],
       1, "secrets is designed for generating secure tokens and random values."),

    _q("Which module provides secure hashing and message authentication primitives?",
       ["hashlib", "itertools", "collections", "textwrap"],
       0, "hashlib provides secure hash algorithms such as SHA-256."),

    _q("What is the purpose of hmac.compare_digest()?",
       ["Sort two strings", "Compare cryptographic values in a timing-resistant way", "Encrypt a file", "Generate random passwords"],
       1, "compare_digest() helps avoid timing analysis during sensitive comparisons."),

    _q("What is SQL injection?",
       ["A Python syntax error", "An attack that manipulates SQL through untrusted input", "A type of sorting algorithm", "A file compression technique"],
       1, "SQL injection occurs when untrusted input is improperly incorporated into SQL statements."),

    _q("What is the recommended approach for preventing SQL injection?",
       ["Build SQL using string concatenation", "Use parameterized queries", "Disable database indexes", "Store SQL in comments"],
       1, "Parameterized queries separate SQL structure from user-provided values."),

    _q("What is the purpose of TLS in network communication?",
       ["Compress all network data", "Provide encryption and authentication for communication", "Replace HTTP methods", "Create database tables"],
       1, "TLS protects communication confidentiality and integrity and can authenticate servers."),

    _q("Why should API secrets and passwords not be hardcoded in source code?",
       ["They increase indentation", "They can be exposed through repositories and application artifacts", "They prevent Python compilation", "They make functions slower"],
       1, "Secrets should be stored securely outside source code and managed through appropriate secret-management practices."),

    # 91–100: Advanced Modules and Python Best Practices

    _q("Which module provides tools for functional programming with iterators?",
       ["itertools", "sqlite3", "tkinter", "platform"],
       0, "itertools provides efficient iterator-building tools such as chain, product and groupby."),

    _q("What does itertools.groupby() do?",
       ["Groups consecutive elements sharing the same key", "Sorts every element automatically", "Creates a dictionary of all possible values", "Removes duplicates globally"],
       0, "groupby() groups consecutive elements with equal keys; sorting may be needed first for global grouping."),

    _q("Which module provides tools for inspecting live objects and their members?",
       ["inspect", "random", "decimal", "uuid"],
       0, "inspect provides utilities for examining functions, classes, frames and other live objects."),

    _q("Which module provides access to Python's abstract syntax tree?",
       ["ast", "dis", "gc", "weakref"],
       0, "ast provides tools for parsing and working with Python abstract syntax trees."),

    _q("Which module disassembles Python bytecode?",
       ["dis", "ast", "compileall", "tokenize"],
       0, "dis disassembles Python bytecode into human-readable instructions."),

    _q("What is the purpose of weak references?",
       ["Keep an object alive permanently", "Refer to an object without preventing its garbage collection", "Duplicate an object", "Serialize an object"],
       1, "Weak references do not increase an object's strong reference count."),

    _q("Which module provides weak-reference support?",
       ["weakref", "gc", "copy", "types"],
       0, "The weakref module provides weak references to objects."),

    _q("What is the purpose of Python type hints?",
       ["Force runtime type checking automatically", "Provide type information for tools, editors and static analysis", "Replace all exceptions", "Improve CPU scheduling"],
       1, "Type hints document expected types and support static analysis, but are not automatically enforced at runtime."),

    _q("Which module provides runtime support for structural typing protocols?",
       ["typing", "decimal", "fractions", "numbers"],
       0, "typing.Protocol supports structural subtyping and protocol definitions."),

    _q("What is the main purpose of a virtual environment?",
       ["Run multiple operating systems", "Isolate project dependencies and package installations", "Compile Python into Java", "Replace the Python interpreter"],
       1, "Virtual environments isolate project-specific Python packages and dependencies."),
]
