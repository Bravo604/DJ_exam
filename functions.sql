
CREATE OR REPLACE FUNCTION   get_course_id_by_email(student_email VARCHAR(34))
RETURNS INTEGER AS $body$
	SELECT id FROM user_course
	WHERE (SELECT * FROM user_student WHERE email = student_email)
;
$body$ LANGUAGE SQL

SELECT make_transaction('aman@mail.ru');