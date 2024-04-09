--find earthquakes that happened after January 20 with magnitude of 5 or greater
select * from earthquakes 
where extract(day from quakedate) > 20 
and extract(month from quakedate) = 1 
and mag >= 5;

-- find the top 10 strongest earthquakes that happened in Hawaii
select * from earthquakes 
where place like '%Hawaii%' 
order by mag desc 
fetch first 10 rows only;

-- find the average depth and magnitude of all earthquakes in the southern hemisphere
select avg(quakedepth) as Depth, avg(mag) as Magnitude from earthquakes
where latitude < 0;