import wikipedia as wiki

def search_list(keysearch):

    srch_list = wiki.search(keysearch)

    if (not(srch_list)):
        print("Invalid search element. Please try again.")
        return 0
    
    for i in range(0,len(srch_list)):
        print(str(i+1)+") "+srch_list[i])  

    return 1  

def search_wiki(keysearch,index):

    srch_list = wiki.search(keysearch)

    keyword = srch_list[int(index)]

    x = 0
    try:
        summary = wiki.summary(keyword)
    except wiki.exceptions.DisambiguationError as e:
        summary = ';'.join(e.options)
        x = 1
        
    return (summary, x)
