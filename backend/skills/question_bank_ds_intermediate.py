
QUESTION_BANK_DS_INTERMEDIATE = [
    {
        "skill": "Data Structures",
        "difficulty": "intermediate",
        "questions": [
            {
                "question_text": "What is the time complexity of accessing an element using its index in an array?",
                "options": ["O(1)", "O(n)", "O(log n)", "O(n²)"],
                "correct_answer": 0,
                "explanation": "Array elements can be accessed directly using their index in constant time."
            },
            {
                "question_text": "What is the time complexity of inserting an element at the beginning of an array?",
                "options": ["O(1)", "O(log n)", "O(n)", "O(n log n)"],
                "correct_answer": 2,
                "explanation": "Existing elements generally need to be shifted to make space."
            },
            {
                "question_text": "What is the average time complexity of searching for an element in a hash table?",
                "options": ["O(n)", "O(1)", "O(log n)", "O(n²)"],
                "correct_answer": 1,
                "explanation": "A well-designed hash table provides average constant-time lookup."
            },
            {
                "question_text": "What is the worst-case time complexity of searching in a hash table?",
                "options": ["O(1)", "O(log n)", "O(n)", "O(n log n)"],
                "correct_answer": 2,
                "explanation": "Severe collisions can cause a search to examine all stored elements."
            },
            {
                "question_text": "Which linked list allows traversal in both forward and backward directions?",
                "options": ["Singly linked list", "Doubly linked list", "Circular singly linked list", "Linear array"],
                "correct_answer": 1,
                "explanation": "A doubly linked list stores both next and previous references."
            },
            {
                "question_text": "What is the time complexity of inserting a node at the beginning of a singly linked list?",
                "options": ["O(1)", "O(n)", "O(log n)", "O(n²)"],
                "correct_answer": 0,
                "explanation": "Only the new node and head pointer need to be updated."
            },
            {
                "question_text": "Which algorithm can detect a cycle in a linked list using two pointers?",
                "options": ["Binary search", "Floyd's cycle detection", "Merge sort", "Dijkstra's algorithm"],
                "correct_answer": 1,
                "explanation": "Floyd's algorithm uses slow and fast pointers to detect a cycle."
            },
            {
                "question_text": "What is the time complexity of reversing a singly linked list iteratively?",
                "options": ["O(1)", "O(log n)", "O(n)", "O(n²)"],
                "correct_answer": 2,
                "explanation": "Each node is visited once while its next pointer is reversed."
            },
            {
                "question_text": "Which data structure is used by recursive function calls?",
                "options": ["Queue", "Call stack", "Hash table", "Heap"],
                "correct_answer": 1,
                "explanation": "Recursive calls are managed using the program's call stack."
            },
            {
                "question_text": "What happens when a stack receives a pop operation while it is empty?",
                "options": ["Overflow", "Underflow", "Collision", "Traversal"],
                "correct_answer": 1,
                "explanation": "Removing an element from an empty stack causes underflow."
            },
            {
                "question_text": "What is the time complexity of inserting an element into a binary heap?",
                "options": ["O(1)", "O(log n)", "O(n)", "O(n²)"],
                "correct_answer": 1,
                "explanation": "The inserted element may move up through the heap height."
            },
            {
                "question_text": "In a max heap, where is the maximum element stored?",
                "options": ["At the root", "At the last leaf", "At the leftmost leaf", "At any random node"],
                "correct_answer": 0,
                "explanation": "The maximum element is stored at the root of a max heap."
            },
            {
                "question_text": "What is the height complexity of a balanced binary search tree?",
                "options": ["O(1)", "O(log n)", "O(n)", "O(n²)"],
                "correct_answer": 1,
                "explanation": "A balanced binary search tree has logarithmic height."
            },
            {
                "question_text": "What is the worst-case search complexity of an unbalanced binary search tree?",
                "options": ["O(1)", "O(log n)", "O(n)", "O(n log n)"],
                "correct_answer": 2,
                "explanation": "An unbalanced tree can become similar to a linked list."
            },
            {
                "question_text": "Which traversal of a binary search tree produces values in sorted order?",
                "options": ["Preorder", "Postorder", "Inorder", "Level order"],
                "correct_answer": 2,
                "explanation": "Inorder traversal visits the left subtree, root, and right subtree."
            },
            {
                "question_text": "Which traversal visits the root node before its subtrees?",
                "options": ["Inorder", "Preorder", "Postorder", "Level order"],
                "correct_answer": 1,
                "explanation": "Preorder traversal follows Root, Left, Right."
            },
            {
                "question_text": "Which traversal visits the root node after its subtrees?",
                "options": ["Preorder", "Inorder", "Postorder", "Level order"],
                "correct_answer": 2,
                "explanation": "Postorder traversal follows Left, Right, Root."
            },
            {
                "question_text": "Which data structure is commonly used for level-order traversal of a tree?",
                "options": ["Stack", "Queue", "Heap", "Hash table"],
                "correct_answer": 1,
                "explanation": "A queue processes nodes level by level in breadth-first order."
            },
            {
                "question_text": "What is the maximum number of children a binary tree node can have?",
                "options": ["1", "2", "3", "Unlimited"],
                "correct_answer": 1,
                "explanation": "A binary tree node can have at most two children."
            },
            {
                "question_text": "Which graph traversal commonly uses a queue?",
                "options": ["Depth-First Search", "Breadth-First Search", "Binary search", "Insertion sort"],
                "correct_answer": 1,
                "explanation": "Breadth-First Search uses a queue to explore neighboring vertices."
            }
        ]
    }
]
