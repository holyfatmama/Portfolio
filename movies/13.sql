keving bacon id
SELECT id FROM people WHERE name = 'Kevin Bacon' AND birth = '1958';

klevin bacon movcies
SELECT * FROM stars WHERE person_id = (SELECT id FROM people WHERE name = 'Kevin Bacon' AND birth = '1958');

SELECT movie_id FROM stars WHERE person_id = (SELECT id FROM people WHERE name = 'Kevin Bacon' AND birth = '1958');

movies that have kevin bacon and other stars
SELECT person_id FROM stars WHERE movie_id IN (SELECT movie_id FROM stars WHERE person_id = (SELECT id FROM people WHERE name = 'Kevin Bacon' AND birth = '1958'));

