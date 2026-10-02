from nba_api.stats.endpoints import leaguegamefinder

def fetch_season(season="2023-24"):
    finder = leaguegamefinder.LeagueGameFinder(
        season_nullable=season,
        league_id_nullable="00",
        season_type_nullable="Regular Season",
        timeout=60,
    )
    return finder.get_data_frames()[0]

if __name__ == "__main__":
    df = fetch_season()
    df.to_csv("data/raw/games_2023_24.csv", index=False)
    print(df.shape)
    print(df.head())