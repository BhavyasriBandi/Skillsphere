
_QUESTIONS = [

    # 1. JOINS (1-10)
    ("Which join returns all rows from both tables, matching where possible?", ["INNER JOIN", "LEFT JOIN", "FULL OUTER JOIN", "CROSS JOIN"], 2, "FULL OUTER JOIN preserves unmatched rows from both tables."),
    ("Which join returns rows that have no matching record in the other table?", ["INNER JOIN", "ANTI JOIN", "CROSS JOIN", "SELF JOIN"], 1, "An anti join returns unmatched rows; it is commonly implemented using NOT EXISTS or LEFT JOIN with IS NULL."),
    ("What is a self join?", ["Joining a table with itself", "Joining three databases", "Joining without a condition", "Joining only primary keys"], 0, "A self join compares rows within the same table."),
    ("Which clause specifies the matching condition in a JOIN?", ["GROUP BY", "ON", "HAVING", "ORDER BY"], 1, "ON specifies the join condition."),
    ("What does NATURAL JOIN use to match tables?", ["All columns", "Columns with the same names", "Primary keys only", "Foreign keys only"], 1, "NATURAL JOIN automatically uses identically named columns."),
    ("What is the result of an INNER JOIN when no rows match?", ["All left rows", "All right rows", "No matching rows", "A Cartesian product"], 2, "INNER JOIN returns only matching rows."),
    ("Which join can produce a Cartesian product?", ["INNER JOIN", "CROSS JOIN", "LEFT JOIN", "RIGHT JOIN"], 1, "CROSS JOIN combines every row from one table with every row from the other."),
    ("What is the purpose of table aliases in joins?", ["Delete duplicate rows", "Shorten table references", "Create indexes", "Change table names permanently"], 1, "Aliases make queries shorter and clearer."),
    ("Which join is appropriate to retain every employee even if they have no department?", ["INNER JOIN", "LEFT JOIN from employees to departments", "CROSS JOIN", "RIGHT JOIN from employees to departments"], 1, "LEFT JOIN preserves all employee rows."),
    ("How can you find customers who have no orders?", ["INNER JOIN", "LEFT JOIN followed by WHERE order_id IS NULL", "CROSS JOIN", "GROUP BY only"], 1, "A LEFT JOIN with a NULL check identifies unmatched customers."),

    # 2. SUBQUERIES (11-20)
    ("What is a correlated subquery?", ["A query that runs independently", "A subquery that references the outer query", "A query without WHERE", "A query that creates a table"], 1, "A correlated subquery references columns from its outer query."),
    ("Which operator checks whether a subquery returns at least one row?", ["IN", "EXISTS", "BETWEEN", "LIKE"], 1, "EXISTS tests whether the subquery returns rows."),
    ("Which operator checks whether a value matches any value returned by a subquery?", ["IN", "IS NULL", "LIKE", "CASE"], 0, "IN checks membership in a result set."),
    ("What does NOT EXISTS return?", ["True when the subquery returns rows", "True when the subquery returns no rows", "Only NULL values", "All duplicate rows"], 1, "NOT EXISTS is true when the subquery returns no rows."),
    ("Which comparison operator can compare a value against every value in a subquery result?", ["ANY", "ALL", "LIKE", "IS"], 1, "ALL requires the comparison to be true for every returned value."),
    ("Which keyword can compare a value against at least one value in a subquery result?", ["ALL", "ANY", "NONE", "ONLY"], 1, "ANY succeeds if the comparison is true for at least one value."),
    ("What is a scalar subquery?", ["A subquery returning one column and at most one row", "A subquery returning many tables", "A query without SELECT", "A query returning only indexes"], 0, "A scalar subquery returns a single value."),
    ("What happens if a scalar subquery returns more than one row?", ["The first row is always used", "An error occurs", "All rows are combined", "The result becomes NULL"], 1, "A scalar subquery must return at most one row."),
    ("Where can a subquery be used?", ["Only in WHERE", "Only in SELECT", "In clauses such as SELECT, FROM and WHERE, where supported", "Only in ORDER BY"], 2, "Subqueries can appear in several SQL query clauses."),
    ("Which approach is commonly used to find employees earning more than the average salary?", ["Compare salary with a subquery using AVG()", "Use DELETE", "Use CROSS JOIN only", "Use DROP TABLE"], 0, "A scalar subquery can calculate the average salary for comparison."),

    # 3. AGGREGATION AND GROUPING (21-30)
    ("Which clause filters groups after aggregate calculations?", ["WHERE", "HAVING", "FROM", "DISTINCT"], 1, "HAVING filters grouped results."),
    ("Which clause filters individual rows before grouping?", ["HAVING", "WHERE", "ORDER BY", "LIMIT"], 1, "WHERE filters rows before aggregation."),
    ("What does COUNT(column_name) count?", ["All rows including NULL values", "Non-NULL values in that column", "Only duplicate values", "Only numeric values"], 1, "COUNT(column) ignores NULL values."),
    ("What does COUNT(*) count?", ["Only non-NULL columns", "All rows", "Only unique rows", "Only numeric rows"], 1, "COUNT(*) counts every row."),
    ("Which aggregate function ignores NULL inputs?", ["SUM()", "AVG()", "MIN()", "All of these"], 3, "These aggregate functions ignore NULL inputs."),
    ("What does GROUP BY ROLLUP provide?", ["Only distinct rows", "Hierarchical subtotals and a grand total", "A table backup", "A unique index"], 1, "ROLLUP generates grouping subtotals and a grand total."),
    ("Which PostgreSQL grouping feature creates combinations of grouping sets?", ["CUBE", "LIMIT", "OFFSET", "RETURNING"], 0, "CUBE generates subtotals for combinations of grouping columns."),
    ("What is the purpose of GROUPING SETS?", ["Create multiple grouping combinations in one query", "Create multiple databases", "Remove table constraints", "Sort records"], 0, "GROUPING SETS allows several grouping levels in one query."),
    ("Which expression counts distinct non-NULL department IDs?", ["COUNT(department_id)", "COUNT(DISTINCT department_id)", "SUM(DISTINCT department_id)", "UNIQUE(department_id)"], 1, "COUNT(DISTINCT column) counts unique non-NULL values."),
    ("Can aggregate functions generally be nested directly, such as SUM(AVG(salary)) at the same query level?", ["Yes, always", "No, use a subquery or another query level", "Only with DISTINCT", "Only with ORDER BY"], 1, "Nested aggregates at the same query level are not generally allowed; use separate query levels."),

    # 4. CTE AND SET OPERATIONS (31-40)
    ("What does CTE stand for?", ["Common Table Expression", "Combined Table Element", "Central Transaction Engine", "Common Transaction Entry"], 0, "CTE stands for Common Table Expression."),
    ("Which keyword begins a CTE?", ["WITH", "START", "DEFINE", "TEMP"], 0, "WITH introduces a CTE."),
    ("What is a recursive CTE commonly used for?", ["Hierarchical or repeated relationships", "Deleting indexes", "Encrypting columns", "Changing database users"], 0, "Recursive CTEs can traverse hierarchies and repeated relationships."),
    ("Which keyword is used in a recursive CTE?", ["REPEAT", "RECURSIVE", "LOOP", "ITERATE"], 1, "WITH RECURSIVE defines a recursive CTE."),
    ("What does UNION do by default?", ["Retains all duplicates", "Removes duplicate result rows", "Sorts only by primary key", "Deletes source records"], 1, "UNION removes duplicate rows."),
    ("Which set operator retains duplicate rows?", ["UNION", "UNION ALL", "INTERSECT", "EXCEPT"], 1, "UNION ALL retains duplicates."),
    ("What requirement applies to SELECT queries combined by UNION?", ["Same table name", "Same number of columns with compatible types", "Same primary key", "Same WHERE clause"], 1, "Combined queries need matching column counts and compatible types."),
    ("Which operator returns rows present in both query results?", ["UNION", "EXCEPT", "INTERSECT", "CROSS JOIN"], 2, "INTERSECT returns common rows."),
    ("Which operator returns rows from the first query that are absent from the second?", ["UNION", "EXCEPT", "INTERSECT", "INNER JOIN"], 1, "EXCEPT subtracts the second result from the first."),
    ("Can a CTE be referenced by the main query that follows it?", ["Yes", "No", "Only if it has an index", "Only if it is recursive"], 0, "A CTE is available to the statement that defines it."),

    # 5. WINDOW FUNCTIONS (41-50)
    ("Which clause defines a window for a window function?", ["GROUP BY", "OVER", "HAVING", "WITH"], 1, "OVER defines the window used by a window function."),
    ("Which function assigns a unique sequential number to rows within a window?", ["RANK()", "ROW_NUMBER()", "DENSE_RANK()", "COUNT()"], 1, "ROW_NUMBER assigns a unique sequential number."),
    ("What is the difference between RANK() and DENSE_RANK()?", ["RANK skips numbers after ties; DENSE_RANK does not", "DENSE_RANK skips numbers; RANK does not", "They are always identical", "RANK returns text"], 0, "RANK leaves gaps after tied rankings; DENSE_RANK does not."),
    ("Which window function returns the value from the previous row?", ["LEAD()", "LAG()", "FIRST_VALUE()", "NTILE()"], 1, "LAG accesses a preceding row."),
    ("Which window function returns a value from a following row?", ["LAG()", "LEAD()", "LAST_VALUE()", "ROW_NUMBER()"], 1, "LEAD accesses a subsequent row."),
    ("Which function divides ordered rows into approximately equal groups?", ["NTILE()", "RANK()", "COUNT()", "SUM()"], 0, "NTILE divides rows into a specified number of buckets."),
    ("Which clause partitions rows into groups for window calculations?", ["PARTITION BY", "GROUP BY", "HAVING", "DISTINCT"], 0, "PARTITION BY divides the window into groups."),
    ("Do window functions normally preserve individual rows in the result?", ["Yes", "No, they always collapse rows", "Only with DELETE", "Only with DISTINCT"], 0, "Window functions calculate values while retaining individual rows."),
    ("Which function returns the first value in a window frame?", ["FIRST_VALUE()", "LEAD()", "LAG()", "RANK()"], 0, "FIRST_VALUE returns the first value in the frame."),
    ("Which window function calculates a running total when used with an appropriate frame?", ["SUM() OVER()", "COUNT(*) only", "DISTINCT()", "GROUPING()"], 0, "SUM used as a window function can calculate a running total."),

    # 6. TRANSACTIONS AND CONCURRENCY (51-60)
    ("Which command marks a transaction savepoint?", ["SAVEPOINT", "CHECKPOINT", "COMMITPOINT", "ROLLBACK TO"], 0, "SAVEPOINT creates a point for partial rollback."),
    ("Which command returns a transaction to a named savepoint?", ["COMMIT TO", "ROLLBACK TO SAVEPOINT", "DROP SAVEPOINT", "RESTORE TABLE"], 1, "ROLLBACK TO SAVEPOINT undoes changes made after that savepoint."),
    ("Which PostgreSQL isolation level is the default?", ["READ UNCOMMITTED", "READ COMMITTED", "REPEATABLE READ", "SERIALIZABLE"], 1, "PostgreSQL defaults to READ COMMITTED."),
    ("Which isolation level provides a stable snapshot for a transaction in PostgreSQL?", ["READ COMMITTED", "REPEATABLE READ", "READ UNCOMMITTED", "AUTOCOMMIT"], 1, "REPEATABLE READ uses a transaction-level snapshot."),
    ("Which isolation level offers the strongest standard transaction isolation?", ["READ COMMITTED", "REPEATABLE READ", "SERIALIZABLE", "READ UNCOMMITTED"], 2, "SERIALIZABLE provides the strongest standard isolation level."),
    ("What is a dirty read?", ["Reading uncommitted changes from another transaction", "Reading an indexed row", "Reading duplicate records", "Reading a backup"], 0, "A dirty read observes data that another transaction has not committed."),
    ("What is a non-repeatable read?", ["The same row returns different committed values in one transaction", "A query returns no rows", "An index is rebuilt", "A table is renamed"], 0, "A non-repeatable read occurs when another transaction changes a row between reads."),
    ("What is a phantom read?", ["A repeated query returns a different set of rows", "A table disappears", "A transaction commits twice", "A query has no WHERE clause"], 0, "Phantom reads involve changes to the set of rows matching a repeated condition."),
    ("What is a deadlock?", ["Two or more transactions wait on each other in a cycle", "A server has no indexes", "A query returns duplicates", "A database is read-only"], 0, "A deadlock occurs when transactions wait on each other's locks."),
    ("Which PostgreSQL clause locks selected rows for updating?", ["FOR UPDATE", "LOCK TABLE ONLY", "UPDATE LOCK", "WITH LOCK"], 0, "SELECT ... FOR UPDATE locks selected rows against conflicting updates."),

    # 7. INDEXES AND PERFORMANCE (61-70)
    ("Which PostgreSQL index type is the default?", ["GIN", "GiST", "B-tree", "BRIN"], 2, "B-tree is the default PostgreSQL index type."),
    ("Which index type is often useful for full-text search and array containment?", ["B-tree", "GIN", "BRIN", "Hash only"], 1, "GIN is useful for composite values such as arrays and full-text search."),
    ("Which PostgreSQL index type can be useful for very large tables with naturally ordered data?", ["BRIN", "GIN", "Hash", "Bitmap"], 0, "BRIN indexes summarize ranges of physically adjacent table pages."),
    ("What is a composite index?", ["An index on multiple columns", "An index on multiple databases", "A duplicate table", "An index without columns"], 0, "A composite index contains more than one indexed column."),
    ("What is a partial index?", ["An index covering only rows that satisfy a condition", "An index covering every database", "An index without a key", "An index on a view only"], 0, "A partial index includes only rows matching its predicate."),
    ("What does EXPLAIN show in PostgreSQL?", ["The planned execution strategy", "The complete database backup", "All user passwords", "Only table constraints"], 0, "EXPLAIN displays the query execution plan."),
    ("What does EXPLAIN ANALYZE additionally do?", ["Executes the query and reports actual execution details", "Only checks syntax", "Creates an index automatically", "Deletes unused rows"], 0, "EXPLAIN ANALYZE runs the statement and reports actual execution information."),
    ("Why might a database not use an available index?", ["The planner estimates a sequential scan is cheaper", "Indexes cannot be used with WHERE", "Indexes work only on text", "Every query must use an index"], 0, "The planner chooses the estimated lowest-cost execution plan."),
    ("What is the purpose of ANALYZE in PostgreSQL?", ["Collect planner statistics", "Delete table rows", "Create a view", "Commit a transaction"], 0, "ANALYZE collects statistics used by the query planner."),
    ("What is an index-only scan?", ["A scan that can satisfy a query using index data without fetching table rows in all cases", "A scan that deletes an index", "A scan that reads every database", "A scan without a query"], 0, "An index-only scan can return data from the index when visibility information permits."),

    # 8. CONSTRAINTS AND SCHEMA DESIGN (71-80)
    ("What is a composite foreign key?", ["A foreign key containing multiple columns", "A foreign key in multiple databases", "A key without a reference", "A key that allows all duplicates"], 0, "A composite foreign key uses multiple columns."),
    ("Which constraint can enforce that a salary is greater than zero?", ["DEFAULT", "CHECK", "UNIQUE", "FOREIGN KEY"], 1, "CHECK can enforce salary > 0."),
    ("What does ON DELETE CASCADE do?", ["Deletes referencing rows when the referenced row is deleted", "Prevents every delete", "Sets all values to zero", "Creates a backup"], 0, "CASCADE propagates deletion to referencing rows."),
    ("What does ON DELETE SET NULL do?", ["Deletes the child table", "Sets referencing foreign-key columns to NULL", "Sets the primary key to zero", "Blocks all updates"], 1, "SET NULL clears the referencing foreign-key values."),
    ("What is a candidate key?", ["A minimal set of columns that uniquely identifies a row", "Any non-unique column", "A temporary table", "A database index only"], 0, "A candidate key is a minimal unique identifier."),
    ("What is a surrogate key?", ["An artificial identifier with no business meaning", "A natural email address", "A duplicated foreign key", "A calculated report"], 0, "A surrogate key is an artificial identifier, often generated by the database."),
    ("What is a natural key?", ["A key derived from meaningful real-world data", "A randomly generated identifier", "A temporary sequence", "An index name"], 0, "A natural key uses an attribute with real-world meaning."),
    ("What is referential integrity?", ["Ensuring references between related tables remain valid", "Sorting every table", "Encrypting every column", "Removing all NULL values"], 0, "Referential integrity keeps foreign-key references consistent."),
    ("Which PostgreSQL feature can generate sequential numeric values?", ["SEQUENCE", "VIEW", "TRIGGER only", "SCHEMA"], 0, "A sequence generates numeric values, often used for identifiers."),
    ("What does GENERATED ALWAYS AS IDENTITY provide?", ["Automatically generated identity values", "A calculated text column", "A foreign-key relationship", "An index on every column"], 0, "IDENTITY columns generate values using an associated sequence."),

    # 9. VIEWS, FUNCTIONS AND TRIGGERS (81-90)
    ("What is a materialized view?", ["A query result stored physically", "A normal table alias", "A temporary variable", "A foreign key"], 0, "A materialized view stores the result of its defining query."),
    ("Which PostgreSQL command refreshes a materialized view?", ["UPDATE VIEW", "REFRESH MATERIALIZED VIEW", "REBUILD VIEW", "ALTER VIEW REFRESH"], 1, "REFRESH MATERIALIZED VIEW recalculates its stored result."),
    ("What is a database trigger?", ["A routine automatically invoked by a specified database event", "A query alias", "A primary key", "A database backup"], 0, "Triggers execute in response to events such as INSERT, UPDATE or DELETE."),
    ("Which PostgreSQL command defines a trigger?", ["CREATE TRIGGER", "ADD EVENT", "MAKE FUNCTION", "CREATE EVENT"], 0, "CREATE TRIGGER defines a trigger."),
    ("What must a PostgreSQL trigger execute through?", ["A trigger function", "A normal view", "A sequence only", "A database index"], 0, "A PostgreSQL trigger invokes a trigger function."),
    ("Which special variable refers to the new row in a PostgreSQL row-level INSERT or UPDATE trigger?", ["OLD", "NEW", "CURRENT", "NEXT"], 1, "NEW contains the new row values."),
    ("Which special variable refers to the old row in a PostgreSQL DELETE trigger?", ["NEW", "OLD", "PREVIOUS", "LAST"], 1, "OLD contains the row values before deletion."),
    ("What is a stored function?", ["A reusable routine stored in the database", "A database backup file", "A table constraint", "A query result"], 0, "Stored functions encapsulate reusable database logic."),
    ("Which PostgreSQL command removes a function?", ["DELETE FUNCTION", "DROP FUNCTION", "REMOVE FUNCTION", "CLEAR FUNCTION"], 1, "DROP FUNCTION removes a stored function."),
    ("What does the RETURNING clause do in PostgreSQL?", ["Returns values from rows affected by a statement", "Rolls back a transaction", "Creates a new table", "Sorts output automatically"], 0, "RETURNING can return affected row values after INSERT, UPDATE or DELETE."),

    # 10. ADVANCED QUERY PRACTICE (91-100)
    ("Which PostgreSQL expression safely divides by zero by returning NULL for a zero denominator?", ["numerator / NULLIF(denominator, 0)", "numerator / COALESCE(denominator, 0)", "numerator * 0", "numerator / CASE"], 0, "NULLIF returns NULL when its arguments are equal, avoiding division by zero."),
    ("What does COALESCE(a, b, c) return?", ["The first non-NULL argument", "The last argument always", "The largest argument", "The sum of arguments"], 0, "COALESCE returns the first non-NULL expression."),
    ("What does NULLIF(a, b) return when a equals b?", ["a", "b", "NULL", "Zero"], 2, "NULLIF returns NULL when the two expressions are equal."),
    ("Which expression converts a value to a specified data type in PostgreSQL?", ["CAST(value AS type)", "CONVERT ONLY value", "CHANGE(value)", "TYPE(value)"], 0, "CAST converts an expression to a target type."),
    ("Which PostgreSQL operator extracts a JSON field as text?", ["->", "->>", "#>", "::"], 1, "The ->> operator extracts a JSON field as text."),
    ("Which PostgreSQL function returns the current date and time?", ["NOW()", "TODAY()", "CURRENT()", "DATE_NOW()"], 0, "NOW() returns the current transaction timestamp."),
    ("Which function returns the number of characters in a string in PostgreSQL?", ["SIZE()", "LENGTH()", "COUNT()", "WIDTH()"], 1, "LENGTH() returns the number of characters in a string."),
    ("Which PostgreSQL function concatenates strings with a separator?", ["CONCAT_WS()", "JOIN_TEXT()", "STRING_JOIN()", "MERGE_TEXT()"], 0, "CONCAT_WS concatenates values using a specified separator."),
    ("Which PostgreSQL clause allows an INSERT statement to update a row when a unique conflict occurs?", ["ON CONFLICT DO UPDATE", "ON ERROR UPDATE", "WHEN DUPLICATE", "IF EXISTS UPDATE"], 0, "ON CONFLICT DO UPDATE implements an upsert."),
    ("What is the purpose of OFFSET in a SELECT query?", ["Skip a specified number of rows", "Limit column count", "Delete old records", "Skip table constraints"], 0, "OFFSET skips a number of rows before returning results."),
]


QUESTION_BANK_SQL_INTERMEDIATE1 = [
    {
        "skill": "SQL & Databases",
        "difficulty": "intermediate",
        "question_text": question,
        "options": options,
        "correct_answer": answer,
        "explanation": explanation,
    }
    for question, options, answer, explanation in _QUESTIONS
]
