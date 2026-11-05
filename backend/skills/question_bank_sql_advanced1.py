
_QUESTIONS = [

    # RECURSIVE CTEs (1-10)
    ("Which keyword enables recursive common table expressions in PostgreSQL?", ["WITH LOOP", "WITH RECURSIVE", "REPEAT QUERY", "START RECURSION"], 1, "WITH RECURSIVE enables recursive CTE execution."),
    ("What are the two typical parts of a recursive CTE?", ["Anchor and recursive term", "SELECT and DELETE", "Index and constraint", "Trigger and function"], 0, "A recursive CTE normally contains an initial anchor term and a recursive term."),
    ("Which operator commonly combines the anchor and recursive terms?", ["JOIN", "UNION ALL", "INTERSECT", "EXCEPT"], 1, "UNION ALL commonly combines recursive CTE terms."),
    ("What prevents an unbounded recursive CTE from continuing indefinitely?", ["A termination condition", "An index", "A foreign key", "A primary key"], 0, "The recursive term needs a condition that eventually stops producing rows."),
    ("Which PostgreSQL clause can limit recursion iterations?", ["MAX RECURSION", "CYCLE LIMIT", "No general MAXRECURSION clause; use a termination condition", "STOP AFTER"], 2, "PostgreSQL recursion is generally controlled through the recursive term and termination conditions."),
    ("What is the purpose of the CYCLE clause in a recursive CTE?", ["Detect cycles in recursive traversal", "Create an index", "Delete duplicate tables", "Commit a transaction"], 0, "CYCLE can detect repeated values in recursive paths."),
    ("Which data structure is commonly represented using a recursive CTE?", ["Employee reporting hierarchy", "A simple flat lookup table", "A database password", "An ordinary index"], 0, "Recursive CTEs are useful for hierarchical relationships."),
    ("What does SEARCH DEPTH FIRST provide in a recursive CTE?", ["A depth-first ordering column", "A new database", "A permanent index", "A transaction lock"], 0, "SEARCH DEPTH FIRST generates an ordering column for depth-first traversal."),
    ("Can a recursive CTE reference itself?", ["Yes", "No", "Only in MySQL", "Only when creating a table"], 0, "The recursive term references the CTE itself."),
    ("What is an important risk when writing recursive queries?", ["Uncontrolled recursion or repeated rows", "Automatic database deletion", "Automatic index creation", "Changing column data types"], 0, "Incorrect termination or cycle handling can cause excessive recursion."),

    # WINDOW FUNCTIONS AND FRAMES (11-20)
    ("What does ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW define?", ["A frame from the partition start through the current row", "Only the next row", "The entire database", "A table constraint"], 0, "It defines a cumulative window frame."),
    ("What does RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW commonly include?", ["Rows up to the current ordering value, including peers", "Only one physical row", "All database tables", "Only NULL values"], 0, "RANGE uses ordering values and includes peer rows."),
    ("What is a peer group in a window function?", ["Rows equal on the window ORDER BY expressions", "Rows from different databases", "Rows with duplicate primary keys", "Rows without indexes"], 0, "Peer rows have equal values for the window ordering expressions."),
    ("Which window frame unit counts physical rows?", ["RANGE", "ROWS", "GROUPS", "PARTITION"], 1, "ROWS defines a frame using physical row offsets."),
    ("Which window frame unit counts peer groups?", ["ROWS", "RANGE", "GROUPS", "RECORDS"], 2, "GROUPS measures offsets in peer groups."),
    ("What does FIRST_VALUE() return?", ["The first value in the window frame", "The first table in the database", "The smallest primary key always", "The first inserted row always"], 0, "FIRST_VALUE returns the first value according to the window frame ordering."),
    ("What does LAST_VALUE() depend on?", ["The window frame boundaries", "Only the table name", "The database owner", "The number of indexes"], 0, "LAST_VALUE returns the last value in the current window frame."),
    ("Why is an explicit frame often useful with LAST_VALUE()?", ["The default frame may end at the current row's peer group", "It automatically creates indexes", "It changes the table structure", "It disables sorting"], 0, "An explicit frame can extend to UNBOUNDED FOLLOWING to get the partition's final value."),
    ("Which function returns a relative rank between zero and one?", ["RANK()", "PERCENT_RANK()", "ROW_NUMBER()", "NTILE()"], 1, "PERCENT_RANK calculates relative rank within a partition."),
    ("Which function calculates the cumulative distribution of a row?", ["CUME_DIST()", "DENSE_RANK()", "LAG()", "FIRST_VALUE()"], 0, "CUME_DIST returns the fraction of partition rows preceding or tied with the current row."),

    # LATERAL JOINS AND ADVANCED QUERYING (21-30)
    ("What does LATERAL allow a FROM-subquery to do?", ["Reference columns from preceding FROM items", "Create a permanent table", "Commit another transaction", "Disable foreign keys"], 0, "LATERAL allows a subquery to reference preceding FROM items."),
    ("Which join is commonly used with a LATERAL subquery to preserve left-side rows?", ["CROSS JOIN", "LEFT JOIN LATERAL", "FULL JOIN only", "NATURAL JOIN"], 1, "LEFT JOIN LATERAL preserves left rows when the lateral subquery returns no rows."),
    ("What is the purpose of DISTINCT ON in PostgreSQL?", ["Return the first row for each distinct group", "Remove an entire table", "Create a unique index", "Count all records"], 0, "DISTINCT ON selects one row per distinct expression group."),
    ("What is required when using DISTINCT ON with ORDER BY?", ["DISTINCT ON expressions must match the leftmost ORDER BY expressions", "ORDER BY must be omitted", "Every column must be unique", "A foreign key is required"], 0, "PostgreSQL requires DISTINCT ON expressions to match the leftmost ORDER BY expressions."),
    ("Which PostgreSQL feature allows a query to return data-modification results?", ["RETURNING", "OUTPUT TABLE", "GET CHANGES", "RESULT SET"], 0, "RETURNING returns values from rows affected by INSERT, UPDATE or DELETE."),
    ("What is an anti-join used for?", ["Finding rows without matching rows in another relation", "Finding only matching rows", "Combining every possible row pair", "Sorting duplicate rows"], 0, "An anti-join identifies unmatched rows."),
    ("Which approach is generally safe for checking that no matching child row exists?", ["NOT EXISTS", "NOT IN with possible NULL values", "CROSS JOIN", "ORDER BY"], 0, "NOT EXISTS avoids the NULL-related pitfalls that can affect NOT IN."),
    ("What does a semi-join return?", ["Rows from one side that have a match on the other side", "All combinations of both tables", "Only unmatched rows", "Only duplicate columns"], 0, "A semi-join returns qualifying rows from one relation without duplicating them for multiple matches."),
    ("What is the purpose of a correlated LATERAL subquery?", ["Compute a result for each preceding row", "Create a database backup", "Delete an index", "Change transaction isolation"], 0, "A LATERAL subquery can calculate results using each preceding row."),
    ("Which SQL feature is useful for selecting the top three orders for each customer?", ["Window ranking with PARTITION BY", "DROP TABLE", "CROSS JOIN without conditions", "TRUNCATE"], 0, "ROW_NUMBER or RANK partitioned by customer can identify top orders."),

    # JSON AND JSONB (31-40)
    ("What is a key difference between PostgreSQL JSON and JSONB?", ["JSONB stores a decomposed binary representation", "JSONB cannot store objects", "JSON is always indexed automatically", "JSONB stores only numbers"], 0, "JSONB stores data in a decomposed binary format suitable for efficient processing."),
    ("Which operator extracts a JSON object field as JSON in PostgreSQL?", ["->", "->>", "#>>", "::"], 0, "The -> operator returns a JSON value."),
    ("Which operator extracts a JSON field as text?", ["->", "->>", "@>", "#"], 1, "The ->> operator returns a text value."),
    ("Which operator tests whether JSONB contains another JSONB value?", ["@>", "||", "->>", "#-"], 0, "The @> operator tests JSONB containment."),
    ("Which operator tests JSONB key existence?", ["?", "@>", "->>", "||"], 0, "The ? operator checks whether a top-level key or array element exists."),
    ("Which operator removes a key or array element from JSONB?", ["||", "#-", "->", "@@"], 1, "The #- operator removes a field or path from JSONB."),
    ("Which PostgreSQL function expands a JSON array into a set of JSON values?", ["jsonb_array_elements()", "jsonb_object_keys()", "jsonb_build_object()", "jsonb_typeof()"], 0, "jsonb_array_elements expands a JSON array into rows."),
    ("Which function returns the keys of a JSON object?", ["jsonb_array_elements()", "jsonb_object_keys()", "jsonb_each_text()", "jsonb_strip_nulls()"], 1, "jsonb_object_keys returns the top-level object keys."),
    ("Which index type is commonly used to accelerate JSONB containment queries?", ["GIN", "BRIN only", "Hash only", "No index type"], 0, "GIN indexes support many JSONB containment and key-existence operations."),
    ("What does jsonb_set() do?", ["Updates or creates a value at a specified JSONB path", "Deletes the whole table", "Creates a JSON index", "Converts JSONB to SQL"], 0, "jsonb_set returns a JSONB value with the specified path updated."),

    # ARRAY AND FULL TEXT SEARCH (41-50)
    ("Which PostgreSQL operator checks whether an array contains another array?", ["@>", "->>", "||", "#-"], 0, "The @> array operator checks containment."),
    ("Which operator checks whether two arrays overlap?", ["&&", "@>", "->", "IS"], 0, "The && operator checks whether arrays share any elements."),
    ("Which function expands an array into rows?", ["unnest()", "array_length()", "array_append()", "array_to_string()"], 0, "unnest converts array elements into a set of rows."),
    ("Which function returns the number of dimensions in an array?", ["array_length()", "array_ndims()", "cardinality()", "unnest()"], 1, "array_ndims returns the number of array dimensions."),
    ("Which function returns the total number of elements in an array?", ["array_dims()", "cardinality()", "array_ndims()", "array_lower()"], 1, "cardinality returns the total number of array elements."),
    ("Which PostgreSQL type represents a parsed text-search document?", ["tsvector", "tsquery", "textsearch", "varchar"], 0, "tsvector stores normalized lexemes for full-text search."),
    ("Which PostgreSQL type represents a full-text search query?", ["tsvector", "tsquery", "jsonb", "bytea"], 1, "tsquery stores normalized search terms and operators."),
    ("Which operator matches a tsvector against a tsquery?", ["@@", "@>", "&&", "->"], 0, "The @@ operator performs a full-text search match."),
    ("Which function converts text into a tsvector using a text-search configuration?", ["to_tsvector()", "to_tsquery()", "ts_headline()", "plainto_tsquery()"], 0, "to_tsvector parses text into normalized lexemes."),
    ("Which PostgreSQL index type is commonly useful for full-text search?", ["GIN", "BRIN only", "B-tree only", "Hash only"], 0, "GIN is commonly used to index tsvector values."),

    # INDEXING AND QUERY PLANNING (51-60)
    ("What is a covering index?", ["An index containing all columns needed by a query", "An index on every database", "A temporary table", "An index with no key"], 0, "A covering index includes the data needed by a query, potentially enabling index-only scans."),
    ("Which PostgreSQL clause adds non-key columns to an index?", ["INCLUDE", "COVER", "APPEND", "STORE"], 0, "INCLUDE stores additional non-key columns in an index."),
    ("What is an expression index?", ["An index built on an expression or function result", "An index without data", "An index on a database name", "An index on every table"], 0, "An expression index stores values computed from an expression."),
    ("Which index could help a query filtering on LOWER(email)?", ["An expression index on LOWER(email)", "An index on an unrelated column", "A BRIN index on a timestamp only", "No index can help"], 0, "An expression index can index the result of LOWER(email)."),
    ("What is a partial index predicate?", ["A condition defining which rows are indexed", "A query sorting condition only", "A foreign key", "A transaction rule"], 0, "The predicate restricts the rows included in a partial index."),
    ("What does index selectivity describe?", ["How effectively an indexed condition narrows rows", "The number of database users", "The size of a transaction log", "The number of tables"], 0, "Selective conditions match relatively few rows."),
    ("What is a sequential scan?", ["Reading table pages sequentially", "Reading only an index", "Reading only primary keys", "Scanning database users"], 0, "A sequential scan reads table pages rather than navigating an index."),
    ("What does a bitmap heap scan combine?", ["Bitmap index results with heap access", "Two database backups", "Two transactions", "Two foreign keys"], 0, "A bitmap heap scan uses bitmap information to visit matching heap pages."),
    ("What is the purpose of VACUUM in PostgreSQL?", ["Reclaim or make reusable space occupied by dead tuples", "Create primary keys", "Encrypt tables", "Change column types"], 0, "VACUUM handles dead tuples and helps maintain table storage."),
    ("What does VACUUM FULL do differently from ordinary VACUUM?", ["Rewrites the table and can return space to the operating system", "Only collects query statistics", "Only rebuilds foreign keys", "Does not lock the table"], 0, "VACUUM FULL rewrites the table and requires a stronger lock."),

    # PARTITIONING AND STORAGE (61-70)
    ("What is table partitioning?", ["Dividing a large logical table into smaller physical pieces", "Creating duplicate databases", "Splitting one query into users", "Deleting table indexes"], 0, "Partitioning divides a table into partitions based on a partition key."),
    ("Which partitioning method divides data into non-overlapping value ranges?", ["LIST", "RANGE", "HASH", "ROUND"], 1, "RANGE partitioning assigns values to ranges."),
    ("Which partitioning method assigns rows based on specific listed values?", ["RANGE", "HASH", "LIST", "SEQUENCE"], 2, "LIST partitioning assigns rows to specified value lists."),
    ("Which partitioning method distributes rows using a hash of the partition key?", ["LIST", "RANGE", "HASH", "ORDER"], 2, "HASH partitioning distributes rows using a hash calculation."),
    ("What is partition pruning?", ["Skipping partitions that cannot match a query", "Deleting old partitions", "Rebuilding every index", "Merging all databases"], 0, "Partition pruning avoids scanning irrelevant partitions."),
    ("What is a partition key?", ["The column or expression used to determine a row's partition", "The database password", "The primary key of every database", "A query alias"], 0, "The partition key determines which partition receives a row."),
    ("Can a PostgreSQL partitioned table have a primary key?", ["Yes, subject to partition-key requirements", "No", "Only if it has one partition", "Only if it has no indexes"], 0, "A partitioned table can have a primary key, which must include all partition key columns."),
    ("What is a default partition?", ["A partition that stores rows not matching any explicitly defined partition", "A backup table", "A temporary index", "A system database"], 0, "A default partition catches rows not assigned to another partition."),
    ("What is partition-wise join?", ["Joining corresponding partitions where the planner can do so", "Joining every database", "Joining only indexes", "A join without a condition"], 0, "Partition-wise joins can execute joins separately across matching partitions."),
    ("Why might time-based partitioning be useful for event tables?", ["It can simplify retention and reduce scans to relevant periods", "It automatically encrypts events", "It prevents all inserts", "It removes the need for constraints"], 0, "Time partitions help manage historical data and prune irrelevant periods."),

    # TRANSACTIONS, LOCKS AND CONCURRENCY (71-80)
    ("What is MVCC in PostgreSQL?", ["Multi-Version Concurrency Control", "Multiple View Column Creation", "Managed Virtual Cache Control", "Multi-Value Command Commit"], 0, "MVCC allows concurrent transactions to work with different row versions."),
    ("What is a serialization failure?", ["A transaction cannot be completed under serializable isolation without violating serial execution", "A table has invalid columns", "An index is missing", "A user has no password"], 0, "PostgreSQL can abort a transaction when it detects a serialization anomaly."),
    ("What should an application generally do after a serialization failure?", ["Retry the complete transaction when appropriate", "Ignore the error", "Drop the database", "Disable all constraints"], 0, "Applications commonly retry the transaction after a serialization failure."),
    ("Which PostgreSQL lock mode is acquired by SELECT FOR UPDATE?", ["ROW SHARE", "ROW EXCLUSIVE", "A row-level lock that conflicts with competing updates", "ACCESS EXCLUSIVE"], 2, "FOR UPDATE obtains row-level locks on selected rows."),
    ("Which command can inspect currently held locks in PostgreSQL?", ["Query pg_locks", "SHOW LOCKS only", "LIST LOCKS", "DESCRIBE LOCKS"], 0, "The pg_locks system view exposes lock information."),
    ("What does SKIP LOCKED do in a locking SELECT?", ["Skips rows that cannot be locked immediately", "Deletes locked rows", "Waits forever for all locks", "Releases all locks"], 0, "SKIP LOCKED is useful for queue-like workloads with multiple workers."),
    ("What does NOWAIT do in a locking SELECT?", ["Raises an error instead of waiting for a conflicting lock", "Waits until all rows are free", "Deletes locked rows", "Commits the transaction"], 0, "NOWAIT avoids waiting for a conflicting lock."),
    ("What is a lock escalation?", ["Replacing many fine-grained locks with a coarser lock", "Turning an index into a table", "Increasing a column size", "Changing a password"], 0, "Lock escalation replaces many fine-grained locks with a larger lock; PostgreSQL does not generally use automatic row-to-table lock escalation."),
    ("What is the purpose of advisory locks?", ["Application-defined coordination using lock identifiers", "Automatic index creation", "Data encryption", "Changing isolation levels"], 0, "Advisory locks let applications coordinate access to resources."),
    ("Which PostgreSQL function can acquire a transaction-level advisory lock?", ["pg_advisory_xact_lock()", "pg_create_index()", "pg_lock_table()", "pg_begin_lock()"], 0, "pg_advisory_xact_lock obtains an advisory lock released at transaction end."),

    # FUNCTIONS, SECURITY AND DATABASE OPERATIONS (81-90)
    ("What is the difference between a procedure and a function in PostgreSQL?", ["Procedures are called with CALL and can support transaction control in appropriate contexts", "Functions cannot return values", "Procedures must be indexes", "They are identical in every way"], 0, "Procedures are invoked with CALL and have different return and transaction-control behavior."),
    ("Which command invokes a PostgreSQL stored procedure?", ["SELECT", "CALL", "EXECUTE TABLE", "RUN FUNCTION"], 1, "CALL invokes a stored procedure."),
    ("What does SECURITY DEFINER mean for a PostgreSQL routine?", ["It executes with the privileges of its owner", "It executes without permissions", "It runs as every database user", "It disables SQL checks"], 0, "SECURITY DEFINER routines execute using the routine owner's privileges."),
    ("Why should search_path be carefully controlled in SECURITY DEFINER routines?", ["To reduce object-shadowing and privilege-escalation risks", "To improve image loading", "To remove all indexes", "To increase column length"], 0, "An unsafe search_path can allow malicious objects to shadow trusted objects."),
    ("What does EXPLAIN (BUFFERS) provide?", ["Buffer activity information for a query plan", "A database backup", "A list of passwords", "Only SQL syntax"], 0, "BUFFERS reports buffer hits, reads and related activity."),
    ("What is pg_stat_statements used for?", ["Tracking planning and execution statistics for SQL statements", "Creating tables automatically", "Managing user passwords", "Encrypting backups"], 0, "pg_stat_statements provides aggregated statement statistics."),
    ("What does pg_stat_activity show?", ["Current database sessions and activity", "Only table indexes", "Only stored procedures", "Database backup contents"], 0, "pg_stat_activity provides information about server processes and active sessions."),
    ("Which PostgreSQL command changes ownership of a table?", ["ALTER TABLE ... OWNER TO", "UPDATE OWNER", "CHANGE USER", "SET TABLE USER"], 0, "ALTER TABLE can change the table owner."),
    ("Which SQL command removes a role's privileges on an object?", ["REVOKE", "DELETE", "DROP", "TRUNCATE"], 0, "REVOKE removes granted privileges."),
    ("What is row-level security (RLS)?", ["A feature that restricts which rows a user can access or modify", "A method for compressing rows", "An indexing method", "A transaction isolation level"], 0, "RLS policies control row access for database users."),

    # BACKUP, REPLICATION AND RELIABILITY (91-100)
    ("Which PostgreSQL utility creates a logical backup in custom archive format?", ["pg_dump -Fc", "pg_restore -Fc", "pg_basebackup -Fc", "psql -Fc"], 0, "pg_dump with -Fc creates a custom-format archive."),
    ("Which utility restores a custom-format pg_dump archive?", ["pg_dump", "pg_restore", "pg_basebackup", "vacuumdb"], 1, "pg_restore restores archives produced by pg_dump in formats such as custom."),
    ("Which PostgreSQL utility creates a physical base backup?", ["pg_dump", "pg_restore", "pg_basebackup", "createdb"], 2, "pg_basebackup creates a physical backup of a PostgreSQL cluster."),
    ("What is point-in-time recovery (PITR)?", ["Restoring a database to a chosen time using a base backup and WAL", "Restoring only one index", "Rebuilding a view", "Deleting old transactions"], 0, "PITR uses a base backup and archived WAL to recover to a target time."),
    ("What does WAL stand for in PostgreSQL?", ["Write-Ahead Logging", "Wide Access Layer", "Write-After Locking", "Web Application Log"], 0, "WAL stands for Write-Ahead Logging."),
    ("What is the purpose of WAL?", ["Record changes for durability and recovery", "Store frontend CSS", "Replace all indexes", "Manage user interfaces"], 0, "WAL records changes so PostgreSQL can recover committed data."),
    ("What is streaming replication?", ["Continuously sending WAL records from a primary to standby servers", "Copying SQL queries into views", "Synchronizing browser sessions", "Replicating only table names"], 0, "Streaming replication sends WAL from a primary server to standby servers."),
    ("What is a hot standby?", ["A standby server that can accept read-only queries while replaying WAL", "A server with no recovery", "A backup stored in memory only", "A database without users"], 0, "A hot standby supports read-only queries during recovery."),
    ("What is synchronous replication?", ["The primary waits for confirmation from configured synchronous standbys", "All replicas are always offline", "Only schema changes are copied", "Every query runs on every server"], 0, "Synchronous replication waits for acknowledgement according to its configured mode."),
    ("What is logical replication based on in PostgreSQL?", ["Publication and subscription of logical data changes", "Copying physical data files only", "Sharing database passwords", "Replicating query plans"], 0, "Logical replication uses publications and subscriptions to transfer data changes."),
]


QUESTION_BANK_SQL_ADVANCED1 = [
    {
        "skill": "SQL & Databases",
        "difficulty": "advanced",
        "question_text": question,
        "options": options,
        "correct_answer": answer,
        "explanation": explanation,
    }
    for question, options, answer, explanation in _QUESTIONS
]
