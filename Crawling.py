import requests
from bs4 import BeautifulSoup
import datetime

def show_probable():
    probable = []
    today = str(datetime.date.today())

    data = requests.get("https://www.mlb.com/probable-pitchers/"+today)

    soup = BeautifulSoup(data.text,"html.parser")

    games = soup.find_all('div',class_=lambda x: x and 'probable-pitchers__matchup probable-pitchers__matchup' in x)

    probable.append("# "+today+" Game Schedule")
    probable.append("## "+str(len(games))+" Games")
    for game in games:
        match_information = "```"
        away_team = game.find('span',class_="probable-pitchers__team-name--away").text.strip()
        home_team = game.find('span',class_="probable-pitchers__team-name--home").text.strip()
        team_record = list(map(lambda s:s.text.strip(),game.find_all('div',class_="probable-pitchers__team-record")))
        pitchers = list(map(lambda s:s.text.strip(),game.find_all('div',class_="probable-pitchers__pitcher-name")))
        pitch_hands = list(map(lambda s:s.text.strip(),game.find_all('span',class_="probable-pitchers__pitcher-pitch-hand")))
        pitch_summary = list(map(lambda s:s.text.strip(),game.find_all('div',class_="probable-pitchers__pitcher-stats-summary")))
        i = 0
        if pitchers[0] == "TBD":
            match_information += "{:10}{:9}{:20}\n".format(away_team,team_record[0],pitchers[0])
        else:
            match_information += "{:10}{:9}{:20}{} {}\n".format(away_team,team_record[0],pitchers[0],pitch_hands[0],pitch_summary[0])
            i += 1
        match_information += "-"*70+"\n"
        if pitchers[1] == "TBD":
            match_information += "{:10}{:9}{:20}\n".format(home_team,team_record[1],pitchers[1])
        else:
            match_information += "{:10}{:9}{:20}{} {}\n".format(home_team,team_record[1],pitchers[1],pitch_hands[i],pitch_summary[i])
        match_information += '```'
        probable.append(match_information)

    return probable