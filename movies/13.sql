keving bacon id
SELECT id FROM people WHERE name = 'Kevin Bacon' AND birth = '1958';

klevin bacon movcies
SELECT * FROM stars WHERE person_id = (SELECT id FROM people WHERE name = 'Kevin Bacon' AND birth = '1958');