import json
import pandas as pd
from tabulate import tabulate

rank_data = []
with open('ranklist.json', encoding='utf-8') as f:
    data = json.load(f)
    rank_data = data

total_teams = 28
team_regions = {"Chennai":["Entropy", "Kodex", "Code Red", "Supreme coders", "White Web Wizards", "Ballmer_PEAK", "Algorhythm", "NLogN", "AsyncThreads"], "Amirtapuri":["See++", "APX", "Cors Policy", "Return 1", "3D-X", "RandomCoders", "Ragnarok", "Codecubed", "Missing Semicolon"]}
print(f"Cit Teams:\nChennai : {len(team_regions['Chennai'])}\nAmirtapuri : {len(team_regions['Amirtapuri'])}\nKanpur : {total_teams - (len(team_regions['Chennai']) + len(team_regions['Amirtapuri']))}\n")
cit_teams = []
i=1
for team in rank_data:
    if team['Institute'] == "Chennai Institute of Technology":
        cit_team = {}
        cit_team['S.No'] = i
        i+=1
        cit_team['name'] = team['Team Name']
        cit_team['id'] = team['Usename']
        cit_team['rank'] = int(team['Rank'])
        cit_team['score'] = int(team['Score'])
        cit_team['Penalties'] = int(team['Penalties'])
        cit_team['Total Time'] = team['Total Time']
        if team['Team Name'] in team_regions['Chennai']:
            cit_team['region'] = 'Chennai'
        elif team['Team Name'] in team_regions['Amirtapuri']:
            cit_team['region'] = 'Amirtapuri'
        else:
            cit_team['region'] = 'Kanpur' 
        cit_teams.append(cit_team)

cit_teams.sort(key=lambda x: x['rank'])

def cit_clg_teams():
    df = pd.DataFrame(cit_teams)
    df = df[['S.No' ,'rank', 'name', 'id', 'region', 'score', 'Penalties', 'Total Time']]
    df.columns = ['S.No', 'Overall Rank', 'Team Name', 'Team ID', 'Region', 'Score', 'Penalties', 'Total Time']
    print(tabulate(df, headers=df.columns, tablefmt='pretty', showindex=False, numalign='left', stralign='left'))
    return df
