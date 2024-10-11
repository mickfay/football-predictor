import pandas as pd

def result_to_df(filepath, team_1, team_2):
    
    df = pd.read_csv(filepath)

    team_1_average_score = get_average_score(df, team_1, team_2)
    team_2_average_score = get_average_score(df, team_2, team_1)
    scores = {team_1: team_1_average_score, team_2: team_2_average_score}
    print(scores)
    print(scores[team_1])
    # if team_1_average_score = 
    scores = {team_1: round(team_1_average_score), team_2: round(team_2_average_score)}



    # print(homes)
    
    return scores



def get_average_score(df, team_1, team_2):

    homes = df[(df.home_team == team_1) & (df.away_team == team_2)]
    aways = df[(df.home_team == team_2) & (df.away_team == team_1)]

    home_scores = homes[["home_team", "home_score"]]
    away_scores = aways[["away_team", "away_score"]]

    home_scores.rename(columns={"home_team": "team", "home_score": "score"}, inplace=True)
    away_scores.rename(
        columns={"away_team": "team", "away_score": "score"}, inplace=True)

    totals = pd.concat([home_scores, away_scores])
    # print(totals)
    team_1_average_score = totals['score'].mean()
    return team_1_average_score
    pass