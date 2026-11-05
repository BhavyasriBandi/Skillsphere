
_QUESTIONS = [

    # HTML BASICS (1-10)
    ("What does HTML stand for?", ["HyperText Markup Language", "HighText Machine Language", "Hyper Transfer Markup Language", "Home Tool Markup Language"], 0, "HTML stands for HyperText Markup Language."),
    ("Which HTML tag defines the main heading?", ["<head>", "<h1>", "<heading>", "<title>"], 1, "The h1 element represents the highest-level heading."),
    ("Which HTML tag creates a paragraph?", ["<para>", "<p>", "<text>", "<paragraph>"], 1, "The p element defines a paragraph."),
    ("Which HTML tag inserts a line break?", ["<break>", "<lb>", "<br>", "<line>"], 2, "The br element creates a line break."),
    ("Which HTML tag creates a hyperlink?", ["<link>", "<a>", "<href>", "<url>"], 1, "The a element creates a hyperlink."),
    ("Which attribute specifies the destination of a hyperlink?", ["src", "alt", "href", "target"], 2, "The href attribute specifies the link destination."),
    ("Which HTML tag displays an image?", ["<picture>", "<img>", "<image>", "<src>"], 1, "The img element embeds an image."),
    ("Which attribute provides alternative text for an image?", ["title", "src", "alt", "name"], 2, "The alt attribute provides alternative text."),
    ("Which HTML element defines the document title shown in the browser tab?", ["<body>", "<header>", "<title>", "<main>"], 2, "The title element defines the document title."),
    ("Which declaration identifies an HTML5 document?", ["<html5>", "<!DOCTYPE html>", "<DOCTYPE HTML5>", "<document html>"], 1, "The HTML5 doctype declaration is <!DOCTYPE html>."),

    # HTML ELEMENTS AND STRUCTURE (11-20)
    ("Which HTML element contains the visible page content?", ["<head>", "<body>", "<title>", "<meta>"], 1, "The body element contains the document's visible content."),
    ("Which element contains metadata and links to stylesheets?", ["<body>", "<footer>", "<head>", "<section>"], 2, "The head element contains document metadata and resource references."),
    ("Which tag creates an unordered list?", ["<ol>", "<ul>", "<li>", "<list>"], 1, "The ul element creates an unordered list."),
    ("Which tag creates an ordered list?", ["<ul>", "<li>", "<ol>", "<dl>"], 2, "The ol element creates an ordered list."),
    ("Which tag represents an individual list item?", ["<item>", "<li>", "<ul>", "<list>"], 1, "The li element represents a list item."),
    ("Which HTML element creates a table row?", ["<td>", "<th>", "<tr>", "<table-row>"], 2, "The tr element defines a table row."),
    ("Which HTML element creates a table header cell?", ["<td>", "<th>", "<tr>", "<thead-cell>"], 1, "The th element defines a header cell."),
    ("Which HTML element creates a table data cell?", ["<td>", "<th>", "<tr>", "<data>"], 0, "The td element defines a standard data cell."),
    ("Which semantic HTML element represents navigation links?", ["<navigate>", "<nav>", "<links>", "<menuitem>"], 1, "The nav element represents a navigation section."),
    ("Which semantic HTML element represents the main content of a page?", ["<main>", "<content>", "<body-main>", "<primary>"], 0, "The main element represents the dominant content of the document."),

    # HTML FORMS (21-30)
    ("Which HTML element creates a form?", ["<input>", "<form>", "<fieldset>", "<submit>"], 1, "The form element groups controls for submitting user data."),
    ("Which input type is used for an email address?", ["text", "mail", "email", "address"], 2, "The email input type is intended for email addresses."),
    ("Which input type hides the characters entered by a user?", ["hidden", "password", "secure", "private"], 1, "The password input type masks entered characters."),
    ("Which HTML element creates a drop-down list?", ["<input>", "<dropdown>", "<select>", "<optionlist>"], 2, "The select element creates a drop-down control."),
    ("Which element defines an option inside a select element?", ["<choice>", "<option>", "<item>", "<select-item>"], 1, "The option element defines a selectable choice."),
    ("Which input type allows selecting one option from a group?", ["checkbox", "radio", "button", "text"], 1, "Radio inputs allow one selection within a same-named group."),
    ("Which input type allows multiple independent selections?", ["radio", "checkbox", "password", "submit"], 1, "Checkbox inputs allow independent selections."),
    ("Which attribute makes a form field mandatory?", ["validate", "required", "must", "mandatory"], 1, "The required attribute prevents submission when the field is empty."),
    ("Which button type submits a form?", ["reset", "button", "submit", "send"], 2, "A button with type submit submits its associated form."),
    ("Which HTML element allows users to enter multiple lines of text?", ["<input>", "<textarea>", "<multiline>", "<text>"], 1, "The textarea element accepts multi-line text."),

    # CSS BASICS (31-40)
    ("What does CSS stand for?", ["Computer Style Sheets", "Cascading Style Sheets", "Creative Styling System", "Colorful Style Syntax"], 1, "CSS stands for Cascading Style Sheets."),
    ("Which HTML element is commonly used to link an external CSS file?", ["<css>", "<style>", "<link>", "<script>"], 2, "The link element connects an external stylesheet."),
    ("Which HTML element can contain internal CSS rules?", ["<css>", "<style>", "<script>", "<design>"], 1, "The style element contains internal CSS."),
    ("Which CSS property changes text color?", ["font-color", "text-color", "color", "foreground"], 2, "The color property sets text color."),
    ("Which CSS property changes the background color?", ["background-color", "color-background", "bgcolor", "background-style"], 0, "background-color sets an element's background color."),
    ("Which CSS property changes the font size?", ["text-size", "font-size", "font-style", "size"], 1, "font-size controls the size of text."),
    ("Which CSS selector targets an element by its ID?", [".", "#", "*", "&"], 1, "The # selector targets an element by ID."),
    ("Which CSS selector targets elements by class?", ["#", ".", "*", ":"], 1, "The dot selector targets elements by class."),
    ("Which CSS property makes text bold?", ["font-weight", "font-style", "text-decoration", "text-transform"], 0, "font-weight controls the boldness of text."),
    ("Which CSS property aligns text horizontally within its block?", ["text-align", "vertical-align", "align-items", "position"], 0, "text-align controls horizontal text alignment."),

    # CSS BOX MODEL AND LAYOUT (41-50)
    ("Which four areas are part of the CSS box model?", ["Content, padding, border, margin", "Text, image, color, font", "Width, height, position, display", "Header, body, footer, section"], 0, "The box model consists of content, padding, border and margin."),
    ("Which CSS property controls the space inside an element's border?", ["margin", "padding", "outline", "gap"], 1, "Padding is the space between content and border."),
    ("Which CSS property controls the space outside an element's border?", ["padding", "margin", "border-spacing", "line-height"], 1, "Margin creates space outside an element's border."),
    ("Which CSS property controls the border around an element?", ["outline-color", "border", "padding", "margin"], 1, "The border property sets an element's border."),
    ("Which CSS property controls how an element is displayed in the layout?", ["display", "visibility-mode", "layout", "render"], 0, "The display property determines an element's layout behavior."),
    ("Which display value makes an element a flex container?", ["display: block", "display: flex", "display: inline", "display: none"], 1, "display: flex enables Flexbox layout."),
    ("Which CSS property controls the direction of a flex container's main axis?", ["flex-direction", "justify-content", "align-items", "flex-wrap"], 0, "flex-direction sets the main axis direction."),
    ("Which CSS property distributes flex items along the main axis?", ["align-items", "justify-content", "align-content", "flex-grow"], 1, "justify-content distributes items along the main axis."),
    ("Which CSS property aligns flex items along the cross axis?", ["justify-content", "align-items", "flex-direction", "order"], 1, "align-items controls cross-axis alignment."),
    ("Which CSS layout system uses rows and columns?", ["Float", "CSS Grid", "Inline layout", "Text flow"], 1, "CSS Grid provides a two-dimensional row-and-column layout."),

    # CSS RESPONSIVE DESIGN (51-60)
    ("What is responsive web design?", ["A design that adapts to different screen sizes", "A design only for desktops", "A design without CSS", "A design using only images"], 0, "Responsive design adapts layouts to different devices and screen sizes."),
    ("Which CSS feature applies styles based on screen or device conditions?", ["@media", "@screen", "@device", "@responsive"], 0, "@media rules apply CSS based on media conditions."),
    ("What is the purpose of the viewport meta tag?", ["Set the browser's default font", "Control the layout viewport on mobile devices", "Connect a CSS file", "Load JavaScript"], 1, "The viewport meta tag helps control page scaling and layout on mobile devices."),
    ("Which CSS unit is relative to the root element's font size?", ["px", "em", "rem", "%"], 2, "rem is relative to the root element's font size."),
    ("Which CSS unit is relative to the font size of the element or its parent, depending on the property?", ["px", "em", "rem", "vw"], 1, "The em unit is relative to a font-size context."),
    ("Which CSS unit represents one percent of the viewport width?", ["vh", "vw", "rem", "pt"], 1, "1vw equals one percent of the viewport width."),
    ("Which CSS property can prevent content from overflowing its container?", ["overflow", "float", "font-style", "z-index"], 0, "The overflow property controls content that exceeds an element's box."),
    ("Which CSS property controls stacking order of positioned elements?", ["position", "z-index", "order", "display"], 1, "z-index controls the stacking order of positioned elements."),
    ("Which CSS value hides an element and removes it from normal layout?", ["visibility: hidden", "display: none", "opacity: 0", "position: hidden"], 1, "display: none removes the element from layout."),
    ("Which CSS value makes an element invisible while preserving its layout space?", ["display: none", "visibility: hidden", "position: none", "overflow: hidden"], 1, "visibility: hidden hides the element but preserves its layout space."),

    # JAVASCRIPT BASICS (61-70)
    ("What is JavaScript primarily used for in web development?", ["Adding interactivity and behavior", "Defining database tables", "Replacing HTML completely", "Creating image files only"], 0, "JavaScript adds behavior and interactivity to web pages."),
    ("Which HTML element is used to include JavaScript?", ["<javascript>", "<script>", "<js>", "<code>"], 1, "The script element embeds or references JavaScript."),
    ("Which keyword declares a block-scoped variable that can be reassigned?", ["const", "let", "static", "define"], 1, "let declares a block-scoped variable that can be reassigned."),
    ("Which keyword declares a block-scoped variable that cannot be reassigned?", ["var", "let", "const", "static"], 2, "const prevents reassignment of the variable binding."),
    ("Which symbol starts a single-line comment in JavaScript?", ["<!--", "//", "##", "**"], 1, "Two forward slashes start a single-line JavaScript comment."),
    ("Which function displays a message in the browser console?", ["alert()", "console.log()", "print()", "display()"], 1, "console.log() writes a message to the browser console."),
    ("Which operator checks strict equality in JavaScript?", ["=", "==", "===", "!="], 2, "The === operator compares values without type coercion."),
    ("Which operator is used for addition in JavaScript?", ["+", "&", "*", "%"], 0, "The plus operator performs addition or string concatenation."),
    ("Which JavaScript structure repeats a block while a condition is true?", ["if", "for", "switch", "return"], 1, "A for loop repeats code according to its conditions."),
    ("Which keyword defines a function in JavaScript?", ["method", "function", "define", "func"], 1, "The function keyword declares a function."),

    # JAVASCRIPT AND DOM (71-80)
    ("What does DOM stand for?", ["Document Object Model", "Data Output Method", "Document Oriented Mode", "Digital Object Management"], 0, "DOM stands for Document Object Model."),
    ("What does the DOM represent?", ["The page as a tree of objects", "A database table", "A CSS file", "A web server"], 0, "The DOM represents document elements as objects that scripts can access."),
    ("Which method selects an element by its ID?", ["getElementsByClassName()", "getElementById()", "queryById()", "selectId()"], 1, "getElementById selects an element by its ID."),
    ("Which method selects the first element matching a CSS selector?", ["querySelector()", "querySelectorAll()", "getAll()", "findElement()"], 0, "querySelector returns the first matching element."),
    ("Which method selects all elements matching a CSS selector?", ["querySelector()", "getElementById()", "querySelectorAll()", "selectFirst()"], 2, "querySelectorAll returns all matching elements."),
    ("Which property changes the text content of an element?", ["innerTextColor", "textContent", "textStyle", "nodeName"], 1, "textContent gets or sets an element's text content."),
    ("Which method attaches an event handler to an element?", ["attach()", "addEventListener()", "setEvent()", "listen()"], 1, "addEventListener registers an event listener."),
    ("Which event occurs when a user clicks an element?", ["change", "click", "load", "submit"], 1, "The click event occurs when an element is clicked."),
    ("Which event is commonly used when a form is submitted?", ["hover", "submit", "scroll", "focus"], 1, "The submit event fires when a form is submitted."),
    ("Which method prevents the default action of an event?", ["stop()", "preventDefault()", "cancelEvent()", "removeDefault()"], 1, "preventDefault prevents the browser's default event action."),

    # WEB AND HTTP BASICS (81-90)
    ("What does HTTP stand for?", ["HyperText Transfer Protocol", "High Transfer Text Program", "Hyperlink Transmission Process", "Home Text Transfer Protocol"], 0, "HTTP stands for HyperText Transfer Protocol."),
    ("What does HTTPS add to HTTP?", ["Encrypted communication using TLS", "A different HTML language", "Automatic database storage", "A faster JavaScript engine"], 0, "HTTPS protects communication using TLS."),
    ("Which HTTP method is commonly used to retrieve a resource?", ["POST", "GET", "DELETE", "PATCH"], 1, "GET requests a representation of a resource."),
    ("Which HTTP method is commonly used to submit data to create a resource?", ["GET", "POST", "HEAD", "OPTIONS"], 1, "POST submits data for processing and is commonly used to create resources."),
    ("Which HTTP status code means OK?", ["200", "301", "404", "500"], 0, "200 indicates a successful request."),
    ("Which HTTP status code means Not Found?", ["200", "201", "404", "503"], 2, "404 indicates that the requested resource was not found."),
    ("Which HTTP status code indicates an internal server error?", ["301", "400", "403", "500"], 3, "500 indicates an internal server error."),
    ("What does a URL identify?", ["The location of a resource", "Only a computer's password", "A CSS property", "A database table"], 0, "A URL identifies the location of a resource."),
    ("What does DNS do?", ["Translates domain names into IP addresses", "Styles HTML pages", "Executes JavaScript", "Stores browser history"], 0, "DNS resolves domain names to IP addresses and other DNS records."),
    ("What is a web browser?", ["Software used to access and display web content", "A database server", "A programming language", "A network cable"], 0, "A web browser retrieves and displays web content."),

    # CLIENT SERVER AND WEB CONCEPTS (91-100)
    ("What is the client in a client-server architecture?", ["The system that requests a service", "The system that only stores backups", "The database schema", "The web server's operating system"], 0, "A client sends requests to a server."),
    ("What is the role of a web server?", ["Receive requests and serve web resources", "Design HTML automatically", "Replace the browser", "Create CSS selectors"], 0, "A web server handles requests and delivers resources or application responses."),
    ("What is an IP address used for?", ["Identifying a device or network interface on an IP network", "Styling a web page", "Naming HTML elements", "Encrypting CSS"], 0, "IP addresses identify network interfaces for communication."),
    ("What is a domain name?", ["A human-readable name associated with internet resources", "A JavaScript variable", "An HTML form field", "A CSS selector"], 0, "Domain names provide human-readable names for internet resources."),
    ("What is a cookie in web development?", ["Small data stored by the browser for a website", "A CSS framework", "A type of HTML heading", "A database server"], 0, "Cookies store small pieces of data associated with a website."),
    ("What is localStorage used for?", ["Storing key-value data in the browser across sessions", "Sending emails", "Creating server databases", "Styling HTML"], 0, "localStorage stores browser data that persists across browser sessions."),
    ("What is sessionStorage used for?", ["Storing data for the lifetime of a page session", "Permanent server backups", "Creating CSS animations", "Resolving domain names"], 0, "sessionStorage stores data for the current page session."),
    ("What is an API?", ["An interface that allows software systems to communicate", "A CSS color format", "An HTML heading", "A browser bookmark"], 0, "An API defines how software components communicate."),
    ("What is JSON commonly used for in web applications?", ["Exchanging structured data", "Styling page layouts", "Creating hyperlinks", "Encrypting network connections"], 0, "JSON is a lightweight format for exchanging structured data."),
    ("What does responsive navigation help with?", ["Making navigation usable across different screen sizes", "Increasing database storage", "Changing HTTP status codes", "Creating server passwords"], 0, "Responsive navigation adapts to different devices and viewport sizes."),
]


QUESTION_BANK_WEB_BEGINNER1 = [
    {
        "skill": "Web Technologies",
        "difficulty": "beginner",
        "question_text": question,
        "options": options,
        "correct_answer": answer,
        "explanation": explanation,
    }
    for question, options, answer, explanation in _QUESTIONS
]
