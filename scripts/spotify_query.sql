SELECT * FROM "Top10albums2010-2021";

SELECT * FROM "Top10albums2010-2021"
WHERE "Track_Popularity" >= 40
ORDER BY "Track_Popularity" DESC;

SELECT * FROM "Top10albums2010-2021"
WHERE "Track_Popularity" <= 40
ORDER BY "Track_Popularity" ASC;

SELECT * FROM "Top10albums2010-2021"
ORDER BY "Track_Popularity", "Release_Date" ASC;

SELECT COUNT("Song_Name"), "Album_Owner"
FROM "Top10albums2010-2021"
WHERE "Track_Popularity" <= 40
GROUP BY "Album_Owner";

SELECT ROUND(AVG("Track_Popularity"), 2), "Album_Owner"
FROM "Top10albums2010-2021"
GROUP BY "Album_Owner"
ORDER BY "round" DESC;

SELECT MAX("Track_Popularity"), "Album_Owner"
FROM "Top10albums2010-2021"
GROUP BY "Album_Owner"
ORDER BY "max" DESC;

SELECT MIN("Track_Popularity"), "Album_Owner"
FROM "Top10albums2010-2021"
GROUP BY "Album_Owner"
ORDER BY "min" DESC;

SELECT MAX("Album_Popularity"), "Album_Name", "Album_Owner"
FROM "Top10albums2010-2021"
GROUP BY "Album_Owner", "Album_Name"
ORDER BY "max" DESC
LIMIT 20;

SELECT MIN("Album_Popularity"), "Album_Name", "Album_Owner"
FROM "Top10albums2010-2021"
GROUP BY "Album_Owner", "Album_Name"
ORDER BY "min" ASC
LIMIT 20;

SELECT MAX("Track_Popularity"), "Song_Name", "Album_Owner"
FROM "Top10albums2010-2021"
GROUP BY "Song_Name", "Album_Owner"
ORDER BY "max" DESC
LIMIT 50;