# Your code here


def hist(file):
    with open(file) as f:
        s = f.read()
    # Your code here
    dic = {}
    excluded = '":;,.-+=/\\|[]{}()*^&'
    if s == '':
        return dic
    s = s.lower()
    s = s.replace('\r', ' ')
    s = s.replace('\n', ' ')
    s = s.replace('\t', ' ')
    words = s.split(' ')
    for word in words:
        for char in excluded:
            if char in word:
                word = word.replace(char, '')
        if word != '':
            if word in dic:
                dic[word] += 1
            else:
                dic[word] = 1
    dic = {k: v for k, v in sorted(
        dic.items(), key=lambda item: item[0])}
    dic = {k: v for k, v in sorted(
        dic.items(), key=lambda item: item[1], reverse=True)}
    for key in dic:
        l = len(key)
        space = (20 - l)*' '
        print(key, space, dic[key]*'#')


hist("./robin.txt")
