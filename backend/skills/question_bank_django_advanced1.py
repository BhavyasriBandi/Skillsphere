
QUESTION_BANK_DJANGO_ADVANCED1 = [
    {
        "skill": "Django / REST APIs",
        "difficulty": "advanced",
        "questions": [
            {
                "question_text": "What is the N+1 query problem in Django ORM?",
                "options": ["One initial query followed by an additional query for each related object", "Executing one query for the entire database", "Running migrations repeatedly", "Creating duplicate primary keys"],
                "correct_answer": 0,
                "explanation": "The N+1 problem occurs when related objects are fetched through repeated queries instead of being loaded efficiently."
            },
            {
                "question_text": "Which ORM technique is generally appropriate for optimizing ForeignKey access?",
                "options": ["select_related()", "prefetch_related() only", "bulk_create()", "values_list() only"],
                "correct_answer": 0,
                "explanation": "select_related() uses SQL joins to load single-valued relationships such as ForeignKey and OneToOneField."
            },
            {
                "question_text": "Which ORM technique is generally appropriate for optimizing many-to-many relationship access?",
                "options": ["prefetch_related()", "select_related() only", "get_or_create()", "update_fields()"],
                "correct_answer": 0,
                "explanation": "prefetch_related() loads multi-valued relationships using additional queries and joins the results in Python."
            },
            {
                "question_text": "What is the main benefit of QuerySet.defer()?",
                "options": ["Avoid loading selected model fields until accessed", "Delete selected fields from the database", "Disable database transactions", "Convert a QuerySet into JSON"],
                "correct_answer": 0,
                "explanation": "defer() postpones loading specified fields, which can reduce the initial query data."
            },
            {
                "question_text": "What does QuerySet.only() do?",
                "options": ["Initially loads only the specified fields and the required primary key", "Deletes all fields except the specified fields", "Returns only one database row", "Locks every selected row"],
                "correct_answer": 0,
                "explanation": "only() limits the fields initially loaded; deferred fields are fetched if later accessed."
            },
            {
                "question_text": "What is the purpose of select_for_update() inside a transaction?",
                "options": ["Lock selected rows against concurrent updates until the transaction ends", "Create a new database index", "Prevent all SELECT queries", "Convert a table into a view"],
                "correct_answer": 0,
                "explanation": "select_for_update() requests row-level locks on supported databases when used inside a transaction."
            },
            {
                "question_text": "Why should select_for_update() generally be used inside transaction.atomic()?",
                "options": ["The row lock must be held within a database transaction", "It automatically creates migrations", "It disables ORM caching", "It converts the query into a POST request"],
                "correct_answer": 0,
                "explanation": "The database lock is associated with the transaction and is released when that transaction ends."
            },
            {
                "question_text": "What is a database transaction's atomicity property?",
                "options": ["All operations succeed together or are rolled back together", "Every query runs without a database connection", "All records are automatically encrypted", "Queries are always executed in alphabetical order"],
                "correct_answer": 0,
                "explanation": "Atomicity ensures that a transaction is treated as one indivisible unit."
            },
            {
                "question_text": "What is the purpose of transaction.on_commit() in Django?",
                "options": ["Run a callback only after a successful database commit", "Run a callback before every SQL query", "Rollback a committed transaction", "Create a database connection"],
                "correct_answer": 0,
                "explanation": "on_commit() registers a callback that executes after the outer transaction successfully commits."
            },
            {
                "question_text": "What is a race condition in database-backed Django code?",
                "options": ["The result depends on the timing of concurrent operations", "A model has too many fields", "A URL contains a query parameter", "A serializer returns JSON"],
                "correct_answer": 0,
                "explanation": "Race conditions occur when concurrent operations interact in an order that can produce incorrect or inconsistent results."
            },
            {
                "question_text": "Which Django ORM expression can atomically increment a numeric field in the database?",
                "options": ["F() expression", "Q() expression", "ValueError()", "HttpResponse()"],
                "correct_answer": 0,
                "explanation": "F() expressions let the database perform calculations using the current field value."
            },
            {
                "question_text": "What is the purpose of a database index?",
                "options": ["Improve lookup performance for suitable queries", "Guarantee that every query is faster", "Encrypt table records", "Automatically validate API permissions"],
                "correct_answer": 0,
                "explanation": "Indexes can speed up reads for indexed fields, with storage and write-performance trade-offs."
            },
            {
                "question_text": "What is a trade-off of adding many database indexes?",
                "options": ["Additional storage and slower writes or updates", "Automatic removal of foreign keys", "Elimination of all database locks", "Guaranteed faster inserts"],
                "correct_answer": 0,
                "explanation": "Indexes consume storage and must be maintained when indexed data changes."
            },
            {
                "question_text": "What is the purpose of QuerySet.explain()?",
                "options": ["Inspect the database execution plan for a query", "Explain a serializer field to a user", "Generate API documentation", "Display Django migration history"],
                "correct_answer": 0,
                "explanation": "explain() returns the database query plan, helping diagnose query performance."
            },
            {
                "question_text": "What is a composite database index?",
                "options": ["An index involving multiple fields", "An index stored only in Python memory", "A table without a primary key", "A relationship between two serializers"],
                "correct_answer": 0,
                "explanation": "A composite index covers multiple columns and can help queries filtering or ordering by those columns."
            },
            {
                "question_text": "What is the purpose of UniqueConstraint in Django model Meta constraints?",
                "options": ["Enforce uniqueness across one or more fields or expressions", "Automatically encrypt model fields", "Create a REST API endpoint", "Prevent all database reads"],
                "correct_answer": 0,
                "explanation": "UniqueConstraint enforces a uniqueness rule at the database level."
            },
            {
                "question_text": "What is the purpose of CheckConstraint in Django?",
                "options": ["Enforce a condition on values stored in the database", "Check whether an API URL exists", "Validate only HTML form labels", "Check the Python interpreter version"],
                "correct_answer": 0,
                "explanation": "CheckConstraint adds a database-level condition that stored rows must satisfy."
            },
            {
                "question_text": "What is the main benefit of using database-level constraints in addition to serializer validation?",
                "options": ["They protect data integrity even when writes bypass the API serializer", "They automatically create frontend forms", "They replace authentication", "They guarantee zero database latency"],
                "correct_answer": 0,
                "explanation": "Database constraints enforce integrity for writes from different application paths and concurrent requests."
            },
            {
                "question_text": "What is the purpose of a custom Django model manager?",
                "options": ["Encapsulate reusable database query behavior", "Define browser-side event handlers", "Generate JWT signatures", "Configure HTTP response headers only"],
                "correct_answer": 0,
                "explanation": "Custom managers provide reusable methods for querying model objects."
            },
            {
                "question_text": "What is the purpose of a custom QuerySet method?",
                "options": ["Provide reusable query operations that can be chained", "Modify the Python interpreter", "Create API authentication headers", "Replace database migrations"],
                "correct_answer": 0,
                "explanation": "Custom QuerySet methods package reusable filtering and query logic."
            },
            {
                "question_text": "What does a DRF throttling scope identify?",
                "options": ["A named request-rate policy that can be configured separately", "A database schema", "A serializer relationship", "A URL namespace"],
                "correct_answer": 0,
                "explanation": "Throttling scopes allow different rate limits for different categories of API actions."
            },
            {
                "question_text": "Which DRF throttling class is commonly used to apply different rates to anonymous and authenticated users?",
                "options": ["AnonRateThrottle", "IsAdminUser", "JSONRenderer", "SessionAuthentication"],
                "correct_answer": 0,
                "explanation": "AnonRateThrottle applies a rate limit to unauthenticated users."
            },
            {
                "question_text": "What is the purpose of ScopedRateThrottle in DRF?",
                "options": ["Apply rate limits according to a view's throttle scope", "Restrict access to database tables", "Validate nested serializers", "Generate API schemas"],
                "correct_answer": 0,
                "explanation": "ScopedRateThrottle uses a view's throttle_scope to select the configured rate."
            },
            {
                "question_text": "Why should DRF throttling not be treated as a complete defense against denial-of-service attacks?",
                "options": ["Its rate calculations and cache behavior are not a complete infrastructure-level security boundary", "It encrypts all requests", "It blocks every network packet", "It prevents all database writes"],
                "correct_answer": 0,
                "explanation": "Application throttling is useful for usage control but should be combined with infrastructure-level protections."
            },
            {
                "question_text": "What is the purpose of a custom DRF permission class?",
                "options": ["Implement application-specific access rules", "Automatically serialize every model", "Create database indexes", "Configure static file storage"],
                "correct_answer": 0,
                "explanation": "Custom permission classes implement rules beyond the built-in permission classes."
            },
            {
                "question_text": "Which method is commonly implemented in a custom DRF permission class for general request-level checks?",
                "options": ["has_permission()", "get_queryset()", "to_representation()", "perform_create()"],
                "correct_answer": 0,
                "explanation": "has_permission() determines whether a request may access the view."
            },
            {
                "question_text": "Which method is commonly implemented for object-specific checks in a custom DRF permission class?",
                "options": ["has_object_permission()", "has_serializer_permission()", "get_object_queryset()", "validate_object_field()"],
                "correct_answer": 0,
                "explanation": "has_object_permission() checks whether a request may access a particular object."
            },
            {
                "question_text": "What is the purpose of perform_create() in a DRF generic view?",
                "options": ["Customize how a validated serializer is saved during creation", "Customize URL routing", "Override database migration generation", "Configure response rendering"],
                "correct_answer": 0,
                "explanation": "perform_create() is a hook that can customize serializer saving, such as assigning the current user."
            },
            {
                "question_text": "What is the purpose of perform_update() in a DRF generic view?",
                "options": ["Customize saving behavior during an update", "Create a new URL router", "Change the database engine", "Authenticate every anonymous user"],
                "correct_answer": 0,
                "explanation": "perform_update() provides a hook for customizing how an updated serializer is saved."
            },
            {
                "question_text": "What does get_permissions() allow a DRF view to do?",
                "options": ["Choose permission instances dynamically for a request or action", "Choose database indexes dynamically", "Generate serializer fields from URLs", "Change the HTTP method"],
                "correct_answer": 0,
                "explanation": "Overriding get_permissions() allows permission policies to vary by action or request."
            },
            {
                "question_text": "What is the purpose of a custom DRF exception handler?",
                "options": ["Customize how API exceptions are converted into responses", "Change database transaction isolation", "Create model migrations", "Generate user passwords"],
                "correct_answer": 0,
                "explanation": "A custom exception handler can standardize or enrich API error responses."
            },
            {
                "question_text": "What is the purpose of content negotiation in a DRF API?",
                "options": ["Select an appropriate renderer for the response", "Select the database user", "Choose a model's primary key", "Determine the user's password strength"],
                "correct_answer": 0,
                "explanation": "Content negotiation selects the response renderer based on the request and available renderers."
            },
            {
                "question_text": "What is the purpose of a DRF versioning scheme?",
                "options": ["Allow APIs to expose and distinguish different API versions", "Track Python package versions only", "Automatically migrate database tables", "Encrypt API responses"],
                "correct_answer": 0,
                "explanation": "API versioning lets clients use defined versions while an API evolves."
            },
            {
                "question_text": "What is the purpose of namespace versioning in DRF?",
                "options": ["Determine the API version from the URL namespace", "Determine the database schema version", "Read the version from a JWT signature", "Choose a serializer field type"],
                "correct_answer": 0,
                "explanation": "NamespaceVersioning uses the URL namespace to identify the API version."
            },
            {
                "question_text": "What is the purpose of schema generation in DRF?",
                "options": ["Describe API operations, parameters, and request and response formats", "Create database indexes", "Generate Django model migrations", "Encrypt API tokens"],
                "correct_answer": 0,
                "explanation": "API schemas describe an API's interface and can power documentation tools."
            },
            {
                "question_text": "What is OpenAPI commonly used for?",
                "options": ["Describe HTTP APIs in a machine-readable format", "Define Python package dependencies", "Store relational database records", "Manage browser cookies"],
                "correct_answer": 0,
                "explanation": "OpenAPI provides a standard description format for HTTP APIs."
            },
            {
                "question_text": "What is the purpose of idempotency in an API operation?",
                "options": ["Repeated identical requests have the same intended effect as one request", "Every request creates a new record", "The server always returns the same status code", "The API never modifies data"],
                "correct_answer": 0,
                "explanation": "An idempotent operation has the same intended server-side effect when repeated with the same input."
            },
            {
                "question_text": "Which HTTP method is defined as idempotent when used according to its standard semantics?",
                "options": ["PUT", "POST", "CONNECT", "PATCH in every possible implementation"],
                "correct_answer": 0,
                "explanation": "PUT is defined as idempotent, while POST is not generally idempotent."
            },
            {
                "question_text": "What is the purpose of an idempotency key for a payment-style API request?",
                "options": ["Help prevent duplicate processing when a client retries a request", "Encrypt the user's payment card", "Create a new database table", "Replace API authentication"],
                "correct_answer": 0,
                "explanation": "A server can use an idempotency key to recognize retries and avoid repeating the same operation."
            },
            {
                "question_text": "What is the purpose of a correlation ID in distributed API systems?",
                "options": ["Trace related requests across services and logs", "Identify a database primary key type", "Store a user's password", "Select a serializer automatically"],
                "correct_answer": 0,
                "explanation": "Correlation IDs help associate logs and events belonging to the same request flow."
            },
            {
                "question_text": "What is the purpose of structured logging in a Django API?",
                "options": ["Record log events with consistent fields that can be searched and analyzed", "Serialize database models", "Create API routes", "Automatically retry every failed request"],
                "correct_answer": 0,
                "explanation": "Structured logs make application events easier to filter, correlate, and analyze."
            },
            {
                "question_text": "What is a common benefit of caching read-heavy API responses?",
                "options": ["Reduce repeated computation and database access", "Guarantee that data is always fresh", "Remove the need for authentication", "Prevent all concurrent requests"],
                "correct_answer": 0,
                "explanation": "Caching can reduce repeated work, although invalidation and freshness must be handled carefully."
            },
            {
                "question_text": "What is cache invalidation?",
                "options": ["Removing or refreshing cached data when it is no longer valid", "Encrypting cached data automatically", "Creating a database migration", "Disabling HTTP responses"],
                "correct_answer": 0,
                "explanation": "Cache invalidation keeps cached values from being used after their underlying data changes."
            },
            {
                "question_text": "What is the purpose of a cache key?",
                "options": ["Identify a particular cached value", "Identify a Python class constructor", "Define a database foreign key", "Sign a JWT token"],
                "correct_answer": 0,
                "explanation": "A cache key uniquely identifies the cached entry to retrieve, update, or invalidate."
            },
            {
                "question_text": "What is a common risk of caching personalized API responses under a shared cache key?",
                "options": ["One user's data may be served to another user", "The database automatically deletes all users", "The API becomes a GraphQL endpoint", "The serializer stops validating data"],
                "correct_answer": 0,
                "explanation": "Cache keys must account for user-specific context to avoid leaking personalized responses."
            },
            {
                "question_text": "What is the purpose of a background task queue in a Django application?",
                "options": ["Run time-consuming work outside the request-response cycle", "Replace the Django ORM", "Create URL patterns automatically", "Store all API responses in browser memory"],
                "correct_answer": 0,
                "explanation": "Background workers can process tasks such as email delivery without keeping the HTTP request open."
            },
            {
                "question_text": "Why is sending a large email campaign directly inside an API request often undesirable?",
                "options": ["It can make the request slow and increase timeout risk", "Email cannot be sent from Python", "Django does not support HTTP requests", "It automatically disables database transactions"],
                "correct_answer": 0,
                "explanation": "Long-running work is usually better handled asynchronously so the API can respond promptly."
            },
            {
                "question_text": "What is the purpose of a task retry policy in a background worker?",
                "options": ["Retry eligible tasks after transient failures", "Repeat every successful task forever", "Delete tasks before execution", "Disable exception handling"],
                "correct_answer": 0,
                "explanation": "Retries can recover from temporary failures, but should be bounded and designed to avoid duplicate side effects."
            },
            {
                "question_text": "What is the transactional outbox pattern used for?",
                "options": ["Reliably record an event in the same database transaction as a business change for later publication", "Store uploaded files in a static directory", "Replace database indexes with messages", "Automatically encrypt every HTTP response"],
                "correct_answer": 0,
                "explanation": "The outbox pattern helps avoid losing events when database updates and message publication cannot be committed atomically together."
            },
            {
                "question_text": "What is the purpose of Django's signal dispatch_uid argument?",
                "options": ["Help prevent the same receiver from being registered more than once", "Identify a database transaction", "Set a user's primary key", "Generate a JWT refresh token"],
                "correct_answer": 0,
                "explanation": "dispatch_uid provides a unique identifier for a signal receiver registration."
            },
            {
                "question_text": "Why should Django signal handlers generally be kept focused and lightweight?",
                "options": ["Hidden side effects and slow operations can make application behavior harder to reason about", "Signals cannot access model instances", "Signals only work with HTML templates", "Signals automatically disable transactions"],
                "correct_answer": 0,
                "explanation": "Signals can introduce implicit behavior, so complex workflows are often clearer in explicit service functions."
            },
            {
                "question_text": "What is the purpose of a service layer in a Django application?",
                "options": ["Organize reusable business logic separately from HTTP views", "Replace the database with HTML files", "Store all settings in serializers", "Automatically create API documentation"],
                "correct_answer": 0,
                "explanation": "A service layer can keep business operations reusable and easier to test independently of views."
            },
            {
                "question_text": "What is the purpose of dependency injection in application design?",
                "options": ["Provide dependencies to a component rather than having it construct them directly", "Automatically delete unused database tables", "Convert HTTP methods into model fields", "Generate random API endpoints"],
                "correct_answer": 0,
                "explanation": "Dependency injection reduces tight coupling and makes components easier to test and replace."
            },
            {
                "question_text": "What is the purpose of a database connection pool?",
                "options": ["Reuse a managed set of database connections", "Cache every SQL result permanently", "Create a separate database for each request", "Replace transaction management"],
                "correct_answer": 0,
                "explanation": "Connection pooling reduces the overhead of repeatedly opening and closing database connections."
            },
            {
                "question_text": "What is the purpose of a health-check endpoint?",
                "options": ["Report whether an application or its dependencies are functioning", "Return every user password", "Create database migrations", "Expose all internal configuration values"],
                "correct_answer": 0,
                "explanation": "Health checks help monitoring systems determine whether an application is ready or healthy."
            },
            {
                "question_text": "What is the difference between liveness and readiness checks?",
                "options": ["Liveness checks whether a process should be restarted; readiness checks whether it can receive traffic", "Both always mean the database is writable", "Readiness checks Python syntax while liveness checks CSS", "Liveness is only for frontend applications"],
                "correct_answer": 0,
                "explanation": "Liveness indicates whether an application is alive; readiness indicates whether it is prepared to serve requests."
            }
        ]
    }
]
