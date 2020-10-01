# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.
with open("ciphertext.txt") as f:
    encoded = f.read()
# Your code here
freq = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
        'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']
dic = {}
for i in encoded:
    if i in freq:
        if i in dic:
            val = dic[i]+1
            dic[i] = val
        else:
            dic[i] = 1

dic = {k: v for k, v in sorted(
    dic.items(), key=lambda item: item[1], reverse=True)}
# print(dic)
index = 0
for key in dic:
    dic[key] = freq[index]
    index += 1
# print(dic)
decoded = ""
for i in range(0, len(encoded)):
    if encoded[i] in freq:
        decoded += dic[encoded[i]]
    else:
        decoded += encoded[i]
print(decoded)
