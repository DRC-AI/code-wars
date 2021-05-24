def duplicate_count(tex: 
    d = [ l for l in list(dict.fromkeys(list(text.lower()))) if text.lower().count(l) >= 2]
    return len(d)


print(duplicate_count('abcdeaB'))
