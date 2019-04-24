from operator import itemgetter
from constants import TEAMS, PLAYERS

def cleaned_experience(answer):
    if answer == 'YES':
        return True
    return False

def cleaned_height(heights):
    heights = heights.replace(' inches',' ')
    return heights

def cleaned_code():
    clean_code_list = []
    for player in PLAYERS:
        name = player.get('name')
        guardians = player.get('guardians')
        answer = player.get('experience')
        experience = cleaned_experience(answer)
        heights = player.get('height')
        height = cleaned_height(heights)
        clean_code_list.append({'name': name, 'guardians': guardians, 'experience': experience, 'height': height})
    return clean_code_list

def list_players_on_team():
    teams_roster = {team: [] for team in TEAMS}
    return teams_roster

def sort_players():
    sorted_players = sorted(clean_code_list, key=itemgetter('experience'), reverse=True)
    return sorted_players

def balanced_teams(teams_roster, sorted_players):
    for index, player in enumerate(sorted_players):
        teams_roster[TEAMS[index % len(TEAMS)]].append(player.get('name'))
    return teams_roster

def app(teams_roster):
    print('''
    BASKETBALL TEAM STATS TOOL

        ----- Menu -----''')
    print('''
    Here's your choices:
    1) Display Team Stats
    2) Quit ''')

    team_names = int(input('\nEnter an option (1 or 2):  '))

    if team_names == 1:
        print("")
        for count, team in enumerate(TEAMS, start = 1):
            print(str(count) + ')', team)
        print("")

    elif team_names == 2:
        print("")
        print('Closing app, thanks for stopping by! ')
        exit()

    else:
        print("that's not a valid option")
        exit()

    pick_team = int(input('Enter an option:  '))

    if pick_team == 1:
        print('''
Team: Panthers Stats
-----------------------------''')
        print('Total Players: {}'.format(len(teams_roster['Panthers'])))
        print("")
        print('Players: {}'.format(teams_roster['Panthers']))

    elif pick_team == 2:
        print('''
Team: Bandits Stats
-----------------------------''')
        print('Total Players: {}'.format(len(teams_roster['Bandits'])))
        print("")
        print('Players: {}'.format(teams_roster['Bandits']))

    elif pick_team == 3:
        print('''
Team: Warriors Stats
-----------------------------''')
        print('Total Players: {}'.format(len(teams_roster['Warriors'])))
        print("")
        print('Players: {}'.format(teams_roster['Warriors']))

    else:
        print("That is not a valid option")
        exit()

if __name__ == "__main__":
    clean_code_list = cleaned_code()
    sorted_players = sort_players()
    teams_roster = list_players_on_team()
    teams_roster = balanced_teams(teams_roster, sorted_players)
    app(teams_roster)
