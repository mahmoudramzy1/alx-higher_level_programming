-- join.
SELECT cities.id, cities.name, states.name FROM cities
JOIN STATES ON cities.states_id=states.id
ORDER BY cities.id;
