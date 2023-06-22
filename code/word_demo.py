file = open('code/RandJ.txt','r')
text = file.read()
file.close()
print('the number of characters is',len(text))

lines = text.split('\n')
print('the number of lines is',len(lines))

print(text.count('love'))

for line in lines:
    if 'love' in line.split():
        print(line)
