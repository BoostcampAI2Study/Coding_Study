import re
from collections import defaultdict

def solution(word, pages):
    base_score, link_score = [0] * len(pages), [0] * len(pages)
    page_url, external_url = [], defaultdict(list)
    word = word.lower()
    
    # head - content & body - a tag and sentence
    for idx, page in enumerate(pages):
        external_url_cnt = 0
        page_url.append(re.search(r"<meta property.+content=\"(https://.*)\"/>", page).group(1))
        
        for url in re.findall(r"<a href=\"(https://\S*)\">", page):
            external_url[url].append(idx)
            external_url_cnt += 1
        
        for contents in re.findall('[a-z]+', page.lower()):
            if contents == word:
                base_score[idx] += 1
        
        if external_url_cnt > 0 :
            link_score[idx] = base_score[idx] / external_url_cnt
    
    answer, max_score = -1, -1
    for idx in range(len(pages)):
        score = base_score[idx]
        for num in external_url[page_url[idx]]:
            score += link_score[num]
        
        if max_score < score:
            answer = idx
            max_score = score
    
    return answer
