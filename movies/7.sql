SELECT title FROM movies WHERE year = '2010';

SELECT rating FROM ratings WHERE movie_id LIKE (SELECT id FROM movies WHERE year = '2010');