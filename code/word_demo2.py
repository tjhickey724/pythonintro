with open('code/RandJ.txt','r') as file:
    for i in range(50):
        line = file.readline()
        print(line[:-1])
