SELECT 
    id,
    CASE
        WHEN p_id IS NULL THEN 'Root'
        WHEN id in (SELECT p_id from Tree) THEN 'Inner'
        ELSE 'Leaf'
    END AS type
FROM Tree;
