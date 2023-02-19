k = 2
string = "geegsforgeeeks"

for i in range(len(string) - 1):
    if string[i] and string[i + 1] == string[i]:
        string2 = string.replace(string[i], "")
        print(string2)
