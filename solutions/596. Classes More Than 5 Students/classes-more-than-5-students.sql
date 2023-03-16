SELECT class FROM Courses GROUP BY class HAVING COUNT(student) >= 5 ORDER BY class ASC;
