def solution(n, info):
    max_diff_lion_arrows, max_difference = [-1], -1
    
    def dfs(arrows_cnt, idx, lion_arrows):
        nonlocal max_diff_lion_arrows, max_difference, info, n
        
        # shot n arrows.
        if arrows_cnt == n:
            # calculate apeach and lion scores.
            apeach_score, lion_score = 0, 0
            for score, (a_cnt, l_cnt) in enumerate(zip(info, lion_arrows)):
                if l_cnt > a_cnt:
                    lion_score += (10-score)
                elif a_cnt != 0 and a_cnt >= l_cnt:
                    apeach_score += (10-score)
            
            # compare and get max difference.
            difference = (lion_score - apeach_score)
            if difference > 0 and difference >= max_difference:
                if difference == max_difference:
                    for idx in range(10,-1,-1):
                        if lion_arrows[idx] > max_diff_lion_arrows[idx]: break
                        elif lion_arrows[idx] < max_diff_lion_arrows[idx]: return
                max_difference, max_diff_lion_arrows = difference, lion_arrows[:]
                return
        
        # The end of a list.
        if idx == len(info): return
        
        # lion gets score.
        new_arrows_cnt = n-arrows_cnt if arrows_cnt+(info[idx]+1) > n else info[idx]+1
        if (arrows_cnt + new_arrows_cnt) <= n:
            lion_arrows[idx] = new_arrows_cnt
            dfs((arrows_cnt + new_arrows_cnt), idx+1, lion_arrows[:])
        # apeach or nobody gets score.
        lion_arrows[idx] = 0
        dfs(arrows_cnt, idx+1, lion_arrows[:])
        
    dfs(0, 0, [0 for _ in range(11)])
    
    return max_diff_lion_arrows