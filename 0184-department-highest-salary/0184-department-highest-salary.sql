SELECT Department, Employee, Salary
FROM 
(SELECT 
d.name AS Department, e.name AS Employee, e.salary AS Salary,
RANK() OVER (PARTITION BY e.departmentId ORDER BY e.salary DESC) AS salary_rank
FROM Employee e
JOIN Department d ON e.departmentId = d.id
) AS RankedData
WHERE salary_rank = 1;