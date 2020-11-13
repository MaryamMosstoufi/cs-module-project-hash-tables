def no_dups(s):
    # Your code here
    dic = {}
    words = s.split(' ')
    for word in words:
        if word not in dic:
            dic[word] = True
    string = ""
    for key in dic:
        string = string + ' ' + key
    string = string.replace(' ', '', 1)

    return (string)


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
