from src.result_to_df import result_to_df
import pandas as pd
import json

def test_returns_dict_of_avg_scores():
    result = result_to_df('data/results.csv', 'Germany', 'Switzerland')
    # print(result)
    # print(result_to_df('data/results.csv', 'Germany', 'Scotland'))
    # print(result_to_df('data/results.csv', 'Hungary', 'Switzerland'))
    # print(result_to_df('data/results.csv', 'Spain', 'Croatia'))
    # print(result_to_df('data/results.csv', 'Italy', 'Albania'))
    # print(result_to_df('data/results.csv', 'Poland', 'Netherlands'))
    # print(result_to_df('data/results.csv', 'Slovenia', 'Denmark'))
    # print(result_to_df('data/results.csv', 'Serbia', 'England'))
    # print(result_to_df('data/results.csv', 'Romania', 'Ukraine'))
    # print(result_to_df('data/results.csv', 'Belgium', 'Slovakia'))
    # print(result_to_df('data/results.csv', 'Austria', 'France'))
    # print(result_to_df('data/results.csv', 'Turkey', 'Georgia'))
    # print(result_to_df('data/results.csv', 'Portugal', 'Czech Republic'))
    games = []
    with open('semis.csv', 'r') as f:
        for l in f:
            teams = l.strip().split(',')
            games.append(teams)
        
    print(games)
    with open('semis.jsonl', 'a') as f:
        for game in games:
            print(game)
            json.dump(result_to_df('data/results.csv', game[0], game[1]), f)
            f.write('\n')

    assert isinstance(result, dict)
    assert result == {'': 4.5, 'Tunisia': 1.0}

    pass
