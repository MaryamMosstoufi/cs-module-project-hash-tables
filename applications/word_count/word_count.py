def word_count(s):
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
    return dic


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
