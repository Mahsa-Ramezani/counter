name=input("Enter file:")
handle=open(name)
counts=dict()
names=list()
for line in handle:
    line=line.rstrip()
    if line.startswith('From:'):
        words=line.split()
        email=words[1]
        names.append(email)
for name in names:
    if name not in counts:
        counts[name]=1
    else:
        counts[name]=counts[name]+1
bigcount=None
bigword=None
for word,count in counts.items():
     if bigcount is None or count>bigcount:
        bigword=word
        bigcount=count
print(bigword,bigcount)
