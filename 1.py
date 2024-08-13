son = int(input("son --> "))
count = {}

for raqam in str(son):
    if raqam in count:
        count[raqam] += 1
    else:
        count[raqam] = 1

for raqam in sorted(count.keys()):
    print(f"{raqam}: {count[raqam]} ta")

