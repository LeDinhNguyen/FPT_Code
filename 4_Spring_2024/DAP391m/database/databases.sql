-- Cau 1

 SELECT  TOP(5) * FROM (SELECT FilmID  , (SUM(Rating)/ COUNT(Rating)) as [NewRating] FROM Rating
GROUP BY FilmID, Rating ) as temp LEFT JOIN Film f on temp.FilmID = f.FilmID
WHERE f.FilmID IS NOT NULL ORDER BY temp.NewRating DESC

-- Cau 2
select top 5 Name, count(FilmID) as NumberOfFilms
from Cast
group by CastID, Name, FilmID
order by NumberOfFilms desc

-- Cau 3
SELECT DISTINCT * FROM
(SELECT * FROM 
(SELECT top(1) KeywordID as TempID, COUNT(FilmID) as [NumberOfSearching] FROM Keyword GROUP BY KeywordID, Keyword) as temp
JOIN Keyword ON temp.TempID = Keyword.KeywordID) as temp2 JOIN Film on temp2.FilmID = Film.FilmID WHERE Film.FilmID IS NOT NULL

-- Cau 4
 SELECT  TOP(3) * FROM (SELECT FilmID  , COUNT(Rating) as [NumberOFRating] FROM Rating
GROUP BY FilmID, Rating ) as temp LEFT JOIN Film f on temp.FilmID = f.FilmID
WHERE f.FilmID IS NOT NULL ORDER BY temp.NumberOFRating DESC

-- Cau 5

SELECT TOP(5) temp.CountryName, SUM(temp.Revenue) as [TotalRevenue] FROM
(SELECT f.*, c.CountryCode, c.CountryName  FROM Film f JOIN dbo.country c on f.FilmID = c.FilmID) as temp
GROUP BY temp.CountryName ORDER BY TotalRevenue DESC

-- Cau 6

SELECT top(5) FilmID, SUM(Film.Revenue - Film.Budget) as [Profit] FROM Film
GROUP BY FilmID
ORDER BY SUM(Film.Revenue - Film.Budget) DESC 

-- Cau 7

SELECT TOP(1) temp.Hour, COUNT(Hour) as [CountHour] FROM
(SELECT DATEPART(HOUR, Rating.Timestamp) as [Hour] FROM Rating) as temp
GROUP BY Hour
ORDER BY COUNT(Hour) DESC

-- Cau 8

SELECT TOP(5) temp.FilmID, temp.CountCast + temp2.CountCrew as [ToTalStaffs] FROM 
(SELECT FilmID, COUNT(CastID) as [CountCast] FROM Cast GROUP BY FilmID) as temp JOIN 
(SELECT FilmID, COUNT(CrewID) as [CountCrew] FROM Crew GROUP BY FilmID) as temp2 on temp.FilmID = temp2.FilmID
ORDER BY ToTalStaffs DESC