
QUESTION_BANK_DJANGO_INTERMEDIATE2 = [
    {
        "skill": "Django / REST APIs",
        "difficulty": "intermediate",
        "questions": [
            {
                "question_text": "Which DRF generic view is designed to create a new model object?",
                "options": ["CreateAPIView", "ListAPIView", "RetrieveAPIView", "DestroyAPIView"],
                "correct_answer": 0,
                "explanation": "CreateAPIView provides a POST handler for creating an object."
            },
            {
                "question_text": "Which DRF generic view returns a collection of objects?",
                "options": ["ListAPIView", "CreateAPIView", "UpdateAPIView", "DestroyAPIView"],
                "correct_answer": 0,
                "explanation": "ListAPIView provides a GET handler for listing a queryset."
            },
            {
                "question_text": "Which DRF generic view retrieves one object?",
                "options": ["RetrieveAPIView", "ListAPIView", "CreateAPIView", "ListCreateAPIView"],
                "correct_answer": 0,
                "explanation": "RetrieveAPIView provides a GET handler for a single object."
            },
            {
                "question_text": "Which DRF generic view supports updating an existing object?",
                "options": ["UpdateAPIView", "ListAPIView", "CreateAPIView", "APIViewRoot"],
                "correct_answer": 0,
                "explanation": "UpdateAPIView provides handlers for updating an existing object."
            },
            {
                "question_text": "Which DRF generic view is used to delete an object?",
                "options": ["DestroyAPIView", "RetrieveAPIView", "CreateAPIView", "ListAPIView"],
                "correct_answer": 0,
                "explanation": "DestroyAPIView provides a DELETE handler for an object."
            },
            {
                "question_text": "Which DRF generic view supports both listing and creating objects?",
                "options": ["ListCreateAPIView", "RetrieveUpdateAPIView", "DestroyAPIView", "CreateAPIView"],
                "correct_answer": 0,
                "explanation": "ListCreateAPIView supports GET for listing and POST for creation."
            },
            {
                "question_text": "Which DRF generic view supports retrieving and updating an object?",
                "options": ["RetrieveUpdateAPIView", "ListCreateAPIView", "ListAPIView", "DestroyAPIView"],
                "correct_answer": 0,
                "explanation": "RetrieveUpdateAPIView supports retrieving and updating a single object."
            },
            {
                "question_text": "Which DRF generic view supports retrieving, updating, and deleting one object?",
                "options": ["RetrieveUpdateDestroyAPIView", "ListCreateAPIView", "CreateAPIView", "ListAPIView"],
                "correct_answer": 0,
                "explanation": "RetrieveUpdateDestroyAPIView combines retrieve, update, and destroy operations."
            },
            {
                "question_text": "What is the purpose of get_object() in a DRF generic view?",
                "options": ["Retrieve the object targeted by the request", "Create a new database", "Generate a serializer file", "Return all URL patterns"],
                "correct_answer": 0,
                "explanation": "get_object() retrieves the specific object identified by the view's lookup configuration."
            },
            {
                "question_text": "Which attribute commonly determines the URL keyword used to look up an object in a DRF generic view?",
                "options": ["lookup_field", "serializer_field", "request_field", "database_field"],
                "correct_answer": 0,
                "explanation": "lookup_field specifies the model field used for object lookup."
            },
            {
                "question_text": "What is the default lookup field commonly used by DRF generic views?",
                "options": ["pk", "name", "email", "created_at"],
                "correct_answer": 0,
                "explanation": "The default lookup_field is pk."
            },
            {
                "question_text": "What does partial=True do when a serializer is used for an update?",
                "options": ["Allows omitted fields during validation", "Deletes fields from the model", "Skips authentication", "Disables all validation"],
                "correct_answer": 0,
                "explanation": "partial=True allows a partial update without requiring every required field."
            },
            {
                "question_text": "Which HTTP method is normally associated with a full update in a DRF update endpoint?",
                "options": ["PUT", "GET", "OPTIONS", "HEAD"],
                "correct_answer": 0,
                "explanation": "PUT is conventionally used for a full resource update."
            },
            {
                "question_text": "Which HTTP method is normally associated with a partial update in DRF?",
                "options": ["PATCH", "GET", "TRACE", "CONNECT"],
                "correct_answer": 0,
                "explanation": "PATCH is used to apply partial changes to a resource."
            },
            {
                "question_text": "What is the purpose of serializer context?",
                "options": ["Pass additional information to a serializer", "Create database indexes", "Configure URL routing", "Start authentication middleware"],
                "correct_answer": 0,
                "explanation": "Serializer context can provide request, view, and other custom information to serializer methods."
            },
            {
                "question_text": "How can a serializer access the current request when it is included in its context?",
                "options": ["self.context.get('request')", "self.request.GET", "self.serializer.request", "request.context()"],
                "correct_answer": 0,
                "explanation": "The request can be accessed through the serializer's context dictionary."
            },
            {
                "question_text": "Which serializer method can define validation for one specific field?",
                "options": ["validate_fieldname()", "check_fieldname()", "field_validate_only()", "clean_model_field()"],
                "correct_answer": 0,
                "explanation": "A method named validate_fieldname() performs field-specific validation."
            },
            {
                "question_text": "Which serializer method is used for validation involving multiple fields?",
                "options": ["validate()", "create()", "update()", "to_representation()"],
                "correct_answer": 0,
                "explanation": "validate() can implement validation that depends on multiple input fields."
            },
            {
                "question_text": "What is the purpose of SerializerMethodField?",
                "options": ["Add a read-only field calculated by a serializer method", "Create a database table", "Accept file uploads only", "Authenticate API requests"],
                "correct_answer": 0,
                "explanation": "SerializerMethodField obtains a value from a method on the serializer."
            },
            {
                "question_text": "Which method is commonly used to customize how a serializer instance is represented?",
                "options": ["to_representation()", "get_queryset()", "dispatch()", "get_permissions()"],
                "correct_answer": 0,
                "explanation": "to_representation() customizes the serialized output representation."
            },
            {
                "question_text": "What does source='user.email' do on a DRF serializer field?",
                "options": ["Reads a nested attribute from the related user object", "Creates a new email account", "Changes the database table name", "Validates the email server"],
                "correct_answer": 0,
                "explanation": "The source argument maps a serializer field to an attribute path on the object."
            },
            {
                "question_text": "What is the purpose of StringRelatedField?",
                "options": ["Represent a related object using its string representation", "Convert strings into database tables", "Encrypt text fields", "Create a foreign key automatically"],
                "correct_answer": 0,
                "explanation": "StringRelatedField represents a relationship using the related object's __str__() value."
            },
            {
                "question_text": "What is the purpose of PrimaryKeyRelatedField?",
                "options": ["Represent a relationship using the related object's primary key", "Represent a relationship as an image", "Create a new primary key for every request", "Validate only text fields"],
                "correct_answer": 0,
                "explanation": "PrimaryKeyRelatedField represents related objects by their primary key."
            },
            {
                "question_text": "What does depth in a ModelSerializer Meta class control?",
                "options": ["How deeply relationships are represented in serialized output", "The number of database connections", "The maximum API request rate", "The number of URL patterns"],
                "correct_answer": 0,
                "explanation": "The depth option controls nested relationship representation."
            },
            {
                "question_text": "What is the purpose of select_related() in Django ORM?",
                "options": ["Fetch related single-valued objects using a SQL join", "Delete related records", "Create a many-to-many relationship", "Sort model fields alphabetically"],
                "correct_answer": 0,
                "explanation": "select_related() uses SQL joins for ForeignKey and OneToOne relationships."
            },
            {
                "question_text": "What is the purpose of prefetch_related() in Django ORM?",
                "options": ["Fetch related collections using additional queries and combine them in Python", "Create a database migration", "Encrypt related records", "Delete duplicate rows"],
                "correct_answer": 0,
                "explanation": "prefetch_related() efficiently loads many-valued relationships with separate queries."
            },
            {
                "question_text": "Which Django ORM method returns the number of records in a QuerySet?",
                "options": ["count()", "length()", "size()", "total_records()"],
                "correct_answer": 0,
                "explanation": "count() returns the number of records represented by a QuerySet."
            },
            {
                "question_text": "Which Django ORM method checks whether a QuerySet contains at least one record?",
                "options": ["exists()", "contains_all()", "has_data()", "is_present()"],
                "correct_answer": 0,
                "explanation": "exists() efficiently checks whether a QuerySet contains any results."
            },
            {
                "question_text": "Which Django ORM method returns the first object in a QuerySet?",
                "options": ["first()", "initial()", "head()", "start()"],
                "correct_answer": 0,
                "explanation": "first() returns the first object or None if no object exists."
            },
            {
                "question_text": "Which Django ORM method returns the last object in a QuerySet?",
                "options": ["last()", "final()", "tail()", "end()"],
                "correct_answer": 0,
                "explanation": "last() returns the last object or None if the QuerySet is empty."
            },
            {
                "question_text": "What does get_or_create() do in Django ORM?",
                "options": ["Gets an existing object or creates one if it does not exist", "Always creates two objects", "Deletes an object and recreates it", "Returns only a model class"],
                "correct_answer": 0,
                "explanation": "get_or_create() returns an existing object or creates one using the supplied defaults and lookup values."
            },
            {
                "question_text": "What does update_or_create() do in Django ORM?",
                "options": ["Updates an existing object or creates it if missing", "Updates every table in the database", "Creates a migration file", "Deletes matching objects"],
                "correct_answer": 0,
                "explanation": "update_or_create() updates a matching object or creates one when no match exists."
            },
            {
                "question_text": "Which Django ORM method performs a bulk update on matching records?",
                "options": ["update()", "save_all()", "modify_many()", "bulk_save()"],
                "correct_answer": 0,
                "explanation": "QuerySet.update() performs a direct SQL update for matching records."
            },
            {
                "question_text": "Which Django ORM method creates multiple objects efficiently?",
                "options": ["bulk_create()", "create_many_only()", "insert_all_rows()", "save_queryset()"],
                "correct_answer": 0,
                "explanation": "bulk_create() inserts multiple model instances efficiently."
            },
            {
                "question_text": "What is the purpose of transaction.atomic() in Django?",
                "options": ["Execute database operations as an atomic transaction", "Automatically encrypt all model fields", "Create API documentation", "Disable database constraints"],
                "correct_answer": 0,
                "explanation": "transaction.atomic() ensures a group of database operations commits together or rolls back on failure."
            },
            {
                "question_text": "What is the purpose of F expressions in Django ORM?",
                "options": ["Refer to model field values directly in database operations", "Create form classes", "Format HTML templates", "Define API permissions"],
                "correct_answer": 0,
                "explanation": "F expressions let database operations refer to field values without loading them into Python first."
            },
            {
                "question_text": "What is the purpose of Q objects in Django ORM?",
                "options": ["Build complex queries using logical conditions", "Create query documentation", "Configure database passwords", "Serialize model instances"],
                "correct_answer": 0,
                "explanation": "Q objects support complex query expressions using AND, OR, and NOT operations."
            },
            {
                "question_text": "Which symbol combines two Q objects using logical OR?",
                "options": ["|", "&", "^", "%"],
                "correct_answer": 0,
                "explanation": "The pipe operator combines Q objects with OR logic."
            },
            {
                "question_text": "What does the Django ORM lookup __icontains do?",
                "options": ["Performs a case-insensitive containment search", "Checks exact equality only", "Sorts results in descending order", "Checks whether a value is null"],
                "correct_answer": 0,
                "explanation": "icontains matches text containing a substring without case sensitivity."
            },
            {
                "question_text": "What does the Django ORM lookup __isnull=True check?",
                "options": ["Whether a field value is NULL", "Whether a field is unique", "Whether a string is empty only", "Whether a model has a primary key"],
                "correct_answer": 0,
                "explanation": "isnull filters records based on whether a field contains SQL NULL."
            },
            {
                "question_text": "What is the purpose of Django's get_object_or_404() shortcut?",
                "options": ["Retrieve an object or raise an HTTP 404 response if it does not exist", "Create an object if missing", "Return every object in a table", "Redirect to the admin page"],
                "correct_answer": 0,
                "explanation": "get_object_or_404() raises Http404 when the requested object cannot be found."
            },
            {
                "question_text": "What does the DRF exception NotFound represent?",
                "options": ["A requested resource or object could not be found", "The database connection succeeded", "A user was authenticated", "A new resource was created"],
                "correct_answer": 0,
                "explanation": "NotFound is a DRF APIException that results in an HTTP 404 response."
            },
            {
                "question_text": "Which DRF exception represents invalid request data?",
                "options": ["ValidationError", "NotFound", "PermissionDenied", "NotAuthenticated"],
                "correct_answer": 0,
                "explanation": "ValidationError is used to report data validation failures."
            },
            {
                "question_text": "What is the purpose of APIException in DRF?",
                "options": ["Provide a base class for API-related exceptions", "Define model relationships", "Create serializers automatically", "Configure static files"],
                "correct_answer": 0,
                "explanation": "APIException is the base class for many DRF exceptions that produce API responses."
            },
            {
                "question_text": "What does the DRF status constant HTTP_204_NO_CONTENT indicate?",
                "options": ["The request succeeded and there is no response content", "The resource was not found", "The user is unauthorized", "The server failed"],
                "correct_answer": 0,
                "explanation": "204 No Content indicates success without a response body."
            },
            {
                "question_text": "What is the purpose of the Accept HTTP header?",
                "options": ["Tell the server which response media types the client can accept", "Send the user's password", "Specify the database table", "Set the API authentication method"],
                "correct_answer": 0,
                "explanation": "Accept communicates the media types that the client can process."
            },
            {
                "question_text": "What is the purpose of the Content-Type HTTP header?",
                "options": ["Describe the media type of the request or response body", "Identify the database host", "Specify the user's role", "Set the HTTP method"],
                "correct_answer": 0,
                "explanation": "Content-Type indicates the media type of the message body."
            },
            {
                "question_text": "What does application/json indicate as a Content-Type?",
                "options": ["The message body is JSON data", "The message body is an image", "The message body is plain HTML only", "The message body is a PDF file"],
                "correct_answer": 0,
                "explanation": "application/json is the media type used for JSON data."
            },
            {
                "question_text": "What is CORS used for in browser-based applications?",
                "options": ["Control cross-origin access to resources", "Encrypt database backups", "Create JWT tokens", "Generate Django migrations"],
                "correct_answer": 0,
                "explanation": "CORS defines how browsers permit web pages to access resources from other origins."
            },
            {
                "question_text": "What is the purpose of a CORS preflight request?",
                "options": ["Check whether a cross-origin request is permitted before sending the actual request", "Create a user account", "Refresh an access token", "Retrieve all database records"],
                "correct_answer": 0,
                "explanation": "Browsers use an OPTIONS preflight request to check permission for certain cross-origin requests."
            },
            {
                "question_text": "What is the purpose of the OPTIONS HTTP method in API communication?",
                "options": ["Describe communication options supported by the target resource", "Delete the target resource", "Replace the target resource", "Create a new database record"],
                "correct_answer": 0,
                "explanation": "OPTIONS asks the server about communication options for a resource."
            }
        ]
    }
]
