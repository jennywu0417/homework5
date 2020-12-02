a = int(input('請輸入班級人數:'))
name = []
num = []
for i in range(a):
    stu = input('請輸入姓名:')
    name.append(stu)
    e = int(input('請輸入分數:'))
    num.append(e)
    
d = 0

for i in range(a):
    d = d + num[i]
#print('sum: ',d)
avg = d/a
print('平均分:',avg)

biggest = 0
indexbig = 0
for i in range(a):
    if num[i] > biggest:
        biggest = num[i]
        indexbig  = i
print(name[indexbig],'最高分: ', biggest)

small = 100
indexsmall = 0
for i in range(a):
    if num[i] < small:
        small = num[i]
        indesxmall = i
print(name[indexsmall],'最低分:', small)

