def build_question(question, options, answer, explanation):
    return {
        "skill": "Web Technologies",
        "difficulty": "intermediate",
        "question_text": question,
        "options": options,
        "correct_answer": answer,
        "explanation": explanation,
    }


QUESTION_BANK_WEB_INTERMEDIATE1 = [

    # HTML5 (1-10)

    build_question(
        "Which HTML5 element is used to group introductory content?",
        ["footer", "header", "article", "aside"],
        1, "The header element represents introductory content or navigation."
    ),
    build_question(
        "Which attribute makes an input field mandatory?",
        ["validate", "required", "mandatory", "must"],
        1, "The required attribute prevents form submission when the field is empty."
    ),
    build_question(
        "Which element is used to display scalable vector graphics?",
        ["canvas", "svg", "picture", "vector"],
        1, "The SVG element defines scalable vector graphics."
    ),
    build_question(
        "Which HTML element provides a caption for a figure?",
        ["caption", "figcaption", "legend", "summary"],
        1, "The figcaption element provides a caption for its parent figure."
    ),
    build_question(
        "Which attribute specifies that a video should start automatically?",
        ["controls", "autoplay", "muted", "loop"],
        1, "The autoplay attribute requests automatic video playback."
    ),
    build_question(
        "Which input type provides a color picker?",
        ["text", "color", "palette", "paint"],
        1, "The color input type provides a browser color picker."
    ),
    build_question(
        "Which element represents a self-contained composition?",
        ["section", "article", "div", "span"],
        1, "Article represents independently reusable or distributable content."
    ),
    build_question(
        "Which attribute connects a label to an input element?",
        ["name", "for", "target", "connect"],
        1, "The label's for attribute matches the input's id."
    ),
    build_question(
        "Which HTML element is used for expandable and collapsible content?",
        ["details", "dialog", "summary", "toggle"],
        0, "The details element creates disclosure content."
    ),
    build_question(
        "Which element defines a machine-readable date or time?",
        ["date", "time", "datetime", "timestamp"],
        1, "The time element represents a date or time."
    ),

    # CSS3 (11-20)

    build_question(
        "Which CSS property controls the stacking order of positioned elements?",
        ["position", "z-index", "display", "float"],
        1, "The z-index property controls stacking order."
    ),
    build_question(
        "Which CSS layout system is primarily designed for one-dimensional layouts?",
        ["Grid", "Flexbox", "Table", "Float"],
        1, "Flexbox is designed primarily for one-dimensional layouts."
    ),
    build_question(
        "Which CSS property defines space between grid rows?",
        ["gap-row", "row-gap", "grid-space", "margin-row"],
        1, "The row-gap property defines spacing between grid rows."
    ),
    build_question(
        "What does box-sizing: border-box do?",
        [
            "Excludes padding from width",
            "Includes padding and border in width",
            "Removes element borders",
            "Includes margin in width"
        ],
        1, "Border-box includes content, padding and border in the declared dimensions."
    ),
    build_question(
        "Which pseudo-class selects an element when the pointer is over it?",
        [":focus", ":active", ":hover", ":visited"],
        2, "The hover pseudo-class applies styles while the pointer hovers over an element."
    ),
    build_question(
        "Which CSS unit is relative to the root element's font size?",
        ["em", "rem", "px", "%"],
        1, "The rem unit is relative to the root element's font size."
    ),
    build_question(
        "Which property controls how an image fits inside its container?",
        ["image-fit", "object-fit", "background-size", "content-fit"],
        1, "Object-fit controls how replaced content fits its container."
    ),
    build_question(
        "Which media query targets screens with a maximum width of 768px?",
        [
            "@media (min-width: 768px)",
            "@media (max-width: 768px)",
            "@screen (width: 768px)",
            "@media (height: 768px)"
        ],
        1, "Max-width targets viewports no wider than 768px."
    ),
    build_question(
        "Which CSS property creates rounded corners?",
        ["corner-radius", "border-radius", "round-edge", "outline-radius"],
        1, "Border-radius controls the rounding of element corners."
    ),
    build_question(
        "Which selector has the highest specificity?",
        ["p", ".content", "#header", "*"],
        2, "An ID selector has higher specificity than a class or element selector."
    ),

    # JavaScript ES6+ (21-35)

    build_question(
        "Which keyword declares a block-scoped variable that can be reassigned?",
        ["const", "let", "static", "final"],
        1, "Let declares a block-scoped variable that can be reassigned."
    ),
    build_question(
        "What is the result of typeof null in JavaScript?",
        ["null", "undefined", "object", "boolean"],
        2, "JavaScript historically returns object for typeof null."
    ),
    build_question(
        "Which array method creates a new array by transforming each element?",
        ["filter()", "map()", "reduce()", "find()"],
        1, "Map transforms each element and returns a new array."
    ),
    build_question(
        "Which operator provides a fallback only when the left operand is null or undefined?",
        ["||", "&&", "??", "!="],
        2, "The nullish coalescing operator checks specifically for null and undefined."
    ),
    build_question(
        "What does the spread operator do when used with an array?",
        [
            "Deletes array elements",
            "Expands iterable elements",
            "Sorts the array",
            "Converts the array to a string"
        ],
        1, "Spread syntax expands iterable elements into individual values."
    ),
    build_question(
        "Which syntax creates an arrow function?",
        [
            "function => ()",
            "() => {}",
            "function -> {}",
            "() = {}"
        ],
        1, "Arrow functions use the => syntax."
    ),
    build_question(
        "Which method converts a JSON string into a JavaScript object?",
        ["JSON.stringify()", "JSON.parse()", "JSON.convert()", "JSON.object()"],
        1, "JSON.parse converts a valid JSON string into a JavaScript value."
    ),
    build_question(
        "Which array method returns the first element that satisfies a condition?",
        ["map()", "find()", "filter()", "reduce()"],
        1, "Find returns the first matching element or undefined."
    ),
    build_question(
        "What is the purpose of a JavaScript Promise?",
        [
            "To define CSS styles",
            "To represent eventual completion or failure of an asynchronous operation",
            "To create HTML elements",
            "To store browser cookies"
        ],
        1, "A Promise represents the eventual result of an asynchronous operation."
    ),
    build_question(
        "Which keyword pauses execution inside an async function until a Promise settles?",
        ["defer", "await", "yield", "pause"],
        1, "Await pauses the async function until the Promise settles."
    ),
    build_question(
        "What does Array.prototype.filter() return?",
        [
            "A single matching element",
            "A new array containing matching elements",
            "A modified original array",
            "A Boolean value"
        ],
        1, "Filter creates a new array containing elements that pass the test."
    ),
    build_question(
        "What is a closure in JavaScript?",
        [
            "A function that remembers its lexical environment",
            "A function without parameters",
            "A method that closes the browser",
            "A loop that stops automatically"
        ],
        0, "A closure retains access to variables from its lexical scope."
    ),
    build_question(
        "Which keyword is used to export a default value from an ES module?",
        ["export default", "import default", "module default", "return default"],
        0, "Export default declares the module's default export."
    ),
    build_question(
        "What is the result of [1, 2, 3].reduce((a, b) => a + b, 0)?",
        ["3", "5", "6", "123"],
        2, "Reduce accumulates the sum: 1 + 2 + 3 = 6."
    ),
    build_question(
        "Which method checks whether at least one array element passes a test?",
        ["every()", "some()", "includes()", "findIndex()"],
        1, "Some returns true when at least one element passes the callback test."
    ),

    # DOM Manipulation (36-45)

    build_question(
        "Which method selects the first element matching a CSS selector?",
        ["getElementsByClassName()", "querySelector()", "querySelectorAll()", "getElementById()"],
        1, "QuerySelector returns the first matching element."
    ),
    build_question(
        "Which property changes the text content of an element?",
        ["innerStyle", "textContent", "outerHTML", "nodeType"],
        1, "TextContent gets or sets an element's text content."
    ),
    build_question(
        "Which method attaches an event handler to an element?",
        ["attach()", "addEventListener()", "addEvent()", "onEvent()"],
        1, "AddEventListener registers an event listener."
    ),
    build_question(
        "Which event occurs when a user submits an HTML form?",
        ["click", "change", "submit", "input"],
        2, "The submit event is fired when a form is submitted."
    ),
    build_question(
        "Which method creates a new HTML element?",
        ["document.createElement()", "document.newNode()", "document.addElement()", "document.make()"],
        0, "CreateElement creates a new element node."
    ),
    build_question(
        "Which property adds a CSS class without replacing existing classes?",
        ["className", "classList.add()", "style.add()", "setAttribute()"],
        1, "ClassList.add adds a class while preserving existing classes."
    ),
    build_question(
        "Which method removes an element from the DOM?",
        ["delete()", "remove()", "clear()", "destroy()"],
        1, "Remove removes an element from its parent."
    ),
    build_question(
        "What does event.preventDefault() do?",
        [
            "Stops event propagation",
            "Prevents the browser's default action",
            "Removes the event listener",
            "Reloads the page"
        ],
        1, "PreventDefault cancels the default browser action when the event is cancelable."
    ),
    build_question(
        "Which event property identifies the element that triggered the event?",
        ["currentStyle", "target", "source", "originElement"],
        1, "Event.target identifies the element on which the event originated."
    ),
    build_question(
        "What does event bubbling mean?",
        [
            "Events move from parent to child",
            "Events propagate from target toward ancestors",
            "Events execute only once",
            "Events are removed automatically"
        ],
        1, "During bubbling, events propagate from the target through ancestor elements."
    ),

    # Asynchronous JavaScript (46-55)

    build_question(
        "Which Promise method runs when a Promise is fulfilled?",
        ["catch()", "then()", "finally()", "resolve()"],
        1, "Then registers a fulfillment handler."
    ),
    build_question(
        "Which Promise method handles rejection?",
        ["then()", "catch()", "map()", "filter()"],
        1, "Catch registers a rejection handler."
    ),
    build_question(
        "Which Promise method waits for all supplied Promises to fulfill?",
        ["Promise.race()", "Promise.all()", "Promise.any()", "Promise.resolve()"],
        1, "Promise.all fulfills when all inputs fulfill and rejects if an input rejects."
    ),
    build_question(
        "What does setTimeout(callback, 1000) do?",
        [
            "Executes callback exactly after one second",
            "Schedules callback after at least approximately one second",
            "Repeats callback every second",
            "Blocks JavaScript for one second"
        ],
        1, "SetTimeout schedules a callback after the specified minimum delay; actual execution may be later."
    ),
    build_question(
        "Which function runs repeatedly at a specified interval?",
        ["setTimeout()", "setInterval()", "request()", "repeat()"],
        1, "SetInterval schedules repeated callback execution."
    ),
    build_question(
        "What is the purpose of async before a function declaration?",
        [
            "It makes the function return a Promise",
            "It prevents function execution",
            "It converts the function to a generator",
            "It makes the function synchronous"
        ],
        0, "An async function always returns a Promise."
    ),
    build_question(
        "Which Promise method fulfills with the first fulfilled input?",
        ["Promise.all()", "Promise.any()", "Promise.race()", "Promise.reject()"],
        1, "Promise.any fulfills with the first fulfilled input."
    ),
    build_question(
        "What happens when an awaited Promise rejects without local handling?",
        [
            "The rejection becomes an error in the async function",
            "The Promise is automatically fulfilled",
            "The browser closes",
            "The function restarts"
        ],
        0, "An unhandled awaited rejection throws within the async function."
    ),
    build_question(
        "What is the JavaScript event loop responsible for?",
        [
            "Rendering CSS selectors",
            "Coordinating execution of queued callbacks and tasks",
            "Creating database tables",
            "Compiling HTML elements"
        ],
        1, "The event loop coordinates task execution and queued callbacks with the call stack."
    ),
    build_question(
        "Which queue processes Promise reaction callbacks in the standard event loop model?",
        ["Task queue", "Microtask queue", "Render queue only", "Storage queue"],
        1, "Promise reaction callbacks are scheduled as microtasks."
    ),

    # Fetch API (56-63)

    build_question(
        "Which browser API is commonly used to make HTTP requests using Promises?",
        ["XMLParser", "Fetch API", "DOMParser", "Canvas API"],
        1, "Fetch provides a Promise-based interface for network requests."
    ),
    build_question(
        "Which method converts a Fetch response body into JSON?",
        ["response.parse()", "response.json()", "response.stringify()", "response.textJSON()"],
        1, "Response.json reads and parses the response body as JSON."
    ),
    build_question(
        "Does Fetch automatically reject its Promise for HTTP 404 responses?",
        ["Yes, always", "No, it resolves with a Response", "It returns null", "It retries automatically"],
        1, "HTTP error statuses normally resolve Fetch; check response.ok or response.status."
    ),
    build_question(
        "Which option specifies the HTTP method in a Fetch request?",
        ["method", "type", "action", "requestType"],
        0, "The method option specifies GET, POST, PUT, DELETE and other HTTP methods."
    ),
    build_question(
        "Which Fetch option supplies request headers?",
        ["headers", "metadata", "content", "responseHeaders"],
        0, "The headers option specifies HTTP request headers."
    ),
    build_question(
        "Which browser interface can cancel an ongoing Fetch request?",
        ["CancelFetch", "AbortController", "FetchStop", "RequestManager"],
        1, "AbortController provides an AbortSignal that Fetch can use to cancel requests."
    ),
    build_question(
        "Which property indicates whether an HTTP response has a successful status?",
        ["response.success", "response.ok", "response.valid", "response.done"],
        1, "Response.ok is true for HTTP status codes from 200 through 299."
    ),
    build_question(
        "Which request body format is commonly used to send JSON?",
        [
            "JSON.stringify(data)",
            "JSON.parse(data)",
            "data.toHTML()",
            "String.toJSON(data)"
        ],
        0, "JSON.stringify serializes a JavaScript value into JSON text."
    ),

    # REST API (64-73)

    build_question(
        "What does REST stand for?",
        [
            "Remote Execution State Transfer",
            "Representational State Transfer",
            "Request Server Transfer",
            "Resource Exchange Standard Technology"
        ],
        1, "REST stands for Representational State Transfer."
    ),
    build_question(
        "Which HTTP method is commonly used to retrieve a resource?",
        ["POST", "GET", "PATCH", "DELETE"],
        1, "GET retrieves a representation of a resource."
    ),
    build_question(
        "Which HTTP method is commonly used to create a resource?",
        ["GET", "POST", "HEAD", "OPTIONS"],
        1, "POST is commonly used to submit data that creates a resource."
    ),
    build_question(
        "Which HTTP method replaces a resource representation?",
        ["PATCH", "PUT", "GET", "TRACE"],
        1, "PUT is used to create or replace the target resource representation."
    ),
    build_question(
        "Which HTTP method is commonly used for partial resource updates?",
        ["PUT", "PATCH", "HEAD", "OPTIONS"],
        1, "PATCH applies partial modifications to a resource."
    ),
    build_question(
        "What does statelessness mean in REST?",
        [
            "The server stores all client session state between requests",
            "Each request contains the information needed to process it",
            "The API cannot use authentication",
            "The client cannot store data"
        ],
        1, "Stateless interactions require each request to carry the necessary context."
    ),
    build_question(
        "Which format is widely used for REST API data exchange?",
        ["JSON", "BMP", "MP3", "EXE"],
        0, "JSON is a widely used lightweight data-interchange format."
    ),
    build_question(
        "What is the main purpose of an API endpoint?",
        [
            "To define a resource or operation's network address",
            "To compile JavaScript",
            "To style a webpage",
            "To store browser cookies"
        ],
        0, "An endpoint identifies a network-accessible API resource or operation."
    ),
    build_question(
        "Which HTTP method is generally considered idempotent?",
        ["POST", "PUT", "CONNECT", "PATCH always"],
        1, "PUT is idempotent: repeating the same request has the same intended effect."
    ),
    build_question(
        "What is API versioning used for?",
        [
            "To change browser screen size",
            "To manage API changes while supporting compatibility",
            "To encrypt passwords automatically",
            "To remove HTTP status codes"
        ],
        1, "Versioning helps manage changes and compatibility between API clients and servers."
    ),

    # HTTP (74-82)

    build_question(
        "What does HTTP status code 200 indicate?",
        ["Created", "OK", "No Content", "Not Found"],
        1, "200 indicates that the request succeeded."
    ),
    build_question(
        "Which status code indicates successful resource creation?",
        ["200", "201", "204", "301"],
        1, "201 Created indicates successful resource creation."
    ),
    build_question(
        "What does HTTP status code 204 represent?",
        ["Bad Request", "No Content", "Unauthorized", "Forbidden"],
        1, "204 indicates successful processing with no response content."
    ),
    build_question(
        "Which status code indicates a malformed client request?",
        ["400", "401", "403", "500"],
        0, "400 Bad Request indicates that the server cannot process the request due to a client error."
    ),
    build_question(
        "What does HTTP status code 401 indicate?",
        ["Forbidden", "Unauthorized", "Not Found", "Server Error"],
        1, "401 indicates that valid authentication credentials are missing or invalid."
    ),
    build_question(
        "What does HTTP status code 403 indicate?",
        ["Created", "Forbidden", "Redirect", "Not Modified"],
        1, "403 means the server understood the request but refuses authorization."
    ),
    build_question(
        "Which status code indicates that a requested resource was not found?",
        ["302", "404", "409", "503"],
        1, "404 Not Found indicates that the requested resource cannot be found."
    ),
    build_question(
        "Which HTTP header commonly identifies the media type of the request body?",
        ["Accept-Language", "Content-Type", "Host", "Referer"],
        1, "Content-Type specifies the media type of the message body."
    ),
    build_question(
        "Which HTTP method retrieves response headers without the response body?",
        ["GET", "HEAD", "POST", "PATCH"],
        1, "HEAD is like GET but the server does not return response content."
    ),

    # Web Storage (83-88)

    build_question(
        "Which browser storage persists data after the browser is closed?",
        ["Session Storage", "Local Storage", "Temporary DOM", "Event Storage"],
        1, "Local Storage generally persists until cleared by the user or application."
    ),
    build_question(
        "When does sessionStorage data normally become unavailable?",
        [
            "When the current page scrolls",
            "When the associated browsing session ends",
            "After every JavaScript function",
            "When a CSS file changes"
        ],
        1, "Session Storage is scoped to a page's browsing session and is cleared when that session ends."
    ),
    build_question(
        "Which method stores a value in localStorage?",
        ["localStorage.save()", "localStorage.setItem()", "localStorage.push()", "localStorage.add()"],
        1, "SetItem stores a key-value pair in localStorage."
    ),
    build_question(
        "What data type does localStorage return from getItem()?",
        ["Number", "Boolean", "String or null", "Object"],
        2, "GetItem returns a string when the key exists, otherwise null."
    ),
    build_question(
        "Which method removes one key from localStorage?",
        ["deleteItem()", "removeItem()", "clearKey()", "erase()"],
        1, "RemoveItem deletes the specified key."
    ),
    build_question(
        "What does localStorage.clear() do?",
        [
            "Removes one selected key",
            "Removes all keys from that storage area",
            "Closes the browser",
            "Deletes browser history"
        ],
        1, "Clear removes all keys from the local storage area for the origin."
    ),

    # Responsive Design (89-94)

    build_question(
        "What is the purpose of the viewport meta tag?",
        [
            "To define database permissions",
            "To control viewport dimensions and scaling on mobile browsers",
            "To load JavaScript modules",
            "To create CSS animations"
        ],
        1, "The viewport meta tag helps control layout viewport dimensions and scaling."
    ),
    build_question(
        "Which CSS approach adapts layouts to different screen sizes?",
        ["Fixed design", "Responsive design", "Static rendering", "Server routing"],
        1, "Responsive design adapts layouts to different viewport sizes."
    ),
    build_question(
        "Which CSS function is useful for fluid values with minimum and maximum limits?",
        ["limit()", "clamp()", "bound()", "range()"],
        1, "Clamp accepts a minimum, preferred value and maximum."
    ),
    build_question(
        "Which image property helps an image maintain its aspect ratio while filling available width?",
        ["width: 100%; height: 100%", "width: 100%; height: auto", "position: fixed", "float: left"],
        1, "Width 100% with automatic height preserves the intrinsic aspect ratio."
    ),
    build_question(
        "What is a CSS breakpoint?",
        [
            "A point where JavaScript stops",
            "A viewport threshold where responsive styles change",
            "A browser storage limit",
            "An HTML validation error"
        ],
        1, "Breakpoints define viewport conditions for responsive layout changes."
    ),
    build_question(
        "Which CSS unit is based on the viewport width?",
        ["vh", "vw", "rem", "em"],
        1, "One vw unit represents one percent of the viewport width."
    ),

    # Web Security (95-100)

    build_question(
        "What does XSS stand for?",
        [
            "Cross-Site Scripting",
            "External Server Security",
            "Cross-System Storage",
            "Extended Style Sheets"
        ],
        0, "XSS is Cross-Site Scripting, involving injection of malicious scripts into web content."
    ),
    build_question(
        "Which security practice helps prevent SQL injection?",
        [
            "Building SQL with string concatenation",
            "Using parameterized queries",
            "Disabling HTML forms",
            "Storing queries in CSS"
        ],
        1, "Parameterized queries separate SQL commands from supplied data."
    ),
    build_question(
        "What is the main purpose of HTTPS?",
        [
            "To compress HTML files",
            "To protect communication using TLS encryption and authentication",
            "To replace JavaScript",
            "To increase image resolution"
        ],
        1, "HTTPS uses TLS to protect data in transit and authenticate the server."
    ),
    build_question(
        "What is the purpose of the Same-Origin Policy?",
        [
            "To prevent all network requests",
            "To restrict certain interactions between different origins",
            "To disable browser storage",
            "To block all JavaScript execution"
        ],
        1, "The Same-Origin Policy restricts how documents and scripts from different origins interact."
    ),
    build_question(
        "Which security header helps control permitted content sources?",
        [
            "Content-Security-Policy",
            "Content-Length",
            "Accept-Encoding",
            "Cache-Control"
        ],
        0, "Content-Security-Policy controls permitted sources for resources loaded by a page."
    ),
    build_question(
        "What is CSRF?",
        [
            "A technique for compressing web resources",
            "An attack that tricks an authenticated browser into making an unwanted request",
            "A method for caching API responses",
            "A JavaScript module format"
        ],
        1, "Cross-Site Request Forgery tricks an authenticated user's browser into submitting an unwanted request."
    ),

]