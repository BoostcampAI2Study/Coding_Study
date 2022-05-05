import collections

def solution(sales, links):
    dp = [[0]*2 for _ in range(len(sales))] # 0: not attend case, 1: attend case
    teams = collections.defaultdict(list)
    for a, b in links:
        teams[a-1].append(b-1)
        
    def dfs(team_leader):
        nonlocal dp, teams, sales
        
        if team_leader not in teams: # not a team leader (leaf node)
            dp[team_leader][0], dp[team_leader][1] = 0, sales[team_leader]
        else:
            teammates_total_sales, teammate_attend_flag, min_difference = 0, False, 1e5
            for teammate in teams[team_leader]:
                dfs(teammate)
                if dp[teammate][0] > dp[teammate][1]: # teammate can represent the team (attendee).
                    teammate_attend_flag = True
                    teammates_total_sales += dp[teammate][1]
                else:
                    min_difference = min(min_difference, dp[teammate][1] - dp[teammate][0])
                    teammates_total_sales += dp[teammate][0]
            
            dp[team_leader][0] = teammates_total_sales if teammate_attend_flag else teammates_total_sales + min_difference 
            dp[team_leader][1] = sales[team_leader] + teammates_total_sales
    
    dfs(0)
    return min(dp[0][0], dp[0][1])