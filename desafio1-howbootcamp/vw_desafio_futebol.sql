-- public.vw_desafio_futebol source
create or replace view public.desafio_fut as SELECT
	r.date as game_date,
	r.home_team as home_team,
	r.away_team as away_team,
	r.home_score as home_score,
	r.away_score as away_score,
	case when r.home_score > r.away_score then r.home_team else r.away_team end as match_winner,
	r.tournament as tournament,
	r.city as city,
	r.country as country,
	g.team as scorer_team,
	g.scorer as scorer,
	g.minute as minute,
	g.own_goal as own_goal,
	g.penalty as penalty
from
	results r
left join goalscorers g on
	r.date = g.date
	and r.home_team = g.home_team
	and r.away_team = g.away_team