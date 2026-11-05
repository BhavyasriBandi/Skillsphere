
QUESTION_BANK_DS_INTERMEDIATE4 = [
    {
        "skill": "Data Structures",
        "difficulty": "intermediate",
        "questions": [
            {
                "question_text": "What is the time complexity of deleting a node from a binary search tree when its position is already known?",
                "options": ["O(1)", "O(log n) in a balanced tree", "O(n²)", "O(n log n)"],
                "correct_answer": 1,
                "explanation": "In a balanced BST, finding and restructuring around the node takes logarithmic time."
            },
            {
                "question_text": "Which case occurs when a BST node to be deleted has two children?",
                "options": ["Delete the entire tree", "Replace it with its inorder successor or predecessor", "Always replace it with the root", "Ignore the deletion"],
                "correct_answer": 1,
                "explanation": "The inorder successor or predecessor can replace a node with two children while preserving BST ordering."
            },
            {
                "question_text": "What is the maximum number of nodes in a binary tree of height h when the root is at height 0?",
                "options": ["2h", "2^(h+1) - 1", "h²", "2^h - 1"],
                "correct_answer": 1,
                "explanation": "A full binary tree with levels 0 through h has at most 2^(h+1) - 1 nodes."
            },
            {
                "question_text": "Which traversal is useful for deleting an entire binary tree?",
                "options": ["Preorder", "Inorder", "Postorder", "Level order only"],
                "correct_answer": 2,
                "explanation": "Postorder processes children before their parent, allowing safe deletion from the leaves upward."
            },
            {
                "question_text": "What is the main property of a complete binary tree?",
                "options": ["Every node has two children", "All levels except possibly the last are full, and the last is filled from left to right", "Every node has exactly one child", "All leaves are at the same depth"],
                "correct_answer": 1,
                "explanation": "A complete binary tree fills each level from left to right, with only the last level possibly incomplete."
            },
            {
                "question_text": "Which tree is commonly used to implement an efficient ordered set with guaranteed logarithmic height?",
                "options": ["Skewed tree", "AVL tree", "Unbalanced BST", "Expression tree"],
                "correct_answer": 1,
                "explanation": "An AVL tree maintains balance and guarantees logarithmic height."
            },
            {
                "question_text": "What is the primary purpose of a B-tree?",
                "options": ["Efficient storage and searching on secondary storage", "Implementing recursion", "Sorting only small arrays", "Representing only binary expressions"],
                "correct_answer": 0,
                "explanation": "B-trees reduce disk access by storing multiple keys per node and keeping the tree balanced."
            },
            {
                "question_text": "Which data structure is commonly used in database indexes?",
                "options": ["B-tree or B+ tree", "Simple stack", "Circular queue", "Unsorted array only"],
                "correct_answer": 0,
                "explanation": "B-tree variants support efficient ordered lookup and range queries in databases."
            },
            {
                "question_text": "What is a key feature of a B+ tree?",
                "options": ["Records are commonly stored in leaf nodes, which are linked", "Every node has exactly one key", "It is always an unbalanced tree", "It does not support range queries"],
                "correct_answer": 0,
                "explanation": "B+ trees store data entries in linked leaves, making sequential and range access efficient."
            },
            {
                "question_text": "Which data structure is best suited for implementing an LRU cache efficiently?",
                "options": ["Hash map with doubly linked list", "Stack only", "Queue only", "Binary search only"],
                "correct_answer": 0,
                "explanation": "A hash map provides fast lookup while a doubly linked list maintains usage order."
            },
            {
                "question_text": "What does LRU stand for?",
                "options": ["Least Recently Used", "Last Randomly Updated", "Least Repeated Unit", "Latest Read Utility"],
                "correct_answer": 0,
                "explanation": "LRU means Least Recently Used and is a cache replacement policy."
            },
            {
                "question_text": "What is the average time complexity of lookup in an LRU cache implemented with a hash map and doubly linked list?",
                "options": ["O(1)", "O(log n)", "O(n)", "O(n²)"],
                "correct_answer": 0,
                "explanation": "The hash map provides average constant-time lookup."
            },
            {
                "question_text": "Which data structure can efficiently maintain the median of a stream of numbers?",
                "options": ["Two heaps", "One simple queue", "One stack", "A linked list without ordering"],
                "correct_answer": 0,
                "explanation": "A max heap for the lower half and a min heap for the upper half can maintain the median efficiently."
            },
            {
                "question_text": "In the two-heap approach for finding a running median, what does the max heap store?",
                "options": ["The larger half", "The smaller half", "Only duplicate values", "All values in sorted order"],
                "correct_answer": 1,
                "explanation": "The max heap stores the smaller half, with its largest value at the root."
            },
            {
                "question_text": "What is the time complexity of inserting an element into a two-heap running median structure?",
                "options": ["O(1)", "O(log n)", "O(n)", "O(n²)"],
                "correct_answer": 1,
                "explanation": "Heap insertion and possible rebalancing take logarithmic time."
            },
            {
                "question_text": "Which technique is used to find connected components in an undirected graph?",
                "options": ["BFS or DFS", "Binary search", "Merge sort", "Heap sort"],
                "correct_answer": 0,
                "explanation": "BFS or DFS can visit each connected component separately."
            },
            {
                "question_text": "What is a connected component in an undirected graph?",
                "options": ["A maximal set of vertices connected by paths", "A single edge only", "A graph with no vertices", "A sorted list of edges"],
                "correct_answer": 0,
                "explanation": "A connected component is a maximal group in which every pair of vertices has a path between them."
            },
            {
                "question_text": "Which algorithm is suitable for detecting a cycle in an undirected graph using a disjoint set?",
                "options": ["Kruskal's cycle check", "Binary search", "Merge sort", "Insertion sort"],
                "correct_answer": 0,
                "explanation": "If an edge connects vertices already in the same set, it forms a cycle."
            },
            {
                "question_text": "Which condition indicates a cycle in a directed graph during DFS?",
                "options": ["An edge to a vertex currently in the recursion stack", "An edge to any visited vertex", "A vertex with no outgoing edges", "A graph with one vertex"],
                "correct_answer": 0,
                "explanation": "A back edge to a vertex on the active DFS path indicates a directed cycle."
            },
            {
                "question_text": "What is the time complexity of topological sorting using Kahn's algorithm?",
                "options": ["O(V + E)", "O(V²)", "O(E²)", "O(log V)"],
                "correct_answer": 0,
                "explanation": "Each vertex and edge is processed a constant number of times."
            },
            {
                "question_text": "Which shortest-path algorithm can handle negative edge weights but not negative cycles?",
                "options": ["Dijkstra's algorithm", "Bellman-Ford algorithm", "Prim's algorithm", "Kruskal's algorithm"],
                "correct_answer": 1,
                "explanation": "Bellman-Ford supports negative edge weights and can detect reachable negative cycles."
            },
            {
                "question_text": "What is the time complexity of the standard Bellman-Ford algorithm?",
                "options": ["O(V + E)", "O(VE)", "O(E log V)", "O(V² log V)"],
                "correct_answer": 1,
                "explanation": "The algorithm relaxes all edges up to V - 1 times."
            },
            {
                "question_text": "Why does Dijkstra's algorithm not work correctly with negative edge weights in general?",
                "options": ["It assumes finalized shortest distances will not improve later", "It requires a binary tree", "It cannot use a priority queue", "It only works on undirected graphs"],
                "correct_answer": 0,
                "explanation": "A negative edge can later improve a distance that Dijkstra's algorithm has already finalized."
            },
            {
                "question_text": "Which data structure is often used to optimize Dijkstra's algorithm?",
                "options": ["Priority queue", "Stack", "Trie", "Disjoint set only"],
                "correct_answer": 0,
                "explanation": "A priority queue efficiently selects the unsettled vertex with the smallest tentative distance."
            },
            {
                "question_text": "What is the main purpose of a monotonic stack?",
                "options": ["Maintain elements in increasing or decreasing order", "Store graph edges only", "Perform hashing", "Balance a binary tree"],
                "correct_answer": 0,
                "explanation": "A monotonic stack maintains an ordered sequence to solve next-greater or next-smaller element problems."
            },
            {
                "question_text": "Which problem can be efficiently solved using a monotonic stack?",
                "options": ["Next greater element", "Matrix multiplication", "Finding a hash function", "Creating a database index"],
                "correct_answer": 0,
                "explanation": "A monotonic stack finds the next greater element in linear time."
            },
            {
                "question_text": "What is the time complexity of finding the next greater element for all elements using a monotonic stack?",
                "options": ["O(n)", "O(n²)", "O(log n)", "O(n log n)"],
                "correct_answer": 0,
                "explanation": "Each element is pushed and popped at most once."
            },
            {
                "question_text": "Which data structure is suitable for efficiently finding the minimum value in a range with updates?",
                "options": ["Segment tree", "Simple stack", "Queue only", "Trie"],
                "correct_answer": 0,
                "explanation": "A segment tree supports range queries and point updates efficiently."
            }
        ]
    }
]
