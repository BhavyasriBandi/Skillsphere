
QUESTION_BANK_DS_ADVANCED2 = [
    {
        "skill": "Data Structures",
        "difficulty": "advanced",
        "questions": [
            {
                "question_text": "What is the worst-case time complexity of searching for an element in a hash table using separate chaining?",
                "options": ["O(1)", "O(log n)", "O(n)", "O(n log n)"],
                "correct_answer": 2,
                "explanation": "In the worst case, all keys may be stored in the same bucket."
            },
            {
                "question_text": "Which hash table collision resolution method can suffer from secondary clustering?",
                "options": ["Quadratic probing", "Separate chaining", "Double hashing only", "Tree traversal"],
                "correct_answer": 0,
                "explanation": "Quadratic probing can cause keys with the same initial hash value to follow the same probe sequence."
            },
            {
                "question_text": "What is the main advantage of double hashing over linear probing?",
                "options": ["It eliminates all collisions", "It reduces primary clustering", "It guarantees O(1) worst-case search", "It does not require a hash function"],
                "correct_answer": 1,
                "explanation": "Double hashing uses a second hash function to determine the probe step, reducing primary clustering."
            },
            {
                "question_text": "What is the expected search complexity of a hash table when its load factor is controlled and hashing is well distributed?",
                "options": ["O(1)", "O(log n)", "O(n)", "O(n²)"],
                "correct_answer": 0,
                "explanation": "With a suitable hash function and controlled load factor, expected lookup time is constant."
            },
            {
                "question_text": "Which property must a hash function ideally satisfy for a hash table?",
                "options": ["It should distribute keys uniformly across table positions", "It should always return zero", "It should sort keys", "It should produce a unique index for every possible key"],
                "correct_answer": 0,
                "explanation": "Uniform distribution helps reduce collisions."
            },
            {
                "question_text": "What is the purpose of a bloom filter?",
                "options": ["Probabilistically test set membership", "Store sorted records permanently", "Find shortest paths", "Balance binary trees"],
                "correct_answer": 0,
                "explanation": "A Bloom filter tests probable membership using a bit array and multiple hash functions."
            },
            {
                "question_text": "Which statement about a standard Bloom filter is correct?",
                "options": ["It can produce false positives but not false negatives", "It can produce false negatives but not false positives", "It always stores the original elements", "It guarantees exact membership answers"],
                "correct_answer": 0,
                "explanation": "A standard Bloom filter may report an absent item as present, but does not report an inserted item as absent."
            },
            {
                "question_text": "What happens when more elements are inserted into a Bloom filter without increasing its size?",
                "options": ["The false positive probability generally increases", "The false positive probability becomes zero", "All bits are cleared", "The filter becomes a binary search tree"],
                "correct_answer": 0,
                "explanation": "More inserted elements set more bits, increasing the chance that an absent item appears present."
            },
            {
                "question_text": "Which data structure is commonly used for approximate membership checking in large-scale systems?",
                "options": ["Bloom filter", "Stack", "Binary search tree only", "Circular queue"],
                "correct_answer": 0,
                "explanation": "Bloom filters provide memory-efficient approximate membership tests."
            },
            {
                "question_text": "What is the main purpose of a cuckoo hash table?",
                "options": ["Resolve collisions using multiple possible locations and relocation", "Sort keys using recursion", "Store graph paths", "Build a balanced binary tree"],
                "correct_answer": 0,
                "explanation": "Cuckoo hashing resolves collisions by moving existing keys between their candidate locations."
            },
            {
                "question_text": "Which operation is commonly used to restore the heap property after removing the root?",
                "options": ["Sift down", "Binary search", "Path compression", "Inorder traversal"],
                "correct_answer": 0,
                "explanation": "Sift down moves the replacement root toward a valid position."
            },
            {
                "question_text": "What is the time complexity of decrease-key in a binary heap?",
                "options": ["O(1)", "O(log n)", "O(n)", "O(n log n)"],
                "correct_answer": 1,
                "explanation": "The decreased key may move upward through the height of the heap."
            },
            {
                "question_text": "Which heap structure supports O(1) amortized decrease-key operations?",
                "options": ["Fibonacci heap", "Binary heap", "Sorted array", "Min-max array"],
                "correct_answer": 0,
                "explanation": "Fibonacci heaps provide O(1) amortized decrease-key."
            },
            {
                "question_text": "What is the amortized time complexity of extract-min in a Fibonacci heap?",
                "options": ["O(1)", "O(log n)", "O(n)", "O(n²)"],
                "correct_answer": 1,
                "explanation": "Fibonacci heaps provide O(log n) amortized extract-min."
            },
            {
                "question_text": "Which algorithm can benefit from Fibonacci heaps because it performs many decrease-key operations?",
                "options": ["Dijkstra's algorithm", "Binary search", "Insertion sort", "KMP string matching"],
                "correct_answer": 0,
                "explanation": "Dijkstra's algorithm frequently updates tentative distances, making decrease-key performance useful."
            },
            {
                "question_text": "What is the main difference between a binary heap and a binary search tree?",
                "options": ["A heap maintains parent-child priority order, while a BST maintains key ordering", "A heap is always sorted in inorder", "A BST always has complete levels", "They have identical ordering rules"],
                "correct_answer": 0,
                "explanation": "Heaps maintain a priority relationship, while BSTs maintain left-right key ordering."
            },
            {
                "question_text": "Which tree structure is used to represent range queries over an array?",
                "options": ["Segment tree", "Trie", "Expression tree", "Red-black tree only"],
                "correct_answer": 0,
                "explanation": "A segment tree stores information about intervals of an array."
            },
            {
                "question_text": "What is the space complexity of a conventional segment tree built over n elements?",
                "options": ["O(1)", "O(log n)", "O(n)", "O(n log n)"],
                "correct_answer": 2,
                "explanation": "A conventional segment tree requires linear space, commonly allocated using an array of approximately 4n positions."
            },
            {
                "question_text": "Which technique can support range addition and range sum queries efficiently in a segment tree?",
                "options": ["Lazy propagation", "Linear probing", "Path compression", "Topological sorting"],
                "correct_answer": 0,
                "explanation": "Lazy propagation postpones updates to child segments while maintaining query information."
            },
            {
                "question_text": "What is a persistent segment tree?",
                "options": ["A segment tree that preserves previous versions after updates", "A segment tree that stores only one value", "A tree that cannot be modified", "A heap-based sorting structure"],
                "correct_answer": 0,
                "explanation": "Persistent segment trees retain earlier versions, often through path copying."
            },
            {
                "question_text": "Which data structure is suitable for two-dimensional range sum queries?",
                "options": ["Two-dimensional Fenwick tree", "Simple stack", "Binary heap", "Single linked list"],
                "correct_answer": 0,
                "explanation": "A two-dimensional Fenwick tree supports point updates and rectangular prefix or range sum queries."
            },
            {
                "question_text": "What is the typical update complexity of a two-dimensional Fenwick tree over an n by m grid?",
                "options": ["O(1)", "O(log n log m)", "O(nm)", "O(n + m)"],
                "correct_answer": 1,
                "explanation": "The update visits logarithmically many indices in each dimension."
            },
            {
                "question_text": "Which data structure is suitable for finding the k-th smallest element in a dynamic set using order statistics?",
                "options": ["Order-statistic tree", "Stack", "Queue", "Bloom filter"],
                "correct_answer": 0,
                "explanation": "An order-statistic tree stores subtree sizes to support rank and selection queries."
            },
            {
                "question_text": "What additional information does an order-statistic tree commonly maintain in each node?",
                "options": ["The size of its subtree", "The number of graph edges", "A queue index", "A hash function"],
                "correct_answer": 0,
                "explanation": "Subtree sizes allow the tree to calculate ranks and select elements by order."
            },
            {
                "question_text": "Which technique is used to find the longest common prefix of two suffixes efficiently after suffix-array preprocessing?",
                "options": ["LCP array with range minimum queries", "Stack reversal", "Heap insertion", "Disjoint set union"],
                "correct_answer": 0,
                "explanation": "The LCP array and range minimum queries help answer longest common prefix queries between suffixes."
            },
            {
                "question_text": "What does the LCP array store in suffix-array processing?",
                "options": ["Longest common prefix lengths of neighboring suffixes in sorted order", "Lengths of all substrings", "Only unique characters", "Positions of graph vertices"],
                "correct_answer": 0,
                "explanation": "An LCP array stores common-prefix lengths for adjacent suffixes in suffix-array order."
            },
            {
                "question_text": "Which data structure supports efficient longest-prefix matching for IP routing?",
                "options": ["Trie or prefix tree", "Stack", "Binary heap only", "Circular queue"],
                "correct_answer": 0,
                "explanation": "Prefix trees can efficiently find the longest stored prefix matching an address."
            },
            {
                "question_text": "What is a radix tree?",
                "options": ["A compressed trie that combines chains of single-child nodes", "A binary heap with duplicate values", "A graph with weighted edges", "A queue implemented with arrays"],
                "correct_answer": 0,
                "explanation": "A radix tree compresses common single-child paths in a trie."
            },
            {
                "question_text": "Which data structure is useful for representing a large sparse graph efficiently?",
                "options": ["Adjacency list", "Adjacency matrix", "Full binary tree", "Sorted array of all possible vertex pairs"],
                "correct_answer": 0,
                "explanation": "An adjacency list stores only existing edges and is space-efficient for sparse graphs."
            },
            {
                "question_text": "What is the space complexity of an adjacency list representation of a graph with V vertices and E edges?",
                "options": ["O(V + E)", "O(V²)", "O(E²)", "O(log V)"],
                "correct_answer": 0,
                "explanation": "The representation stores the vertices and their existing adjacency entries."
            },
            {
                "question_text": "Which algorithm finds articulation points and bridges in an undirected graph in linear time?",
                "options": ["DFS with low-link values", "Dijkstra's algorithm", "Prim's algorithm", "Floyd-Warshall algorithm"],
                "correct_answer": 0,
                "explanation": "A DFS traversal with discovery and low-link values identifies articulation points and bridges in O(V + E)."
            },
            {
                "question_text": "What is the time complexity of Tarjan's algorithm for strongly connected components?",
                "options": ["O(V + E)", "O(V²)", "O(VE)", "O(E log V)"],
                "correct_answer": 0,
                "explanation": "Tarjan's algorithm visits vertices and edges in linear time."
            },
            {
                "question_text": "Which graph algorithm uses a priority queue to repeatedly select the minimum-weight edge connecting a growing tree to an outside vertex?",
                "options": ["Prim's algorithm", "Bellman-Ford algorithm", "Kosaraju's algorithm", "KMP algorithm"],
                "correct_answer": 0,
                "explanation": "Prim's algorithm grows a minimum spanning tree by selecting a minimum connecting edge."
            },
            {
                "question_text": "What is the time complexity of Kruskal's algorithm when edges are sorted first and Disjoint Set Union is used?",
                "options": ["O(E log E)", "O(V²)", "O(V + E)", "O(log V)"],
                "correct_answer": 0,
                "explanation": "Sorting edges dominates the complexity, while DSU operations are nearly constant amortized."
            },
            {
                "question_text": "Which condition must hold for a graph to have a minimum spanning tree containing all its vertices?",
                "options": ["The graph must be connected and undirected", "The graph must be directed", "Every edge must have equal weight", "The graph must contain a negative cycle"],
                "correct_answer": 0,
                "explanation": "A connected, weighted, undirected graph has a spanning tree and therefore a minimum spanning tree."
            },
            {
                "question_text": "Which algorithm is suitable for shortest paths in a graph with negative edges and no reachable negative cycles?",
                "options": ["Bellman-Ford", "Prim", "Kruskal", "Heap sort"],
                "correct_answer": 0,
                "explanation": "Bellman-Ford supports negative edge weights and detects reachable negative cycles."
            },
            {
                "question_text": "What is the purpose of Johnson's algorithm?",
                "options": ["Find all-pairs shortest paths in sparse graphs, allowing negative edges but no negative cycles", "Find a minimum spanning tree only", "Sort vertices by degree", "Detect only undirected cycles"],
                "correct_answer": 0,
                "explanation": "Johnson's algorithm reweights edges using Bellman-Ford and then runs Dijkstra from each vertex."
            },
            {
                "question_text": "Which technique is used by Johnson's algorithm to remove negative edge weights while preserving shortest paths?",
                "options": ["Reweighting with vertex potentials", "Linear probing", "Tree rotation", "Heap construction"],
                "correct_answer": 0,
                "explanation": "Vertex potentials reweight edges to non-negative costs while preserving shortest paths."
            },
            {
                "question_text": "What is the purpose of a topological ordering in dependency scheduling?",
                "options": ["Ensure each prerequisite appears before the task that depends on it", "Sort tasks by memory size", "Find the largest edge weight", "Remove all graph cycles automatically"],
                "correct_answer": 0,
                "explanation": "A topological order respects every directed dependency edge in a DAG."
            },
            {
                "question_text": "Which algorithm can find a maximum flow in a flow network using augmenting paths?",
                "options": ["Ford-Fulkerson", "Kruskal", "Prim", "KMP"],
                "correct_answer": 0,
                "explanation": "Ford-Fulkerson repeatedly finds augmenting paths and increases the flow."
            },
            {
                "question_text": "Which algorithm uses BFS to find shortest augmenting paths for maximum flow?",
                "options": ["Edmonds-Karp", "Dijkstra", "Floyd-Warshall", "Kosaraju"],
                "correct_answer": 0,
                "explanation": "Edmonds-Karp is a Ford-Fulkerson implementation that uses BFS."
            },
            {
                "question_text": "What is the time complexity of the Edmonds-Karp maximum-flow algorithm?",
                "options": ["O(VE²)", "O(V + E)", "O(E log V)", "O(V³)"],
                "correct_answer": 0,
                "explanation": "The standard Edmonds-Karp bound is O(VE²)."
            },
            {
                "question_text": "Which data structure is used in a standard implementation of the Aho-Corasick algorithm?",
                "options": ["Trie with failure links", "Binary heap", "Segment tree", "Disjoint set"],
                "correct_answer": 0,
                "explanation": "Aho-Corasick builds a trie and adds failure links to support multiple-pattern matching."
            },
            {
                "question_text": "What is the purpose of a suffix automaton?",
                "options": ["Represent all substrings of a string compactly", "Maintain a minimum spanning tree", "Implement a priority queue", "Store only prefixes of a graph"],
                "correct_answer": 0,
                "explanation": "A suffix automaton represents the substrings of a string using a compact state-transition structure."
            },
            {
                "question_text": "Which data structure can support efficient union and intersection operations on sets represented as bit vectors?",
                "options": ["Bitset", "Stack", "Queue", "Binary search tree only"],
                "correct_answer": 0,
                "explanation": "Bitsets use bitwise operations to perform set operations efficiently."
            },
            {
                "question_text": "What is the main advantage of a van Emde Boas tree?",
                "options": ["Fast operations on integer keys from a bounded universe", "Constant-time sorting of arbitrary strings", "Efficient graph traversal only", "It uses no memory"],
                "correct_answer": 0,
                "explanation": "Van Emde Boas trees support predecessor, successor, insertion, and deletion in O(log log U) time for a universe of size U."
            },
            {
                "question_text": "Which data structure supports predecessor and successor queries in O(log log U) time for a bounded integer universe?",
                "options": ["Van Emde Boas tree", "Ordinary stack", "Circular queue", "Unsorted linked list"],
                "correct_answer": 0,
                "explanation": "Van Emde Boas trees provide logarithmic-in-logarithm universe bounds for these operations."
            },
            {
                "question_text": "What is the main purpose of a Cartesian tree?",
                "options": ["Maintain heap order on values and inorder order on positions", "Represent only weighted graphs", "Store keys using hashing", "Implement a circular queue"],
                "correct_answer": 0,
                "explanation": "A Cartesian tree combines heap order on priorities with inorder order on sequence positions."
            },
            {
                "question_text": "Which data structure is commonly used to answer range minimum queries in O(1) after preprocessing static data?",
                "options": ["Sparse table", "Stack", "Queue", "Hash map only"],
                "correct_answer": 0,
                "explanation": "A sparse table can answer idempotent range minimum queries in constant time after preprocessing."
            },
            {
                "question_text": "What is the preprocessing time complexity of a conventional sparse table for range minimum queries?",
                "options": ["O(n log n)", "O(1)", "O(log n)", "O(n² log n)"],
                "correct_answer": 0,
                "explanation": "The table stores answers for intervals of powers-of-two lengths."
            },
            {
                "question_text": "Which data structure is suitable for maintaining a dynamic sequence with split and merge operations in expected logarithmic time?",
                "options": ["Implicit treap", "Simple stack", "Bloom filter", "Adjacency matrix"],
                "correct_answer": 0,
                "explanation": "An implicit treap combines randomized priorities with sequence positions to support split and merge efficiently."
            }
        ]
    }
]
