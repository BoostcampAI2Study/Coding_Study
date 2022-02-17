N = int(input())
max_A_cnts = [if_only_print_A_cnt for if_only_print_A_cnt in range(N+1)]
# copy&paste dp (bottom-up)
for cur_click_cnt in range(4, N+1): # click_cnt < 4, cannot copy&paste.
    paste_cnt = 1
    for click_cnt in range(3, cur_click_cnt): # 3 is the minimum necessary click count for copy&paste
        max_A_cnts[cur_click_cnt] = max(max_A_cnts[cur_click_cnt], max_A_cnts[cur_click_cnt-click_cnt]*(paste_cnt+1))
        paste_cnt += 1
                                        
print(max_A_cnts[-1])