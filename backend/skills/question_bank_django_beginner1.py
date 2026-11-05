
QUESTION_BANK_DJANGO_BEGINNER1 = [
    {
        "skill": "Django / REST APIs",
        "difficulty": "beginner",
        "questions": [
            {
                "question_text": "What is Django?",
                "options": ["A Python web framework", "A database", "A programming language", "An operating system"],
                "correct_answer": 0,
                "explanation": "Django is a high-level Python web framework."
            },
            {
                "question_text": "Which programming language is used with Django?",
                "options": ["Java", "Python", "C++", "JavaScript only"],
                "correct_answer": 1,
                "explanation": "Django is built using Python."
            },
            {
                "question_text": "Which architectural pattern does Django follow?",
                "options": ["MVC only", "MVT", "MVVM", "Microkernel"],
                "correct_answer": 1,
                "explanation": "Django follows the Model-View-Template architecture."
            },
            {
                "question_text": "What does MVT stand for in Django?",
                "options": ["Model View Template", "Main View Tool", "Module Variable Type", "Model Version Table"],
                "correct_answer": 0,
                "explanation": "MVT stands for Model, View, and Template."
            },
            {
                "question_text": "Which command creates a new Django project?",
                "options": ["django-admin startproject", "django-admin startapp", "python createproject", "django runproject"],
                "correct_answer": 0,
                "explanation": "The startproject command creates a Django project."
            },
            {
                "question_text": "Which command creates a new Django application?",
                "options": ["python manage.py runserver", "python manage.py startapp", "python manage.py migrate", "python manage.py check"],
                "correct_answer": 1,
                "explanation": "The startapp command creates a Django application."
            },
            {
                "question_text": "Which file contains the main Django project settings?",
                "options": ["urls.py", "models.py", "settings.py", "views.py"],
                "correct_answer": 2,
                "explanation": "settings.py contains project configuration."
            },
            {
                "question_text": "Which file defines URL patterns in a Django application?",
                "options": ["urls.py", "admin.py", "apps.py", "tests.py"],
                "correct_answer": 0,
                "explanation": "urls.py maps URL patterns to views."
            },
            {
                "question_text": "Which file is commonly used to define database models?",
                "options": ["views.py", "models.py", "urls.py", "settings.py"],
                "correct_answer": 1,
                "explanation": "Django models define the structure of database data."
            },
            {
                "question_text": "Which command starts the Django development server?",
                "options": ["python manage.py migrate", "python manage.py runserver", "python manage.py createsuperuser", "python manage.py startapp"],
                "correct_answer": 1,
                "explanation": "The runserver command starts Django's development server."
            },
            {
                "question_text": "What is the default development server port used by Django?",
                "options": ["3000", "5000", "8000", "8080"],
                "correct_answer": 2,
                "explanation": "Django's development server uses port 8000 by default."
            },
            {
                "question_text": "Which Django component handles incoming HTTP requests?",
                "options": ["View", "Model", "Database table", "Migration"],
                "correct_answer": 0,
                "explanation": "A Django view receives a request and returns a response."
            },
            {
                "question_text": "What is the purpose of a Django model?",
                "options": ["Define database structure", "Design HTML pages only", "Configure browser settings", "Start the server"],
                "correct_answer": 0,
                "explanation": "Models define data fields and database relationships."
            },
            {
                "question_text": "Which command creates migration files after model changes?",
                "options": ["python manage.py migrate", "python manage.py makemigrations", "python manage.py runserver", "python manage.py shell"],
                "correct_answer": 1,
                "explanation": "makemigrations creates migration files based on model changes."
            },
            {
                "question_text": "Which command applies migrations to the database?",
                "options": ["makemigrations", "migrate", "startapp", "collectstatic"],
                "correct_answer": 1,
                "explanation": "The migrate command applies database migrations."
            },
            {
                "question_text": "What is the purpose of Django migrations?",
                "options": ["Track and apply database schema changes", "Create HTML templates", "Manage browser cookies only", "Compile Python code"],
                "correct_answer": 0,
                "explanation": "Migrations manage changes to database schema over time."
            },
            {
                "question_text": "Which Django command creates an administrator account?",
                "options": ["createsuperuser", "startadmin", "makeadmin", "createuser"],
                "correct_answer": 0,
                "explanation": "createsuperuser creates a privileged Django admin account."
            },
            {
                "question_text": "Which URL commonly opens the Django admin site?",
                "options": ["/dashboard/", "/admin/", "/manage/", "/control/"],
                "correct_answer": 1,
                "explanation": "The default Django admin URL is /admin/."
            },
            {
                "question_text": "Which file is used to register models with the Django admin site?",
                "options": ["admin.py", "models.py", "forms.py", "apps.py"],
                "correct_answer": 0,
                "explanation": "Models are registered with the admin site in admin.py."
            },
            {
                "question_text": "Which Django ORM method retrieves all records from a model?",
                "options": ["Model.objects.all()", "Model.objects.getall()", "Model.fetch()", "Model.records()"],
                "correct_answer": 0,
                "explanation": "objects.all() returns a QuerySet containing all matching records."
            },
            {
                "question_text": "Which ORM method retrieves a single object matching given conditions?",
                "options": ["filter()", "get()", "all()", "exclude()"],
                "correct_answer": 1,
                "explanation": "get() retrieves one object and raises an exception if the result is missing or multiple."
            },
            {
                "question_text": "Which ORM method returns all objects matching specified conditions?",
                "options": ["filter()", "create()", "delete()", "save()"],
                "correct_answer": 0,
                "explanation": "filter() returns a QuerySet matching the specified conditions."
            },
            {
                "question_text": "Which method saves a model instance to the database?",
                "options": ["store()", "save()", "insert()", "commit()"],
                "correct_answer": 1,
                "explanation": "The save() method persists a model instance."
            },
            {
                "question_text": "Which Django model field stores short text?",
                "options": ["CharField", "IntegerField", "BooleanField", "DateField"],
                "correct_answer": 0,
                "explanation": "CharField stores short strings with a defined maximum length."
            },
            {
                "question_text": "Which Django model field stores longer text content?",
                "options": ["TextField", "BooleanField", "DateField", "AutoField"],
                "correct_answer": 0,
                "explanation": "TextField is used for larger text content."
            },
            {
                "question_text": "Which field stores integer values in a Django model?",
                "options": ["EmailField", "IntegerField", "TextField", "FileField"],
                "correct_answer": 1,
                "explanation": "IntegerField stores integer values."
            },
            {
                "question_text": "Which field stores true or false values?",
                "options": ["BooleanField", "CharField", "DateTimeField", "DecimalField"],
                "correct_answer": 0,
                "explanation": "BooleanField stores Boolean values."
            },
            {
                "question_text": "Which field stores both date and time?",
                "options": ["DateField", "TimeField", "DateTimeField", "DurationField"],
                "correct_answer": 2,
                "explanation": "DateTimeField stores a date and time value."
            },
            {
                "question_text": "What does a ForeignKey represent in Django?",
                "options": ["A many-to-one relationship", "A one-to-one relationship only", "A text field", "A database index"],
                "correct_answer": 0,
                "explanation": "ForeignKey defines a many-to-one relationship between models."
            },
            {
                "question_text": "Which Django field represents a many-to-many relationship?",
                "options": ["OneToOneField", "ForeignKey", "ManyToManyField", "CharField"],
                "correct_answer": 2,
                "explanation": "ManyToManyField defines a many-to-many relationship."
            },
            {
                "question_text": "Which field represents a one-to-one relationship?",
                "options": ["OneToOneField", "ManyToManyField", "TextField", "ForeignKey only"],
                "correct_answer": 0,
                "explanation": "OneToOneField creates a one-to-one model relationship."
            },
            {
                "question_text": "What is Django ORM?",
                "options": ["Object Relational Mapper", "Online Request Manager", "Object Runtime Method", "Operating Resource Module"],
                "correct_answer": 0,
                "explanation": "Django ORM allows database operations using Python objects and QuerySets."
            },
            {
                "question_text": "Which method deletes a model instance from the database?",
                "options": ["remove()", "delete()", "drop()", "clear()"],
                "correct_answer": 1,
                "explanation": "The delete() method removes a model instance from the database."
            },
            {
                "question_text": "What is a Django QuerySet?",
                "options": ["A collection of database query results", "An HTML template", "A Python package installer", "A URL configuration"],
                "correct_answer": 0,
                "explanation": "A QuerySet represents a collection of database objects."
            },
            {
                "question_text": "What is the purpose of Django templates?",
                "options": ["Generate dynamic HTML output", "Create database migrations", "Manage Python packages", "Configure database connections"],
                "correct_answer": 0,
                "explanation": "Templates generate presentation output using HTML and template syntax."
            },
            {
                "question_text": "Which template syntax displays a variable in Django?",
                "options": ["{{ variable }}", "{% variable %}", "<variable>", "[[ variable ]]"],
                "correct_answer": 0,
                "explanation": "Django uses double curly braces to display template variables."
            },
            {
                "question_text": "Which Django template tag is used for loops?",
                "options": ["{% for %}", "{{ for }}", "<for>", "{# for #}"],
                "correct_answer": 0,
                "explanation": "The for template tag iterates over a sequence."
            },
            {
                "question_text": "Which Django template tag is used for conditional logic?",
                "options": ["{% if %}", "{{ if }}", "<condition>", "{# if #}"],
                "correct_answer": 0,
                "explanation": "The if template tag supports conditional rendering."
            },
            {
                "question_text": "What is middleware in Django?",
                "options": ["A component that processes requests and responses globally", "A database table", "A template file", "A model field"],
                "correct_answer": 0,
                "explanation": "Middleware hooks into Django's request-response processing."
            },
            {
                "question_text": "Where are installed Django applications configured?",
                "options": ["INSTALLED_APPS in settings.py", "urlpatterns in urls.py", "MIDDLEWARE in models.py", "DATABASES in views.py"],
                "correct_answer": 0,
                "explanation": "INSTALLED_APPS lists the applications enabled in a Django project."
            },
            {
                "question_text": "What is the purpose of the SECRET_KEY setting?",
                "options": ["Provide a secret used by Django's cryptographic signing features", "Store database passwords only", "Name the project", "Set the server port"],
                "correct_answer": 0,
                "explanation": "SECRET_KEY is used for cryptographic signing and other security-related operations."
            },
            {
                "question_text": "What does DEBUG=True enable in Django?",
                "options": ["Detailed debugging information during development", "Automatic production deployment", "Database encryption", "User registration"],
                "correct_answer": 0,
                "explanation": "DEBUG enables detailed error pages and development debugging features."
            },
            {
                "question_text": "Which Django setting specifies the database configuration?",
                "options": ["DATABASES", "INSTALLED_APPS", "TEMPLATES", "STATIC_URL"],
                "correct_answer": 0,
                "explanation": "DATABASES configures database connections for the project."
            },
            {
                "question_text": "Which HTTP method is commonly used to retrieve a resource?",
                "options": ["GET", "POST", "DELETE", "PATCH"],
                "correct_answer": 0,
                "explanation": "GET is used to retrieve a resource."
            },
            {
                "question_text": "Which HTTP method is commonly used to create a new resource?",
                "options": ["GET", "POST", "DELETE", "HEAD"],
                "correct_answer": 1,
                "explanation": "POST commonly submits data to create a resource."
            },
            {
                "question_text": "Which HTTP method is commonly used to replace an entire resource?",
                "options": ["PATCH", "PUT", "GET", "OPTIONS"],
                "correct_answer": 1,
                "explanation": "PUT is commonly used to replace a resource representation."
            },
            {
                "question_text": "Which HTTP method is commonly used for a partial resource update?",
                "options": ["PATCH", "GET", "HEAD", "TRACE"],
                "correct_answer": 0,
                "explanation": "PATCH applies partial modifications to a resource."
            },
            {
                "question_text": "Which HTTP status code indicates a successful request?",
                "options": ["200", "404", "500", "403"],
                "correct_answer": 0,
                "explanation": "200 OK indicates that the request succeeded."
            },
            {
                "question_text": "Which HTTP status code indicates that a resource was created successfully?",
                "options": ["200", "201", "400", "404"],
                "correct_answer": 1,
                "explanation": "201 Created indicates successful resource creation."
            },
            {
                "question_text": "Which HTTP status code indicates that a requested resource was not found?",
                "options": ["200", "201", "404", "500"],
                "correct_answer": 2,
                "explanation": "404 Not Found indicates that the requested resource could not be found."
            }
        ]
    }
]
