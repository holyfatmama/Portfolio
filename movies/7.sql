SELECT title FROM movies WHERE year = '2010';

SELECT rating FROM ratings WHERE movie_id = (SELECT id FROM movies WHERE year = '2010');