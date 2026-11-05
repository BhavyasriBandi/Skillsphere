
QUESTION_BANK_DJANGO_ADVANCED2 = [
    {
        "skill": "Django / REST APIs",
        "difficulty": "advanced",
        "questions": [
            {
                "question_text": "What is the purpose of a custom DRF serializer field?",
                "options": ["Implement specialized input validation or output representation for a field", "Create a database table automatically", "Replace all API views", "Configure Django middleware"],
                "correct_answer": 0,
                "explanation": "Custom serializer fields allow developers to define specialized representation and parsing behavior."
            },
            {
                "question_text": "Which method is commonly overridden when implementing a custom DRF Field for converting primitive input into an internal value?",
                "options": ["to_internal_value()", "get_queryset()", "perform_destroy()", "get_permissions()"],
                "correct_answer": 0,
                "explanation": "to_internal_value() converts incoming primitive data into the field's internal Python value."
            },
            {
                "question_text": "Which method is commonly overridden in a custom DRF Field to convert an internal value into output data?",
                "options": ["to_representation()", "to_internal_value()", "get_object()", "perform_update()"],
                "correct_answer": 0,
                "explanation": "to_representation() converts an internal value into a primitive representation for the response."
            },
            {
                "question_text": "What is the purpose of ListSerializer in Django REST Framework?",
                "options": ["Handle serialization and validation of multiple objects", "Define database indexes", "Authenticate multiple users", "Create URL namespaces"],
                "correct_answer": 0,
                "explanation": "ListSerializer is used when a serializer is instantiated with many=True."
            },
            {
                "question_text": "What does the many=True option enable for a ModelSerializer?",
                "options": ["Serialize or validate a collection of model instances or input items", "Automatically create many database tables", "Skip validation for every item", "Enable many database connections"],
                "correct_answer": 0,
                "explanation": "many=True wraps the serializer in a ListSerializer to process a collection."
            },
            {
                "question_text": "What must commonly be customized to support bulk creation with a DRF ListSerializer?",
                "options": ["The ListSerializer create() method", "The Django URL resolver", "The model __str__() method", "The authentication header"],
                "correct_answer": 0,
                "explanation": "A custom ListSerializer create() can define how multiple validated items are saved, often using bulk_create()."
            },
            {
                "question_text": "What is the purpose of a nested writable serializer?",
                "options": ["Create or update related objects using nested input data", "Display related objects without accepting input", "Create database indexes automatically", "Replace authentication classes"],
                "correct_answer": 0,
                "explanation": "Writable nested serializers support creating or updating related objects and usually require explicit persistence logic."
            },
            {
                "question_text": "Why may a writable nested serializer require an overridden create() method?",
                "options": ["The application must define how nested related objects are saved", "DRF cannot validate nested data", "Django models cannot have relationships", "The serializer must create URL patterns"],
                "correct_answer": 0,
                "explanation": "The default ModelSerializer create behavior does not automatically handle every writable nested relationship."
            },
            {
                "question_text": "What is the purpose of a serializer's partial update mode?",
                "options": ["Allow clients to submit only fields they want to change", "Skip authentication and permissions", "Delete unspecified model fields", "Disable database constraints"],
                "correct_answer": 0,
                "explanation": "Partial updates allow omitted required fields to remain unchanged."
            },
            {
                "question_text": "What is the purpose of a custom BasePermission class in DRF?",
                "options": ["Define reusable request-level and object-level access rules", "Generate SQL migrations", "Render HTML templates", "Create database connections"],
                "correct_answer": 0,
                "explanation": "A custom permission class encapsulates application-specific authorization logic."
            },
            {
                "question_text": "What is a security risk of filtering a user's records only in the frontend?",
                "options": ["Users may still access other records by calling the API directly", "The frontend automatically encrypts the database", "Django disables all authentication", "The API cannot return JSON"],
                "correct_answer": 0,
                "explanation": "Access restrictions must be enforced on the server, not just by hiding records in the interface."
            },
            {
                "question_text": "What is the purpose of restricting a queryset to request.user in a DRF view?",
                "options": ["Limit the records returned or accessed to those belonging to the current user", "Automatically create a new user", "Disable object permissions", "Change the database engine"],
                "correct_answer": 0,
                "explanation": "User-scoped querysets help prevent unauthorized access to other users' records."
            },
            {
                "question_text": "What is an insecure direct object reference (IDOR) vulnerability?",
                "options": ["A user accesses another user's object by manipulating an identifier without proper authorization checks", "A database query uses an index", "A serializer contains a read-only field", "An API uses pagination"],
                "correct_answer": 0,
                "explanation": "IDOR occurs when the server fails to enforce authorization for objects referenced by client-controlled identifiers."
            },
            {
                "question_text": "Why should sensitive fields such as password hashes be excluded from ordinary API responses?",
                "options": ["To reduce exposure of sensitive authentication data", "To make JSON arrays shorter only", "To enable pagination", "To improve URL routing"],
                "correct_answer": 0,
                "explanation": "Sensitive authentication data should not be exposed unnecessarily, even when it is hashed."
            },
            {
                "question_text": "What is the purpose of rotating JWT signing keys?",
                "options": ["Replace signing keys periodically while managing token verification during transition", "Change every user's database ID", "Automatically refresh all browser pages", "Remove API permissions"],
                "correct_answer": 0,
                "explanation": "Key rotation limits long-term reliance on one key and requires a safe verification transition strategy."
            },
            {
                "question_text": "What is a JWT token revocation strategy?",
                "options": ["Prevent a previously issued token from being accepted before its natural expiration", "Increase the token's expiration indefinitely", "Change the token's JSON formatting", "Store every token in a frontend component"],
                "correct_answer": 0,
                "explanation": "Revocation mechanisms such as token blacklists can invalidate tokens before their expiry."
            },
            {
                "question_text": "What is the purpose of refresh-token rotation?",
                "options": ["Issue a new refresh token when one is used and invalidate the previous token", "Use the same refresh token forever", "Replace the access token with a password", "Disable token expiration"],
                "correct_answer": 0,
                "explanation": "Refresh-token rotation reduces the usefulness of stolen refresh tokens and can help detect reuse."
            },
            {
                "question_text": "Why should JWT expiration be validated by an API?",
                "options": ["To reject tokens that are no longer valid for authentication", "To increase the token payload size", "To create a database migration", "To enable CORS automatically"],
                "correct_answer": 0,
                "explanation": "Expiration validation prevents an expired token from being accepted as a valid credential."
            },
            {
                "question_text": "What is the purpose of HTTPS for an authenticated REST API?",
                "options": ["Protect data in transit using TLS", "Encrypt database backups automatically", "Replace API permissions", "Prevent all application bugs"],
                "correct_answer": 0,
                "explanation": "HTTPS protects communication between clients and servers against interception and tampering in transit."
            },
            {
                "question_text": "Why should a production Django SECRET_KEY not be committed to a public source repository?",
                "options": ["Exposure can compromise security features that rely on the secret", "It makes Python syntax invalid", "It prevents migrations from running", "It disables JSON rendering"],
                "correct_answer": 0,
                "explanation": "Secrets should be managed outside source control because public exposure can enable security attacks."
            },
            {
                "question_text": "What is the purpose of environment variables in production Django configuration?",
                "options": ["Keep environment-specific settings and secrets outside source code", "Replace all Python packages", "Store every user's session in the browser", "Generate database models"],
                "correct_answer": 0,
                "explanation": "Environment variables help configure deployments without hardcoding sensitive or environment-specific values."
            },
            {
                "question_text": "What does Django's ALLOWED_HOSTS setting protect against?",
                "options": ["Host header attacks involving unexpected Host values", "SQL injection in every ORM query", "Weak user passwords", "Cross-site scripting in all templates"],
                "correct_answer": 0,
                "explanation": "ALLOWED_HOSTS validates the HTTP Host header against configured allowed hostnames."
            },
            {
                "question_text": "What is the purpose of Django's SECURE_SSL_REDIRECT setting?",
                "options": ["Redirect eligible HTTP requests to HTTPS", "Encrypt database columns", "Disable user registration", "Require JWT authentication for every request"],
                "correct_answer": 0,
                "explanation": "SECURE_SSL_REDIRECT redirects non-secure requests to HTTPS when configured appropriately."
            },
            {
                "question_text": "What is the purpose of SECURE_HSTS_SECONDS in Django?",
                "options": ["Configure the duration for which browsers should enforce HTTPS through HSTS", "Set the JWT access token lifetime", "Configure database connection timeouts", "Set the session cookie name"],
                "correct_answer": 0,
                "explanation": "HSTS tells browsers to use HTTPS for a specified period after receiving the policy."
            },
            {
                "question_text": "What is the main risk of trusting user-supplied file extensions during uploads?",
                "options": ["A file may contain unexpected or malicious content despite its extension", "The file will always be too large", "The database will automatically reject the file", "Django will convert it to JSON"],
                "correct_answer": 0,
                "explanation": "File extensions can be spoofed, so uploads need appropriate validation and safe storage."
            },
            {
                "question_text": "What is a recommended security practice for uploaded files?",
                "options": ["Validate file type and size, use safe storage, and avoid executing uploaded content", "Trust every filename supplied by the client", "Store all uploads in the application source directory", "Allow uploaded files to execute as server code"],
                "correct_answer": 0,
                "explanation": "Upload handling should validate content and size and isolate stored files from executable application code."
            },
            {
                "question_text": "What is the purpose of a Content Security Policy (CSP)?",
                "options": ["Restrict the sources from which a browser may load certain content", "Control database transaction isolation", "Validate Django model relationships", "Manage JWT refresh tokens"],
                "correct_answer": 0,
                "explanation": "CSP helps mitigate content injection attacks by restricting allowed content sources."
            },
            {
                "question_text": "What is the purpose of preventing SQL injection?",
                "options": ["Stop untrusted input from changing the structure or intent of SQL queries", "Prevent all database connection failures", "Automatically encrypt every model field", "Disable ORM filtering"],
                "correct_answer": 0,
                "explanation": "Parameterized queries and safe ORM usage help keep user input separate from SQL instructions."
            },
            {
                "question_text": "Why is using Django ORM filter arguments generally safer than building SQL with string concatenation?",
                "options": ["The ORM parameterizes values rather than treating them as SQL syntax", "The ORM disables database permissions", "The ORM automatically encrypts all query results", "The ORM prevents every possible security vulnerability"],
                "correct_answer": 0,
                "explanation": "ORM query construction safely handles values, whereas manually concatenated SQL can introduce injection vulnerabilities."
            },
            {
                "question_text": "What is the purpose of transaction isolation in a relational database?",
                "options": ["Control how concurrent transactions can observe each other's changes", "Define API response serialization", "Set the frontend development port", "Choose a Django template engine"],
                "correct_answer": 0,
                "explanation": "Isolation levels define the visibility and interaction of concurrent transactions."
            },
            {
                "question_text": "What is a deadlock in database transactions?",
                "options": ["Two or more transactions wait indefinitely for locks held by one another until the database resolves the conflict", "A query returns no rows", "A serializer contains invalid JSON", "A database index is missing"],
                "correct_answer": 0,
                "explanation": "Deadlocks occur when transactions form a cycle of lock dependencies; databases typically detect and abort one transaction."
            },
            {
                "question_text": "What is a common way to reduce deadlock risk when locking multiple rows?",
                "options": ["Acquire locks in a consistent order", "Disable all database transactions", "Use random lock ordering", "Run every query without a transaction"],
                "correct_answer": 0,
                "explanation": "Consistent lock ordering reduces circular wait conditions among concurrent transactions."
            },
            {
                "question_text": "What is the purpose of optimistic concurrency control?",
                "options": ["Detect conflicting updates rather than locking every record in advance", "Prevent all concurrent requests", "Create a separate database for every user", "Disable update operations"],
                "correct_answer": 0,
                "explanation": "Optimistic concurrency commonly uses version numbers or conditional updates to detect conflicts."
            },
            {
                "question_text": "What is the purpose of an ETag in HTTP?",
                "options": ["Provide a validator for a particular representation of a resource", "Store a user's access token", "Identify a Django model class", "Specify a database index"],
                "correct_answer": 0,
                "explanation": "ETags can support cache validation and conditional requests."
            },
            {
                "question_text": "What does the HTTP If-Match header commonly support?",
                "options": ["Perform a request only if the current entity tag matches a supplied value", "Force every request to return JSON", "Authenticate a user with a password", "Create a new database table"],
                "correct_answer": 0,
                "explanation": "If-Match supports conditional requests and can help prevent lost updates."
            },
            {
                "question_text": "What is the purpose of HTTP conditional requests?",
                "options": ["Perform operations based on validators such as ETags or modification dates", "Disable server-side validation", "Replace database transactions", "Generate API serializers"],
                "correct_answer": 0,
                "explanation": "Conditional requests can reduce unnecessary transfers and help coordinate updates."
            },
            {
                "question_text": "What is the purpose of a database migration squashing operation in Django?",
                "options": ["Combine a sequence of migrations into a more compact migration representation", "Delete all database records", "Convert a Django project into an API", "Encrypt migration files"],
                "correct_answer": 0,
                "explanation": "Migration squashing consolidates migration operations while preserving the resulting schema changes."
            },
            {
                "question_text": "Why should a data migration use historical models through the migration app registry?",
                "options": ["Historical models represent the model state at that migration point", "Current models always contain every past field", "Historical models automatically skip database constraints", "The registry creates API endpoints"],
                "correct_answer": 0,
                "explanation": "Migrations must use historical model definitions so they remain reliable as application models evolve."
            },
            {
                "question_text": "What is the purpose of RunPython in a Django migration?",
                "options": ["Execute custom Python code as part of a migration", "Run a Django development server", "Create a REST API serializer", "Compile Python source files"],
                "correct_answer": 0,
                "explanation": "RunPython supports data migrations and other custom migration-time operations."
            },
            {
                "question_text": "What is the purpose of a reversible Django data migration?",
                "options": ["Provide a reverse operation to undo the data transformation when rolling back", "Automatically restore deleted source code", "Prevent all future migrations", "Replace the database backup process"],
                "correct_answer": 0,
                "explanation": "A reversible migration defines how to reverse its data changes when possible."
            },
            {
                "question_text": "What is the purpose of a database backup before a risky schema migration?",
                "options": ["Provide a recovery path if the migration causes data loss or failure", "Automatically optimize every query", "Replace migration testing", "Disable database constraints"],
                "correct_answer": 0,
                "explanation": "A tested backup provides a recovery option for unexpected migration problems."
            },
            {
                "question_text": "What is the purpose of contract testing between API services?",
                "options": ["Verify that service interactions follow an agreed request and response contract", "Measure only database storage size", "Generate random user passwords", "Replace all integration tests"],
                "correct_answer": 0,
                "explanation": "Contract tests help detect incompatible changes between API providers and consumers."
            },
            {
                "question_text": "What is the purpose of an integration test for a Django REST API?",
                "options": ["Verify that multiple components work together through an API workflow", "Test only a single Python expression", "Measure frontend screen brightness", "Generate production secrets"],
                "correct_answer": 0,
                "explanation": "Integration tests exercise interactions such as routing, authentication, serializers, views, and persistence."
            },
            {
                "question_text": "What is the purpose of mocking an external service in a Django API unit test?",
                "options": ["Isolate the test from the real external dependency", "Change the production database schema", "Disable all application validation", "Automatically deploy the service"],
                "correct_answer": 0,
                "explanation": "Mocking allows a test to control dependency behavior without making real external calls."
            },
            {
                "question_text": "What is the purpose of testing API authorization separately from authentication?",
                "options": ["Verify both user identity and permission to perform specific actions", "Ensure every authenticated user is an administrator", "Replace serializer validation", "Disable anonymous endpoints"],
                "correct_answer": 0,
                "explanation": "Authentication identifies the user; authorization tests whether that user may access a resource or action."
            },
            {
                "question_text": "What is the purpose of load testing a Django REST API?",
                "options": ["Measure behavior and performance under expected or high request volumes", "Check only Python formatting", "Generate database migrations", "Validate HTML template syntax"],
                "correct_answer": 0,
                "explanation": "Load testing evaluates throughput, latency, and resource behavior under simulated traffic."
            },
            {
                "question_text": "What is the purpose of profiling a slow Django API endpoint?",
                "options": ["Identify where execution time or resources are being spent", "Automatically rewrite every serializer", "Remove all database indexes", "Disable logging permanently"],
                "correct_answer": 0,
                "explanation": "Profiling helps locate expensive functions, database queries, and other performance bottlenecks."
            },
            {
                "question_text": "What is the purpose of graceful shutdown in a Django application server?",
                "options": ["Allow in-flight work to finish or stop safely before the process exits", "Delete all active user accounts", "Force every request to fail immediately", "Clear the production database"],
                "correct_answer": 0,
                "explanation": "Graceful shutdown helps prevent interrupted requests and incomplete work during deployments or restarts."
            }
        ]
    }
]
