w = input("Enter your string: ")
def most_frequent(w):
    d = dict()
    for key in w:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    return d

d = most_frequent(w)
sorted_dict = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
for i in sorted_dict:
    print(i, ' = ', sorted_dict[i]) 
