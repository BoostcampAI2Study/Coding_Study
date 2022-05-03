#ref: https://loosie.tistory.com/188
from collections import defaultdict
def solution(sales, links):
    link_dict = defaultdict(list)
    for link in links:
        link_dict[link[0]].append(link[1])
    
    cost = [[0] * 2 for _ in range(len(sales) + 1)]
    def dfs(cur_id):
        temp_cost = 1e9
        cost[cur_id][1] = sales[cur_id - 1]
        if len(link_dict[cur_id]) == 0: return
        for next_id in link_dict[cur_id]:
            dfs(next_id)
            if cost[next_id][0] < cost[next_id][1]:
                cost[cur_id][0] += cost[next_id][0]
                cost[cur_id][1] += cost[next_id][0]
                temp_cost = min(temp_cost, cost[next_id][1] - cost[next_id][0])
            else:
                cost[cur_id][1] += cost[next_id][1]
                cost[cur_id][0] += cost[next_id][1]
                temp_cost = 0
        cost[cur_id][0] += temp_cost
    
    dfs(1)
    return min(cost[1])
