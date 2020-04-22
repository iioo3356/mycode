def count_1(string): # 1 개수 세기 #20191581 김하연
    count=0
    for i in range(len(string)):
        if string[i]=="1":
            count+=1
    return count

def similar(string1,string2): #1 차이가 나는지 안 나는지, 차이가 나면 _포함한 문자열 함께 리턴
    count=0
    index=-1
    string=string1
    for i in range(arg):
        if string1[i]!=string2[i]:
            index=i
            count+=1
    if count==1:
        string=string[0:index]+'_'+string[index+1:]
        return True, string
    else:
        return False,""

def convert(binstr): #bin 들을 예쁘게 정리
    string=''
    for i in range(len(binstr)):
        if binstr[i]=='0':
            string+='x'+str(i+1)+'\''
        elif binstr[i]=='1':
            string+='x'+str(i+1)
    return string


min_arr = []
while True:
    arg = int(input("입력의 개수는? 3이상만 입력하세요."))
    if arg >=3:
        break
big_str =""
for i in range(arg):
    big_str+="1"
big_min = int(big_str,2)

while True:
    minterm = int(input("몇 번 minterm이 1인지 입력하세요. m1이면 1을 입력하세요.\n 음수나 가장 큰 minterm 개수보다 큰 값을 넣으면 종료."))
    if minterm<0 or minterm>big_min:
        break
    else:
        min_arr.append(minterm)

min_arr.sort()
print(min_arr)
bin_arr=[]
for i in range(len(min_arr)):
    strmin = bin(min_arr[i])
    binmin='0'*(arg-(len(strmin)-2))+strmin[2:len(strmin)]
    bin_arr.append(binmin)
print(bin_arr)

dic={}
for i in range(arg+1):
    dic.update({i:None})
    arr=[]
    for j in range(len(bin_arr)):
        if count_1(bin_arr[j])==i:
            arr.append(bin_arr[j])
    dic[i]=arr

print(dic)
nonmatches=[]
matches=[]
pi_arr=[]


while(True):
    count=0
    for i in range(arg):
        for j in range(len(dic[i])):
            for k in range(len(dic[i+1])):
                a,b = similar(dic[i][j],dic[i+1][k])
                if a==True:
                    if not(b in pi_arr):
                        pi_arr.append(b)
                    matches.extend([dic[i][j],dic[i+1][k]])
                    count =1
                else:
                    nonmatches.extend([dic[i][j],dic[i+1][k]])

    for i in nonmatches:
        if not (i in matches):
            pi_arr.append(i)

    if count == 0:
        break

    dic = {}
    for i in range(arg + 1):
        dic.update({i: None})
        arr = []
        for j in range(len(pi_arr)):
            if count_1(pi_arr[j]) == i:
                arr.append(pi_arr[j])
        dic[i] = arr

    pi_arr=[]
    nonmatches = []
    matches = []


print(pi_arr)

pi=[]
for i in pi_arr:
    if i in pi_arr and not(i in pi):
        pi.append(i)

print(pi)
for i in range(len(pi)):
    pi[i] = convert(pi[i])

print(pi) # pi 도출
