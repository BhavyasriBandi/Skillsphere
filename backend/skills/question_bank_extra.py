
QUESTION_BANK_EXTRA = [
    {
        "skill": "Data Structures",
        "difficulty": "beginner",
        "questions": [
            {
                "question_text": "Which data structure allows insertion and deletion at both ends?",
                "options": ["Simple Stack", "Deque", "Binary Tree", "Hash Table"],
                "correct_answer": 1,
                "explanation": "A deque allows insertion and deletion at both the front and rear."
            },
            {
                "question_text": "Which data structure is commonly used to implement a browser's back button?",
                "options": ["Queue", "Stack", "Graph", "Array"],
                "correct_answer": 1,
                "explanation": "A stack stores browsing history so the most recently visited page can be revisited first."
            },
            {
                "question_text": "What is the main purpose of a hash function?",
                "options": ["Sort elements", "Convert a key into a hash value", "Reverse a list", "Create a tree"],
                "correct_answer": 1,
                "explanation": "A hash function maps a key to a hash value used to determine its storage location."
            },
            {
                "question_text": "Which data structure is generally used to implement a priority queue?",
                "options": ["Heap", "Stack", "Simple Array only", "Linked List only"],
                "correct_answer": 0,
                "explanation": "A heap efficiently supports retrieving the highest- or lowest-priority element."
            },
            {
                "question_text": "In a singly linked list, what does the last node point to?",
                "options": ["The first node", "The previous node", "Null", "The middle node"],
                "correct_answer": 2,
                "explanation": "The last node points to null, indicating the end of a singly linked list."
            },
            {
                "question_text": "Which linked list allows traversal in both forward and backward directions?",
                "options": ["Singly Linked List", "Doubly Linked List", "Circular Queue", "Stack"],
                "correct_answer": 1,
                "explanation": "A doubly linked list stores references to both the next and previous nodes."
            },
            {
                "question_text": "What is the first index of a typical zero-indexed array?",
                "options": ["0", "1", "-1", "2"],
                "correct_answer": 0,
                "explanation": "In zero-indexed arrays, the first element is stored at index 0."
            },
            {
                "question_text": "Which traversal visits the root node before its subtrees?",
                "options": ["Inorder", "Postorder", "Preorder", "Level order"],
                "correct_answer": 2,
                "explanation": "Preorder traversal visits the root first, followed by the left and right subtrees."
            },
            {
                "question_text": "Which traversal visits the root node after its subtrees?",
                "options": ["Preorder", "Inorder", "Postorder", "Level order"],
                "correct_answer": 2,
                "explanation": "Postorder traversal visits the left subtree, right subtree, and then the root."
            },
            {
                "question_text": "Which data structure is used to represent a collection of unique elements?",
                "options": ["Set", "Queue", "Stack", "Linked List"],
                "correct_answer": 0,
                "explanation": "A set stores unique elements and does not allow duplicate values."
            },
            {
                "question_text": "What is a cycle in a graph?",
                "options": ["A path that starts and ends at the same vertex", "A vertex with no edges", "A disconnected vertex", "A graph with one vertex"],
                "correct_answer": 0,
                "explanation": "A cycle is a path that returns to its starting vertex."
            },
            {
                "question_text": "What is an edge in a graph?",
                "options": ["A data value", "A connection between two vertices", "The root node", "An array position"],
                "correct_answer": 1,
                "explanation": "An edge represents a connection between two vertices in a graph."
            },
            {
                "question_text": "Which data structure is commonly used for function call management?",
                "options": ["Queue", "Stack", "Graph", "Hash Set"],
                "correct_answer": 1,
                "explanation": "The call stack manages function calls and their execution contexts."
            },
            {
                "question_text": "What is the time complexity of searching an unsorted array using linear search in the worst case?",
                "options": ["O(1)", "O(log n)", "O(n)", "O(n²)"],
                "correct_answer": 2,
                "explanation": "Linear search may need to examine every element, resulting in O(n) time."
            },
            {
                "question_text": "Which condition must be satisfied before applying binary search to a standard array?",
                "options": ["The array must be sorted", "The array must contain duplicates", "The array must have an even length", "The array must contain strings"],
                "correct_answer": 0,
                "explanation": "Binary search requires sorted data so it can eliminate half of the search range at each step."
            },
            {
                "question_text": "What is the main advantage of a linked list over a fixed-size array?",
                "options": ["Constant-time access by index", "Dynamic size", "Always uses less memory", "Automatic sorting"],
                "correct_answer": 1,
                "explanation": "A linked list can grow or shrink dynamically as nodes are added or removed."
            },
            {
                "question_text": "Which data structure is suitable for managing tasks in the order they arrive?",
                "options": ["Stack", "Queue", "Heap only", "Tree"],
                "correct_answer": 1,
                "explanation": "A queue processes tasks in FIFO order."
            },
            {
                "question_text": "What is the height of a tree commonly measured by?",
                "options": ["Number of edges on the longest root-to-leaf path", "Number of array elements", "Number of graph cycles", "Number of leaf values only"],
                "correct_answer": 0,
                "explanation": "Tree height is commonly measured by the number of edges in the longest path from the root to a leaf."
            },
            {
                "question_text": "Which structure is commonly used to represent a sparse matrix efficiently?",
                "options": ["Triplet representation", "A full stack", "A simple queue", "A binary search tree only"],
                "correct_answer": 0,
                "explanation": "Triplet representation stores only non-zero values along with their row and column positions."
            },
            {
                "question_text": "What does FIFO stand for?",
                "options": ["First In, First Out", "Fast In, Fast Out", "First Index, First Order", "Final In, First Out"],
                "correct_answer": 0,
                "explanation": "FIFO means the first element inserted is the first element removed."
            },
            {
                "question_text": "Which data structure is commonly used to implement recursion?",
                "options": ["Queue", "Stack", "Graph", "Hash Table"],
                "correct_answer": 1,
                "explanation": "Recursion uses the call stack to manage function calls."
            },
            {
                "question_text": "What is the main purpose of a binary search tree?",
                "options": ["Store elements randomly", "Organize values for efficient searching", "Process elements in FIFO order", "Store only strings"],
                "correct_answer": 1,
                "explanation": "A binary search tree organizes values so searching can be efficient."
            },
            {
                "question_text": "In a binary search tree, values smaller than a node are generally stored where?",
                "options": ["Right subtree", "Left subtree", "Root only", "Outside the tree"],
                "correct_answer": 1,
                "explanation": "In a standard binary search tree, smaller values are stored in the left subtree."
            },
            {
                "question_text": "Which data structure is commonly used to implement a dictionary?",
                "options": ["Hash Table", "Stack", "Queue", "Simple Tree only"],
                "correct_answer": 0,
                "explanation": "A hash table supports storing and retrieving values using keys."
            },
            {
                "question_text": "What is a collision in hashing?",
                "options": ["Deleting a key", "Two keys producing the same hash location", "Sorting a table", "Creating a new array"],
                "correct_answer": 1,
                "explanation": "A collision occurs when different keys map to the same hash table location."
            },
            {
                "question_text": "Which technique can handle collisions in a hash table?",
                "options": ["Chaining", "Binary traversal", "Inorder sorting", "Recursion only"],
                "correct_answer": 0,
                "explanation": "Chaining stores multiple entries that map to the same hash location in a collection such as a linked list."
            },
            {
                "question_text": "What is the main property of a max heap?",
                "options": ["The smallest element is always at the root", "The largest element is at the root", "All elements are sorted", "Every node has exactly two children"],
                "correct_answer": 1,
                "explanation": "In a max heap, every parent is greater than or equal to its children."
            },
            {
                "question_text": "What is the main property of a min heap?",
                "options": ["The largest element is at the root", "The smallest element is at the root", "All leaves are equal", "It follows FIFO"],
                "correct_answer": 1,
                "explanation": "In a min heap, every parent is smaller than or equal to its children."
            },
            {
                "question_text": "Which traversal visits tree nodes level by level?",
                "options": ["Preorder", "Inorder", "Postorder", "Level order"],
                "correct_answer": 3,
                "explanation": "Level-order traversal visits nodes one level at a time, usually using a queue."
            },
            {
                "question_text": "What is the number of edges in a tree with n nodes?",
                "options": ["n", "n + 1", "n - 1", "2n"],
                "correct_answer": 2,
                "explanation": "A connected tree with n nodes always contains n - 1 edges."
            },
            {
                "question_text": "Which graph has edges with no direction?",
                "options": ["Directed graph", "Undirected graph", "Weighted tree", "Binary tree"],
                "correct_answer": 1,
                "explanation": "An undirected graph has edges that connect vertices without a specified direction."
            },
            {
                "question_text": "What does a weighted graph associate with its edges?",
                "options": ["A color only", "A numerical value or cost", "A parent node", "An array index"],
                "correct_answer": 1,
                "explanation": "A weighted graph assigns values such as distance or cost to its edges."
            },
            {
                "question_text": "Which representation stores graph connections in a two-dimensional table?",
                "options": ["Adjacency Matrix", "Stack", "Linked Stack", "Binary Heap"],
                "correct_answer": 0,
                "explanation": "An adjacency matrix uses rows and columns to represent connections between vertices."
            },
            {
                "question_text": "Which graph representation stores a list of neighboring vertices for each vertex?",
                "options": ["Adjacency List", "Stack Array", "Priority Queue", "Binary Search Tree"],
                "correct_answer": 0,
                "explanation": "An adjacency list records the neighboring vertices of each vertex."
            },
            {
                "question_text": "What is a disconnected graph?",
                "options": ["A graph with no vertices", "A graph where at least one vertex cannot be reached from another", "A graph with only one edge", "A graph where every vertex has a loop"],
                "correct_answer": 1,
                "explanation": "A disconnected graph contains vertices that are not connected by paths."
            },
            {
                "question_text": "Which data structure is suitable for reversing a sequence of elements?",
                "options": ["Queue", "Stack", "Graph", "Priority Queue"],
                "correct_answer": 1,
                "explanation": "A stack reverses order because it removes the most recently inserted element first."
            },
            {
                "question_text": "What does the term underflow mean in a stack?",
                "options": ["Adding an element to a full stack", "Removing an element from an empty stack", "Sorting a stack", "Increasing stack capacity"],
                "correct_answer": 1,
                "explanation": "Stack underflow occurs when a removal operation is attempted on an empty stack."
            },
            {
                "question_text": "What does overflow mean in a fixed-size stack?",
                "options": ["Removing the bottom element", "Attempting to add an element when the stack is full", "Searching for an element", "Reversing the stack"],
                "correct_answer": 1,
                "explanation": "Stack overflow occurs when an insertion is attempted beyond the stack's capacity."
            },
            {
                "question_text": "Which data structure is commonly used in printer job scheduling?",
                "options": ["Queue", "Stack", "Binary Tree only", "Graph only"],
                "correct_answer": 0,
                "explanation": "A queue can process printer jobs in the order they are received."
            },
            {
                "question_text": "What is the main purpose of a circular linked list?",
                "options": ["Make the last node point back to the first node", "Store data in sorted order automatically", "Remove all pointers", "Allow only one node"],
                "correct_answer": 0,
                "explanation": "In a circular linked list, the last node links back to the first node."
            },
            {
                "question_text": "Which data structure is commonly used to evaluate postfix expressions?",
                "options": ["Queue", "Stack", "Graph", "Tree"],
                "correct_answer": 1,
                "explanation": "A stack stores operands and applies operators during postfix expression evaluation."
            },
            {
                "question_text": "Which data structure is used to convert an infix expression into postfix form?",
                "options": ["Stack", "Queue", "Graph", "Array only"],
                "correct_answer": 0,
                "explanation": "A stack temporarily stores operators and parentheses during infix-to-postfix conversion."
            },
            {
                "question_text": "What is the main feature of a circular queue?",
                "options": ["It follows LIFO", "It connects the last position to the first position logically", "It stores only sorted data", "It has no deletion operation"],
                "correct_answer": 1,
                "explanation": "A circular queue reuses positions by wrapping around to the beginning."
            },
            {
                "question_text": "Which data structure is suitable for maintaining elements according to priority?",
                "options": ["Priority Queue", "Simple Stack", "Circular Linked List", "Array Index"],
                "correct_answer": 0,
                "explanation": "A priority queue removes elements according to their priority rather than only their insertion order."
            },
            {
                "question_text": "What is the balance factor of an AVL tree node?",
                "options": ["Sum of its child values", "Difference between the heights of its left and right subtrees", "Number of nodes in the tree", "Number of edges in the graph"],
                "correct_answer": 1,
                "explanation": "The AVL balance factor is the height of the left subtree minus the height of the right subtree."
            },
            {
                "question_text": "Which data structure is used to implement an undo feature in a text editor?",
                "options": ["Queue", "Stack", "Graph", "Heap"],
                "correct_answer": 1,
                "explanation": "A stack stores recent actions so the latest action can be undone first."
            },
            {
                "question_text": "What is the worst-case time complexity of inserting an element at the beginning of a singly linked list?",
                "options": ["O(1)", "O(n)", "O(log n)", "O(n²)"],
                "correct_answer": 0,
                "explanation": "Insertion at the beginning only requires updating the new node and head pointer."
            },
            {
                "question_text": "Which data structure is best suited for implementing a first-come, first-served waiting line?",
                "options": ["Stack", "Queue", "Tree", "Heap"],
                "correct_answer": 1,
                "explanation": "A queue serves people or tasks in the order in which they arrive."
            },
            {
                "question_text": "What is the main purpose of a sentinel node in a linked list?",
                "options": ["To store the largest value", "To simplify insertion and deletion operations", "To sort all nodes", "To remove the head pointer"],
                "correct_answer": 1,
                "explanation": "A sentinel node is a special dummy node that can simplify linked-list boundary operations."
            },
            {
                "question_text": "Which data structure allows efficient retrieval of the minimum element when implemented as a min heap?",
                "options": ["Stack", "Queue", "Heap", "Graph"],
                "correct_answer": 2,
                "explanation": "A min heap keeps the smallest element at its root."
            },
            {
                "question_text": "What does a graph vertex represent?",
                "options": ["A connection", "A node or entity", "A sorting operation", "An array position only"],
                "correct_answer": 1,
                "explanation": "A vertex represents an individual node or entity in a graph."
            },
            {
                "question_text": "Which algorithm finds shortest paths from a source in a graph with non-negative edge weights?",
                "options": ["Bubble Sort", "Dijkstra's Algorithm", "Binary Search", "Inorder Traversal"],
                "correct_answer": 1,
                "explanation": "Dijkstra's algorithm finds shortest paths from a source when edge weights are non-negative."
            },
            {
                "question_text": "Which data structure is commonly used to store the nodes waiting to be explored in BFS?",
                "options": ["Stack", "Queue", "Heap", "Hash Set only"],
                "correct_answer": 1,
                "explanation": "BFS uses a queue to explore vertices in the order they are discovered."
            },
            {
                "question_text": "What is the purpose of a visited array in graph traversal?",
                "options": ["To sort vertices", "To avoid processing the same vertex repeatedly", "To increase graph size", "To remove all edges"],
                "correct_answer": 1,
                "explanation": "A visited array records processed vertices and helps prevent repeated visits."
            },
            {
                "question_text": "Which data structure is commonly used to implement a symbol table?",
                "options": ["Hash Table", "Simple Queue", "Stack only", "Circular Queue"],
                "correct_answer": 0,
                "explanation": "A hash table can store identifiers and their associated information for efficient lookup."
            },
            {
                "question_text": "What is the main difference between a stack and a queue?",
                "options": ["A stack uses LIFO and a queue uses FIFO", "Both always use FIFO", "A queue uses LIFO and a stack uses FIFO", "Neither supports removal"],
                "correct_answer": 0,
                "explanation": "A stack removes the most recently added item, while a queue removes the earliest added item."
            },
            {
                "question_text": "Which data structure is commonly used for autocomplete suggestions?",
                "options": ["Trie", "Stack", "Simple Queue", "Circular Array"],
                "correct_answer": 0,
                "explanation": "A trie stores strings by shared prefixes and supports efficient prefix searches."
            },
            {
                "question_text": "In a trie, what does a path from the root represent?",
                "options": ["A sequence of characters", "A sorting order", "A graph cycle", "A queue position"],
                "correct_answer": 0,
                "explanation": "Each path from the root represents a sequence of characters in a stored word or prefix."
            },
            {
                "question_text": "Which data structure is useful for checking whether a path exists between two graph vertices?",
                "options": ["Stack or Queue during graph traversal", "Only a sorted array", "Only a heap", "Only a circular queue"],
                "correct_answer": 0,
                "explanation": "DFS using a stack or BFS using a queue can explore a graph to determine whether a path exists."
            },
            {
                "question_text": "What is the main purpose of a disjoint-set data structure?",
                "options": ["Manage groups of non-overlapping sets", "Sort a linked list", "Reverse a queue", "Store tree heights only"],
                "correct_answer": 0,
                "explanation": "A disjoint-set structure manages separate groups and supports union and find operations."
            }
        ]
    }
]
