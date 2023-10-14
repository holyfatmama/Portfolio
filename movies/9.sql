movies, 2004
people, names
stars

SELECT name FROM people WHERE id IN (SELECT person_id FROM stars WHERE movie_id IN (SELECT movie_id FROM movies WHERE year = '2004'));