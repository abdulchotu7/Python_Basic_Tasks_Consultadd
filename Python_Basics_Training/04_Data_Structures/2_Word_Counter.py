from collections import defaultdict
d=defaultdict(int)
text=input("Enter a text: ")
for word in text.split():
    d[word]+=1
print("Word count:")
for word,count in d.items():
    print(f"{word}: {count}")