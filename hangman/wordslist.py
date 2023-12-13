f = open("Oxford 5000.txt", 'r')
wordlist = f.readlines()

print(wordlist[0:2])
print(len(wordlist))
for x in range(len(wordlist)):
    wordlist[x] = wordlist[x].strip()
f.close()