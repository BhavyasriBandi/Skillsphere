
QUESTION_BANK_C_INTERMEDIATE1 = [
    {
        "skill": "C Programming",
        "difficulty": "intermediate",
        "questions": [
            {
                "question": "What does a pointer store?",
                "options": ["A variable value", "The address of a variable", "A data type", "A function name"],
                "correct_answer": 1,
                "explanation": "A pointer stores the memory address of another variable."
            },
            {
                "question": "Which operator is used to access the value stored at a pointer address?",
                "options": ["&", "*", "%", "#"],
                "correct_answer": 1,
                "explanation": "The dereference operator (*) accesses the value at the address stored in a pointer."
            },
            {
                "question": "What does the address-of operator (&) return?",
                "options": ["Variable value", "Variable address", "Variable size", "Variable type"],
                "correct_answer": 1,
                "explanation": "The & operator returns the memory address of a variable."
            },
            {
                "question": "What is a NULL pointer?",
                "options": ["A pointer pointing to zero-valued data", "A pointer that points to no valid object", "An integer pointer", "A pointer to a function"],
                "correct_answer": 1,
                "explanation": "A NULL pointer does not point to a valid memory object."
            },
            {
                "question": "Which header file declares malloc()?",
                "options": ["stdio.h", "string.h", "stdlib.h", "math.h"],
                "correct_answer": 2,
                "explanation": "malloc() is declared in stdlib.h."
            },
            {
                "question": "What does malloc() return when allocation fails?",
                "options": ["-1", "0.0", "NULL", "EOF"],
                "correct_answer": 2,
                "explanation": "malloc() returns NULL if it cannot allocate the requested memory."
            },
            {
                "question": "Which function releases dynamically allocated memory?",
                "options": ["delete()", "remove()", "free()", "clear()"],
                "correct_answer": 2,
                "explanation": "free() releases memory allocated dynamically."
            },
            {
                "question": "Which function allocates memory and initializes it to zero?",
                "options": ["malloc()", "calloc()", "realloc()", "free()"],
                "correct_answer": 1,
                "explanation": "calloc() allocates memory for multiple elements and initializes the allocated bytes to zero."
            },
            {
                "question": "Which function changes the size of an allocated memory block?",
                "options": ["malloc()", "calloc()", "realloc()", "sizeof()"],
                "correct_answer": 2,
                "explanation": "realloc() changes the size of a previously allocated memory block."
            },
            {
                "question": "What is a dangling pointer?",
                "options": ["A pointer initialized to NULL", "A pointer referring to memory that is no longer valid", "A pointer to an array", "A pointer to a function"],
                "correct_answer": 1,
                "explanation": "A dangling pointer refers to memory that has been freed or whose lifetime has ended."
            },
            {
                "question": "What is a wild pointer?",
                "options": ["An uninitialized pointer", "A NULL pointer", "A constant pointer", "A pointer to a string"],
                "correct_answer": 0,
                "explanation": "An uninitialized pointer is commonly called a wild pointer."
            },
            {
                "question": "What is pointer arithmetic?",
                "options": ["Adding two pointer addresses directly", "Performing arithmetic operations on pointers", "Converting pointers into strings", "Comparing data types"],
                "correct_answer": 1,
                "explanation": "Pointer arithmetic allows operations such as incrementing or decrementing pointers."
            },
            {
                "question": "If p is an int pointer, what does p++ do?",
                "options": ["Increases the stored integer by one", "Moves the pointer to the next int element", "Sets the pointer to NULL", "Doubles the pointer address"],
                "correct_answer": 1,
                "explanation": "Pointer increment advances by the size of the pointed-to type."
            },
            {
                "question": "Which declaration represents a pointer to a pointer to int?",
                "options": ["int *p", "int **p", "int &p", "int p**"],
                "correct_answer": 1,
                "explanation": "int **p declares a pointer that stores the address of an int pointer."
            },
            {
                "question": "What is a void pointer?",
                "options": ["A pointer that cannot store addresses", "A generic pointer type", "A pointer to void functions only", "A NULL pointer"],
                "correct_answer": 1,
                "explanation": "A void pointer can hold the address of an object of any data type."
            },
            {
                "question": "Can a void pointer be dereferenced directly in standard C?",
                "options": ["Yes, always", "No, it must first be converted to an appropriate object pointer type", "Only when it is NULL", "Only inside main()"],
                "correct_answer": 1,
                "explanation": "A void pointer must be converted to a suitable object pointer type before dereferencing."
            },
            {
                "question": "What does sizeof(pointer) return?",
                "options": ["Size of the pointed-to object", "Size of the pointer variable", "Number of array elements", "Always 4"],
                "correct_answer": 1,
                "explanation": "sizeof applied to a pointer gives the size of the pointer type."
            },
            {
                "question": "Which expression accesses the third element of an array named a?",
                "options": ["a[3]", "a[2]", "a[1]", "a[0]"],
                "correct_answer": 1,
                "explanation": "C arrays use zero-based indexing, so the third element is at index 2."
            },
            {
                "question": "In most expressions, an array name is converted to what?",
                "options": ["The value of its first element", "A pointer to its first element", "The size of the array", "A pointer to its last element"],
                "correct_answer": 1,
                "explanation": "An array expression usually converts to a pointer to its first element."
            },
            {
                "question": "Which declaration creates an array of 5 pointers to int?",
                "options": ["int (*p)[5]", "int *p[5]", "int p*[5]", "int **p[5]"],
                "correct_answer": 1,
                "explanation": "int *p[5] declares an array containing five int pointers."
            },
            {
                "question": "Which declaration creates a pointer to an array of 5 integers?",
                "options": ["int *p[5]", "int (*p)[5]", "int **p", "int p[5]"],
                "correct_answer": 1,
                "explanation": "Parentheses make p a pointer to an array of five integers."
            },
            {
                "question": "What is the last valid index of an array declared as int a[10]?",
                "options": ["10", "9", "11", "1"],
                "correct_answer": 1,
                "explanation": "An array of ten elements has indexes from 0 through 9."
            },
            {
                "question": "What happens when a program accesses an array outside its bounds?",
                "options": ["The compiler always fixes it", "Undefined behavior", "The array automatically expands", "The value is always zero"],
                "correct_answer": 1,
                "explanation": "Out-of-bounds array access causes undefined behavior in C."
            },
            {
                "question": "Which is the correct declaration of a two-dimensional integer array with 3 rows and 4 columns?",
                "options": ["int a[3,4]", "int a[3][4]", "int a(3)(4)", "int a[4][3]"],
                "correct_answer": 1,
                "explanation": "A two-dimensional array uses separate bracket pairs for rows and columns."
            },
            {
                "question": "How are elements of a two-dimensional array stored in C?",
                "options": ["Column-major order", "Row-major order", "Random order", "Reverse order"],
                "correct_answer": 1,
                "explanation": "C stores multidimensional arrays in row-major order."
            },
            {
                "question": "Which function is used to find the length of a null-terminated string?",
                "options": ["strcpy()", "strlen()", "strcmp()", "strcat()"],
                "correct_answer": 1,
                "explanation": "strlen() returns the number of characters before the terminating null character."
            },
            {
                "question": "Which function copies one string into another?",
                "options": ["strcpy()", "strcmp()", "strlen()", "strchr()"],
                "correct_answer": 0,
                "explanation": "strcpy() copies a source string, including its terminating null character."
            },
            {
                "question": "Which function compares two strings?",
                "options": ["strcat()", "strcmp()", "strcpy()", "strlen()"],
                "correct_answer": 1,
                "explanation": "strcmp() compares two strings lexicographically."
            },
            {
                "question": "Which function appends one string to another?",
                "options": ["strcat()", "strcmp()", "strncpy()", "strstr()"],
                "correct_answer": 0,
                "explanation": "strcat() appends the source string to the destination string."
            },
            {
                "question": "What character terminates a C string?",
                "options": ["\\n", "\\t", "\\0", "\\r"],
                "correct_answer": 2,
                "explanation": "C strings end with the null character '\\0'."
            },
            {
                "question": "What is recursion?",
                "options": ["A loop without a condition", "A function calling itself", "A pointer operation", "A file operation"],
                "correct_answer": 1,
                "explanation": "Recursion occurs when a function calls itself directly or indirectly."
            },
            {
                "question": "Why is a base case important in recursion?",
                "options": ["It increases memory usage", "It stops recursive calls", "It declares a pointer", "It opens a file"],
                "correct_answer": 1,
                "explanation": "A base case provides a stopping condition for recursive calls."
            },
            {
                "question": "What can happen if recursion has no reachable base case?",
                "options": ["The function always returns zero", "Recursive calls may continue until resources are exhausted", "The compiler converts it into a loop", "The program automatically exits successfully"],
                "correct_answer": 1,
                "explanation": "Unbounded recursion can exhaust the call stack."
            },
            {
                "question": "Which memory area typically stores function call information?",
                "options": ["Heap", "Stack", "Text segment", "File buffer only"],
                "correct_answer": 1,
                "explanation": "Function call frames are typically maintained on the call stack."
            },
            {
                "question": "What is the output of a recursive function that returns 1 when n equals 0 and otherwise returns n * f(n-1), for f(4)?",
                "options": ["10", "16", "24", "4"],
                "correct_answer": 2,
                "explanation": "The function calculates 4 * 3 * 2 * 1, which equals 24."
            },
            {
                "question": "What is a function prototype?",
                "options": ["A function call", "A declaration specifying a function's interface", "A function output", "A loop declaration"],
                "correct_answer": 1,
                "explanation": "A function prototype declares its name, return type, and parameter types."
            },
            {
                "question": "What is the purpose of a function parameter?",
                "options": ["To pass information into a function", "To terminate a program", "To allocate a file", "To declare a header"],
                "correct_answer": 0,
                "explanation": "Parameters receive values supplied to a function."
            },
            {
                "question": "How are ordinary arguments passed to functions in C?",
                "options": ["Always by reference", "By value", "By name", "By inheritance"],
                "correct_answer": 1,
                "explanation": "C passes function arguments by value. Pointers can be used to modify caller-owned objects."
            },
            {
                "question": "How can a function modify a variable belonging to its caller?",
                "options": ["Pass the variable's address and modify through a pointer", "Declare another local variable", "Use sizeof()", "Use continue"],
                "correct_answer": 0,
                "explanation": "Passing a pointer lets the function access and modify the original object."
            },
            {
                "question": "What does the return statement do in a non-void function?",
                "options": ["Declares a variable", "Returns a value to the caller", "Starts a loop", "Opens a file"],
                "correct_answer": 1,
                "explanation": "return supplies the function result to its caller."
            },
            {
                "question": "What is a static local variable?",
                "options": ["A variable recreated on every function call", "A local variable that retains its value between function calls", "A global constant", "A pointer variable only"],
                "correct_answer": 1,
                "explanation": "A static local variable has static storage duration and retains its value between calls."
            },
            {
                "question": "What is the default initial value of a static storage duration integer object when no explicit initializer is provided?",
                "options": ["An indeterminate value", "Zero", "One", "-1"],
                "correct_answer": 1,
                "explanation": "Objects with static storage duration are initialized to zero by default."
            },
            {
                "question": "What is the scope of a variable declared inside a function block?",
                "options": ["Entire program", "The block in which it is declared", "All source files", "Only the header file"],
                "correct_answer": 1,
                "explanation": "A block-scope variable is visible from its declaration to the end of its enclosing block."
            },
            {
                "question": "Which keyword prevents modification through a particular variable or pointer expression?",
                "options": ["static", "const", "extern", "register"],
                "correct_answer": 1,
                "explanation": "const specifies that an object is not modifiable through that lvalue."
            },
            {
                "question": "What does extern commonly indicate in a declaration?",
                "options": ["A variable is always local", "An object or function is defined elsewhere", "A variable is constant", "A function is recursive"],
                "correct_answer": 1,
                "explanation": "extern declares an object or function with external linkage in common usage."
            },
            {
                "question": "What is a structure in C?",
                "options": ["A collection of members that can have different types", "A collection of only characters", "A loop structure", "A function pointer"],
                "correct_answer": 0,
                "explanation": "A structure groups related members, which may have different data types."
            },
            {
                "question": "Which keyword declares a structure?",
                "options": ["union", "struct", "enum", "typedef"],
                "correct_answer": 1,
                "explanation": "The struct keyword declares a structure type."
            },
            {
                "question": "Which operator accesses a structure member through a structure variable?",
                "options": ["->", ".", "&", "*"],
                "correct_answer": 1,
                "explanation": "The dot operator accesses a member through a structure object."
            },
            {
                "question": "Which operator accesses a structure member through a pointer?",
                "options": [".", "->", "::", "#"],
                "correct_answer": 1,
                "explanation": "The arrow operator accesses a member through a pointer to a structure."
            },
            {
                "question": "Which declaration creates a pointer to a structure named Student?",
                "options": ["struct Student p", "struct Student *p", "Student &p", "struct *Student p"],
                "correct_answer": 1,
                "explanation": "struct Student *p declares a pointer to a Student structure."
            },
            {
                "question": "What is a self-referential structure?",
                "options": ["A structure containing a pointer to its own structure type", "A structure with no members", "A structure containing only integers", "A structure declared inside main()"],
                "correct_answer": 0,
                "explanation": "A self-referential structure contains a pointer to the same structure type."
            },
            {
                "question": "Which data structure is commonly implemented using self-referential structures?",
                "options": ["Linked list", "Simple integer", "Character constant", "Enumeration"],
                "correct_answer": 0,
                "explanation": "Linked-list nodes commonly contain a pointer to another node of the same structure type."
            },
            {
                "question": "What is a union in C?",
                "options": ["A type whose members share the same storage", "A type where every member has separate storage", "A loop statement", "A function declaration"],
                "correct_answer": 0,
                "explanation": "Union members overlap in storage, so they share the same memory area."
            },
            {
                "question": "What determines the size of a union?",
                "options": ["Sum of all member sizes", "Enough space for its largest member, with required alignment", "Always one byte", "Number of union variables"],
                "correct_answer": 1,
                "explanation": "A union must provide enough storage for its largest member, subject to alignment and implementation requirements."
            },
            {
                "question": "What is the main difference between a structure and a union?",
                "options": ["Structures cannot contain pointers", "Structure members have separate storage while union members share storage", "Unions cannot contain integers", "Structures cannot be passed to functions"],
                "correct_answer": 1,
                "explanation": "Structure members occupy separate storage; union members overlap."
            },
            {
                "question": "Which keyword creates an alias for an existing type?",
                "options": ["typedef", "sizeof", "extern", "volatile"],
                "correct_answer": 0,
                "explanation": "typedef introduces an alternative name for a type."
            },
            {
                "question": "What is an enumeration in C?",
                "options": ["A user-defined type consisting of named integer constants", "A dynamic array", "A file pointer", "A function pointer"],
                "correct_answer": 0,
                "explanation": "An enum defines named integer constants."
            },
            {
                "question": "Which keyword declares an enumeration?",
                "options": ["struct", "enum", "union", "typedef"],
                "correct_answer": 1,
                "explanation": "The enum keyword declares an enumeration type."
            },
            {
                "question": "What is the usual value of the first enumerator when no value is specified?",
                "options": ["-1", "0", "1", "Undefined"],
                "correct_answer": 1,
                "explanation": "The first enumerator has value zero by default."
            },
            {
                "question": "Which function opens a file in C?",
                "options": ["fopen()", "openfile()", "fileopen()", "readfile()"],
                "correct_answer": 0,
                "explanation": "fopen() opens a file and returns a FILE pointer on success."
            },
            {
                "question": "Which function closes an opened file?",
                "options": ["fclose()", "closefile()", "endfile()", "fend()"],
                "correct_answer": 0,
                "explanation": "fclose() closes a stream."
            },
            {
                "question": "Which file mode opens a file for reading?",
                "options": ["w", "a", "r", "x"],
                "correct_answer": 2,
                "explanation": "The r mode opens an existing file for reading."
            },
            {
                "question": "Which file mode opens a file for writing and truncates an existing file?",
                "options": ["r", "w", "a", "rb"],
                "correct_answer": 1,
                "explanation": "The w mode creates a file or truncates an existing file for writing."
            },
            {
                "question": "Which file mode opens a file for appending?",
                "options": ["r", "w", "a", "x"],
                "correct_answer": 2,
                "explanation": "The a mode writes new data at the end of the file."
            },
            {
                "question": "What does fopen() return if a file cannot be opened?",
                "options": ["EOF", "NULL", "-1", "A zero-length string"],
                "correct_answer": 1,
                "explanation": "fopen() returns a null pointer when opening a stream fails."
            },
            {
                "question": "Which function reads formatted data from a file stream?",
                "options": ["fprintf()", "fscanf()", "fputs()", "fclose()"],
                "correct_answer": 1,
                "explanation": "fscanf() reads formatted input from a stream."
            },
            {
                "question": "Which function writes formatted output to a file stream?",
                "options": ["fscanf()", "fgets()", "fprintf()", "fread()"],
                "correct_answer": 2,
                "explanation": "fprintf() writes formatted output to a stream."
            },
            {
                "question": "Which function reads a character from a file stream?",
                "options": ["fputc()", "fgetc()", "fputs()", "fwrite()"],
                "correct_answer": 1,
                "explanation": "fgetc() reads the next character from a stream."
            },
            {
                "question": "Which function writes a character to a file stream?",
                "options": ["fgetc()", "fputc()", "fscanf()", "fread()"],
                "correct_answer": 1,
                "explanation": "fputc() writes a character to a stream."
            },
            {
                "question": "Which function reads a line or string from a file stream with a size limit?",
                "options": ["fgets()", "fputs()", "fprintf()", "fseek()"],
                "correct_answer": 0,
                "explanation": "fgets() reads at most one less than the specified number of characters and adds a null terminator."
            },
            {
                "question": "Which function writes a string to a file stream?",
                "options": ["fgets()", "fputs()", "fscanf()", "fread()"],
                "correct_answer": 1,
                "explanation": "fputs() writes a string to a stream."
            },
            {
                "question": "Which function changes the file position indicator?",
                "options": ["fseek()", "fclose()", "feof()", "ferror()"],
                "correct_answer": 0,
                "explanation": "fseek() repositions the file position indicator."
            },
            {
                "question": "Which function returns the current file position?",
                "options": ["fseek()", "ftell()", "rewind()", "fopen()"],
                "correct_answer": 1,
                "explanation": "ftell() returns the current file position indicator value."
            },
            {
                "question": "Which function moves the file position indicator to the beginning of a stream?",
                "options": ["rewind()", "ftell()", "fwrite()", "ferror()"],
                "correct_answer": 0,
                "explanation": "rewind() sets the file position to the beginning of the stream."
            },
            {
                "question": "What does EOF represent?",
                "options": ["End-of-file indicator value", "Beginning of file", "A file name", "A file pointer"],
                "correct_answer": 0,
                "explanation": "EOF is a negative integer constant used to indicate end-of-file or certain input failures."
            },
            {
                "question": "Which function checks whether a stream's end-of-file indicator is set?",
                "options": ["ferror()", "feof()", "fseek()", "fputs()"],
                "correct_answer": 1,
                "explanation": "feof() tests the stream's end-of-file indicator."
            },
            {
                "question": "Which function checks whether an error indicator is set for a stream?",
                "options": ["feof()", "ferror()", "ftell()", "rewind()"],
                "correct_answer": 1,
                "explanation": "ferror() tests the stream's error indicator."
            },
            {
                "question": "What is a preprocessor directive?",
                "options": ["An instruction processed before the main compilation phase", "A runtime function", "A database command", "A pointer operation"],
                "correct_answer": 0,
                "explanation": "Preprocessor directives are handled before the compiler translates the program."
            },
            {
                "question": "Which symbol begins a C preprocessor directive?",
                "options": ["@", "#", "$", "&"],
                "correct_answer": 1,
                "explanation": "Preprocessor directives begin with the # character."
            },
            {
                "question": "What does #include do?",
                "options": ["Defines a function", "Requests inclusion of a header or source file", "Ends a program", "Declares an array"],
                "correct_answer": 1,
                "explanation": "#include requests that the preprocessor include the specified file."
            },
            {
                "question": "What does #define commonly do?",
                "options": ["Defines a macro", "Opens a file", "Declares a structure", "Frees memory"],
                "correct_answer": 0,
                "explanation": "#define creates an object-like or function-like macro."
            },
            {
                "question": "Which directive can conditionally compile code when a macro is defined?",
                "options": ["#ifdef", "#include", "#undef", "#line"],
                "correct_answer": 0,
                "explanation": "#ifdef checks whether a macro name is defined."
            },
            {
                "question": "Which directive ends a conditional compilation block?",
                "options": ["#endif", "#end", "#stop", "#else"],
                "correct_answer": 0,
                "explanation": "#endif marks the end of a conditional compilation group."
            },
            {
                "question": "What does #undef do?",
                "options": ["Defines a new function", "Undefines a macro", "Includes a header", "Terminates the program"],
                "correct_answer": 1,
                "explanation": "#undef removes a macro definition."
            },
            {
                "question": "What is a macro with parameters called?",
                "options": ["Object-like macro", "Function-like macro", "Global variable", "Structure macro"],
                "correct_answer": 1,
                "explanation": "A function-like macro accepts arguments in its replacement list."
            },
            {
                "question": "Why should arguments in function-like macros often be parenthesized?",
                "options": ["To avoid operator-precedence surprises", "To allocate memory", "To create a file", "To prevent compilation"],
                "correct_answer": 0,
                "explanation": "Parentheses help preserve the intended grouping of macro arguments and expressions."
            },
            {
                "question": "Which operator is used for bitwise AND?",
                "options": ["&&", "&", "|", "^"],
                "correct_answer": 1,
                "explanation": "The single ampersand operator performs bitwise AND."
            },
            {
                "question": "Which operator performs bitwise OR?",
                "options": ["||", "&", "|", "~"],
                "correct_answer": 2,
                "explanation": "The single vertical bar operator performs bitwise OR."
            },
            {
                "question": "Which operator performs bitwise XOR?",
                "options": ["&&", "^", "|", "~"],
                "correct_answer": 1,
                "explanation": "The caret operator performs bitwise exclusive OR."
            },
            {
                "question": "Which operator performs bitwise complement?",
                "options": ["!", "~", "^", "&"],
                "correct_answer": 1,
                "explanation": "The tilde operator complements each bit of its integer operand."
            },
            {
                "question": "What does the expression x << 1 do for an unsigned integer x?",
                "options": ["Shifts bits one position to the left", "Shifts bits one position to the right", "Complements all bits", "Adds one to x"],
                "correct_answer": 0,
                "explanation": "The left-shift operator moves the bits toward higher-order positions."
            },
            {
                "question": "What does the expression x >> 1 do for an unsigned integer x?",
                "options": ["Shifts bits one position to the left", "Shifts bits one position to the right", "Multiplies x by two", "Sets all bits to one"],
                "correct_answer": 1,
                "explanation": "The right-shift operator moves bits toward lower-order positions."
            },
            {
                "question": "Which operator is the logical AND operator?",
                "options": ["&", "&&", "|", "^"],
                "correct_answer": 1,
                "explanation": "&& performs logical AND and produces either 0 or 1."
            },
            {
                "question": "Which operator is the logical OR operator?",
                "options": ["||", "|", "&&", "~"],
                "correct_answer": 0,
                "explanation": "|| performs logical OR and produces either 0 or 1."
            },
            {
                "question": "What is short-circuit evaluation?",
                "options": ["Skipping evaluation when the result is already determined", "Executing every expression twice", "Stopping compilation", "Skipping variable declarations"],
                "correct_answer": 0,
                "explanation": "Logical operators may skip the second operand when the first determines the result."
            },
            {
                "question": "What is the result of 5 & 3 in C?",
                "options": ["1", "2", "7", "8"],
                "correct_answer": 0,
                "explanation": "Binary 0101 AND 0011 gives 0001, which is 1."
            },
            {
                "question": "What is the result of 5 | 3 in C?",
                "options": ["1", "6", "7", "8"],
                "correct_answer": 2,
                "explanation": "Binary 0101 OR 0011 gives 0111, which is 7."
            },
            {
                "question": "What is the result of 5 ^ 3 in C?",
                "options": ["1", "6", "7", "8"],
                "correct_answer": 1,
                "explanation": "Binary 0101 XOR 0011 gives 0110, which is 6."
            },
            {
                "question": "Which operator returns the remainder of integer division?",
                "options": ["/", "%", "*", "//"],
                "correct_answer": 1,
                "explanation": "The modulo operator % gives the remainder for integer operands."
            },
            {
                "question": "What is the result of 17 % 5?",
                "options": ["2", "3", "5", "12"],
                "correct_answer": 0,
                "explanation": "17 divided by 5 leaves a remainder of 2."
            },
            {
                "question": "What does the break statement do inside a loop?",
                "options": ["Skips only the current iteration", "Terminates the nearest enclosing loop", "Restarts the program", "Pauses the loop permanently"],
                "correct_answer": 1,
                "explanation": "break exits the nearest enclosing loop or switch statement."
            },
            {
                "question": "What does continue do inside a loop?",
                "options": ["Terminates the program", "Skips the rest of the current iteration", "Exits every nested loop", "Returns from the function"],
                "correct_answer": 1,
                "explanation": "continue transfers control to the next iteration of the nearest enclosing loop."
            },
            {
                "question": "Which loop checks its condition after executing the loop body?",
                "options": ["for", "while", "do-while", "Nested for"],
                "correct_answer": 2,
                "explanation": "A do-while loop evaluates its condition after the body, so it executes at least once."
            },
            {
                "question": "What is an infinite loop?",
                "options": ["A loop that executes exactly once", "A loop whose termination condition never becomes false", "A loop with no body", "A loop that always uses break"],
                "correct_answer": 1,
                "explanation": "An infinite loop continues indefinitely unless control exits it through another mechanism."
            },
            {
                "question": "Which storage class gives a local variable static storage duration?",
                "options": ["auto", "static", "register", "volatile"],
                "correct_answer": 1,
                "explanation": "The static storage-class specifier gives a local object static storage duration."
            },
            {
                "question": "What does volatile tell the compiler?",
                "options": ["The object can never change", "The object's value may change in ways not apparent to the compiler", "The object must be stored in a register", "The object is always constant"],
                "correct_answer": 1,
                "explanation": "volatile tells the implementation that accesses to the object are significant and its value may change unexpectedly."
            },
            {
                "question": "What is a function pointer?",
                "options": ["A pointer that stores a function address", "A function that returns an array", "A pointer that stores only integers", "A pointer that always points to NULL"],
                "correct_answer": 0,
                "explanation": "A function pointer can store the address of a function with a compatible type."
            },
            {
                "question": "Which declaration represents a pointer to a function taking an int and returning an int?",
                "options": ["int *fp(int)", "int (*fp)(int)", "int fp*(int)", "int **fp(int)"],
                "correct_answer": 1,
                "explanation": "Parentheses around *fp declare fp as a pointer to a function."
            },
            {
                "question": "What is a callback function in C?",
                "options": ["A function passed to another function to be called later", "A function that always calls main()", "A function without parameters", "A function that cannot return"],
                "correct_answer": 0,
                "explanation": "A callback is commonly passed through a function pointer and invoked by another function."
            },
            {
                "question": "Which standard library function can sort an array using a comparison callback?",
                "options": ["qsort()", "bsearch()", "strlen()", "memcpy()"],
                "correct_answer": 0,
                "explanation": "qsort() sorts an array using a supplied comparison function."
            },
            {
                "question": "Which standard library function searches a sorted array using binary search?",
                "options": ["qsort()", "bsearch()", "strstr()", "memset()"],
                "correct_answer": 1,
                "explanation": "bsearch() searches an array using binary search and a comparison function."
            },
            {
                "question": "Which function copies a specified number of bytes between memory areas?",
                "options": ["memcpy()", "strlen()", "strcmp()", "strcat()"],
                "correct_answer": 0,
                "explanation": "memcpy() copies a specified number of bytes; source and destination must not overlap."
            },
            {
                "question": "Which function copies bytes while allowing overlapping memory regions?",
                "options": ["memcpy()", "memmove()", "memcmp()", "memset()"],
                "correct_answer": 1,
                "explanation": "memmove() safely handles overlapping source and destination regions."
            },
            {
                "question": "Which function fills a block of memory with a byte value?",
                "options": ["memcpy()", "memcmp()", "memset()", "memmove()"],
                "correct_answer": 2,
                "explanation": "memset() sets each of the specified bytes to the given byte value."
            },
            {
                "question": "Which function compares two blocks of memory?",
                "options": ["memcmp()", "memset()", "memcpy()", "memmove()"],
                "correct_answer": 0,
                "explanation": "memcmp() compares two memory regions byte by byte."
            },
            {
                "question": "What is a memory leak?",
                "options": ["Memory allocated but no longer reachable for release", "A syntax error", "A pointer initialized to NULL", "A file opened in read mode"],
                "correct_answer": 0,
                "explanation": "A memory leak occurs when allocated memory is no longer accessible for proper deallocation."
            },
            {
                "question": "What is the purpose of checking the return value of malloc()?",
                "options": ["To check whether allocation succeeded", "To check array sorting", "To check file permissions", "To calculate string length"],
                "correct_answer": 0,
                "explanation": "Checking for NULL allows the program to handle allocation failure safely."
            },
            {
                "question": "What is the purpose of sizeof in dynamic allocation?",
                "options": ["To obtain the size of a type or object in bytes", "To free memory", "To open a file", "To compare strings"],
                "correct_answer": 0,
                "explanation": "sizeof helps calculate the number of bytes required for an allocation."
            },
            {
                "question": "What is the result of sizeof(char) in C?",
                "options": ["Always 2", "Always 4", "Always 1", "Depends on the compiler"],
                "correct_answer": 2,
                "explanation": "sizeof(char) is defined to be 1 byte in C."
            },
            {
                "question": "What does the const qualifier in int * const p mean?",
                "options": ["The pointed-to integer cannot change through p", "The pointer itself cannot be reassigned", "Both pointer and integer are constant", "p is a NULL pointer"],
                "correct_answer": 1,
                "explanation": "int * const p makes the pointer itself constant, while the pointed-to int is not const-qualified."
            },
            {
                "question": "What does const int *p mean?",
                "options": ["The pointer cannot be reassigned", "The pointed-to integer cannot be modified through p", "Both pointer and integer are constant", "p must be initialized to NULL"],
                "correct_answer": 1,
                "explanation": "const int *p prevents modification of the pointed-to int through p."
            },
            {
                "question": "What is the purpose of a header guard?",
                "options": ["To prevent repeated inclusion of a header's contents", "To allocate memory", "To execute a function", "To close a file"],
                "correct_answer": 0,
                "explanation": "Header guards prevent a header from being processed repeatedly in the same translation unit."
            },
            {
                "question": "Which pair of directives is commonly used to create a header guard?",
                "options": ["#ifdef and #define, followed by #endif", "#include and #undef only", "#if and #error only", "#line and #pragma only"],
                "correct_answer": 0,
                "explanation": "A macro is checked and defined before the header contents, with #endif closing the condition."
            },
            {
                "question": "What is the purpose of the main() function in a hosted C program?",
                "options": ["It is the program's designated entry point", "It is always a recursive function", "It allocates all global variables", "It must return a pointer"],
                "correct_answer": 0,
                "explanation": "In a hosted C environment, execution begins at the designated main function."
            },
            {
                "question": "Which standard header declares the printf() function?",
                "options": ["stdlib.h", "stdio.h", "string.h", "ctype.h"],
                "correct_answer": 1,
                "explanation": "printf() is declared in stdio.h."
            },
            {
                "question": "Which header declares character classification functions such as isdigit()?",
                "options": ["ctype.h", "math.h", "time.h", "assert.h"],
                "correct_answer": 0,
                "explanation": "Character classification functions are declared in ctype.h."
            },
            {
                "question": "Which function converts a string to a long integer with error handling support?",
                "options": ["atoi()", "strtol()", "strlen()", "strcpy()"],
                "correct_answer": 1,
                "explanation": "strtol() converts a string to a long integer and provides ways to detect conversion issues."
            },
            {
                "question": "Which function converts a string to a double?",
                "options": ["strtod()", "strtol()", "atoi()", "strcmp()"],
                "correct_answer": 0,
                "explanation": "strtod() converts the initial portion of a string to a double."
            },
            {
                "question": "What does the comma operator do?",
                "options": ["Evaluates its left operand, then its right operand, and yields the right operand's value", "Adds two strings", "Declares two functions", "Separates structure members"],
                "correct_answer": 0,
                "explanation": "The comma operator sequences evaluation and yields the value of its right operand."
            },
            {
                "question": "What is the conditional operator in C?",
                "options": ["?:", "&&", "sizeof", "->"],
                "correct_answer": 0,
                "explanation": "The conditional operator uses the form condition ? expression1 : expression2."
            },
            {
                "question": "Which operator has higher precedence: multiplication or addition?",
                "options": ["Addition", "Multiplication", "They always have equal precedence", "It depends on variable names"],
                "correct_answer": 1,
                "explanation": "Multiplication has higher precedence than addition."
            },
            {
                "question": "What is the purpose of parentheses in an expression?",
                "options": ["To control grouping and evaluation order", "To allocate heap memory", "To declare a pointer", "To end a statement"],
                "correct_answer": 0,
                "explanation": "Parentheses explicitly group expressions and can override normal precedence."
            },
            {
                "question": "What is undefined behavior in C?",
                "options": ["Behavior for which the C standard imposes no requirements", "A guaranteed runtime error message", "A compiler warning only", "A valid output of zero"],
                "correct_answer": 0,
                "explanation": "Undefined behavior means the C standard imposes no requirements on the behavior."
            },
            {
                "question": "Which situation can cause undefined behavior?",
                "options": ["Reading an uninitialized automatic int", "Declaring an int variable", "Using printf() correctly", "Including stdio.h"],
                "correct_answer": 0,
                "explanation": "Using an indeterminate automatic int value can result in undefined behavior."
            },
            {
                "question": "What is implementation-defined behavior?",
                "options": ["Behavior where the implementation chooses and documents a choice", "Behavior that is always undefined", "Behavior that is identical on every system", "Behavior that prevents compilation"],
                "correct_answer": 0,
                "explanation": "The implementation selects and documents one permitted behavior."
            },
            {
                "question": "What is the purpose of assert()?",
                "options": ["To test a condition during program execution", "To allocate memory", "To compare files", "To define a macro"],
                "correct_answer": 0,
                "explanation": "assert() checks a condition and reports a diagnostic if it is false, unless assertions are disabled."
            },
            {
                "question": "Which header declares assert()?",
                "options": ["assert.h", "stdio.h", "stdlib.h", "limits.h"],
                "correct_answer": 0,
                "explanation": "The assert macro is defined in assert.h."
            },
            {
                "question": "Which header provides integer type limits such as INT_MAX?",
                "options": ["limits.h", "float.h", "string.h", "errno.h"],
                "correct_answer": 0,
                "explanation": "limits.h defines limits for standard integer types."
            },
            {
                "question": "Which header provides floating-point limits such as DBL_MAX?",
                "options": ["limits.h", "float.h", "ctype.h", "signal.h"],
                "correct_answer": 1,
                "explanation": "float.h defines characteristics and limits of floating-point types."
            },
            {
                "question": "What does the expression *(arr + 2) access when arr points to the first element of an array?",
                "options": ["First element", "Second element", "Third element", "Fourth element"],
                "correct_answer": 2,
                "explanation": "Pointer arithmetic advances two elements, so the expression accesses index 2."
            },
            {
                "question": "Which expression is equivalent to arr[i] in C?",
                "options": ["*(arr + i)", "&arr + i", "*arr + i", "arr * i"],
                "correct_answer": 0,
                "explanation": "Array subscripting is defined in terms of pointer addition and dereferencing."
            },
            {
                "question": "What does a function return type of void indicate?",
                "options": ["The function returns an integer", "The function does not return a value", "The function returns a pointer", "The function cannot have parameters"],
                "correct_answer": 1,
                "explanation": "A void return type indicates that the function does not return a value."
            },
            {
                "question": "What is the purpose of the restrict qualifier?",
                "options": ["It provides a promise about pointer-based access to an object for optimization", "It makes a pointer constant", "It makes a variable global", "It allocates memory"],
                "correct_answer": 0,
                "explanation": "restrict is an optimization-related pointer qualifier with rules about accessing the referenced object."
            },
            {
                "question": "What does the expression (int)3.8 do?",
                "options": ["Rounds to 4", "Truncates the fractional part to produce 3", "Produces 3.8 as an int", "Causes a syntax error"],
                "correct_answer": 1,
                "explanation": "Conversion from floating point to integer discards the fractional part when the value is representable."
            },
            {
                "question": "Which function can remove a file by its name?",
                "options": ["remove()", "fclose()", "fseek()", "rename()"],
                "correct_answer": 0,
                "explanation": "remove() attempts to remove the file specified by its pathname."
            },
            {
                "question": "Which function can rename a file?",
                "options": ["rename()", "remove()", "rewind()", "fread()"],
                "correct_answer": 0,
                "explanation": "rename() changes the name or location of a file according to the implementation's filesystem rules."
            },
            {
                "question": "Which function reads a block of data from a stream?",
                "options": ["fread()", "fwrite()", "fprintf()", "fputs()"],
                "correct_answer": 0,
                "explanation": "fread() reads a specified number of elements from a stream."
            },
            {
                "question": "Which function writes a block of data to a stream?",
                "options": ["fread()", "fwrite()", "fscanf()", "fgetc()"],
                "correct_answer": 1,
                "explanation": "fwrite() writes a specified number of elements to a stream."
            },
            {
                "question": "What is the purpose of fflush() for an output stream?",
                "options": ["To force buffered output to be delivered to the host environment", "To delete the file", "To reset the file name", "To read a character"],
                "correct_answer": 0,
                "explanation": "fflush() requests that buffered output be written to the host environment."
            },
            {
                "question": "What is a command-line argument in C?",
                "options": ["A value supplied when starting a program", "A value stored only in a file", "A preprocessor directive", "A pointer arithmetic operator"],
                "correct_answer": 0,
                "explanation": "Command-line arguments are commonly received through argc and argv parameters in main()."
            },
            {
                "question": "In int main(int argc, char *argv[]), what does argc represent?",
                "options": ["The number of command-line arguments", "The first argument string", "The program's return value", "The number of functions"],
                "correct_answer": 0,
                "explanation": "argc contains the count of command-line arguments, including the program name."
            },
            {
                "question": "In int main(int argc, char *argv[]), what does argv represent?",
                "options": ["An array of argument strings", "An integer array of return values", "A file pointer", "A structure variable"],
                "correct_answer": 0,
                "explanation": "argv is an array of pointers to character strings containing command-line arguments."
            },
            {
                "question": "What is the purpose of the return value from main() in a hosted environment?",
                "options": ["It communicates a termination status to the host environment", "It stores the program name", "It allocates stack memory", "It declares a global variable"],
                "correct_answer": 0,
                "explanation": "The return value from main communicates the program's termination status."
            }
        ]
    }
]
