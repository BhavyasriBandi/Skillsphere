
QUESTION_BANK_DS_INTERMEDIATE3 = [
    {
        "skill": "Data Structures",
        "difficulty": "intermediate",
        "questions": [
            {
                "question_text": "Which data structure is used to efficiently find the shortest path in an unweighted graph?",
                "options": ["Stack", "Queue", "Heap", "Hash Table"],
                "correct_answer": 1,
                "explanation": "Breadth-First Search uses a queue and finds shortest paths in unweighted graphs."
            },
            {
                "question_text": "What is the time complexity of BFS using an adjacency list?",
                "options": ["O(V + E)", "O(V²)", "O(E²)", "O(log V)"],
                "correct_answer": 0,
                "explanation": "BFS visits vertices and examines edges, giving O(V + E) complexity."
            },
            {
                "question_text": "What is the time complexity of DFS using an adjacency list?",
                "options": ["O(V)", "O(V + E)", "O(V² + E)", "O(log V)"],
                "correct_answer": 1,
                "explanation": "DFS visits each vertex and examines each edge at most a constant number of times."
            },
            {
                "question_text": "Which data structure is commonly used to implement DFS iteratively?",
                "options": ["Queue", "Stack", "Priority Queue", "Deque only"],
                "correct_answer": 1,
                "explanation": "An explicit stack manages the order in which DFS visits vertices."
            },
            {
                "question_text": "Which graph representation stores a list of neighboring vertices for each vertex?",
                "options": ["Adjacency matrix", "Adjacency list", "Binary heap", "Hash function"],
                "correct_answer": 1,
                "explanation": "An adjacency list stores the neighbors of each vertex."
            },
            {
                "question_text": "What is the space complexity of an adjacency matrix for V vertices?",
                "options": ["O(V)", "O(E)", "O(V²)", "O(V + E)"],
                "correct_answer": 2,
                "explanation": "An adjacency matrix stores V by V entries."
            },
            {
                "question_text": "Which algorithm finds a minimum spanning tree in a connected weighted undirected graph by selecting the smallest available edge?",
                "options": ["Dijkstra's algorithm", "Kruskal's algorithm", "Binary search", "Floyd-Warshall algorithm"],
                "correct_answer": 1,
                "explanation": "Kruskal's algorithm selects edges in increasing weight order while avoiding cycles."
            },
            {
                "question_text": "Which data structure helps Kruskal's algorithm detect cycles efficiently?",
                "options": ["Stack", "Disjoint Set Union", "Queue", "Trie"],
                "correct_answer": 1,
                "explanation": "Disjoint Set Union tracks connected components and detects whether an edge joins vertices already connected."
            },
            {
                "question_text": "Which algorithm finds shortest paths from a source vertex when all edge weights are non-negative?",
                "options": ["Dijkstra's algorithm", "Kruskal's algorithm", "Prim's algorithm", "DFS only"],
                "correct_answer": 0,
                "explanation": "Dijkstra's algorithm computes shortest paths when edge weights are non-negative."
            },
            {
                "question_text": "Which algorithm can find shortest paths between every pair of vertices?",
                "options": ["BFS", "Floyd-Warshall", "Prim's algorithm", "Kruskal's algorithm"],
                "correct_answer": 1,
                "explanation": "Floyd-Warshall computes all-pairs shortest paths using dynamic programming."
            },
            {
                "question_text": "What is a directed acyclic graph commonly abbreviated as?",
                "options": ["BST", "DAG", "AVL", "DSU"],
                "correct_answer": 1,
                "explanation": "DAG stands for Directed Acyclic Graph."
            },
            {
                "question_text": "Which technique is commonly used to produce a topological ordering of a DAG?",
                "options": ["Binary search", "DFS or Kahn's algorithm", "Bubble sort", "Hashing"],
                "correct_answer": 1,
                "explanation": "Topological ordering can be generated using DFS finishing times or Kahn's indegree-based algorithm."
            },
            {
                "question_text": "What does the indegree of a vertex represent in a directed graph?",
                "options": ["Number of outgoing edges", "Number of incoming edges", "Total number of vertices", "Number of connected components"],
                "correct_answer": 1,
                "explanation": "Indegree counts the edges entering a vertex."
            },
            {
                "question_text": "Which data structure is useful for implementing Kahn's topological sorting algorithm?",
                "options": ["Queue", "Stack only", "Heap only", "Linked list only"],
                "correct_answer": 0,
                "explanation": "Kahn's algorithm uses a queue to process vertices with zero indegree."
            },
            {
                "question_text": "What is the main property of a min heap?",
                "options": ["Every parent is greater than its children", "Every parent is smaller than or equal to its children", "All leaves are sorted", "Every node has two children"],
                "correct_answer": 1,
                "explanation": "In a min heap, each parent has a value no greater than its children."
            },
            {
                "question_text": "What is the time complexity of retrieving the minimum element from a min heap?",
                "options": ["O(1)", "O(log n)", "O(n)", "O(n log n)"],
                "correct_answer": 0,
                "explanation": "The minimum element is stored at the root of a min heap."
            },
            {
                "question_text": "What is the time complexity of removing the root element from a binary heap?",
                "options": ["O(1)", "O(log n)", "O(n)", "O(n²)"],
                "correct_answer": 1,
                "explanation": "After removing the root, heapify restores the heap property in logarithmic time."
            },
            {
                "question_text": "What is the time complexity of building a binary heap from an array using bottom-up heap construction?",
                "options": ["O(n)", "O(n log n)", "O(log n)", "O(n²)"],
                "correct_answer": 0,
                "explanation": "Bottom-up heap construction takes linear time."
            },
            {
                "question_text": "Which sorting algorithm uses a binary heap as its main data structure?",
                "options": ["Insertion sort", "Heap sort", "Bubble sort", "Merge sort"],
                "correct_answer": 1,
                "explanation": "Heap sort repeatedly extracts the root element from a heap."
            },
            {
                "question_text": "What is the worst-case time complexity of heap sort?",
                "options": ["O(n)", "O(n log n)", "O(n²)", "O(log n)"],
                "correct_answer": 1,
                "explanation": "Building the heap and performing n extractions takes O(n log n) time overall."
            },
            {
                "question_text": "Which tree structure maintains a balance factor of -1, 0, or 1 at every node?",
                "options": ["Binary search tree", "AVL tree", "Expression tree", "Complete binary tree"],
                "correct_answer": 1,
                "explanation": "An AVL tree maintains the height difference between child subtrees within one."
            },
            {
                "question_text": "Which AVL rotation corrects a right-right imbalance?",
                "options": ["Right rotation", "Left rotation", "Left-right rotation", "Right-left rotation"],
                "correct_answer": 1,
                "explanation": "A left rotation corrects a right-right imbalance."
            },
            {
                "question_text": "Which AVL rotation corrects a left-right imbalance?",
                "options": ["Single left rotation", "Single right rotation", "Left rotation followed by right rotation", "Right rotation followed by left rotation"],
                "correct_answer": 2,
                "explanation": "A left-right imbalance is corrected by a left rotation on the left child followed by a right rotation."
            },
            {
                "question_text": "Which AVL rotation corrects a right-left imbalance?",
                "options": ["Left rotation followed by right rotation", "Right rotation followed by left rotation", "Single left rotation", "Single right rotation"],
                "correct_answer": 1,
                "explanation": "A right-left imbalance is corrected by a right rotation on the right child followed by a left rotation."
            },
            {
                "question_text": "What is the main advantage of a balanced binary search tree over an ordinary unbalanced BST?",
                "options": ["It always uses less memory", "It keeps operations logarithmic in height", "It stores duplicate values only", "It does not require comparisons"],
                "correct_answer": 1,
                "explanation": "Balancing prevents the tree from becoming highly skewed."
            },
            {
                "question_text": "Which data structure is especially useful for prefix-based word searching?",
                "options": ["Trie", "Stack", "Queue", "Binary heap"],
                "correct_answer": 0,
                "explanation": "A trie stores strings by shared prefixes."
            },
            {
                "question_text": "What does each edge in a standard trie commonly represent?",
                "options": ["A complete word", "A character", "A sorted array", "A hash collision"],
                "correct_answer": 1,
                "explanation": "Trie edges commonly represent individual characters."
            },
            {
                "question_text": "What is a common use of a trie?",
                "options": ["Prefix search", "Heap sorting", "Queue scheduling only", "Matrix multiplication"],
                "correct_answer": 0,
                "explanation": "Tries efficiently support prefix lookup and autocomplete."
            },
            {
                "question_text": "Which data structure is commonly used in autocomplete systems?",
                "options": ["Trie", "Stack only", "Circular queue only", "Disjoint set"],
                "correct_answer": 0,
                "explanation": "A trie organizes words by their prefixes for autocomplete."
            },
            {
                "question_text": "What is a collision in hashing?",
                "options": ["Two keys map to the same table index", "A table has no empty slots", "A key is deleted", "An array is sorted"],
                "correct_answer": 0,
                "explanation": "A collision occurs when distinct keys produce the same hash-table index."
            },
            {
                "question_text": "Which method resolves hash collisions by checking successive table positions?",
                "options": ["Linear probing", "Separate chaining", "Tree traversal", "Merge operation"],
                "correct_answer": 0,
                "explanation": "Linear probing checks the next available positions in the table."
            },
            {
                "question_text": "What is one disadvantage of linear probing in hash tables?",
                "options": ["It cannot store integers", "Primary clustering can occur", "It always needs a tree", "It prevents searching"],
                "correct_answer": 1,
                "explanation": "Linear probing can create groups of occupied consecutive slots called primary clusters."
            },
            {
                "question_text": "Which collision resolution technique stores collided entries in linked collections at table positions?",
                "options": ["Linear probing", "Separate chaining", "Binary search", "Heapify"],
                "correct_answer": 1,
                "explanation": "Separate chaining stores multiple entries in a bucket, often using a linked list."
            },
            {
                "question_text": "What does rehashing usually involve?",
                "options": ["Deleting all keys", "Resizing the table and reinserting entries", "Sorting every key alphabetically", "Converting a hash table into a stack"],
                "correct_answer": 1,
                "explanation": "Rehashing rebuilds the table, usually with a new capacity and recalculated indices."
            },
            {
                "question_text": "What is the purpose of a deque?",
                "options": ["To allow insertion and deletion at both ends", "To sort graph vertices", "To store only unique keys", "To balance a binary tree"],
                "correct_answer": 0,
                "explanation": "A double-ended queue supports operations at both its front and rear."
            },
            {
                "question_text": "Which data structure can efficiently support both stack and queue operations at its ends?",
                "options": ["Deque", "Binary search tree", "Trie", "Disjoint set"],
                "correct_answer": 0,
                "explanation": "A deque supports insertion and removal at both ends."
            },
            {
                "question_text": "What is the time complexity of inserting an element at either end of a properly implemented deque?",
                "options": ["O(1)", "O(log n)", "O(n)", "O(n²)"],
                "correct_answer": 0,
                "explanation": "A deque supports constant-time insertion at both ends."
            },
            {
                "question_text": "Which data structure is suitable for maintaining the maximum element in a sliding window efficiently?",
                "options": ["Monotonic deque", "Simple stack only", "Binary search tree only", "Circular linked list only"],
                "correct_answer": 0,
                "explanation": "A monotonic deque maintains useful candidates for the sliding-window maximum."
            },
            {
                "question_text": "What is the purpose of a disjoint set data structure?",
                "options": ["To maintain non-overlapping groups", "To sort strings", "To store graph weights only", "To implement recursion"],
                "correct_answer": 0,
                "explanation": "Disjoint Set Union maintains a collection of non-overlapping sets."
            },
            {
                "question_text": "Which operation in Disjoint Set Union combines two sets?",
                "options": ["Find", "Union", "Push", "Pop"],
                "correct_answer": 1,
                "explanation": "Union merges the sets containing the specified elements."
            },
            {
                "question_text": "What does the find operation do in Disjoint Set Union?",
                "options": ["Sorts all elements", "Identifies the representative of an element's set", "Deletes a set", "Creates a queue"],
                "correct_answer": 1,
                "explanation": "Find returns the representative or root of the set containing an element."
            },
            {
                "question_text": "Which optimization makes Disjoint Set Union operations faster by flattening trees?",
                "options": ["Path compression", "Bubble sorting", "Linear probing", "Inorder traversal"],
                "correct_answer": 0,
                "explanation": "Path compression makes visited nodes point closer to the set representative."
            },
            {
                "question_text": "Which optimization attaches the smaller set tree below the larger one?",
                "options": ["Union by size", "Binary search", "Heap sort", "Topological sorting"],
                "correct_answer": 0,
                "explanation": "Union by size attaches the smaller tree under the larger tree."
            },
            {
                "question_text": "What is dynamic programming commonly used to avoid?",
                "options": ["Repeated computation of overlapping subproblems", "All loops", "All recursion", "Memory allocation"],
                "correct_answer": 0,
                "explanation": "Dynamic programming stores subproblem results to avoid recomputing them."
            },
            {
                "question_text": "Which technique stores results of previously solved recursive subproblems?",
                "options": ["Memoization", "Linear probing", "Partitioning", "Traversal"],
                "correct_answer": 0,
                "explanation": "Memoization caches results of function calls for reuse."
            },
            {
                "question_text": "Which dynamic programming approach fills a table from smaller subproblems toward larger ones?",
                "options": ["Tabulation", "Backtracking", "Hash collision", "Depth-first traversal only"],
                "correct_answer": 0,
                "explanation": "Tabulation solves subproblems iteratively and stores their results in a table."
            },
            {
                "question_text": "Which property means a problem's optimal solution can be built from optimal solutions to its subproblems?",
                "options": ["Optimal substructure", "Primary clustering", "Tree rotation", "Linear probing"],
                "correct_answer": 0,
                "explanation": "Optimal substructure is a key property used in dynamic programming and greedy algorithms."
            },
            {
                "question_text": "What is the time complexity of the standard dynamic programming solution for the 0/1 knapsack problem with n items and capacity W?",
                "options": ["O(n + W)", "O(nW)", "O(2n)", "O(W²)"],
                "correct_answer": 1,
                "explanation": "The standard table-based solution considers each item and each capacity."
            },
            {
                "question_text": "Which technique explores possible choices and reverses a choice when it cannot lead to a solution?",
                "options": ["Backtracking", "Hashing", "Heapify", "Linear probing"],
                "correct_answer": 0,
                "explanation": "Backtracking explores choices and undoes them when a path is unsuccessful."
            },
            {
                "question_text": "Which problem is commonly solved using backtracking?",
                "options": ["N-Queens problem", "Finding an array index", "Appending to a list", "Reading a stack top"],
                "correct_answer": 0,
                "explanation": "Backtracking explores placements while checking constraints in the N-Queens problem."
            },
            {
                "question_text": "What is the main idea of a greedy algorithm?",
                "options": ["Choose a locally best option at each step", "Explore every possible sequence", "Always use recursion", "Store every subproblem in a matrix"],
                "correct_answer": 0,
                "explanation": "A greedy algorithm makes a locally optimal choice at each step."
            },
            {
                "question_text": "Which algorithm is commonly used to find a minimum spanning tree by growing one tree from a starting vertex?",
                "options": ["Prim's algorithm", "Binary search", "Merge sort", "Floyd-Warshall algorithm"],
                "correct_answer": 0,
                "explanation": "Prim's algorithm repeatedly adds the lowest-weight edge connecting the growing tree to a new vertex."
            }
        ]
    }
]
