-- script that lists all shows, and all genres linked to show from the database hbtn_0d_tvshows
SELECT A.title, C.name
FROM tv_shows A
LEFT JOIN tv_show_genres B
ON A.id = B.show_id
LEFT JOIN tv_genres C
ON B.genre_id = C.id
ORDER BY 1,2 ASC;
