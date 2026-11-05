
QUESTION_BANK_DS_ADVANCED1 = [
    {
        "skill": "Data Structures",
        "difficulty": "advanced",
        "questions": [
            {
                "question_text": "What is the amortized time complexity of an append operation in a dynamic array?",
                "options": ["O(1)", "O(log n)", "O(n)", "O(n²)"],
                "correct_answer": 0,
                "explanation": "Although resizing occasionally takes O(n), append has amortized O(1) complexity."
            },
            {
                "question_text": "Which technique is commonly used to analyze the amortized cost of dynamic array insertion?",
                "options": ["Potential method", "Binary search", "Graph coloring", "Backtracking"],
                "correct_answer": 0,
                "explanation": "The potential method accounts for occasional expensive resizing operations."
            },
            {
                "question_text": "What is the worst-case time complexity of searching for a key in a well-balanced AVL tree?",
                "options": ["O(1)", "O(log n)", "O(n)", "O(n log n)"],
                "correct_answer": 1,
                "explanation": "AVL trees maintain logarithmic height, so searching takes O(log n) time."
            },
            {
                "question_text": "What is the maximum allowed difference between the heights of the left and right subtrees at an AVL node?",
                "options": ["0", "1", "2", "3"],
                "correct_answer": 1,
                "explanation": "An AVL node's balance factor must be -1, 0, or 1."
            },
            {
                "question_text": "Which data structure is commonly used to implement an ordered map with guaranteed logarithmic operations?",
                "options": ["Balanced search tree", "Unsorted array", "Simple stack", "Circular queue"],
                "correct_answer": 0,
                "explanation": "Balanced search trees support ordered lookup, insertion, and deletion in logarithmic time."
            },
            {
                "question_text": "What is the worst-case search complexity in a red-black tree?",
                "options": ["O(1)", "O(log n)", "O(n)", "O(n²)"],
                "correct_answer": 1,
                "explanation": "Red-black tree balancing guarantees logarithmic height."
            },
            {
                "question_text": "Which property is maintained by a red-black tree?",
                "options": ["Every path from a node to its descendant NIL leaves has the same number of black nodes", "Every node must have two red children", "All leaves must contain data", "Every node must have exactly one child"],
                "correct_answer": 0,
                "explanation": "Equal black height on paths is one of the red-black tree invariants."
            },
            {
                "question_text": "What is the maximum number of children of a node in a B-tree of order m?",
                "options": ["m", "m - 1", "2m", "m + 1"],
                "correct_answer": 0,
                "explanation": "Under the common order-m definition, a B-tree node can have at most m children."
            },
            {
                "question_text": "Why are B+ trees especially useful for database range queries?",
                "options": ["Their leaf nodes are linked for sequential access", "They store all records only at the root", "They do not require sorting", "They have no internal nodes"],
                "correct_answer": 0,
                "explanation": "Linked leaf nodes make it efficient to scan consecutive key ranges."
            },
            {
                "question_text": "What is the primary purpose of a skip list?",
                "options": ["Provide expected logarithmic search using multiple forward links", "Implement recursive calls", "Store graph adjacency matrices", "Guarantee constant-time sorting"],
                "correct_answer": 0,
                "explanation": "Skip lists use layered forward links to support expected O(log n) search."
            },
            {
                "question_text": "What is the expected search complexity of a properly randomized skip list?",
                "options": ["O(1)", "O(log n)", "O(n)", "O(n²)"],
                "correct_answer": 1,
                "explanation": "Randomized levels provide expected logarithmic search time."
            },
            {
                "question_text": "Which data structure supports efficient range sum queries and point updates?",
                "options": ["Fenwick tree", "Stack", "Trie", "Simple queue"],
                "correct_answer": 0,
                "explanation": "A Fenwick tree supports prefix sums and point updates in O(log n) time."
            },
            {
                "question_text": "What is another common name for a Fenwick tree?",
                "options": ["Binary Indexed Tree", "Binary Search Tree", "Segment Graph", "Priority Tree"],
                "correct_answer": 0,
                "explanation": "A Fenwick tree is also known as a Binary Indexed Tree."
            },
            {
                "question_text": "What is the time complexity of a point update in a Fenwick tree?",
                "options": ["O(1)", "O(log n)", "O(n)", "O(n log n)"],
                "correct_answer": 1,
                "explanation": "A Fenwick tree updates logarithmically many indexed positions."
            },
            {
                "question_text": "What is the typical time complexity of a range query in a segment tree?",
                "options": ["O(1)", "O(log n)", "O(n)", "O(n²)"],
                "correct_answer": 1,
                "explanation": "A segment tree decomposes a range into logarithmically many tree segments."
            },
            {
                "question_text": "What is lazy propagation used for in a segment tree?",
                "options": ["Deferring updates to child segments until needed", "Sorting all leaves", "Deleting the root", "Reducing the tree to a linked list"],
                "correct_answer": 0,
                "explanation": "Lazy propagation postpones applying updates to descendants until those nodes are visited."
            },
            {
                "question_text": "Which data structure is suitable for answering range minimum queries with point updates in O(log n) time?",
                "options": ["Segment tree", "Stack", "Queue", "Unsorted linked list"],
                "correct_answer": 0,
                "explanation": "A segment tree supports range minimum queries and point updates efficiently."
            },
            {
                "question_text": "What is the main advantage of a persistent data structure?",
                "options": ["It preserves access to previous versions after updates", "It always uses constant memory", "It prevents all duplicate values", "It removes the need for pointers"],
                "correct_answer": 0,
                "explanation": "Persistence allows previous versions of a data structure to remain accessible."
            },
            {
                "question_text": "Which technique allows a persistent tree to share unchanged nodes between versions?",
                "options": ["Path copying", "Linear probing", "Heap sorting", "Level-order traversal"],
                "correct_answer": 0,
                "explanation": "Path copying creates new nodes along the modified path while sharing unchanged subtrees."
            },
            {
                "question_text": "What is the purpose of a monotonic queue in a sliding-window maximum problem?",
                "options": ["Maintain candidates in decreasing order", "Sort the entire input repeatedly", "Store only the first element", "Build a binary search tree"],
                "correct_answer": 0,
                "explanation": "A decreasing deque keeps the largest useful candidates at its front."
            },
            {
                "question_text": "What is the time complexity of finding sliding-window maximums for all windows using a deque?",
                "options": ["O(n)", "O(n log n)", "O(n²)", "O(log n)"],
                "correct_answer": 0,
                "explanation": "Each element enters and leaves the deque at most once."
            },
            {
                "question_text": "Which data structure is useful for maintaining the k largest elements in a stream?",
                "options": ["Min heap of size k", "Stack of size k", "Queue of all elements", "Trie"],
                "correct_answer": 0,
                "explanation": "A min heap of size k keeps the smallest of the current k largest elements at its root."
            },
            {
                "question_text": "What is the time complexity of maintaining the k largest elements from n values using a min heap of size k?",
                "options": ["O(n log k)", "O(n²)", "O(log n)", "O(k²)"],
                "correct_answer": 0,
                "explanation": "Each value may require a logarithmic heap update, giving O(n log k) time."
            },
            {
                "question_text": "Which algorithm is commonly used to find strongly connected components in a directed graph?",
                "options": ["Kosaraju's algorithm", "Kruskal's algorithm", "Prim's algorithm", "Binary search"],
                "correct_answer": 0,
                "explanation": "Kosaraju's algorithm uses DFS passes on a graph and its transpose."
            },
            {
                "question_text": "Which algorithm finds strongly connected components using discovery times and low-link values?",
                "options": ["Tarjan's algorithm", "Dijkstra's algorithm", "Floyd-Warshall algorithm", "Kahn's algorithm"],
                "correct_answer": 0,
                "explanation": "Tarjan's algorithm identifies strongly connected components using DFS and low-link values."
            },
            {
                "question_text": "What does a strongly connected component represent in a directed graph?",
                "options": ["A maximal group where every vertex can reach every other vertex", "A group with no edges", "A set of isolated vertices only", "A tree with one root"],
                "correct_answer": 0,
                "explanation": "Every vertex in a strongly connected component is reachable from every other vertex in that component."
            },
            {
                "question_text": "Which algorithm can find bridges in an undirected graph?",
                "options": ["DFS using discovery and low-link times", "Binary search", "Heap sort", "Kruskal's algorithm only"],
                "correct_answer": 0,
                "explanation": "DFS low-link values identify edges whose removal disconnects a component."
            },
            {
                "question_text": "What is a bridge in an undirected graph?",
                "options": ["An edge whose removal increases the number of connected components", "A vertex with maximum degree", "A cycle containing every vertex", "An edge with zero weight"],
                "correct_answer": 0,
                "explanation": "Removing a bridge disconnects part of the graph."
            },
            {
                "question_text": "What is an articulation point in an undirected graph?",
                "options": ["A vertex whose removal increases the number of connected components", "A vertex with no edges", "The vertex with the smallest label", "A vertex in every cycle"],
                "correct_answer": 0,
                "explanation": "Removing an articulation point increases the number of connected components."
            },
            {
                "question_text": "Which data structure is used by Tarjan's strongly connected components algorithm to track active vertices?",
                "options": ["Stack", "Queue", "Min heap", "Fenwick tree"],
                "correct_answer": 0,
                "explanation": "Tarjan's algorithm uses a stack to maintain vertices in the current DFS component search."
            },
            {
                "question_text": "Which algorithm computes all-pairs shortest paths using dynamic programming?",
                "options": ["Floyd-Warshall", "Prim", "Kruskal", "Topological sort"],
                "correct_answer": 0,
                "explanation": "Floyd-Warshall repeatedly considers intermediate vertices to improve all-pairs distances."
            },
            {
                "question_text": "What is the time complexity of the Floyd-Warshall algorithm?",
                "options": ["O(V³)", "O(V + E)", "O(E log V)", "O(V² log V)"],
                "correct_answer": 0,
                "explanation": "The algorithm uses three nested loops over the vertices."
            },
            {
                "question_text": "Which algorithm can detect a negative-weight cycle reachable from a source vertex?",
                "options": ["Bellman-Ford", "Prim", "Kruskal", "Binary search"],
                "correct_answer": 0,
                "explanation": "An additional relaxation after V - 1 passes can reveal a reachable negative cycle."
            },
            {
                "question_text": "Which algorithm is suitable for finding shortest paths in a DAG even when some edges have negative weights?",
                "options": ["Topological-order relaxation", "Dijkstra without restrictions", "Prim's algorithm", "Kruskal's algorithm"],
                "correct_answer": 0,
                "explanation": "Processing vertices in topological order allows shortest-path relaxation in O(V + E) time."
            },
            {
                "question_text": "What is the time complexity of shortest-path computation in a DAG using topological ordering?",
                "options": ["O(V + E)", "O(V²)", "O(VE)", "O(E log V)"],
                "correct_answer": 0,
                "explanation": "Topological ordering and edge relaxation each take linear time in vertices and edges."
            },
            {
                "question_text": "Which data structure supports efficient prefix lookup for a large collection of strings?",
                "options": ["Trie", "Binary heap", "Disjoint set", "Circular queue"],
                "correct_answer": 0,
                "explanation": "Tries organize strings by their prefixes."
            },
            {
                "question_text": "What is the purpose of a compressed trie?",
                "options": ["Reduce chains of single-child nodes by combining edges", "Store every character in a separate database", "Sort words by length only", "Remove all shared prefixes"],
                "correct_answer": 0,
                "explanation": "A compressed trie combines single-child paths to reduce node overhead."
            },
            {
                "question_text": "Which data structure is commonly used for efficient multi-pattern string matching?",
                "options": ["Aho-Corasick automaton", "Binary heap", "Disjoint set", "Circular queue"],
                "correct_answer": 0,
                "explanation": "Aho-Corasick uses a trie with failure links to search for multiple patterns."
            },
            {
                "question_text": "What is the purpose of failure links in the Aho-Corasick algorithm?",
                "options": ["Move to the longest suffix that is also a trie prefix", "Delete matched patterns", "Sort patterns alphabetically", "Reverse the input text"],
                "correct_answer": 0,
                "explanation": "Failure links allow matching to continue after a mismatch without restarting from the root."
            },
            {
                "question_text": "Which algorithm finds the longest prefix of a string that is also a suffix and is used in KMP matching?",
                "options": ["Prefix function computation", "Heap construction", "Topological sorting", "Union operation"],
                "correct_answer": 0,
                "explanation": "The KMP prefix function records the longest proper prefix that is also a suffix."
            },
            {
                "question_text": "What is the worst-case time complexity of the Knuth-Morris-Pratt string matching algorithm?",
                "options": ["O(n + m)", "O(nm)", "O(n²)", "O(m log n)"],
                "correct_answer": 0,
                "explanation": "KMP preprocesses the pattern and scans the text in linear time."
            },
            {
                "question_text": "Which data structure can represent a suffix array's supporting range minimum queries efficiently?",
                "options": ["Segment tree or sparse table", "Stack only", "Queue only", "Hash set only"],
                "correct_answer": 0,
                "explanation": "Range minimum query structures can support efficient longest common prefix queries over suffix-array data."
            },
            {
                "question_text": "What does a suffix array store?",
                "options": ["Starting positions of suffixes in sorted order", "All prefixes in insertion order", "Only repeated characters", "A graph of string transitions"],
                "correct_answer": 0,
                "explanation": "A suffix array stores indices of suffixes ordered lexicographically."
            },
            {
                "question_text": "Which technique is used to reduce repeated work in a dynamic programming solution?",
                "options": ["Memoization", "Linear probing", "Tree rotation", "Graph coloring"],
                "correct_answer": 0,
                "explanation": "Memoization caches solutions to overlapping subproblems."
            },
            {
                "question_text": "What is the time complexity of the standard dynamic programming solution for longest common subsequence of strings of lengths m and n?",
                "options": ["O(mn)", "O(m + n)", "O(log mn)", "O(m² + n²)"],
                "correct_answer": 0,
                "explanation": "The standard DP table has m by n states."
            },
            {
                "question_text": "Which data structure is useful for efficiently finding the median after each insertion?",
                "options": ["Two heaps", "One stack", "One ordinary queue", "Adjacency matrix"],
                "correct_answer": 0,
                "explanation": "A max heap and a min heap maintain the lower and upper halves of the values."
            },
            {
                "question_text": "What is the purpose of union by rank in Disjoint Set Union?",
                "options": ["Keep the representative trees shallow", "Sort set elements", "Find shortest graph paths", "Remove duplicate keys"],
                "correct_answer": 0,
                "explanation": "Union by rank attaches the shallower tree below the deeper tree."
            },
            {
                "question_text": "What is the amortized complexity of Disjoint Set Union operations with path compression and union by rank?",
                "options": ["O(α(n))", "O(n)", "O(log² n)", "O(n log n)"],
                "correct_answer": 0,
                "explanation": "The operations have nearly constant amortized complexity, expressed using the inverse Ackermann function."
            },
            {
                "question_text": "Which data structure is suitable for maintaining a collection of intervals and querying overlaps?",
                "options": ["Interval tree", "Stack only", "Queue only", "Binary heap only"],
                "correct_answer": 0,
                "explanation": "An interval tree is designed to store intervals and efficiently find overlapping intervals."
            },
            {
                "question_text": "What is the purpose of a suffix tree?",
                "options": ["Support efficient substring and pattern queries", "Implement priority scheduling", "Represent minimum spanning trees", "Maintain disjoint sets"],
                "correct_answer": 0,
                "explanation": "Suffix trees index all suffixes of a string and support fast pattern queries."
            },
            {
                "question_text": "Which property makes a Fibonacci heap useful in some graph algorithms?",
                "options": ["Very low amortized cost for decrease-key", "Constant worst-case cost for every operation", "It stores strings only", "It eliminates the need for graph edges"],
                "correct_answer": 0,
                "explanation": "Fibonacci heaps provide O(1) amortized decrease-key, which can improve some implementations of Dijkstra's and Prim's algorithms."
            }
        ]
    }
]
