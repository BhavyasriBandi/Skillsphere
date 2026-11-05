
def _advanced_java_question(question_text, options, correct_answer, explanation):
    return {
        "skill": "Java",
        "difficulty": "Advanced",
        "question_text": question_text,
        "options": options,
        "correct_answer": correct_answer,
        "explanation": explanation
    }


QUESTION_BANK_JAVA_ADVANCED1 = [

    # 1–10: JVM, Memory Management and Garbage Collection

    _advanced_java_question(
        "Which JVM memory area is shared among all threads?",
        ["Java Stack", "Program Counter Register", "Heap", "Native Method Stack"],
        2,
        "The heap is shared among all JVM threads and stores objects and arrays."
    ),

    _advanced_java_question(
        "What causes a StackOverflowError in Java?",
        ["Excessive object creation", "Infinite or excessively deep recursion",
         "Heap memory exhaustion", "Too many class loaders"],
        1,
        "StackOverflowError occurs when a thread's stack exceeds its permitted size."
    ),

    _advanced_java_question(
        "Which garbage collector is designed to minimize pause times?",
        ["Serial GC", "Parallel GC", "ZGC", "Epsilon GC"],
        2,
        "ZGC is a low-latency garbage collector designed to keep pauses very short."
    ),

    _advanced_java_question(
        "What does the finalize() method indicate in Java?",
        ["Guaranteed object destruction", "A deprecated finalization mechanism",
         "Immediate garbage collection", "Thread termination"],
        1,
        "finalize() was a deprecated finalization mechanism and its execution was never guaranteed."
    ),

    _advanced_java_question(
        "Which reference type does not prevent an object from being garbage collected?",
        ["StrongReference", "SoftReference", "WeakReference", "Both SoftReference and WeakReference"],
        3,
        "Soft and weak references do not provide the same strong reachability as ordinary references."
    ),

    _advanced_java_question(
        "What is the primary purpose of the Metaspace in modern HotSpot JVMs?",
        ["Store Java object instances", "Store class metadata",
         "Store local variables", "Store thread stacks"],
        1,
        "Metaspace stores class metadata and uses native memory."
    ),

    _advanced_java_question(
        "Which JVM option sets the maximum heap size?",
        ["-Xms", "-Xmx", "-Xss", "-XX:MaxMetaspaceSize"],
        1,
        "-Xmx specifies the maximum Java heap size."
    ),

    _advanced_java_question(
        "What is a memory leak in Java?",
        ["Memory is never allocated", "Unreachable objects are immediately deleted",
         "Unneeded objects remain reachable and cannot be collected",
         "The JVM automatically increases heap size"],
        2,
        "A memory leak occurs when objects are no longer useful but remain reachable."
    ),

    _advanced_java_question(
        "Which tool can be used to analyze a Java heap dump?",
        ["Javadoc", "Eclipse Memory Analyzer (MAT)", "JShell", "JAR"],
        1,
        "Eclipse MAT analyzes heap dumps to identify memory retention and leaks."
    ),

    _advanced_java_question(
        "What is the main purpose of escape analysis in the JVM?",
        ["Encrypt objects", "Determine whether objects escape a method or thread",
         "Compile Java source code", "Manage database connections"],
        1,
        "Escape analysis helps the JIT compiler optimize object allocation and synchronization."
    ),

    # 11–20: Multithreading and Concurrency

    _advanced_java_question(
        "Which interface represents a task that returns a result and may throw an exception?",
        ["Runnable", "Callable", "Thread", "Executor"],
        1,
        "Callable<V> defines call(), which returns a value and can throw checked exceptions."
    ),

    _advanced_java_question(
        "What is the primary purpose of CountDownLatch?",
        ["Lock multiple objects", "Allow threads to wait until a count reaches zero",
         "Create daemon threads", "Stop a thread permanently"],
        1,
        "CountDownLatch allows one or more threads to wait until a specified number of events occur."
    ),

    _advanced_java_question(
        "Which class provides a lock with optional fairness and interruptible acquisition?",
        ["Object", "ReentrantLock", "StringBuffer", "ThreadLocal"],
        1,
        "ReentrantLock supports fairness configuration and interruptible lock acquisition."
    ),

    _advanced_java_question(
        "What does the volatile keyword guarantee?",
        ["Atomicity of all compound operations", "Visibility of writes across threads",
         "Automatic thread synchronization", "Prevention of deadlocks"],
        1,
        "Volatile establishes visibility and ordering guarantees but does not make compound operations atomic."
    ),

    _advanced_java_question(
        "Which method releases a lock while waiting and reacquires it before returning?",
        ["Thread.sleep()", "Object.wait()", "Thread.yield()", "Thread.start()"],
        1,
        "Object.wait() releases the monitor lock and reacquires it before returning."
    ),

    _advanced_java_question(
        "What is a deadlock?",
        ["A thread executing continuously", "Two or more threads waiting indefinitely for each other's resources",
         "A thread waiting for CPU time", "A thread completing normally"],
        1,
        "Deadlock occurs when threads form a circular dependency on resources."
    ),

    _advanced_java_question(
        "Which executor service method attempts to stop actively executing tasks?",
        ["execute()", "submit()", "shutdownNow()", "invokeAll()"],
        2,
        "shutdownNow() attempts to interrupt active tasks and returns tasks that have not started."
    ),

    _advanced_java_question(
        "Which class provides atomic integer operations without explicit synchronization?",
        ["Integer", "AtomicInteger", "BigInteger", "ThreadLocal"],
        1,
        "AtomicInteger provides atomic operations such as incrementAndGet() using atomic primitives."
    ),

    _advanced_java_question(
        "What is the purpose of a CyclicBarrier?",
        ["Terminate all threads", "Allow a group of threads to wait for each other at a common point",
         "Create a thread pool", "Prevent object serialization"],
        1,
        "CyclicBarrier synchronizes a group of threads at a common barrier point and can be reused."
    ),

    _advanced_java_question(
        "What is the ForkJoinPool primarily designed for?",
        ["Database transactions", "Divide-and-conquer parallel tasks",
         "File encryption", "Network configuration"],
        1,
        "ForkJoinPool efficiently executes tasks that split into smaller subtasks using work stealing."
    ),

    # 21–30: Collections and Generics

    _advanced_java_question(
        "What is the average time complexity of HashMap.get()?",
        ["O(1)", "O(log n)", "O(n)", "O(n log n)"],
        0,
        "HashMap lookup is O(1) on average, although collisions can affect performance."
    ),

    _advanced_java_question(
        "Which collection maintains insertion order and allows duplicate elements?",
        ["HashSet", "LinkedHashSet", "ArrayList", "TreeSet"],
        2,
        "ArrayList preserves insertion order and permits duplicate elements."
    ),

    _advanced_java_question(
        "Which map implementation sorts its keys according to their natural ordering or a comparator?",
        ["HashMap", "LinkedHashMap", "TreeMap", "IdentityHashMap"],
        2,
        "TreeMap maintains keys in sorted order."
    ),

    _advanced_java_question(
        "What happens when two unequal keys have the same hash code in HashMap?",
        ["One key is deleted", "A collision occurs",
         "The map throws an exception", "Both keys become identical"],
        1,
        "HashMap handles hash collisions using buckets and equality checks."
    ),

    _advanced_java_question(
        "What is the purpose of the Comparable interface?",
        ["Define external sorting", "Define an object's natural ordering",
         "Create immutable collections", "Compare object memory addresses"],
        1,
        "Comparable defines natural ordering through the compareTo() method."
    ),

    _advanced_java_question(
        "Which wildcard allows a generic method to consume a collection of Number or its subclasses?",
        ["? super Number", "? extends Number", "<?>", "<? implements Number>"],
        1,
        "? extends Number provides an upper-bounded wildcard for Number and its subclasses."
    ),

    _advanced_java_question(
        "What does PECS stand for in Java generics?",
        ["Producer Extends Consumer Super", "Program Execute Compile System",
         "Private Encapsulation Class Structure", "Producer Execute Consumer Store"],
        0,
        "PECS means Producer Extends, Consumer Super."
    ),

    _advanced_java_question(
        "Which collection is designed for concurrent access with sorted keys?",
        ["HashMap", "TreeMap", "ConcurrentSkipListMap", "ArrayList"],
        2,
        "ConcurrentSkipListMap is a concurrent sorted map implementation."
    ),

    _advanced_java_question(
        "What is the primary difference between fail-fast and fail-safe iterators?",
        ["Fail-fast iterators detect structural modifications, while snapshot or weakly consistent iterators have different modification behavior",
         "Fail-fast iterators are always thread-safe",
         "Fail-safe iterators never allow traversal",
         "There is no difference"],
        0,
        "Fail-fast iterators may throw ConcurrentModificationException; snapshot or weakly consistent iterators have different guarantees."
    ),

    _advanced_java_question(
        "Which interface supports a double-ended queue?",
        ["Queue", "Deque", "Set", "Map"],
        1,
        "Deque supports insertion and removal at both ends."
    ),

    # 31–40: Java 8+ Features and Functional Programming

    _advanced_java_question(
        "Which functional interface accepts one argument and returns a result?",
        ["Consumer", "Supplier", "Function", "Runnable"],
        2,
        "Function<T,R> accepts a value of type T and produces a result of type R."
    ),

    _advanced_java_question(
        "Which functional interface represents an operation that takes no arguments and returns a value?",
        ["Supplier", "Consumer", "Predicate", "BiConsumer"],
        0,
        "Supplier<T> provides a value through its get() method."
    ),

    _advanced_java_question(
        "What is the purpose of Optional in Java?",
        ["Replace all exceptions", "Represent a possibly absent value",
         "Create asynchronous threads", "Store multiple values"],
        1,
        "Optional represents a value that may or may not be present."
    ),

    _advanced_java_question(
        "Which Stream operation is a terminal operation?",
        ["map()", "filter()", "sorted()", "collect()"],
        3,
        "collect() is a terminal operation that gathers stream elements into a result."
    ),

    _advanced_java_question(
        "What is the main characteristic of a parallel stream?",
        ["It always executes sequentially", "It can process elements concurrently",
         "It prevents exceptions", "It guarantees element processing order"],
        1,
        "Parallel streams can divide work across multiple threads, commonly using the common ForkJoinPool."
    ),

    _advanced_java_question(
        "Which method combines two functions where the second function is applied after the first?",
        ["andThen()", "compose()", "filter()", "reduce()"],
        0,
        "andThen() applies the current function first and then applies the supplied function."
    ),

    _advanced_java_question(
        "Which annotation indicates that an interface has exactly one abstract method?",
        ["@Override", "@FunctionalInterface", "@Deprecated", "@SafeVarargs"],
        1,
        "@FunctionalInterface enables compile-time checking of functional interface requirements."
    ),

    _advanced_java_question(
        "What does Stream.flatMap() do?",
        ["Sorts a stream", "Converts each element into a stream and flattens the results",
         "Removes all null values automatically", "Creates a new thread"],
        1,
        "flatMap() maps each element to a stream and combines the resulting streams."
    ),

    _advanced_java_question(
        "Which interface represents a condition that returns true or false?",
        ["Function", "Predicate", "Supplier", "Consumer"],
        1,
        "Predicate<T> defines a test() method that returns a boolean."
    ),

    _advanced_java_question(
        "What is the result of Stream.findFirst()?",
        ["A List", "An Optional containing the first element if present",
         "An integer index", "A boolean"],
        1,
        "findFirst() returns an Optional describing the first stream element, if any."
    ),

    # 41–50: Exception Handling and JVM Internals

    _advanced_java_question(
        "Which exception is checked at compile time?",
        ["NullPointerException", "ArithmeticException", "IOException", "ArrayIndexOutOfBoundsException"],
        2,
        "IOException is a checked exception and must be caught or declared."
    ),

    _advanced_java_question(
        "What happens if a finally block contains a return statement that overrides an earlier return?",
        ["Compilation always fails", "The finally return can override the earlier return value",
         "The finally block is ignored", "The JVM restarts"],
        1,
        "A return in finally can override a return from try or catch and is generally discouraged."
    ),

    _advanced_java_question(
        "Which keyword is used to explicitly throw an exception?",
        ["throws", "throw", "try", "catch"],
        1,
        "The throw keyword explicitly throws a throwable object."
    ),

    _advanced_java_question(
        "What is the purpose of suppressed exceptions in try-with-resources?",
        ["Replace the primary exception", "Preserve exceptions thrown while closing resources",
         "Disable exception handling", "Automatically retry failed operations"],
        1,
        "Exceptions thrown during resource closing can be attached as suppressed exceptions to the primary exception."
    ),

    _advanced_java_question(
        "Which class is the superclass of both Exception and Error?",
        ["Throwable", "Object", "RuntimeException", "Serializable"],
        0,
        "Throwable is the superclass of Exception and Error."
    ),

    _advanced_java_question(
        "What does ClassNotFoundException indicate?",
        ["A class could not be located during explicit loading",
         "A method was overridden incorrectly", "A thread has stopped",
         "An object cannot be serialized"],
        0,
        "ClassNotFoundException commonly occurs when Class.forName() or a class loader cannot find a requested class."
    ),

    _advanced_java_question(
        "What is the purpose of a custom class loader?",
        ["Create database tables", "Load classes from custom locations or sources",
         "Manage garbage collection", "Replace the Java compiler"],
        1,
        "Custom class loaders provide control over how and where classes are loaded."
    ),

    _advanced_java_question(
        "Which JVM component executes bytecode and performs runtime compilation optimizations?",
        ["Garbage Collector", "JIT Compiler", "Class Loader only", "Java Launcher"],
        1,
        "The Just-In-Time compiler compiles frequently executed bytecode into optimized native code."
    ),

    _advanced_java_question(
        "What is bytecode verification responsible for?",
        ["Checking bytecode safety and structural correctness",
         "Increasing network speed", "Creating database indexes",
         "Compressing Java files"],
        0,
        "The bytecode verifier checks class files for structural and type-safety constraints."
    ),

    _advanced_java_question(
        "Which keyword prevents a method from being overridden?",
        ["static", "final", "volatile", "transient"],
        1,
        "A final method cannot be overridden by subclasses."
    ),

    # 51–60: Design Patterns and Object-Oriented Programming

    _advanced_java_question(
        "Which design pattern ensures that a class has only one instance?",
        ["Factory", "Singleton", "Observer", "Decorator"],
        1,
        "Singleton restricts instantiation to a single shared instance."
    ),

    _advanced_java_question(
        "Which design pattern provides a way to create objects without exposing the exact creation logic?",
        ["Observer", "Factory Method", "Strategy", "Adapter"],
        1,
        "Factory Method delegates object creation to factory methods or subclasses."
    ),

    _advanced_java_question(
        "Which pattern allows one object to notify multiple dependent objects about state changes?",
        ["Builder", "Observer", "Prototype", "Facade"],
        1,
        "Observer defines a one-to-many dependency between objects."
    ),

    _advanced_java_question(
        "Which design pattern allows an algorithm to be selected at runtime?",
        ["Strategy", "Singleton", "Adapter", "Proxy"],
        0,
        "Strategy encapsulates interchangeable algorithms behind a common interface."
    ),

    _advanced_java_question(
        "What is the main purpose of the Builder pattern?",
        ["Create complex objects step by step",
         "Restrict inheritance", "Synchronize threads", "Manage memory"],
        0,
        "Builder separates complex object construction from its representation."
    ),

    _advanced_java_question(
        "Which SOLID principle states that a class should have only one reason to change?",
        ["Open/Closed Principle", "Single Responsibility Principle",
         "Liskov Substitution Principle", "Dependency Inversion Principle"],
        1,
        "Single Responsibility Principle assigns a focused responsibility to each class."
    ),

    _advanced_java_question(
        "What does the Open/Closed Principle state?",
        ["Classes should never be instantiated",
         "Software entities should be open for extension but closed for modification",
         "All methods must be static", "Inheritance must always be avoided"],
        1,
        "The Open/Closed Principle encourages extending behavior without modifying stable existing code."
    ),

    _advanced_java_question(
        "Which pattern converts one interface into another expected by a client?",
        ["Adapter", "Observer", "Singleton", "Command"],
        0,
        "Adapter allows incompatible interfaces to work together."
    ),

    _advanced_java_question(
        "What is dependency injection?",
        ["Creating all dependencies inside a class",
         "Providing an object's dependencies externally",
         "Deleting unused objects", "Converting classes into interfaces"],
        1,
        "Dependency injection supplies dependencies from outside instead of constructing them internally."
    ),

    _advanced_java_question(
        "Which principle suggests depending on abstractions rather than concrete implementations?",
        ["DRY", "Dependency Inversion Principle", "YAGNI", "KISS"],
        1,
        "Dependency Inversion Principle reduces coupling by making high-level and low-level modules depend on abstractions."
    ),

    # 61–70: JDBC, Database and Transactions

    _advanced_java_question(
        "Which JDBC interface is used to execute parameterized SQL queries?",
        ["Statement", "PreparedStatement", "ResultSet", "DatabaseMetaData"],
        1,
        "PreparedStatement supports parameterized SQL and helps prevent SQL injection when used correctly."
    ),

    _advanced_java_question(
        "Which ResultSet method moves the cursor to the next row?",
        ["move()", "next()", "forward()", "fetch()"],
        1,
        "ResultSet.next() moves the cursor to the next row."
    ),

    _advanced_java_question(
        "Which JDBC method disables automatic transaction commits?",
        ["commit()", "rollback()", "setAutoCommit(false)", "close()"],
        2,
        "setAutoCommit(false) allows transactions to be committed or rolled back explicitly."
    ),

    _advanced_java_question(
        "What is the purpose of Connection.rollback()?",
        ["Save transaction changes", "Undo uncommitted transaction changes",
         "Close the database", "Create a new connection"],
        1,
        "rollback() undoes changes made in the current uncommitted transaction."
    ),

    _advanced_java_question(
        "Which JDBC interface provides information about database columns and tables?",
        ["ResultSet", "DatabaseMetaData", "CallableStatement", "Driver"],
        1,
        "DatabaseMetaData provides information about database capabilities, tables and columns."
    ),

    _advanced_java_question(
        "Which JDBC interface is used to call stored procedures?",
        ["PreparedStatement", "CallableStatement", "Statement", "ResultSet"],
        1,
        "CallableStatement is designed for executing stored procedures."
    ),

    _advanced_java_question(
        "Which transaction isolation level prevents dirty reads but allows non-repeatable reads?",
        ["READ_UNCOMMITTED", "READ_COMMITTED", "REPEATABLE_READ", "SERIALIZABLE"],
        1,
        "READ_COMMITTED prevents dirty reads but does not prevent non-repeatable reads."
    ),

    _advanced_java_question(
        "What is connection pooling?",
        ["Creating a new database for every query",
         "Reusing a managed pool of database connections",
         "Encrypting database passwords", "Deleting inactive tables"],
        1,
        "Connection pooling reduces connection creation overhead by reusing connections."
    ),

    _advanced_java_question(
        "Which ACID property guarantees that a transaction is completed entirely or not at all?",
        ["Consistency", "Isolation", "Atomicity", "Durability"],
        2,
        "Atomicity ensures all-or-nothing transaction execution."
    ),

    _advanced_java_question(
        "What is the purpose of a Batch in JDBC?",
        ["Execute multiple SQL operations together",
         "Create Java threads", "Encrypt query results", "Load Java classes"],
        0,
        "JDBC batching groups multiple SQL statements or parameter sets for more efficient execution."
    ),

    # 71–80: Serialization, Reflection and Advanced APIs

    _advanced_java_question(
        "Which interface is required for standard Java object serialization?",
        ["Cloneable", "Serializable", "Comparable", "Runnable"],
        1,
        "Serializable is a marker interface indicating that objects may be serialized."
    ),

    _advanced_java_question(
        "What is the purpose of serialVersionUID?",
        ["Identify the serialization version of a class",
         "Identify a running thread", "Store object hash codes", "Create unique database IDs"],
        0,
        "serialVersionUID is used during deserialization to verify class compatibility."
    ),

    _advanced_java_question(
        "Which keyword prevents a field from being serialized by default?",
        ["static", "final", "transient", "volatile"],
        2,
        "Transient fields are excluded from default Java serialization."
    ),

    _advanced_java_question(
        "Which Java API provides runtime inspection of classes, fields and methods?",
        ["Reflection API", "Stream API", "Collections API", "Logging API"],
        0,
        "Reflection allows runtime inspection and interaction with class members."
    ),

    _advanced_java_question(
        "Which method obtains the runtime Class object from an existing object?",
        ["getClass()", "getType()", "classOf()", "getObject()"],
        0,
        "Object.getClass() returns the runtime Class object of an instance."
    ),

    _advanced_java_question(
        "Which interface allows an object to define a custom cloning operation?",
        ["Serializable", "Cloneable", "AutoCloseable", "Comparator"],
        1,
        "Cloneable is a marker interface associated with Object.clone()."
    ),

    _advanced_java_question(
        "What is the primary difference between shallow copy and deep copy?",
        ["Shallow copy duplicates referenced objects recursively",
         "Deep copy duplicates nested mutable objects, while shallow copy shares references",
         "Both are always identical", "Shallow copy is impossible in Java"],
        1,
        "A shallow copy shares references to nested objects, while a deep copy duplicates them."
    ),

    _advanced_java_question(
        "Which interface allows an object to be used with try-with-resources?",
        ["Serializable", "AutoCloseable", "Cloneable", "Comparator"],
        1,
        "AutoCloseable defines close() and supports try-with-resources."
    ),

    _advanced_java_question(
        "Which Java API is commonly used for date and time operations since Java 8?",
        ["java.util.Date only", "java.time", "java.sql only", "java.clock"],
        1,
        "The java.time package provides modern immutable date and time classes."
    ),

    _advanced_java_question(
        "Which class represents an immutable date without a time or time zone?",
        ["LocalDate", "LocalDateTime", "ZonedDateTime", "Instant"],
        0,
        "LocalDate represents a calendar date without time or time zone."
    ),

    # 81–90: Networking, I/O and NIO

    _advanced_java_question(
        "Which class represents a TCP client socket?",
        ["ServerSocket", "Socket", "DatagramSocket", "URLClassLoader"],
        1,
        "Socket represents the client endpoint of a TCP connection."
    ),

    _advanced_java_question(
        "Which Java class is used to create a TCP server socket?",
        ["Socket", "ServerSocket", "DatagramPacket", "URLConnection"],
        1,
        "ServerSocket listens for and accepts incoming TCP connections."
    ),

    _advanced_java_question(
        "Which protocol is connectionless and does not guarantee packet delivery?",
        ["TCP", "HTTP", "UDP", "FTP"],
        2,
        "UDP is connectionless and does not guarantee delivery or ordering."
    ),

    _advanced_java_question(
        "Which NIO component represents a buffer for reading and writing data?",
        ["Channel", "Buffer", "Selector", "Path"],
        1,
        "Buffer stores data and provides operations such as put(), get(), flip() and clear()."
    ),

    _advanced_java_question(
        "What does the flip() method do in a Java NIO Buffer?",
        ["Deletes the buffer", "Switches from writing mode to reading mode",
         "Increases buffer capacity", "Closes the channel"],
        1,
        "flip() sets the limit to the current position and resets the position to zero for reading."
    ),

    _advanced_java_question(
        "What is the purpose of a Selector in Java NIO?",
        ["Monitor multiple selectable channels using a single thread",
         "Create database queries", "Serialize objects", "Manage garbage collection"],
        0,
        "Selector enables multiplexed I/O by monitoring multiple selectable channels."
    ),

    _advanced_java_question(
        "Which class represents a file system path in modern Java NIO?",
        ["FileReader", "Path", "BufferedReader", "FileWriter"],
        1,
        "Path represents a file or directory location in the file system."
    ),

    _advanced_java_question(
        "Which method reads all bytes from a file into a byte array?",
        ["Files.readAllBytes()", "Files.write()", "Files.copy()", "Files.delete()"],
        0,
        "Files.readAllBytes() reads file contents into a byte array."
    ),

    _advanced_java_question(
        "What is the main advantage of BufferedInputStream?",
        ["It encrypts data", "It reduces underlying read operations using buffering",
         "It creates network connections", "It compresses Java classes"],
        1,
        "BufferedInputStream uses an internal buffer to reduce direct input operations."
    ),

    _advanced_java_question(
        "Which class supports asynchronous file channel operations?",
        ["FileReader", "AsynchronousFileChannel", "BufferedWriter", "Scanner"],
        1,
        "AsynchronousFileChannel supports asynchronous file I/O operations."
    ),

    # 91–100: Modern Java, Modules, Security and Performance

    _advanced_java_question(
        "Which feature was introduced in Java 9 to organize applications into modules?",
        ["Lambda expressions", "Java Platform Module System",
         "Records", "Virtual threads"],
        1,
        "JPMS introduced modularization with module-info.java in Java 9."
    ),

    _advanced_java_question(
        "Which keyword declares a module in module-info.java?",
        ["package", "module", "namespace", "import"],
        1,
        "The module keyword declares a Java module."
    ),

    _advanced_java_question(
        "Which keyword allows a module to make a package accessible to other modules?",
        ["requires", "exports", "opens", "uses"],
        1,
        "exports makes a package accessible to other modules at compile time and runtime."
    ),

    _advanced_java_question(
        "What is a Java record primarily intended for?",
        ["Creating mutable thread pools",
         "Declaring concise data-carrier classes",
         "Managing database connections", "Replacing interfaces"],
        1,
        "Records provide a concise syntax for immutable data-carrier classes."
    ),

    _advanced_java_question(
        "Which Java feature allows a type to restrict its permitted subclasses?",
        ["Sealed classes", "Anonymous classes", "Inner classes", "Abstract classes"],
        0,
        "Sealed classes use permits to control which classes can extend or implement them."
    ),

    _advanced_java_question(
        "What is the main purpose of virtual threads?",
        ["Increase object size", "Support large numbers of concurrent tasks with lightweight threads",
         "Replace garbage collection", "Eliminate all synchronization"],
        1,
        "Virtual threads are lightweight threads designed to simplify high-concurrency applications."
    ),

    _advanced_java_question(
        "Which Java class provides a high-resolution monotonic time source?",
        ["System.currentTimeMillis()", "System.nanoTime()",
         "LocalDate.now()", "Calendar.getInstance()"],
        1,
        "System.nanoTime() is intended for measuring elapsed time."
    ),

    _advanced_java_question(
        "Which API provides cryptographic message digest functionality?",
        ["MessageDigest", "StringBuilder", "ObjectStream", "FileChannel"],
        0,
        "MessageDigest supports cryptographic hash functions such as SHA-256."
    ),

    _advanced_java_question(
        "Which class is commonly used to generate cryptographically strong random values?",
        ["Random", "Math", "SecureRandom", "ThreadLocal"],
        2,
        "SecureRandom provides cryptographically strong random number generation."
    ),

    _advanced_java_question(
        "What is the primary purpose of the Java Flight Recorder?",
        ["Compile source code", "Collect runtime diagnostic and performance data",
         "Create database tables", "Generate Java documentation"],
        1,
        "Java Flight Recorder collects detailed runtime events for performance analysis and troubleshooting."
    ),

]

