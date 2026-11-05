
QUESTION_BANK_DJANGO_BEGINNER2 = [
    {
        "skill": "Django / REST APIs",
        "difficulty": "beginner",
        "questions": [
            {
                "question_text": "Which Django function can return an HTTP response containing text?",
                "options": ["HttpResponse", "JsonField", "ModelForm", "URLPattern"],
                "correct_answer": 0,
                "explanation": "HttpResponse is used to return an HTTP response to the client."
            },
            {
                "question_text": "Which Django shortcut renders a template and returns an HTTP response?",
                "options": ["redirect()", "render()", "reverse()", "get_object_or_404()"],
                "correct_answer": 1,
                "explanation": "render() combines a template with context data and returns an HttpResponse."
            },
            {
                "question_text": "Which Django shortcut redirects a user to another URL?",
                "options": ["render()", "redirect()", "include()", "path()"],
                "correct_answer": 1,
                "explanation": "redirect() returns an HTTP redirect response."
            },
            {
                "question_text": "What is the purpose of the path() function in Django URL configuration?",
                "options": ["Define URL patterns", "Create database tables", "Validate forms", "Register models"],
                "correct_answer": 0,
                "explanation": "path() maps a URL route to a view."
            },
            {
                "question_text": "What does include() do in Django URL configuration?",
                "options": ["Includes URL patterns from another URL configuration", "Includes database records", "Imports CSS files", "Creates a model"],
                "correct_answer": 0,
                "explanation": "include() allows a project to include URL patterns from an app."
            },
            {
                "question_text": "Which Django object contains information about an incoming HTTP request?",
                "options": ["HttpRequest", "HttpResponse", "QuerySet", "Migration"],
                "correct_answer": 0,
                "explanation": "Django passes an HttpRequest object to a view."
            },
            {
                "question_text": "Where can a Django view access submitted form data from a POST request?",
                "options": ["request.POST", "request.GET", "request.URL", "request.MODEL"],
                "correct_answer": 0,
                "explanation": "request.POST contains form data submitted using POST."
            },
            {
                "question_text": "Where can a Django view access query parameters from a URL?",
                "options": ["request.POST", "request.GET", "request.FILES", "request.MODEL"],
                "correct_answer": 1,
                "explanation": "request.GET contains query parameters from the URL."
            },
            {
                "question_text": "Which request attribute contains uploaded files?",
                "options": ["request.DATA", "request.POST", "request.FILES", "request.UPLOAD"],
                "correct_answer": 2,
                "explanation": "Uploaded files are available through request.FILES."
            },
            {
                "question_text": "What is the purpose of csrf_token in a Django template?",
                "options": ["Protect against cross-site request forgery", "Encrypt database records", "Create user accounts", "Generate API URLs"],
                "correct_answer": 0,
                "explanation": "The CSRF token helps protect unsafe requests against cross-site request forgery."
            },
            {
                "question_text": "Which Django component is commonly used to validate HTML form input?",
                "options": ["Form", "Migration", "Middleware", "URL resolver"],
                "correct_answer": 0,
                "explanation": "Django Form classes provide input validation and cleaned data."
            },
            {
                "question_text": "What is a ModelForm in Django?",
                "options": ["A form automatically associated with a model", "A database server", "A URL pattern", "A middleware class"],
                "correct_answer": 0,
                "explanation": "ModelForm creates a form using fields defined in a Django model."
            },
            {
                "question_text": "Which method checks whether a Django form contains valid data?",
                "options": ["is_valid()", "is_correct()", "validate_model()", "check_form()"],
                "correct_answer": 0,
                "explanation": "is_valid() validates submitted form data."
            },
            {
                "question_text": "Where does Django store validated form data after is_valid() succeeds?",
                "options": ["cleaned_data", "validated_files", "request.URL", "form.models"],
                "correct_answer": 0,
                "explanation": "Validated form values are available in the cleaned_data dictionary."
            },
            {
                "question_text": "What is the purpose of the __str__() method in a Django model?",
                "options": ["Return a readable string representation", "Create a database table", "Delete an object", "Define a URL"],
                "correct_answer": 0,
                "explanation": "__str__() provides a human-readable representation of a model instance."
            },
            {
                "question_text": "What does the Meta class commonly define inside a Django model?",
                "options": ["Model metadata and options", "HTTP request data", "JavaScript functions", "Server passwords"],
                "correct_answer": 0,
                "explanation": "The inner Meta class defines options such as ordering and database table names."
            },
            {
                "question_text": "What does on_delete=models.CASCADE mean for a ForeignKey?",
                "options": ["Delete related objects when the referenced object is deleted", "Prevent all deletions", "Set the field to an empty string", "Create a new database"],
                "correct_answer": 0,
                "explanation": "CASCADE propagates deletion from the referenced object to related objects."
            },
            {
                "question_text": "What is the purpose of null=True on a Django model field?",
                "options": ["Allow NULL in the database", "Make a field unique", "Hide the field in admin", "Automatically encrypt the field"],
                "correct_answer": 0,
                "explanation": "null=True allows the database column to store NULL."
            },
            {
                "question_text": "What does blank=True mean for a Django model field?",
                "options": ["The field may be left blank during validation", "The database column must be NULL", "The field becomes a primary key", "The field is removed from the model"],
                "correct_answer": 0,
                "explanation": "blank=True allows empty values during form and model validation."
            },
            {
                "question_text": "Which model field option prevents duplicate values?",
                "options": ["unique=True", "blank=True", "null=True", "editable=True"],
                "correct_answer": 0,
                "explanation": "unique=True enforces uniqueness for a field."
            },
            {
                "question_text": "What does auto_now_add=True do on a Django DateTimeField?",
                "options": ["Sets the date and time when the object is first created", "Updates the field on every save", "Deletes old records", "Stores only the current date"],
                "correct_answer": 0,
                "explanation": "auto_now_add sets the field automatically when an object is initially created."
            },
            {
                "question_text": "What does auto_now=True do on a Django DateTimeField?",
                "options": ["Updates the field automatically whenever the object is saved", "Sets the field only during creation", "Makes the field unique", "Prevents updates"],
                "correct_answer": 0,
                "explanation": "auto_now updates the field to the current time on each save."
            },
            {
                "question_text": "Which Django setting defines the default primary key field type for newly created models?",
                "options": ["DEFAULT_AUTO_FIELD", "PRIMARY_KEY_TYPE", "MODEL_ID_FIELD", "DATABASE_KEY"],
                "correct_answer": 0,
                "explanation": "DEFAULT_AUTO_FIELD specifies the default auto-created primary key field type."
            },
            {
                "question_text": "Which command opens Django's interactive Python shell?",
                "options": ["python manage.py shell", "python manage.py runserver", "python manage.py test", "python manage.py collectstatic"],
                "correct_answer": 0,
                "explanation": "The shell command starts an interactive environment with Django configured."
            },
            {
                "question_text": "Which command runs Django's automated tests?",
                "options": ["python manage.py test", "python manage.py checkdb", "python manage.py testserveronly", "python manage.py validate"],
                "correct_answer": 0,
                "explanation": "The test command discovers and runs Django tests."
            },
            {
                "question_text": "Which command checks a Django project for common configuration problems?",
                "options": ["python manage.py check", "python manage.py inspect", "python manage.py verifydb", "python manage.py compile"],
                "correct_answer": 0,
                "explanation": "The check command runs Django system checks."
            },
            {
                "question_text": "What is the purpose of django.contrib.staticfiles?",
                "options": ["Manage static files such as CSS and JavaScript", "Manage database migrations", "Create API tokens", "Send database queries"],
                "correct_answer": 0,
                "explanation": "The staticfiles application helps manage static assets."
            },
            {
                "question_text": "Which Django setting specifies the URL prefix for static files?",
                "options": ["STATIC_URL", "MEDIA_ROOT", "STATIC_ROOT", "FILE_URL"],
                "correct_answer": 0,
                "explanation": "STATIC_URL defines the URL used to serve static files."
            },
            {
                "question_text": "Which setting specifies the filesystem location for uploaded media files?",
                "options": ["MEDIA_ROOT", "STATIC_URL", "TEMPLATE_DIR", "UPLOAD_URL"],
                "correct_answer": 0,
                "explanation": "MEDIA_ROOT specifies where uploaded media files are stored."
            },
            {
                "question_text": "Which Django model field is commonly used for uploading files?",
                "options": ["FileField", "TextField", "IntegerField", "URLField"],
                "correct_answer": 0,
                "explanation": "FileField handles file uploads associated with a model."
            },
            {
                "question_text": "What is the purpose of the apps.py file in a Django application?",
                "options": ["Define application configuration", "Define database queries only", "Store HTML templates", "Configure browser routes"],
                "correct_answer": 0,
                "explanation": "apps.py commonly contains the application's AppConfig class."
            },
            {
                "question_text": "Which file commonly contains automated tests for a Django app?",
                "options": ["tests.py", "admin.py", "settings.py", "manage.py"],
                "correct_answer": 0,
                "explanation": "Django applications commonly place tests in tests.py or a tests package."
            },
            {
                "question_text": "What is the purpose of Django's authentication system?",
                "options": ["Manage users, passwords, groups, and permissions", "Create HTML styles", "Configure network hardware", "Generate database backups automatically"],
                "correct_answer": 0,
                "explanation": "Django authentication provides user management and authorization features."
            },
            {
                "question_text": "Which function can check whether a user is authenticated in a Django view?",
                "options": ["request.user.is_authenticated", "request.user.is_admin", "request.auth.check()", "User.is_logged()"],
                "correct_answer": 0,
                "explanation": "is_authenticated indicates whether the current request user is authenticated."
            },
            {
                "question_text": "Which Django decorator restricts a view to logged-in users?",
                "options": ["login_required", "admin_only", "user_required_only", "authenticated_view"],
                "correct_answer": 0,
                "explanation": "The login_required decorator redirects unauthenticated users to the login page."
            },
            {
                "question_text": "What is the purpose of a Django session?",
                "options": ["Store user-specific data across requests", "Create database migrations", "Compile templates", "Define model relationships"],
                "correct_answer": 0,
                "explanation": "Sessions allow data to persist across multiple requests from a user."
            },
            {
                "question_text": "What is a cookie in web development?",
                "options": ["Small data stored by the browser for a website", "A database migration", "A Django model", "A Python package"],
                "correct_answer": 0,
                "explanation": "Cookies store small pieces of data in the user's browser."
            },
            {
                "question_text": "What does JSON stand for?",
                "options": ["JavaScript Object Notation", "Java Source Object Network", "Joined Standard Output Name", "Java Serialized Open Node"],
                "correct_answer": 0,
                "explanation": "JSON stands for JavaScript Object Notation."
            },
            {
                "question_text": "Which Python module provides JSON encoding and decoding?",
                "options": ["json", "http", "os", "random"],
                "correct_answer": 0,
                "explanation": "Python's built-in json module supports JSON serialization and parsing."
            },
            {
                "question_text": "What is an API?",
                "options": ["A way for software systems to communicate", "A type of database table", "A programming language", "A web browser"],
                "correct_answer": 0,
                "explanation": "An API defines how software components communicate and exchange data."
            },
            {
                "question_text": "What does REST stand for?",
                "options": ["Representational State Transfer", "Remote Execution Software Tool", "Resource System Transfer", "Represented Server Technology"],
                "correct_answer": 0,
                "explanation": "REST stands for Representational State Transfer."
            },
            {
                "question_text": "What is a REST API resource?",
                "options": ["An identifiable entity exposed through an API", "A Python virtual environment", "A CSS selector", "A server log file"],
                "correct_answer": 0,
                "explanation": "A resource is an entity, such as a user or product, exposed through an API."
            },
            {
                "question_text": "Which format is commonly used to exchange data in REST APIs?",
                "options": ["JSON", "DOCX", "MP3", "EXE"],
                "correct_answer": 0,
                "explanation": "JSON is a common lightweight data-interchange format for REST APIs."
            },
            {
                "question_text": "What does the HTTP status code 400 indicate?",
                "options": ["Bad Request", "Created", "Not Found", "Internal Server Error"],
                "correct_answer": 0,
                "explanation": "400 Bad Request indicates that the server cannot process the request due to a client error."
            },
            {
                "question_text": "What does HTTP status code 401 indicate?",
                "options": ["Unauthorized", "Forbidden", "Created", "No Content"],
                "correct_answer": 0,
                "explanation": "401 Unauthorized indicates that valid authentication credentials are missing or invalid."
            },
            {
                "question_text": "What does HTTP status code 403 indicate?",
                "options": ["Forbidden", "Created", "Accepted", "Moved Permanently"],
                "correct_answer": 0,
                "explanation": "403 Forbidden means the server understood the request but refuses to authorize it."
            },
            {
                "question_text": "What does HTTP status code 500 indicate?",
                "options": ["Internal Server Error", "Bad Request", "Not Found", "Unauthorized"],
                "correct_answer": 0,
                "explanation": "500 indicates an unexpected server-side error."
            },
            {
                "question_text": "What is the purpose of an API endpoint?",
                "options": ["Provide a specific URL through which an API resource or operation is accessed", "Store a user's password", "Create a Python class", "Start a database server"],
                "correct_answer": 0,
                "explanation": "An endpoint is a URL where an API can be accessed."
            },
            {
                "question_text": "What is API authentication used for?",
                "options": ["Verify the identity of a client or user", "Format JSON output", "Create database tables", "Compress images"],
                "correct_answer": 0,
                "explanation": "Authentication verifies who is making an API request."
            },
            {
                "question_text": "What is API authorization used for?",
                "options": ["Determine what an authenticated user is allowed to access", "Verify JSON syntax only", "Create user passwords", "Convert Python into JavaScript"],
                "correct_answer": 0,
                "explanation": "Authorization determines which resources or actions a user is permitted to access."
            }
        ]
    }
]
