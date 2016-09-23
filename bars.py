import json
import math
with open('data.json', encoding="utf8") as data:
    data = json.load(data)  
seatList = {}
numb = []

my_x = 59.86967302 # Питер
my_y = 30.30796409 # СтудГородок

distList = {}
dist = []

for i in data:
    seatList[i.get('Cells').get('Name')] = i.get('Cells').get('SeatsCount')
    numb.append (i.get('Cells').get('SeatsCount'))
    x = i.get('Cells').get('geoData').get('coordinates')[0]
    y = i.get('Cells').get('geoData').get('coordinates')[1]
    distList[i.get('Cells').get('Name')] = math.sqrt(math.pow((x-my_x),2) + math.pow((y-my_y),2))
    dist.append( math.sqrt(math.pow((x-my_x),2) + math.pow((y-my_y),2)) )
    
numb.sort()
dist.sort()
minseats = ['Минимальное кол-во мест: '+str(min(numb))]
maxseats = ['Максимальное кол-во мест: '+str(max(numb))]
mindist = ['Ближайший бар: '+str(min(dist))]
maxdist = ['Самый далекий бар: '+str(max(dist))]

def search(lst,amount,mnlist,mxlist):
    for bar in lst.keys():
        if lst.get(bar) == min(amount):
            mnlist.append('\t\t'+bar)
        if lst.get(bar) == max(amount):
            mxlist.append('\t\t'+bar)
    for li in [mnlist,mxlist]:
        for itm in li:
            print (itm)
search(seatList,numb,minseats,maxseats)
search(distList,dist,mindist,maxdist)


