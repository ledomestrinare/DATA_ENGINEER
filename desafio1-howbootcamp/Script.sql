SELECT * FROM goalscorers 

select * from results 

select * from shootouts

select
	city,
	country,
	tournament,
	count(country) as country_games
from
	results
group by
	1,
	2,
	3
order by
	country_games desc
--
-- analise por ano
	
select
	home_team,
	case
		when tournament = 'Friendly' then 0
		else 1
	end as tournament_type ,
	sum(case when home_score > away_score then 1.00 else 0 end)/ count(case when home_score > away_score then 1.00 else 0 end)* 100 as home_win_rate,
	count(*) as games_played
from
	results
where
	neutral = false
group by
	1,2
having
	count(*) > 10
order by
	3 desc

select
	left(date, 4),
	case
		when tournament = 'Friendly' then 0
		else 1
	end as tournament_type,
	sum(case when home_score > away_score then 1.00 else 0 end)/ count(case when home_score > away_score then 1.00 else 0 end)* 100 as home_win_rate,
	count(*) as games_played
from
	results
group by
	1,2
having
	count(*) > 10
order by
	3 desc