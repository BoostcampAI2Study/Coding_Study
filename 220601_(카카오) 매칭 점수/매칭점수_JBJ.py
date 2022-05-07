import re, collections

def solution(word, pages):
    ext_links_dict = collections.defaultdict(list)
    pages_info = collections.OrderedDict()
    max_matching_score_idx, max_matching_score = -1, -1
    
    for page_idx, page in enumerate(pages):
        page = re.sub(r'[\s]', ' ', page)
        url = re.search('<meta property="og:url" content="(\S+)"', page).group(1)
        
        # get the external link score.
        ext_links_dict[url].extend([ext_link for ext_link in re.findall('<a href="(https://[\S]*)"', page)])
        ext_link_score = len(ext_links_dict[url])
        # get the basic score.
        basic_score = 0
        for f in re.findall(r'[a-zA-Z]+', page.lower()):
            if f == word.lower():
                basic_score += 1
        
        pages_info[url] = (page_idx, basic_score, ext_link_score)
    
    for page_url, (page_idx, basic_score, ext_link_score) in pages_info.items():
        # get the link score.
        link_score = 0
        for link_url, ext_links in ext_links_dict.items():
            if page_url in ext_links and link_url in pages_info:
                ext_link_basic_score, ext_link_ext_link_score = pages_info[link_url][1], pages_info[link_url][2]
                link_score += (ext_link_basic_score / ext_link_ext_link_score)
        # get the matching score.
        matching_score = basic_score + link_score
        if matching_score > max_matching_score:
            max_matching_score, max_matching_score_idx = matching_score, page_idx
            
    return max_matching_score_idx