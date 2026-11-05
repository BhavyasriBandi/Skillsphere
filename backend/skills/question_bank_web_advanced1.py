
def build_question(question, options, answer, explanation):
    return {
        "skill": "Web Technologies",
        "difficulty": "advanced",
        "question_text": question,
        "options": options,
        "correct_answer": answer,
        "explanation": explanation,
    }


QUESTION_BANK_WEB_ADVANCED1 = [

    # ========================================================
    # ADVANCED JAVASCRIPT (1-15)
    # ========================================================

    build_question(
        "What is the output of typeof NaN?",
        ["NaN", "undefined", "number", "object"],
        2, "NaN is a special numeric value, so typeof NaN returns number."
    ),
    build_question(
        "What does Object.freeze() do to an object?",
        [
            "Prevents adding, removing and changing its own properties",
            "Deletes all object properties",
            "Converts the object into JSON",
            "Makes every nested object deeply immutable"
        ],
        0, "Object.freeze prevents extensions and makes existing own properties non-writable and non-configurable. It is shallow."
    ),
    build_question(
        "Which method creates an object with a specified prototype?",
        [
            "Object.assign()",
            "Object.create()",
            "Object.freeze()",
            "Object.entries()"
        ],
        1, "Object.create creates a new object with the specified prototype."
    ),
    build_question(
        "What is the purpose of the JavaScript Proxy object?",
        [
            "To intercept and customize operations on another object",
            "To compile JavaScript into CSS",
            "To create database connections",
            "To execute code in another browser tab"
        ],
        0, "Proxy provides traps for operations such as property access, assignment and function calls."
    ),
    build_question(
        "Which method checks whether an object owns a particular property?",
        [
            "Object.hasOwn()",
            "Object.prototype()",
            "Object.includes()",
            "Object.contains()"
        ],
        0, "Object.hasOwn checks whether a property is a direct own property of an object."
    ),
    build_question(
        "What does the bind() method return?",
        [
            "The original function",
            "A new function with a bound this value and optional arguments",
            "A Promise",
            "An immediately executed function result"
        ],
        1, "Bind creates a new function with its this value and optionally initial arguments fixed."
    ),
    build_question(
        "What is the result of using the strict equality operator (===)?",
        [
            "It compares values after type conversion",
            "It compares values without type coercion",
            "It compares only object references",
            "It always returns a string"
        ],
        1, "Strict equality does not perform type coercion before comparison."
    ),
    build_question(
        "What is a JavaScript generator function declared with?",
        [
            "async function",
            "function*",
            "yield function",
            "generate()"
        ],
        1, "The function* syntax declares a generator function that can yield values."
    ),
    build_question(
        "What does the yield keyword do inside a generator?",
        [
            "Terminates the browser process",
            "Pauses generator execution and produces a value",
            "Converts a function into a Promise",
            "Restarts the function from the beginning"
        ],
        1, "Yield pauses generator execution and returns a value to the caller."
    ),
    build_question(
        "Which statement about JavaScript WeakMap is correct?",
        [
            "It accepts only string keys",
            "It holds weak references to its object keys",
            "It is directly iterable",
            "It prevents garbage collection of its keys"
        ],
        1, "WeakMap keys are weakly held, allowing their objects to be garbage-collected when otherwise unreachable."
    ),
    build_question(
        "What is the purpose of Symbol in JavaScript?",
        [
            "To create unique primitive values",
            "To define CSS variables",
            "To convert arrays into objects",
            "To create asynchronous functions"
        ],
        0, "Symbol creates unique primitive values commonly used as property keys."
    ),
    build_question(
        "What does Object.defineProperty() allow developers to configure?",
        [
            "Only an object's prototype",
            "Property descriptors such as writable, enumerable and configurable",
            "Only array indexes",
            "Browser storage permissions"
        ],
        1, "DefineProperty creates or modifies a property with configurable descriptor attributes."
    ),
    build_question(
        "What is the main purpose of optional chaining (?.)?",
        [
            "To prevent all runtime errors",
            "To safely access properties through nullish values",
            "To convert objects into arrays",
            "To enforce strict equality"
        ],
        1, "Optional chaining short-circuits with undefined when the accessed base is null or undefined."
    ),
    build_question(
        "Which method returns an array of an object's own enumerable string-keyed property pairs?",
        [
            "Object.keys()",
            "Object.values()",
            "Object.entries()",
            "Object.getPrototypeOf()"
        ],
        2, "Object.entries returns key-value pairs for own enumerable string-keyed properties."
    ),
    build_question(
        "What is the purpose of the Reflect API?",
        [
            "To provide methods for interceptable JavaScript object operations",
            "To render HTML elements",
            "To encrypt browser cookies",
            "To manage CSS animations"
        ],
        0, "Reflect provides methods corresponding to fundamental object operations, often used with Proxy."
    ),

    # ========================================================
    # EVENT LOOP AND ASYNCHRONOUS PROGRAMMING (16-25)
    # ========================================================

    build_question(
        "In the standard browser event loop model, when are queued microtasks normally processed?",
        [
            "Before the current JavaScript execution finishes",
            "After the current task completes and before the next task begins",
            "Only after the browser closes",
            "Only when setInterval executes"
        ],
        1, "The microtask queue is generally drained after a task completes and before the next task."
    ),
    build_question(
        "Which callback is commonly scheduled as a microtask?",
        [
            "setTimeout callback",
            "Promise.then callback",
            "setInterval callback",
            "A normal click event handler"
        ],
        1, "Promise reaction callbacks are scheduled as microtasks."
    ),
    build_question(
        "What is the purpose of Promise.allSettled()?",
        [
            "To reject immediately when one Promise rejects",
            "To wait for all input Promises to settle and report each outcome",
            "To return only the first fulfilled Promise",
            "To cancel all pending Promises"
        ],
        1, "Promise.allSettled fulfills after every input settles and provides each result status."
    ),
    build_question(
        "What does Promise.race() return?",
        [
            "The result of every Promise",
            "The first input Promise that settles",
            "Only the first fulfilled Promise",
            "An array of rejected Promises"
        ],
        1, "Promise.race settles with the outcome of the first input Promise to settle."
    ),
    build_question(
        "What is the purpose of AbortSignal.timeout()?",
        [
            "To retry a request indefinitely",
            "To create a signal that aborts after a specified time",
            "To delay JavaScript execution",
            "To clear all browser timers"
        ],
        1, "AbortSignal.timeout creates a signal that aborts after the specified active time."
    ),
    build_question(
        "What is the primary purpose of requestAnimationFrame()?",
        [
            "To schedule work before a browser repaint",
            "To send HTTP requests",
            "To execute code every fixed second",
            "To store data in browser memory"
        ],
        0, "RequestAnimationFrame schedules a callback before the next repaint when the browser is ready."
    ),
    build_question(
        "What is the purpose of queueMicrotask()?",
        [
            "To add a callback to the microtask queue",
            "To add a callback to localStorage",
            "To create a Web Worker",
            "To execute a callback after a network response only"
        ],
        0, "QueueMicrotask schedules a callback in the microtask queue."
    ),
    build_question(
        "Which statement about async functions is correct?",
        [
            "They always return a Promise",
            "They always return a number",
            "They cannot use try/catch",
            "They execute in a separate operating-system process"
        ],
        0, "An async function always returns a Promise, adopting the returned value or Promise outcome."
    ),
    build_question(
        "What is the purpose of a Web Worker?",
        [
            "To execute JavaScript in a background worker thread",
            "To replace the browser's rendering engine",
            "To directly modify the DOM from another thread",
            "To store HTTP responses permanently"
        ],
        0, "Web Workers execute scripts separately from the main thread and communicate through messages."
    ),
    build_question(
        "How does a standard dedicated Web Worker communicate with its creating page?",
        [
            "Direct DOM access",
            "postMessage() and message events",
            "CSS selectors",
            "Shared local variables"
        ],
        1, "Dedicated workers communicate with their owner through message passing."
    ),

    # ========================================================
    # DOM AND BROWSER INTERNALS (26-35)
    # ========================================================

    build_question(
        "What is the DOM?",
        [
            "A database query language",
            "A programming interface representing a document as a node tree",
            "A CSS compilation tool",
            "A browser networking protocol"
        ],
        1, "The DOM represents document structure as objects that scripts can inspect and modify."
    ),
    build_question(
        "What is event delegation?",
        [
            "Attaching individual handlers to every child",
            "Handling descendant events through a common ancestor",
            "Removing all event listeners",
            "Preventing events from reaching the document"
        ],
        1, "Event delegation uses event propagation so an ancestor can handle events from its descendants."
    ),
    build_question(
        "What does the capture phase of event propagation represent?",
        [
            "Movement from the target toward ancestors",
            "Movement from ancestors toward the target",
            "Execution after bubbling finishes",
            "Execution only on the document body"
        ],
        1, "During capture, an event travels from the outer ancestors toward the target."
    ),
    build_question(
        "Which property represents the element whose listener is currently executing?",
        [
            "event.target",
            "event.currentTarget",
            "event.source",
            "event.origin"
        ],
        1, "CurrentTarget identifies the element to which the current event listener is attached."
    ),
    build_question(
        "What is the purpose of MutationObserver?",
        [
            "To observe changes to the DOM tree",
            "To observe network speed",
            "To track keyboard hardware",
            "To measure CSS file size"
        ],
        0, "MutationObserver asynchronously observes configured DOM mutations."
    ),
    build_question(
        "What is the purpose of IntersectionObserver?",
        [
            "To observe an element's intersection with a viewport or another root",
            "To compare JavaScript objects",
            "To monitor API authentication",
            "To detect database changes"
        ],
        0, "IntersectionObserver reports changes in the intersection of a target and its root."
    ),
    build_question(
        "Which browser API measures performance entries such as navigation and resource timing?",
        [
            "Performance API",
            "Storage API",
            "Canvas API",
            "History API"
        ],
        0, "The Performance API exposes timing and performance entry information."
    ),
    build_question(
        "What does the browser's critical rendering path describe?",
        [
            "Steps involved in converting HTML, CSS and scripts into rendered pixels",
            "Steps used to authenticate a database",
            "The sequence of HTTP status codes",
            "The browser's download history"
        ],
        0, "The critical rendering path covers processing resources and constructing the render output."
    ),
    build_question(
        "What is layout thrashing?",
        [
            "Repeated layout recalculations caused by interleaved DOM writes and layout reads",
            "Repeated HTTP redirects",
            "Repeated JavaScript compilation",
            "Repeated browser cache deletion"
        ],
        0, "Interleaving layout-affecting writes with forced layout reads can trigger expensive synchronous recalculations."
    ),
    build_question(
        "Which browser API can observe changes to an element's dimensions?",
        [
            "ResizeObserver",
            "MutationObserver only",
            "HistoryObserver",
            "NetworkObserver"
        ],
        0, "ResizeObserver reports changes to an element's content or border box dimensions."
    ),

    # ========================================================
    # HTTP, REST AND NETWORKING (36-45)
    # ========================================================

    build_question(
        "What does HTTP status code 304 indicate?",
        [
            "Created",
            "Not Modified",
            "Bad Gateway",
            "Unauthorized"
        ],
        1, "304 indicates that a conditional request can use a cached representation."
    ),
    build_question(
        "Which HTTP header is commonly used with ETag for conditional requests?",
        [
            "If-None-Match",
            "Content-Length",
            "Accept-Encoding",
            "Location"
        ],
        0, "If-None-Match sends entity tags so a server can determine whether the representation changed."
    ),
    build_question(
        "Which HTTP method is defined as safe and idempotent?",
        [
            "POST",
            "GET",
            "PATCH",
            "CONNECT"
        ],
        1, "GET is a safe and idempotent HTTP method."
    ),
    build_question(
        "What does HTTP status code 429 indicate?",
        [
            "Resource not found",
            "Too Many Requests",
            "Internal Server Error",
            "Permanent Redirect"
        ],
        1, "429 indicates that the client has sent too many requests in a given period."
    ),
    build_question(
        "Which header can communicate a suggested retry delay after rate limiting?",
        [
            "Retry-After",
            "Content-Type",
            "Origin",
            "ETag"
        ],
        0, "Retry-After can indicate when the client should retry."
    ),
    build_question(
        "What is the purpose of CORS?",
        [
            "To control cross-origin access to resources through HTTP headers",
            "To compress JavaScript files",
            "To encrypt all database records",
            "To replace HTTPS"
        ],
        0, "CORS uses HTTP headers to allow servers to declare permitted cross-origin browser access."
    ),
    build_question(
        "When is a CORS preflight request commonly sent?",
        [
            "Before every same-origin GET request",
            "When a cross-origin request requires a preflight under CORS rules",
            "Only after a 500 response",
            "Whenever a webpage loads an image"
        ],
        1, "The browser sends an OPTIONS preflight for cross-origin requests that do not qualify as simple requests."
    ),
    build_question(
        "Which HTTP status code indicates a gateway received an invalid response from an upstream server?",
        [
            "400",
            "502",
            "401",
            "204"
        ],
        1, "502 Bad Gateway indicates an invalid response received by a gateway or proxy."
    ),
    build_question(
        "What is the primary purpose of HTTP content negotiation?",
        [
            "To select an appropriate representation based on request preferences",
            "To generate database schemas",
            "To authenticate users with passwords",
            "To create browser sessions"
        ],
        0, "Content negotiation selects representations using headers such as Accept and Accept-Language."
    ),
    build_question(
        "Which HTTP header indicates the preferred response media types?",
        [
            "Content-Type",
            "Accept",
            "Host",
            "Authorization"
        ],
        1, "Accept communicates media types the client can process."
    ),

    # ========================================================
    # WEB SECURITY (46-60)
    # ========================================================

    build_question(
        "What is the main purpose of a Content Security Policy nonce?",
        [
            "To allow specifically authorized inline scripts or styles",
            "To encrypt all HTTP requests",
            "To replace authentication tokens",
            "To prevent browser caching"
        ],
        0, "A CSP nonce is a unique token included in the policy and authorized script or style element."
    ),
    build_question(
        "Which cookie attribute helps prevent JavaScript from accessing a cookie?",
        [
            "Secure",
            "HttpOnly",
            "SameSite",
            "Domain"
        ],
        1, "HttpOnly prevents access through non-HTTP APIs such as document.cookie."
    ),
    build_question(
        "What is the purpose of the Secure cookie attribute?",
        [
            "To send the cookie only over secure channels such as HTTPS",
            "To make a cookie available to JavaScript",
            "To make a cookie permanent",
            "To prevent all cross-site requests"
        ],
        0, "Secure restricts cookie transmission to secure channels."
    ),
    build_question(
        "Which cookie attribute helps control cross-site cookie sending?",
        [
            "Path",
            "SameSite",
            "Max-Age",
            "Expires"
        ],
        1, "SameSite controls whether cookies are sent with cross-site requests."
    ),
    build_question(
        "What is the primary risk of storing sensitive authentication tokens in localStorage?",
        [
            "They are automatically encrypted",
            "JavaScript running in the origin can access them, including injected scripts",
            "They are inaccessible to browser scripts",
            "They expire after every page navigation"
        ],
        1, "An XSS vulnerability can allow malicious same-origin JavaScript to read localStorage tokens."
    ),
    build_question(
        "What is the purpose of a CSRF token?",
        [
            "To help verify that a state-changing request was intentionally initiated by the application",
            "To compress request bodies",
            "To replace HTTPS encryption",
            "To validate CSS selectors"
        ],
        0, "CSRF tokens provide an unpredictable request value that the server validates."
    ),
    build_question(
        "What is clickjacking?",
        [
            "Tricking a user into interacting with an embedded or disguised interface",
            "Stealing a browser's cache files",
            "Injecting SQL into a database",
            "Overloading a DNS server"
        ],
        0, "Clickjacking uses deceptive framing or overlays to trick users into unintended interactions."
    ),
    build_question(
        "Which response header can restrict which sites may embed a page in a frame?",
        [
            "X-Frame-Options",
            "Accept-Encoding",
            "Content-Length",
            "ETag"
        ],
        0, "X-Frame-Options can restrict framing; CSP frame-ancestors provides a more flexible policy."
    ),
    build_question(
        "What is the main purpose of Subresource Integrity (SRI)?",
        [
            "To verify that fetched external resources match an expected cryptographic hash",
            "To automatically update JavaScript packages",
            "To encrypt HTML source code",
            "To prevent all cookies"
        ],
        0, "SRI uses a cryptographic hash to verify the integrity of externally loaded resources."
    ),
    build_question(
        "Which security practice is most appropriate for password storage?",
        [
            "Store plaintext passwords",
            "Use a dedicated password hashing algorithm with salts",
            "Encrypt passwords with Base64",
            "Store passwords in HTML comments"
        ],
        1, "Passwords should be stored using password hashing algorithms such as Argon2, scrypt or bcrypt."
    ),
    build_question(
        "What is the purpose of TLS certificate validation?",
        [
            "To verify the server's identity and certificate trust",
            "To validate CSS syntax",
            "To increase image resolution",
            "To create browser cookies"
        ],
        0, "Certificate validation helps establish that the server identity is trusted for the requested hostname."
    ),
    build_question(
        "What is a DOM-based XSS vulnerability?",
        [
            "A vulnerability caused by unsafe client-side handling of untrusted data in the DOM",
            "A vulnerability caused only by SQL queries",
            "A vulnerability in DNS caching",
            "A vulnerability caused by image compression"
        ],
        0, "DOM-based XSS occurs when client-side code uses untrusted input in an unsafe DOM operation."
    ),
    build_question(
        "Which method is safer for inserting untrusted plain text into an HTML element?",
        [
            "innerHTML",
            "textContent",
            "document.write()",
            "insertAdjacentHTML()"
        ],
        1, "TextContent inserts text without interpreting it as HTML markup."
    ),
    build_question(
        "What does the principle of least privilege mean?",
        [
            "Give every user administrator access",
            "Grant only the permissions required to perform assigned tasks",
            "Disable all user authentication",
            "Store all application secrets in frontend code"
        ],
        1, "Least privilege limits access rights to the minimum necessary."
    ),
    build_question(
        "What is the purpose of the Permissions Policy HTTP header?",
        [
            "To control which browser features and APIs a document can use",
            "To control database indexes",
            "To define JavaScript variable scopes",
            "To select image formats"
        ],
        0, "Permissions Policy lets a site restrict the use of selected browser features."
    ),

    # ========================================================
    # ADVANCED CSS AND RESPONSIVE DESIGN (61-70)
    # ========================================================

    build_question(
        "What does CSS contain: layout: inline-size enable?",
        [
            "Inline-size containment for container query evaluation",
            "A fixed viewport width",
            "A global JavaScript variable",
            "An HTML form validation rule"
        ],
        0, "Inline-size containment establishes containment in the inline dimension for container queries."
    ),
    build_question(
        "Which CSS at-rule defines styles based on a container's size?",
        [
            "@media",
            "@container",
            "@supports",
            "@layer"
        ],
        1, "Container queries use @container to apply styles based on a query container."
    ),
    build_question(
        "What is the purpose of CSS cascade layers?",
        [
            "To organize and control cascade precedence among groups of CSS rules",
            "To create image layers only",
            "To replace media queries",
            "To control JavaScript execution order"
        ],
        0, "Cascade layers establish explicit ordering for groups of CSS declarations."
    ),
    build_question(
        "Which CSS property controls whether an element establishes a stacking context through opacity?",
        [
            "opacity",
            "margin",
            "font-size",
            "letter-spacing"
        ],
        0, "An opacity value less than 1 creates a stacking context."
    ),
    build_question(
        "Which property can prevent a flex item from shrinking below its content-based minimum size?",
        [
            "min-width: auto",
            "flex-grow: 0",
            "order: 0",
            "align-items: center"
        ],
        0, "The default min-width:auto can preserve a content-based minimum size; explicitly setting min-width:0 permits shrinking."
    ),
    build_question(
        "What does the CSS minmax() function do in Grid?",
        [
            "Defines a track's minimum and maximum sizing constraints",
            "Creates a media query",
            "Sets minimum font weight",
            "Defines an animation duration"
        ],
        0, "Minmax defines a grid track size with minimum and maximum limits."
    ),
    build_question(
        "Which CSS property controls how an element handles content that exceeds its box?",
        [
            "overflow",
            "visibility",
            "position",
            "transform"
        ],
        0, "Overflow controls how content outside an element's box is handled."
    ),
    build_question(
        "What does transform: translateZ(0) commonly do in browser rendering?",
        [
            "It can trigger creation of a composited layer, depending on the browser",
            "It always improves performance",
            "It removes the element from the DOM",
            "It disables GPU rendering"
        ],
        0, "A 3D transform may cause compositing, but layer promotion and performance effects are browser-dependent."
    ),
    build_question(
        "Which CSS feature allows a property to transition between declared values?",
        [
            "transition",
            "outline",
            "float",
            "clear"
        ],
        0, "Transition animates changes in supported CSS property values over time."
    ),
    build_question(
        "What does the prefers-reduced-motion media feature detect?",
        [
            "A user's operating-system preference for reduced motion",
            "The browser's network speed",
            "The user's screen brightness",
            "The available device storage"
        ],
        0, "Prefers-reduced-motion detects a system preference to minimize non-essential motion."
    ),

    # ========================================================
    # WEB PERFORMANCE AND OPTIMIZATION (71-80)
    # ========================================================

    build_question(
        "What is the purpose of code splitting?",
        [
            "To divide application code into smaller bundles loaded when needed",
            "To combine all database records",
            "To duplicate every JavaScript function",
            "To remove browser caching"
        ],
        0, "Code splitting reduces initial loading by dividing code into separately loadable chunks."
    ),
    build_question(
        "What is tree shaking in frontend bundling?",
        [
            "Removing unused exports from the final bundle",
            "Compressing image dimensions",
            "Deleting browser cookies",
            "Splitting CSS into media queries"
        ],
        0, "Tree shaking removes code that bundlers determine is unused, commonly using ES module static analysis."
    ),
    build_question(
        "What does lazy loading achieve for below-the-fold images?",
        [
            "Defers loading until images are closer to being needed",
            "Loads every image before HTML parsing",
            "Converts images to SVG",
            "Prevents images from being cached"
        ],
        0, "Lazy loading defers offscreen image fetching until they approach the viewport."
    ),
    build_question(
        "Which technique can reduce layout shifts caused by images?",
        [
            "Specify image dimensions or aspect ratio",
            "Remove all image alt attributes",
            "Use larger JavaScript bundles",
            "Disable browser caching"
        ],
        0, "Reserving image space using dimensions or aspect-ratio reduces unexpected layout shifts."
    ),
    build_question(
        "What does Largest Contentful Paint (LCP) measure?",
        [
            "The render time of the largest visible content element",
            "The number of JavaScript functions",
            "The total number of CSS selectors",
            "The time needed to close a browser tab"
        ],
        0, "LCP measures when the largest content element in the viewport is rendered."
    ),
    build_question(
        "What does Cumulative Layout Shift (CLS) measure?",
        [
            "Unexpected visual layout movement",
            "Total network requests",
            "JavaScript execution count",
            "Database response time"
        ],
        0, "CLS quantifies unexpected visual stability shifts during a page's lifetime."
    ),
    build_question(
        "What does Interaction to Next Paint (INP) evaluate?",
        [
            "Responsiveness of interactions across a page visit",
            "Image file compression",
            "Total page HTML size",
            "DNS record expiration"
        ],
        0, "INP measures interaction responsiveness using observed interaction latency."
    ),
    build_question(
        "Which resource hint indicates that a resource is likely to be needed for the current navigation?",
        [
            "preload",
            "prefetch",
            "dns-prefetch",
            "prerender"
        ],
        0, "Preload requests a resource needed by the current page as early as possible."
    ),
    build_question(
        "What is the purpose of the Cache-Control: immutable directive?",
        [
            "To indicate that a fresh response will not change during its freshness lifetime",
            "To prevent the browser from storing a response",
            "To force every request to the server",
            "To delete cached files immediately"
        ],
        0, "Immutable indicates that a fresh representation is not expected to change during its freshness lifetime."
    ),
    build_question(
        "Which technique reduces repeated network requests for unchanged resources?",
        [
            "HTTP caching",
            "Disabling response headers",
            "Removing resource URLs",
            "Repeated hard refreshes"
        ],
        0, "HTTP caching allows reusable responses to be served without repeating full network transfers."
    ),

    # ========================================================
    # STORAGE, SERVICE WORKERS AND OFFLINE WEB (81-88)
    # ========================================================

    build_question(
        "What is the primary purpose of a Service Worker?",
        [
            "To act as a programmable network proxy for supported web requests",
            "To directly change the page DOM",
            "To replace the browser engine",
            "To store passwords in plaintext"
        ],
        0, "Service Workers can intercept eligible requests and support caching and background capabilities."
    ),
    build_question(
        "Which API is commonly used with Service Workers for offline resource caching?",
        [
            "Cache API",
            "Canvas API",
            "Geolocation API",
            "History API"
        ],
        0, "The Cache API stores request-response pairs for reuse, commonly in Service Workers."
    ),
    build_question(
        "What does IndexedDB provide?",
        [
            "A transactional client-side database for structured data",
            "A CSS animation engine",
            "A server-side SQL database",
            "An HTTP authentication protocol"
        ],
        0, "IndexedDB is an asynchronous transactional database for structured browser-side data."
    ),
    build_question(
        "Which browser storage mechanism is suitable for larger structured client-side datasets?",
        [
            "IndexedDB",
            "URL fragments",
            "CSS custom properties",
            "HTML comments"
        ],
        0, "IndexedDB supports structured data and larger datasets than simple key-value storage."
    ),
    build_question(
        "What is the purpose of the Broadcast Channel API?",
        [
            "To communicate between browsing contexts of the same origin",
            "To broadcast audio to all websites",
            "To send SQL queries to a server",
            "To replace HTTP requests"
        ],
        0, "BroadcastChannel enables messaging among same-origin browsing contexts."
    ),
    build_question(
        "What is the main purpose of the Cache API's match() method?",
        [
            "To find a stored response matching a request",
            "To remove every cached resource",
            "To create a new Service Worker",
            "To change an HTTP request method"
        ],
        0, "Cache.match searches stored entries for a matching request."
    ),
    build_question(
        "Which event is commonly used to activate a newly installed Service Worker?",
        [
            "activate",
            "DOMContentLoaded",
            "resize",
            "submit"
        ],
        0, "The activate event runs when a Service Worker becomes active."
    ),
    build_question(
        "What is the purpose of navigator.onLine?",
        [
            "To provide an indication of the browser's network connectivity state",
            "To guarantee that a remote API is reachable",
            "To measure internet bandwidth exactly",
            "To verify server authentication"
        ],
        0, "Navigator.onLine indicates a browser connectivity status but does not guarantee internet or server reachability."
    ),

    # ========================================================
    # ACCESSIBILITY AND SEMANTIC WEB (89-94)
    # ========================================================

    build_question(
        "What is the primary purpose of ARIA attributes?",
        [
            "To improve accessibility semantics for assistive technologies",
            "To replace all HTML elements",
            "To execute JavaScript asynchronously",
            "To encrypt form data"
        ],
        0, "ARIA communicates roles, states and properties to assistive technologies."
    ),
    build_question(
        "Which ARIA attribute can identify an element as a live region?",
        [
            "aria-live",
            "aria-hidden",
            "aria-label",
            "aria-current"
        ],
        0, "Aria-live announces relevant updates in a region to assistive technology."
    ),
    build_question(
        "What is the purpose of semantic HTML?",
        [
            "To communicate the meaning and structure of content",
            "To automatically encrypt webpages",
            "To replace CSS styling",
            "To prevent all browser errors"
        ],
        0, "Semantic HTML provides meaningful structure that benefits accessibility and document understanding."
    ),
    build_question(
        "Which attribute provides an accessible name for an element when visible text is unavailable?",
        [
            "aria-label",
            "aria-hidden",
            "aria-expanded",
            "aria-disabled"
        ],
        0, "Aria-label supplies an accessible name for an element."
    ),
    build_question(
        "What is keyboard accessibility?",
        [
            "The ability to operate interface functionality using a keyboard",
            "The ability to change keyboard colors",
            "The ability to disable all mouse events",
            "The ability to run JavaScript without a browser"
        ],
        0, "Keyboard accessibility ensures interactive features can be operated without a mouse."
    ),
    build_question(
        "What is the purpose of a visible focus indicator?",
        [
            "To show which interactive element currently has keyboard focus",
            "To indicate the browser's download progress",
            "To display network latency",
            "To identify cached images"
        ],
        0, "A focus indicator helps users identify the currently focused interactive element."
    ),

    # ========================================================
    # ARCHITECTURE AND TESTING (95-100)
    # ========================================================

    build_question(
        "What is the main purpose of the Model-View-Controller pattern?",
        [
            "To separate application data, presentation and control responsibilities",
            "To combine HTML and SQL into one file",
            "To eliminate all API requests",
            "To replace browser event handling"
        ],
        0, "MVC separates model, view and controller responsibilities."
    ),
    build_question(
        "What is the primary purpose of a Content Delivery Network (CDN)?",
        [
            "To distribute content through geographically distributed servers",
            "To replace the application's database",
            "To compile JavaScript in the browser",
            "To create authentication tokens"
        ],
        0, "A CDN serves content from distributed locations closer to users."
    ),
    build_question(
        "What is the purpose of unit testing in frontend development?",
        [
            "To test small individual units of code in isolation",
            "To test the entire production network only",
            "To measure internet bandwidth",
            "To replace accessibility testing"
        ],
        0, "Unit tests verify individual functions or components independently."
    ),
    build_question(
        "What is the main goal of end-to-end testing?",
        [
            "To validate complete user workflows across application layers",
            "To test only one CSS property",
            "To check only JavaScript syntax",
            "To measure only image dimensions"
        ],
        0, "End-to-end tests validate application behavior through realistic user workflows."
    ),
    build_question(
        "What is the purpose of a frontend build tool?",
        [
            "To transform, bundle and optimize application resources",
            "To replace the browser's DOM",
            "To store user passwords",
            "To host the production database automatically"
        ],
        0, "Build tools process source code and assets into deployable application resources."
    ),
    build_question(
        "What is the main purpose of Progressive Web App (PWA) technology?",
        [
            "To provide app-like web experiences with capabilities such as installation and offline support",
            "To convert every website into a native desktop executable",
            "To eliminate HTML and CSS",
            "To make all web applications serverless"
        ],
        0, "PWAs use web technologies and capabilities such as service workers and web app manifests to provide app-like experiences."
    ),

]
