
# ============================================================
# C PROGRAMMING - ADVANCED QUESTION BANK 1
# Total: 100 Questions
# ============================================================

_C_ADVANCED_QUESTIONS = [

    # ADVANCED POINTERS (1-10)

    (
        "What is the difference between int *p and int **p?",
        ["Both are identical", "p is a pointer to int while **p is a pointer to pointer to int", "p is a pointer to pointer to int while **p is a pointer to int", "Both are integer variables"],
        1,
        "int *p points to an integer, while int **p points to an integer pointer."
    ),
    (
        "What does a pointer to a pointer allow a function to modify?",
        ["Only a constant", "The caller's pointer itself", "Only a structure member", "Only a global variable"],
        1,
        "Passing a pointer to a pointer allows a function to modify the caller's pointer."
    ),
    (
        "What is the result of adding 1 to an int pointer?",
        ["Address increases by one byte", "Address increases by sizeof(int) bytes", "The pointed value increases by one", "Pointer becomes NULL"],
        1,
        "Pointer arithmetic advances by the size of the pointed-to type."
    ),
    (
        "Which declaration represents a constant pointer to constant integer data?",
        ["const int *p", "int * const p", "const int * const p", "int const p"],
        2,
        "const int * const p prevents reassignment of the pointer and modification through that pointer."
    ),
    (
        "What is the purpose of a pointer to an array?",
        ["To point to an entire array object", "To point only to the last element", "To allocate an array automatically", "To convert an array into a string"],
        0,
        "A pointer to an array points to the complete array object."
    ),
    (
        "Which expression accesses the fourth element through pointer p when p points to the first element?",
        ["*p + 4", "*(p + 3)", "*(p + 4)", "&p[4]"],
        1,
        "Pointer indexing starts at zero, so p + 3 points to the fourth element."
    ),
    (
        "What is a pointer to a function returning void and accepting an int?",
        ["void *fp(int)", "void (*fp)(int)", "void **fp(int)", "int (*fp)(void)"],
        1,
        "The parentheses around *fp declare fp as a function pointer."
    ),
    (
        "What is a common use of function pointers?",
        ["Dynamic dispatch through callbacks", "Automatic garbage collection", "Declaring arrays", "Creating preprocessor directives"],
        0,
        "Function pointers support callbacks and selecting functions at runtime."
    ),
    (
        "What happens when a pointer is dereferenced after its allocated memory has been freed?",
        ["It always returns zero", "Undefined behavior", "It reallocates memory", "It automatically becomes NULL"],
        1,
        "Dereferencing a pointer to freed memory causes undefined behavior."
    ),
    (
        "What is pointer aliasing?",
        ["Two or more pointers referring to the same object", "A pointer without a type", "A pointer containing zero", "A pointer to a function only"],
        0,
        "Aliasing occurs when multiple expressions or pointers can access the same object."
    ),

    # DYNAMIC MEMORY MANAGEMENT (11-20)

    (
        "Which function should be used to release memory allocated by malloc?",
        ["delete()", "free()", "remove()", "clear()"],
        1,
        "free() releases dynamically allocated memory."
    ),
    (
        "What happens if free() is called twice on the same allocated pointer without a new allocation?",
        ["Memory is safely freed twice", "Undefined behavior", "The memory is doubled", "The pointer becomes valid again"],
        1,
        "Freeing the same allocation more than once causes undefined behavior."
    ),
    (
        "What is the safest way to handle a failed realloc call when preserving the original allocation?",
        ["Assign realloc directly to the only pointer", "Store the result in a temporary pointer", "Call free before realloc", "Ignore the return value"],
        1,
        "A temporary pointer preserves the original allocation if realloc fails."
    ),
    (
        "What does realloc(ptr, 0) guarantee in modern portable C code?",
        ["It always returns a valid one-byte allocation", "Its behavior is implementation and C-version dependent; avoid relying on it", "It always increases the allocation", "It always returns the original pointer"],
        1,
        "Zero-size realloc behavior has varied across C standards and implementations."
    ),
    (
        "What is heap fragmentation?",
        ["Memory becoming divided into separated free and allocated regions", "A syntax error in malloc", "A pointer changing its type", "A stack overflow"],
        0,
        "Fragmentation can leave free memory in blocks that are difficult to use for larger allocations."
    ),
    (
        "Which allocation function initializes allocated bytes to zero?",
        ["malloc()", "calloc()", "realloc()", "aligned_alloc()"],
        1,
        "calloc() initializes the allocated storage to all-bits-zero."
    ),
    (
        "What is a memory leak?",
        ["Allocated memory that is no longer reachable for release", "A pointer with a valid address", "A stack variable", "A file access error"],
        0,
        "A memory leak occurs when allocated storage cannot be accessed to free it."
    ),
    (
        "What is the purpose of aligned_alloc()?",
        ["To allocate memory with a specified alignment", "To allocate only character arrays", "To release memory", "To initialize a file"],
        0,
        "aligned_alloc() requests dynamically allocated storage with a specified alignment."
    ),
    (
        "What must be true about the size argument passed to aligned_alloc() in C11?",
        ["It must be a multiple of the alignment", "It must always be one", "It must be negative", "It must equal sizeof(void*)"],
        0,
        "C11 aligned_alloc requires the requested size to be an integral multiple of the alignment."
    ),
    (
        "Which operation is valid for a pointer returned by malloc when allocation succeeds?",
        ["Accessing allocated storage within its bounds using a suitable type", "Reading beyond the allocation", "Freeing it twice", "Adding unrelated pointers"],
        0,
        "Allocated storage may be accessed within its bounds using appropriate object types and alignment."
    ),

    # STRUCTURES AND LINKED LISTS (21-30)

    (
        "What is the main purpose of a linked list?",
        ["To store elements connected through links", "To store only sorted integers", "To replace all functions", "To allocate static memory only"],
        0,
        "Linked lists connect nodes using pointers."
    ),
    (
        "What does the next pointer in a singly linked-list node usually store?",
        ["The address of the next node", "The previous node's data", "The list length", "The array index"],
        0,
        "The next pointer links a node to its successor."
    ),
    (
        "What does the next pointer of the last node in a conventional singly linked list contain?",
        ["The first node address", "NULL", "The previous node address", "The node's data"],
        1,
        "The last node usually points to NULL to mark the end of the list."
    ),
    (
        "What is the time complexity of inserting a node at the beginning of a singly linked list?",
        ["O(1)", "O(n)", "O(log n)", "O(n log n)"],
        0,
        "Insertion at the head requires a constant number of pointer updates."
    ),
    (
        "What is the time complexity of searching for a value in an unsorted singly linked list?",
        ["O(1)", "O(log n)", "O(n)", "O(n squared)"],
        2,
        "In the worst case, every node must be checked."
    ),
    (
        "What is a doubly linked list?",
        ["A list whose nodes contain links to both previous and next nodes", "A list with two head nodes only", "A list containing only two elements", "A list without pointers"],
        0,
        "Doubly linked-list nodes commonly contain previous and next pointers."
    ),
    (
        "What is a circular linked list?",
        ["A list whose final node links back to an earlier node, commonly the head", "A list stored in a circle-shaped array", "A list with no nodes", "A list that cannot be traversed"],
        0,
        "In a circular linked list, the final link connects back to the list rather than NULL."
    ),
    (
        "Which pointer is commonly used to maintain the first node of a linked list?",
        ["head", "tail only", "temp only", "NULL only"],
        0,
        "The head pointer identifies the first node."
    ),
    (
        "What is a common use of the slow and fast pointer technique?",
        ["Detecting a cycle in a linked list", "Sorting a file", "Allocating a structure", "Calculating string length"],
        0,
        "Moving pointers at different speeds can detect a cycle using Floyd's algorithm."
    ),
    (
        "What is the time complexity of reversing a singly linked list iteratively?",
        ["O(1)", "O(log n)", "O(n)", "O(n squared)"],
        2,
        "Each node is visited once, so reversal takes linear time."
    ),

    # ADVANCED DATA STRUCTURES AND ALGORITHMS (31-40)

    (
        "Which data structure is commonly used to implement recursion?",
        ["Stack", "Queue", "Graph only", "Hash table only"],
        0,
        "Function calls and their local execution state are typically managed using a call stack."
    ),
    (
        "Which data structure follows the LIFO principle?",
        ["Queue", "Stack", "Linked list only", "Tree"],
        1,
        "LIFO means Last In, First Out."
    ),
    (
        "Which data structure follows the FIFO principle?",
        ["Stack", "Queue", "Binary search tree", "Heap"],
        1,
        "FIFO means First In, First Out."
    ),
    (
        "What is the worst-case time complexity of binary search on a sorted array?",
        ["O(1)", "O(log n)", "O(n)", "O(n squared)"],
        1,
        "Binary search repeatedly halves the search interval."
    ),
    (
        "What is the worst-case time complexity of merge sort?",
        ["O(n)", "O(log n)", "O(n log n)", "O(n squared)"],
        2,
        "Merge sort divides the input and merges sorted parts in O(n log n) time."
    ),
    (
        "What is the worst-case time complexity of quicksort?",
        ["O(n)", "O(log n)", "O(n log n)", "O(n squared)"],
        3,
        "Poor pivot choices can produce highly unbalanced partitions."
    ),
    (
        "Which algorithm is commonly used to find the shortest paths from one source in a graph with non-negative edge weights?",
        ["Dijkstra's algorithm", "Depth-first search only", "Bubble sort", "Binary search"],
        0,
        "Dijkstra's algorithm computes shortest paths when edge weights are non-negative."
    ),
    (
        "Which traversal visits a binary tree's root before its left and right subtrees?",
        ["Inorder", "Preorder", "Postorder", "Level order only"],
        1,
        "Preorder traversal visits root, then left subtree, then right subtree."
    ),
    (
        "Which traversal visits the left subtree, root, and then right subtree?",
        ["Preorder", "Postorder", "Inorder", "Reverse level order"],
        2,
        "Inorder traversal follows left, root, right."
    ),
    (
        "What is the main property of a binary search tree?",
        ["Left subtree keys are smaller and right subtree keys are larger, according to its ordering rule", "Every node has exactly two children", "All leaves are at the same level", "It stores only strings"],
        0,
        "A binary search tree maintains an ordering relationship between node keys and subtrees."
    ),

    # BIT MANIPULATION (41-50)

    (
        "Which expression sets bit position k in unsigned integer x?",
        ["x & ~(1U << k)", "x | (1U << k)", "x ^ ~(1U << k)", "x >> k"],
        1,
        "Bitwise OR with a mask containing one at position k sets that bit."
    ),
    (
        "Which expression clears bit position k in unsigned integer x?",
        ["x | (1U << k)", "x & ~(1U << k)", "x ^ (1U << k)", "x << k"],
        1,
        "AND with the complement of a one-bit mask clears the selected bit."
    ),
    (
        "Which expression toggles bit position k in unsigned integer x?",
        ["x ^ (1U << k)", "x | (1U << k)", "x & (1U << k)", "x >> k"],
        0,
        "XOR with a one-bit mask toggles the selected bit."
    ),
    (
        "How can you test whether bit k is set in unsigned integer x?",
        ["(x & (1U << k)) != 0", "(x | (1U << k)) == 0", "(x ^ k) == 0", "x == k"],
        0,
        "AND with a bit mask tests whether the selected bit is one."
    ),
    (
        "What does x & (x - 1) do for a nonzero unsigned integer x?",
        ["Clears the least significant set bit", "Sets every bit", "Shifts x left", "Always produces x"],
        0,
        "Subtracting one and ANDing clears the lowest set bit."
    ),
    (
        "What is a common use of x & (x - 1)?",
        ["Checking whether an unsigned integer is a power of two", "Sorting a linked list", "Opening a file", "Finding string length"],
        0,
        "For nonzero unsigned x, x & (x - 1) equals zero exactly when x is a power of two."
    ),
    (
        "What is the result of XORing a value with itself?",
        ["The same value", "Zero", "One", "The maximum integer"],
        1,
        "For any integer value, x ^ x evaluates to zero."
    ),
    (
        "Why should unsigned integers be preferred for many bit-mask operations?",
        ["Their arithmetic and shifts avoid some signed-overflow and sign-related issues", "They always use less memory", "They support floating-point values", "They cannot overflow"],
        0,
        "Unsigned arithmetic has well-defined modulo behavior, making it useful for bit manipulation."
    ),
    (
        "What is a potential problem with shifting a value by an amount greater than or equal to its type width?",
        ["The behavior is undefined", "The value always becomes zero", "The compiler automatically corrects it", "The type becomes unsigned"],
        0,
        "C shift counts must be nonnegative and smaller than the width of the promoted left operand."
    ),
    (
        "What is the purpose of a bit field in a structure?",
        ["To specify a member with a particular number of bits", "To create a linked list", "To allocate a file", "To declare a function pointer"],
        0,
        "Bit fields allow structure members to occupy implementation-defined portions of storage units."
    ),

    # FILE HANDLING AND BINARY DATA (51-60)

    (
        "Which function reads binary data from a file stream?",
        ["fread()", "fprintf()", "fputs()", "puts()"],
        0,
        "fread() reads blocks of data from a stream."
    ),
    (
        "Which function writes binary data to a file stream?",
        ["fscanf()", "fwrite()", "fgets()", "fgetc()"],
        1,
        "fwrite() writes blocks of data to a stream."
    ),
    (
        "What does the rb mode mean in fopen()?",
        ["Read a file in binary mode", "Write a file in binary mode", "Append text to a file", "Rename a file"],
        0,
        "The rb mode opens a file for reading in binary mode."
    ),
    (
        "What is the purpose of fseek()?",
        ["Move the stream position indicator", "Close the stream", "Delete the file", "Allocate a buffer"],
        0,
        "fseek() repositions the file position indicator."
    ),
    (
        "What does SEEK_SET represent?",
        ["Beginning of the file", "Current position", "End of the file", "A failed read"],
        0,
        "SEEK_SET specifies the beginning of the file as the reference position."
    ),
    (
        "What does SEEK_CUR represent?",
        ["Beginning of the file", "Current file position", "End of the file", "File size"],
        1,
        "SEEK_CUR uses the current file position as the reference."
    ),
    (
        "What does SEEK_END represent?",
        ["Beginning of the file", "Current position", "End of the file", "Beginning of memory"],
        2,
        "SEEK_END uses the end of the file as the reference position."
    ),
    (
        "Why should the return value of fwrite() be checked?",
        ["To verify how many elements were written", "To determine the compiler version", "To get the file name", "To allocate more stack memory"],
        0,
        "fwrite() returns the number of elements successfully written."
    ),
    (
        "Why can writing a structure directly to a binary file reduce portability?",
        ["Structure padding, representation, and byte order can differ between systems", "Structures cannot contain integers", "Binary files cannot store bytes", "fwrite always converts structures to text"],
        0,
        "Raw structure representations may vary across compilers and architectures."
    ),
    (
        "What is the purpose of fflush() on an output stream?",
        ["To flush buffered output", "To delete buffered input", "To rewind the file", "To close the file permanently"],
        0,
        "fflush() requests that buffered output be delivered to the host environment."
    ),

    # PREPROCESSOR AND MACROS (61-70)

    (
        "What is the token-pasting operator in a C macro?",
        ["#", "##", "@@", "&&"],
        1,
        "The ## operator joins preprocessing tokens."
    ),
    (
        "What does the # operator do inside a function-like macro replacement list?",
        ["Stringizes a macro argument", "Concatenates two tokens", "Includes a file", "Ends preprocessing"],
        0,
        "The # operator converts a macro argument into a string literal."
    ),
    (
        "What is a variadic macro?",
        ["A macro that accepts a variable number of arguments", "A macro without a name", "A macro that only accepts pointers", "A macro that cannot be expanded"],
        0,
        "Variadic macros use ... to accept additional arguments."
    ),
    (
        "Which predefined macro commonly expands to the current source file name?",
        ["__LINE__", "__FILE__", "__DATE__", "__TIME__"],
        1,
        "__FILE__ expands to a string literal containing the presumed source file name."
    ),
    (
        "Which predefined macro expands to the current source line number?",
        ["__FILE__", "__LINE__", "__STDC__", "__TIME__"],
        1,
        "__LINE__ expands to the presumed current source line number."
    ),
    (
        "What is the main purpose of conditional compilation?",
        ["Include or exclude source sections based on preprocessing conditions", "Execute code faster at runtime", "Allocate dynamic memory", "Create a pointer"],
        0,
        "Conditional compilation controls which source sections are processed."
    ),
    (
        "What does #error do?",
        ["Causes a preprocessing diagnostic with the specified message", "Deletes the source file", "Ends the running program", "Defines a function"],
        0,
        "#error directs the implementation to produce a diagnostic."
    ),
    (
        "Why can a macro such as SQUARE(x) ((x) * (x)) evaluate an argument more than once?",
        ["The argument text is substituted at each occurrence", "Macros always create loops", "The compiler duplicates main()", "The preprocessor changes integers to pointers"],
        0,
        "Macro substitution can evaluate an argument once for each occurrence in the replacement list."
    ),
    (
        "What is a key advantage of an inline function over a function-like macro?",
        ["It follows normal function type checking and argument evaluation rules", "It always uses zero memory", "It cannot return a value", "It is processed before preprocessing"],
        0,
        "Inline functions retain ordinary function semantics and type checking."
    ),
    (
        "What does #pragma generally provide?",
        ["An implementation-defined way to control compiler behavior", "A standard method to allocate heap memory", "A runtime file operation", "A replacement for every header"],
        0,
        "#pragma provides implementation-defined compiler instructions."
    ),

    # MEMORY MODEL AND STORAGE (71-80)

    (
        "Which storage duration applies to a dynamically allocated object?",
        ["Automatic", "Static", "Allocated", "Thread only"],
        2,
        "Dynamically allocated objects have allocated storage duration."
    ),
    (
        "Which storage duration applies to a file-scope object?",
        ["Automatic", "Static", "Allocated", "Temporary"],
        1,
        "Objects declared at file scope have static storage duration."
    ),
    (
        "What is the typical lifetime of an automatic local variable?",
        ["The execution of its enclosing block", "The entire program execution", "Until the next computer restart", "Until the file is closed"],
        0,
        "An ordinary automatic local object's lifetime is associated with execution of its block."
    ),
    (
        "What is the purpose of storage duration in C?",
        ["It determines an object's lifetime", "It determines a function's return type", "It specifies an array's index", "It controls file permissions"],
        0,
        "Storage duration describes the lifetime of an object."
    ),
    (
        "What is the difference between scope and lifetime?",
        ["Scope describes where an identifier is visible; lifetime describes how long an object exists", "They always mean the same thing", "Scope describes memory size only", "Lifetime describes variable naming rules"],
        0,
        "Scope is a visibility property, while lifetime is an object existence property."
    ),
    (
        "What does the register storage-class specifier request?",
        ["Suggests that an object may be stored in a CPU register", "Guarantees a CPU register", "Allocates heap memory", "Makes the object constant"],
        0,
        "register is a hint to the implementation and does not guarantee register storage."
    ),
    (
        "What is the purpose of the _Alignof operator in C11?",
        ["To obtain the alignment requirement of a type", "To obtain the number of array elements", "To free memory", "To return a pointer address"],
        0,
        "_Alignof reports the alignment requirement of a type."
    ),
    (
        "Which C11 keyword can specify an alignment requirement?",
        ["_Alignas", "alignof", "register", "restrict"],
        0,
        "_Alignas specifies an alignment requirement for an object or member."
    ),
    (
        "What is strict aliasing related to?",
        ["Rules governing access to an object's stored value through lvalues of different types", "Rules for naming functions", "Rules for opening files", "Rules for sorting arrays"],
        0,
        "Strict aliasing rules constrain which lvalue types may access an object's stored value."
    ),
    (
        "Which type is specifically intended to represent raw bytes?",
        ["unsigned char", "double", "long double", "enum"],
        0,
        "Character types, especially unsigned char, are used to inspect object representations byte by byte."
    ),

    # ADVANCED C LANGUAGE FEATURES (81-90)

    (
        "What does _Generic provide in C11?",
        ["Generic selection based on the type of an expression", "Dynamic memory allocation", "Thread creation", "File compression"],
        0,
        "_Generic selects an expression based on the compatible type of a controlling expression."
    ),
    (
        "What is the purpose of _Static_assert?",
        ["To check a compile-time constant condition", "To check a file at runtime", "To allocate static memory", "To declare a static function"],
        0,
        "_Static_assert checks a constant expression during translation."
    ),
    (
        "Which C11 feature supports multithreading?",
        ["The threads library when supported by the implementation", "The string library only", "The math library only", "The stdio library only"],
        0,
        "C11 introduced optional thread support through the threads library."
    ),
    (
        "What is the purpose of the atomic types introduced in C11?",
        ["To support atomic operations on shared objects", "To allocate arrays", "To create macros", "To open files"],
        0,
        "C11 atomics provide operations designed for safe concurrent access."
    ),
    (
        "Which header declares standard atomic operations in C11?",
        ["stdatomic.h", "threads.h", "stdalign.h", "stdbool.h"],
        0,
        "stdatomic.h declares the C11 atomic types and operations."
    ),
    (
        "What is a data race in a multithreaded C program?",
        ["Conflicting concurrent accesses to the same memory location without required synchronization, with at least one modification", "Two threads reading separate variables", "Two functions having the same name", "Two files with identical contents"],
        0,
        "A data race occurs when conflicting accesses are not properly ordered or atomic."
    ),
    (
        "What is the purpose of a mutex?",
        ["To protect shared resources through mutual exclusion", "To sort arrays", "To allocate a stack", "To format strings"],
        0,
        "A mutex ensures that only one thread at a time holds the associated lock."
    ),
    (
        "What does the volatile qualifier NOT guarantee?",
        ["Thread synchronization or atomicity", "That accesses are significant to the implementation", "That the object may change unexpectedly", "That the compiler observes volatile accesses"],
        0,
        "volatile is not a substitute for atomic operations or synchronization."
    ),
    (
        "What is the purpose of errno?",
        ["To provide an error indicator used by some library functions", "To store the program's command-line arguments", "To count allocated bytes", "To store function pointers"],
        0,
        "errno is used by library functions to report certain error conditions."
    ),
    (
        "Which header declares errno?",
        ["errno.h", "assert.h", "limits.h", "signal.h"],
        0,
        "errno is declared through errno.h."
    ),

    # PORTABILITY, DEBUGGING AND SAFETY (91-100)

    (
        "What is undefined behavior?",
        ["Behavior for which the C standard imposes no requirements", "Behavior that always produces zero", "A compiler warning", "A documented platform-specific choice"],
        0,
        "The C standard imposes no requirements on the behavior of a program that invokes undefined behavior."
    ),
    (
        "What is unspecified behavior?",
        ["One of several permitted behaviors chosen by the implementation, with no requirement to document the choice", "Behavior that is always invalid", "Behavior that must cause a crash", "Behavior that is always documented"],
        0,
        "The standard permits multiple possibilities without requiring the implementation to document which occurs."
    ),
    (
        "What is implementation-defined behavior?",
        ["Behavior where the implementation chooses and documents a permitted choice", "Behavior with no possible valid result", "Behavior that is always identical on all systems", "Behavior that cannot be compiled"],
        0,
        "The implementation must document its choice for implementation-defined behavior."
    ),
    (
        "Why should signed integer overflow be avoided?",
        ["It causes undefined behavior in C", "It always wraps around safely", "It automatically allocates memory", "It converts the integer to unsigned"],
        0,
        "Signed integer overflow is undefined behavior."
    ),
    (
        "What is the purpose of sanitizers during development?",
        ["To detect certain programming errors such as invalid memory access and undefined behavior", "To automatically write all tests", "To replace the compiler", "To optimize every algorithm"],
        0,
        "Sanitizers instrument programs to help detect classes of runtime errors."
    ),
    (
        "Which sanitizer is commonly used to detect out-of-bounds access and use-after-free?",
        ["AddressSanitizer", "ThreadSanitizer", "UndefinedBehaviorSanitizer only", "MemorySanitizer only"],
        0,
        "AddressSanitizer detects many memory safety errors, including out-of-bounds access and use-after-free."
    ),
    (
        "Which sanitizer is designed to detect data races?",
        ["AddressSanitizer", "ThreadSanitizer", "LeakSanitizer", "UndefinedBehaviorSanitizer"],
        1,
        "ThreadSanitizer detects data races in supported environments."
    ),
    (
        "What is the purpose of defensive programming in C?",
        ["Validate inputs and handle errors to reduce failures and vulnerabilities", "Avoid all functions", "Use global variables everywhere", "Disable compiler warnings"],
        0,
        "Defensive programming checks assumptions and handles unexpected conditions."
    ),
    (
        "Why should the return value of scanf() be checked?",
        ["To verify how many input items were successfully assigned", "To obtain the address of stdin", "To allocate memory", "To close the input stream"],
        0,
        "scanf() returns the number of input items successfully assigned, or EOF in certain cases."
    ),
    (
        "What is a buffer overflow?",
        ["Writing beyond the bounds of a buffer", "Reading a valid array element", "Closing a file twice", "Calling a function recursively"],
        0,
        "A buffer overflow occurs when data is written outside the allocated buffer bounds."
    ),
]


# Convert compact question definitions into the format expected by
# SkillSphere's import_question_bank command.

QUESTION_BANK_C_ADVANCED1 = [
    {
        "skill": "C Programming",
        "difficulty": "advanced",
        "questions": [
            {
                "question_text": question,
                "options": options,
                "correct_answer": answer,
                "explanation": explanation,
            }
            for question, options, answer, explanation
            in _C_ADVANCED_QUESTIONS
        ],
    }
]
