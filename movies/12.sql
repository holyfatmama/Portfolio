SELECT movie_id FROM stars WHERE person_id IN (SELECT id FROM people WHERE name = 'Bradley Cooper' OR name = 'Jennifer Lawrence');

SELECT id FROM people WHERE name = 'Bradley Cooper';
SELECT id FROM people WHERE name = 'Jennifer Lawrence';

movies that bradley starred in
SELECT * FROM stars WHERE person_id = (SELECT id FROM people WHERE name = 'Bradley Cooper');

movies that jlaw starred in
SELECT * FROM stars WHERE person_id = (SELECT id FROM people WHERE name = 'Jennifer Lawrence');

'
SELECT movie_id FROM stars JOIN people ON id = person_id WHERE name = 'Jennifer Lawrence' OR name = 'Bradley Cooper' GROUP BY movie_ID HAVING COUNT(movie_id) > 1;