SELECT movie_id FROM stars WHERE person_id IN (SELECT id FROM people WHERE name = 'Bradley Cooper' OR name = 'Jennifer Lawrence');

SELECT id FROM people WHERE name = 'Bradley Cooper';
SELECT id FROM people WHERE name = 'Jennifer Lawrence';