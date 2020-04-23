def remove_escape(d):
    d = d.split('\\')
    d = ' '.join(d)
    return d

def remove_url(d):
    d = d.split()
    i = 0
    while i < len(d):
        if 'https://' in d[i]:
            d.remove(d[i])
            i -= 1
        elif 'http://' in d[i]:
            d.remove(d[i])
            i -= 1
        i += 1

    d = ' '.join(d)
    return d

def remove_punctuation(d):
    d = d.split()
    i = 0
    while i < len(d):
        if len(d) > 0:
            if d[i][0] == 'x' and len(d[i]) == 3:
                d.remove(d[i])
                i -= 1
        if len(d) > 0:
            if len(d[i]) == 1:
                d.remove(d[i])
                i -= 1
        if len(d) > 0:
            if 'rt' in d[i]:
                d.remove(d[i])
                i -= 1
        if len(d) > 0:
            if d[i][0] == '@' or d[i][0] == '#':
                d.remove(d[i])
                i -= 1
        i += 1
    d = ' '.join(d)
    return d

def preprocessing(sent):
    sent_lower = sent.lower()
    sent_escape = remove_escape(sent_lower)
    sent_url = remove_url(sent_escape)
    sent_punctuation = remove_punctuation(sent_url)
    return sent_punctuation