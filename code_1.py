
numberOfSongs = input()                  # Reading input from STDIN
#print('Hi, %s.' % name)         # Writing output to STDOUT
singers=[]
y=int(numberOfSongs)
for x in range(y):
    try:
        playlist = input()
        singers.append(playlist)
    except EOFError  as e:
        pass
    
#print(singers)

thisset=set(singers)
thislist=list(thisset)
#print(thisset)
thislist.sort()
previousCount=0
favsing=[]
for t in thislist:
    currentCount=0
    for s in singers:
          if t==s:
               currentCount=currentCount+1
    if previousCount<=currentCount:
          previousCount=currentCount
          favsing.append(t)

print(len(favsing))