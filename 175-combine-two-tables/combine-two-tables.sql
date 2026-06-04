/* Write your T-SQL query statement below */
SELECT 
    p.firstName, 
    p.lastName, 
    a.city, 
    a.state
FROM Person p WITH (NOLOCK)
LEFT JOIN Address a WITH (NOLOCK) ON p.personId = a.personId;