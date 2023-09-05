list = [1, 3, 4]
string = []

for i in list: 
        for x in range (i):
            string.append("*")
        print(*string)
