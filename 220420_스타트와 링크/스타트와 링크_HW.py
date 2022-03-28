import sys, itertools
N = int(input())
abilities = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
result = 1e9

def get_team_ability(team):
    ability = 0
    for player1 in team:
        for player2 in team:
            ability += abilities[player1][player2]
    return ability

for team1 in itertools.combinations(range(N), N//2):
    team2 = [i for i in range(N) if i not in team1]
    team1_ability, team2_ability = get_team_ability(team1), get_team_ability(team2)
    result = min(result, abs(team1_ability - team2_ability))
print(result)
