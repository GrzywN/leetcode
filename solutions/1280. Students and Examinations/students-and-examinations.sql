SELECT
  Students.student_id,
  student_name,
  Subjects.subject_name,
  COUNT(Examinations.subject_name) AS attended_exams
FROM
  Students
  JOIN Subjects
  LEFT JOIN Examinations ON Students.student_id = Examinations.student_id
  AND Examinations.subject_name = Subjects.subject_name
GROUP BY
  Students.student_id,
  subject_name
ORDER BY
  student_id,
  subject_name;
