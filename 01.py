
#открываем файл, читаем его построчно 
with open('course-217-events.csv') as f:
      data = f.readlines() 

#отрезаем от каждой строки символ переноса строки 
for i in range(len(data)): 
      data[i] = data[i][:-1] 


#делим строку по запятым, получаем список вместо строки 
for i in range(len(data)): 
      data[i] = list(data[i].split(',')) 


#Превращаем все значения в целочисленные 

for i in range(len(data)): 
      for k in range (len(data)): 
            if k==0 or k==2 or k==3: 
                data[i][k] = int(data[i][k]) 


start_time = {} 

for el in data: 
      if el[0] not in start_time.keys(): 
              start_time[el[0]] = el[3] 
      else: 
          if el[3] < start_time[el[0]] : 
              start_time[el[0]] = el[3]
    


#открыли 2 файл      
with open('course-217-structure.csv') as g:
      mark = g.readlines()
for p in range(len(mark)): 
      mark[p] = mark[p][:-1]
for p in range(len(mark)): 
      mark[p] = list(mark[p].split(','))
for p in range(len(mark)): 
      for o in range (len(mark)): 
            if o==5 or o==8: 
                mark[p][o] = int(mark[p][o])

b=int()
bal = {}
for r in mark:
    bal[r[5]]=r[8]
    b+=1;




for i in range(len(data)):
    data[i].append(bal[data[i][2]])

dou = {}
for el in data:
    if el[0] in dou.keys():
        dou[el[0]] += [el]
    else:
        dou[el[0]] =[el]
for user in dou:
    dou[user].sort(key = lambda x: x[3])

for user in dou:
    sum = 0
    x = dou[user] ## list of lists
    sum = 0
    for i in range(len(x)):
        sum += x[i][4]
        if sum == 24:
            start_time[user] =[start_time[user], x[i][3]]
            break    

print('%80')
k =10
kon_time = []
for i in start_time:
      if type(start_time[i])== type([1,2]):
            kon_time.append([i,start_time[i][1] - start_time[i][0]])
kon_time.sort(key = lambda x: x[1])
for i in range(10):
      print (kon_time[i][1],end=", ")

