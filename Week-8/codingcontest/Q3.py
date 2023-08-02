a = ["laxman", "lakhs", "lamb"]
b = []
for i in a:
    b.append(i)
    break
print(b)
for i in b:
    for j in i:
        for k in a:
            for l in k:
                if j == l:
                    print(j, end="")
                    break
