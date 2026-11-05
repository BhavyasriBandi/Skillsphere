
QUESTION_BANK_DJANGO_INTERMEDIATE1 = [
    {
        "skill": "Django / REST APIs",
        "difficulty": "intermediate",
        "questions": [
            {
                "question_text": "What is the main purpose of Django REST Framework (DRF)?",
                "options": ["Build REST APIs using Django", "Create desktop applications", "Manage operating system processes", "Compile Python programs"],
                "correct_answer": 0,
                "explanation": "DRF provides tools for building Web APIs on top of Django."
            },
            {
                "question_text": "What is a serializer in Django REST Framework?",
                "options": ["A component that converts complex data into native Python data types and validates incoming data", "A database server", "A URL router only", "A middleware replacement"],
                "correct_answer": 0,
                "explanation": "Serializers convert model instances and other complex data into representations such as JSON and validate incoming data."
            },
            {
                "question_text": "Which DRF serializer is designed to work with Django model instances?",
                "options": ["ModelSerializer", "JSONSerializerOnly", "DatabaseSerializer", "TemplateSerializer"],
                "correct_answer": 0,
                "explanation": "ModelSerializer automatically derives serializer fields and common create/update behavior from a model."
            },
            {
                "question_text": "Which class is commonly used to create a basic API view with explicit HTTP method handlers?",
                "options": ["APIView", "ModelAdmin", "TemplateView only", "AppConfig"],
                "correct_answer": 0,
                "explanation": "APIView provides a base class for handling API requests with methods such as get() and post()."
            },
            {
                "question_text": "Which DRF class provides read-only access to a collection or individual object?",
                "options": ["ReadOnlyModelViewSet", "ModelForm", "CreateAPIView", "APIViewOnly"],
                "correct_answer": 0,
                "explanation": "ReadOnlyModelViewSet provides list and retrieve actions without write operations."
            },
            {
                "question_text": "What does a DRF ViewSet primarily combine?",
                "options": ["Related API actions for a resource", "Database and operating system drivers", "HTML and CSS files", "Python package installation commands"],
                "correct_answer": 0,
                "explanation": "A ViewSet groups related actions such as list, retrieve, create, update, and destroy."
            },
            {
                "question_text": "Which DRF class provides common create, retrieve, update, and delete actions for a model?",
                "options": ["ModelViewSet", "APIView", "TemplateView", "RedirectView"],
                "correct_answer": 0,
                "explanation": "ModelViewSet provides a standard set of CRUD actions for a model-backed API."
            },
            {
                "question_text": "What is the purpose of a DRF router?",
                "options": ["Automatically generate URL patterns for ViewSets", "Create database migrations", "Encrypt passwords", "Validate model fields"],
                "correct_answer": 0,
                "explanation": "Routers generate URL patterns for registered ViewSets."
            },
            {
                "question_text": "Which DRF router is commonly used for automatic ViewSet URL configuration?",
                "options": ["DefaultRouter", "DatabaseRouter", "TemplateRouter", "AdminRouter"],
                "correct_answer": 0,
                "explanation": "DefaultRouter generates URL patterns and an API root view."
            },
            {
                "question_text": "Which attribute specifies the queryset used by a generic DRF view?",
                "options": ["queryset", "template_name", "database_url", "response_code"],
                "correct_answer": 0,
                "explanation": "The queryset attribute defines the initial set of objects used by the view."
            },
            {
                "question_text": "Which attribute specifies the serializer used by a DRF generic view?",
                "options": ["serializer_class", "model_class_only", "form_template", "request_serializer_url"],
                "correct_answer": 0,
                "explanation": "serializer_class tells the view which serializer should process and represent data."
            },
            {
                "question_text": "What is the purpose of serializer.is_valid()?",
                "options": ["Validate incoming data", "Save a database backup", "Generate URL patterns", "Authenticate a database server"],
                "correct_answer": 0,
                "explanation": "is_valid() runs serializer validation and makes validated data available."
            },
            {
                "question_text": "What does serializer.save() do after successful validation?",
                "options": ["Create or update an object using the serializer's save behavior", "Delete the serializer", "Generate a JWT automatically", "Start the development server"],
                "correct_answer": 0,
                "explanation": "save() calls create() or update() depending on whether an instance was supplied."
            },
            {
                "question_text": "Where can validated serializer input be accessed after successful validation?",
                "options": ["serializer.validated_data", "serializer.raw_html", "serializer.query_params", "serializer.url_patterns"],
                "correct_answer": 0,
                "explanation": "validated_data contains the data after serializer validation."
            },
            {
                "question_text": "Where are serializer validation errors available after validation fails?",
                "options": ["serializer.errors", "serializer.messages_only", "serializer.database", "serializer.headers"],
                "correct_answer": 0,
                "explanation": "The errors property contains validation errors."
            },
            {
                "question_text": "Which serializer option makes a field read-only?",
                "options": ["read_only=True", "editable_only=True", "readonly_field=False", "write_only=True"],
                "correct_answer": 0,
                "explanation": "read_only=True includes a field in output but prevents it from being supplied as writable input."
            },
            {
                "question_text": "What does write_only=True mean for a DRF serializer field?",
                "options": ["Accept the field as input but exclude it from output", "Display the field only in API responses", "Make the field a primary key", "Skip all validation"],
                "correct_answer": 0,
                "explanation": "Write-only fields are accepted during deserialization but omitted from serialized output."
            },
            {
                "question_text": "Which serializer option can allow a field to be omitted during deserialization?",
                "options": ["required=False", "read_only=False", "unique=True", "many=True"],
                "correct_answer": 0,
                "explanation": "required=False means the client does not have to provide the field."
            },
            {
                "question_text": "What does many=True indicate when creating a serializer?",
                "options": ["The serializer should handle a collection of objects", "The serializer should encrypt the data", "The serializer should disable validation", "The serializer should create many databases"],
                "correct_answer": 0,
                "explanation": "many=True uses a ListSerializer to handle multiple objects."
            },
            {
                "question_text": "Which DRF permission class allows access only to authenticated users?",
                "options": ["IsAuthenticated", "AllowAny", "IsAdminUser", "ReadOnly"],
                "correct_answer": 0,
                "explanation": "IsAuthenticated requires the request user to be authenticated."
            },
            {
                "question_text": "Which DRF permission class allows access to any user, including unauthenticated users?",
                "options": ["AllowAny", "IsAuthenticated", "IsAdminUser", "DjangoModelPermissions"],
                "correct_answer": 0,
                "explanation": "AllowAny permits unrestricted access at the permission level."
            },
            {
                "question_text": "What does the DRF IsAdminUser permission check?",
                "options": ["Whether the user has staff status", "Whether the user has a Gmail account", "Whether the request uses POST", "Whether the database is PostgreSQL"],
                "correct_answer": 0,
                "explanation": "IsAdminUser grants access to users whose is_staff attribute is true."
            },
            {
                "question_text": "Where can default DRF permission classes be configured?",
                "options": ["REST_FRAMEWORK in settings.py", "INSTALLED_APPS in models.py", "urlpatterns in admin.py", "DATABASES in serializers.py"],
                "correct_answer": 0,
                "explanation": "DRF settings such as DEFAULT_PERMISSION_CLASSES are configured under REST_FRAMEWORK."
            },
            {
                "question_text": "What is authentication responsible for in DRF?",
                "options": ["Identifying the user associated with a request", "Deciding which HTML template to render", "Creating database indexes", "Generating CSS files"],
                "correct_answer": 0,
                "explanation": "Authentication determines the identity and authentication credentials associated with a request."
            },
            {
                "question_text": "What is permission checking responsible for in DRF?",
                "options": ["Deciding whether the request is allowed", "Converting JSON to HTML", "Creating migrations", "Starting the server"],
                "correct_answer": 0,
                "explanation": "Permissions determine whether an authenticated or anonymous request may perform an action."
            },
            {
                "question_text": "Which DRF authentication class uses a token in the Authorization header?",
                "options": ["TokenAuthentication", "SessionAuthentication only", "BasicViewAuthentication", "CookieModelAuthentication"],
                "correct_answer": 0,
                "explanation": "TokenAuthentication uses a token supplied in the Authorization header."
            },
            {
                "question_text": "Which HTTP header commonly carries a bearer token?",
                "options": ["Authorization", "Content-Length", "Accept-Language", "Referer"],
                "correct_answer": 0,
                "explanation": "Bearer credentials are commonly sent using the Authorization header."
            },
            {
                "question_text": "What does JWT stand for?",
                "options": ["JSON Web Token", "Java Web Transfer", "Joined Web Table", "JSON Working Template"],
                "correct_answer": 0,
                "explanation": "JWT stands for JSON Web Token."
            },
            {
                "question_text": "What is commonly stored in a JWT payload?",
                "options": ["Claims about the token subject and other token data", "The entire database", "Python source code", "HTML templates"],
                "correct_answer": 0,
                "explanation": "A JWT payload contains claims such as subject, issue time, and expiration."
            },
            {
                "question_text": "What is the purpose of a JWT signature?",
                "options": ["Help verify token integrity and authenticity", "Hide all payload data through encryption", "Store uploaded files", "Create a database table"],
                "correct_answer": 0,
                "explanation": "The signature allows a recipient to verify that the token has not been altered and was signed with the expected key."
            },
            {
                "question_text": "Does a standard signed JWT automatically encrypt its payload?",
                "options": ["No, its payload is normally encoded, not encrypted", "Yes, always", "Only when sent using GET", "Only when stored in PostgreSQL"],
                "correct_answer": 0,
                "explanation": "A signed JWT payload is generally readable by anyone who obtains it; signing does not provide confidentiality."
            },
            {
                "question_text": "What is the purpose of an access token in JWT-based authentication?",
                "options": ["Authorize access to protected resources for a limited period", "Store a user's profile picture", "Create a database schema", "Replace all API endpoints"],
                "correct_answer": 0,
                "explanation": "An access token is presented to access protected API resources until it expires."
            },
            {
                "question_text": "What is the common purpose of a refresh token?",
                "options": ["Obtain a new access token without repeating the full login process", "Upload files to the server", "Create a Django application", "Change database column types"],
                "correct_answer": 0,
                "explanation": "A refresh token can be exchanged for a new access token according to the authentication system's rules."
            },
            {
                "question_text": "What is pagination in an API?",
                "options": ["Dividing a large result set into smaller pages", "Encrypting every response", "Deleting old database records", "Converting all requests to POST"],
                "correct_answer": 0,
                "explanation": "Pagination returns large collections in manageable portions."
            },
            {
                "question_text": "Which DRF pagination class uses page numbers?",
                "options": ["PageNumberPagination", "CursorPagination", "LimitOffsetPagination", "TokenPagination"],
                "correct_answer": 0,
                "explanation": "PageNumberPagination divides results into numbered pages."
            },
            {
                "question_text": "Which DRF pagination class uses limit and offset query parameters?",
                "options": ["LimitOffsetPagination", "PageNumberPagination", "CursorPagination", "ModelPagination"],
                "correct_answer": 0,
                "explanation": "LimitOffsetPagination controls result size and starting position using limit and offset."
            },
            {
                "question_text": "What is the purpose of filtering in a REST API?",
                "options": ["Restrict returned records based on specified criteria", "Change the database engine", "Generate access tokens", "Disable authentication"],
                "correct_answer": 0,
                "explanation": "Filtering narrows a result set according to query parameters or other criteria."
            },
            {
                "question_text": "What is the purpose of ordering in a DRF API?",
                "options": ["Sort the returned results by selected fields", "Validate user passwords", "Create model relationships", "Encrypt response headers"],
                "correct_answer": 0,
                "explanation": "Ordering controls the sequence in which results are returned."
            },
            {
                "question_text": "Which DRF feature can help search text fields using query parameters?",
                "options": ["SearchFilter", "TokenAuthentication", "JSONRenderer", "SessionMiddleware"],
                "correct_answer": 0,
                "explanation": "SearchFilter enables search across configured fields using a query parameter."
            },
            {
                "question_text": "Which DRF feature provides ordering through query parameters?",
                "options": ["OrderingFilter", "SearchFilter", "IsAuthenticated", "BrowsableAPIRenderer"],
                "correct_answer": 0,
                "explanation": "OrderingFilter allows clients to specify ordering fields in requests."
            },
            {
                "question_text": "What is the purpose of get_queryset() in a DRF generic view?",
                "options": ["Return the queryset used for the current request", "Create a serializer automatically", "Generate a JWT signature", "Render a static HTML file"],
                "correct_answer": 0,
                "explanation": "get_queryset() can customize which objects are available for a request."
            },
            {
                "question_text": "What is the purpose of get_serializer_class() in a DRF view?",
                "options": ["Choose the serializer class for the current request or action", "Choose the database server", "Set the API port", "Create a user session"],
                "correct_answer": 0,
                "explanation": "get_serializer_class() supports selecting different serializers based on request context or action."
            },
            {
                "question_text": "Which method can be overridden in a ModelSerializer to customize object creation?",
                "options": ["create()", "dispatch()", "get_urls()", "render_to_response()"],
                "correct_answer": 0,
                "explanation": "Overriding create() customizes how a new object is created from validated data."
            },
            {
                "question_text": "Which method can be overridden in a ModelSerializer to customize updates?",
                "options": ["update()", "makemigrations()", "urlpatterns()", "authenticate()"],
                "correct_answer": 0,
                "explanation": "Overriding update() customizes how an existing instance is modified."
            },
            {
                "question_text": "What is object-level permission checking used for?",
                "options": ["Control access to a particular object", "Configure the whole database", "Validate URL syntax only", "Choose a JSON renderer"],
                "correct_answer": 0,
                "explanation": "Object-level permissions decide whether a request can access or modify a specific object."
            },
            {
                "question_text": "Which DRF method is commonly used to check permissions for a retrieved object?",
                "options": ["check_object_permissions()", "check_database_permissions()", "validate_template()", "verify_serializer_url()"],
                "correct_answer": 0,
                "explanation": "Generic views call check_object_permissions() when retrieving an object."
            },
            {
                "question_text": "What does the DRF Response class provide?",
                "options": ["An HTTP response that can render content into an appropriate format", "A database connection pool", "A Django model manager", "A URL configuration file"],
                "correct_answer": 0,
                "explanation": "Response is DRF's flexible response class and works with content negotiation."
            },
            {
                "question_text": "Which DRF decorator can add extra actions to a ViewSet?",
                "options": ["@action", "@route_only", "@serializer", "@permission"],
                "correct_answer": 0,
                "explanation": "The @action decorator adds custom routable actions to a ViewSet."
            },
            {
                "question_text": "What is content negotiation in DRF?",
                "options": ["Selecting a response format based on the request and available renderers", "Negotiating database passwords", "Selecting a user's permissions manually", "Changing the API URL"],
                "correct_answer": 0,
                "explanation": "Content negotiation determines how response content should be rendered for the client."
            },
            {
                "question_text": "Which DRF renderer provides JSON output?",
                "options": ["JSONRenderer", "TemplateHTMLRenderer", "BrowsableAPIRenderer only", "StaticFilesRenderer"],
                "correct_answer": 0,
                "explanation": "JSONRenderer renders response data as JSON."
            },
            {
                "question_text": "What is the purpose of API throttling in DRF?",
                "options": ["Limit the rate of requests made by clients", "Increase database table size", "Automatically create user accounts", "Convert HTTP to HTTPS"],
                "correct_answer": 0,
                "explanation": "Throttling helps control request rates and protect API resources."
            }
        ]
    }
]
