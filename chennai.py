import json
import pandas as pd
from tabulate import tabulate
from collections import defaultdict

teams_data = []
rank_data = []

with open('chennai_teams.json', encoding='utf-8') as f:
    data = json.load(f)
    teams_data.extend(data)
with open('ranklist.json', encoding='utf-8') as f:
    data = json.load(f)
    rank_data.extend(data)

chennai_teams_rank = []
clg_teams = []

for team in teams_data:
    team_name = team['name']
    team_institution = team['institution']
    for rank_entry in rank_data:
        if rank_entry['Team Name'].lower().strip() == team_name.lower().strip() and rank_entry['Institute'].lower().strip() == team_institution.lower().strip():
            chennai_team = {}
            chennai_team['rank'] = int(rank_entry['Rank'])
            chennai_team['name'] = team_name
            chennai_team['id'] = rank_entry['Usename']
            chennai_team['institution'] = team_institution
            chennai_team['score'] = int(rank_entry['Score'])
            chennai_team['Penalties'] = int(rank_entry['Penalties'])
            chennai_team['Total Time'] = rank_entry['Total Time']
            if team_institution == "Chennai Institute of Technology":
                clg_teams.append(chennai_team)
            chennai_teams_rank.append(chennai_team)
            break
chennai_teams_rank.sort(key=lambda x: x['rank'])
clg_teams.sort(key=lambda x: x['rank'])
rank = 1
i=0

diff_clgs = defaultdict(list)
for team in chennai_teams_rank:
    diff_clgs[team['institution']].append(team)
    if team['institution'] == "Chennai Institute of Technology" and team['name'] == clg_teams[i]['name']:
        clg_teams[i]['S.No'] = i+1
        clg_teams[i]['regional_rank'] = rank
        i+=1
    rank += 1

def filter_by_institution_chennai(number_of_teams=3):
    filtered_teams = []

    for teams in diff_clgs.values():
        teams.sort(key=lambda x: x['rank'])
        for i in range(number_of_teams):
            if i < len(teams):
                filtered_teams.append(teams[i])

    filtered_teams.sort(key=lambda x: x['rank'])
    for i in range(len(filtered_teams)):
        filtered_teams[i]['regional rank'] = i + 1

    df = pd.DataFrame(filtered_teams)
    df = df[['regional rank' ,'rank', 'name', 'institution', 'score']]
    df.columns = ['Regional Rank' , 'Overall Rank', 'Team Name', 'Institution', 'Score']
    colors = [''] * len(df)
    for i in range(len(df)):
        if df.iloc[i]['Institution'] == 'Chennai Institute of Technology':
            colors[i] = '\033[92m'
    df['Institution'] = [f"{color}{inst}\033[0m" if color else inst 
                        for color, inst in zip(colors, df['Institution'])]
    
    print(tabulate(df, headers=df.columns, tablefmt='pretty', showindex=False, numalign='left', stralign='left'))

def chennai_region_clg_teams():
    df = pd.DataFrame(clg_teams)
    df = df[['S.No', 'regional_rank', 'rank', 'name', 'id', 'score', 'Penalties', 'Total Time']]
    df.columns = ['S.No', 'Regional Rank', 'Overall Rank', 'Team Name', 'Team ID', 'Score', 'Penalties', 'Total Time']
    print("Total Teams Registered: {}".format(len(teams_data)))
    print("Total Teams Participated: {}".format(len(chennai_teams_rank)))
    print("Total Teams not participated: {}".format(len(teams_data)-len(chennai_teams_rank)))
    print("Teams from Chennai Institute of Technology: {}".format(len(clg_teams)))
    print(tabulate(df, headers=df.columns, tablefmt='pretty', showindex=False, numalign='left', stralign='left'))
    return df