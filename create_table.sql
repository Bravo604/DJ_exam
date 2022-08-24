CREATE TABLE payments
(
    Id SERIAL PRIMARY KEY,
    Course_id integer default 1,
	FOREIGN KEY (Course_id) REFERENCES user_course (Id) ON DELETE SET DEFAULT,
    Amount INTEGER,
    Pay_date Date
);

