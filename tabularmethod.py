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
    for i in range(arg):# (입력 개수는 이진수의 길이임)첫문자부터 끝문자까지 비교하며 다른 부분을 센다.
        if string1[i]!=string2[i]:
            index=i # 다른 부분의 index를 저장한다.
            count+=1
    if count==1: # 다른 부분이 딱 하나 있을 때만 True와 '_'을 포함한 string을 리턴.
        string=string[0:index]+'_'+string[index+1:]
        return True, string
    else: # 그렇지 않을 경우 False, 빈 문자열
        return False,""

def convert(binstr): #이진수 표현을 x1x2x3... 형식으로 정리
    string=''
    for i in range(len(binstr)): #자릿수가 0일 때는 '를 붙여주고 '_'일 때는 아예 문자를 출력하지 않는다.
        if binstr[i]=='0':
            string+='x'+str(i+1)+'\''
        elif binstr[i]=='1':
            string+='x'+str(i+1)
    return string


min_arr = [] #입력받을 minterm들을 저장
while True:
    arg = int(input("입력의 개수는? 3이상만 입력하세요."))
    if arg >=3:
        break
big_str ="" #현재 입력받은 입력의 개수에서 가장 큰 minterm의 숫자
for i in range(arg):
    big_str+="1"
big_min = int(big_str,2) #이진수에서 십진수로 변환해 저장

while True:
    minterm = int(input("몇 번 minterm이 1인지 입력하세요. (Don't care도 입력)\nm1이면 1을 입력하세요.\n 음수나 가장 큰 minterm 개수보다 큰 값을 넣으면 종료."))
    if minterm<0 or minterm>big_min: # 음수나 big_min 보다 큰 값일 때 입력 종료.
        break
    else:
        min_arr.append(minterm)

min_arr.sort() #오름차순으로 정렬
print(min_arr)

bin_arr=[] #min_arr의 원소들을 이진수로 변환
for i in range(len(min_arr)):
    strmin = bin(min_arr[i])
    binmin='0'*(arg-(len(strmin)-2))+strmin[2:len(strmin)]#이진수 출력의 '0b'형태를 제거하고 입력 수와 같은 길이의 string으로 만들어줌.
    bin_arr.append(binmin)
print(bin_arr)

dic={}#1의 개수는 key, bin_arr의 해당 요소는 value로 넣어준다.
for i in range(arg+1):
    dic.update({i:None})
    arr=[] #한 개의 key에 대해 value 값이 여러 개일 수 있음으로 {key:[요소1, 요소2, ..]}이런 식으로 value를 리스트 형태로 만들음.
    for j in range(len(bin_arr)):
        if count_1(bin_arr[j])==i:
            arr.append(bin_arr[j]) #bin_arr에 있는 요소들의 1의 개수를 셌을 때 i의 값이면 arr에 추가
    dic[i]=arr #bin_arr의 모든 요소 검사 후 key i의 value로서 추가.

print(dic)

#PI를 찾는 과정에서 서로 묶이지 않은 요소들 중 한 번도 묶이지 않은 요소만 추가해야하므로
#한번이라도 match된 것은 matches에 한번이라도 묶이지 않은 것은 nonmatches에 추가.
nonmatches=[]
matches=[]
pi_arr=[]#pi들을 저장.


while(True):
    count=0
    for i in range(arg):#i번째 key의 리스트 안 요소들과 i+1번째 key의 리스트 안 요소들을 similar함수를 통해 비교
        for j in range(len(dic[i])):
            for k in range(len(dic[i+1])):
                a,b = similar(dic[i][j],dic[i+1][k])#a는 boolean 값, b는 string
                if a==True:#한 끗 차이가 나서 묶였을 때
                    if not(b in pi_arr):#중복을 피하기 위함.
                        pi_arr.append(b) #pi_arr에 '_'가 들어간 string 추가
                    matches.extend([dic[i][j],dic[i+1][k]])#matches에 추가
                    count =1 #1번이라도 묶으면 count=1
                else:
                    nonmatches.extend([dic[i][j],dic[i+1][k]])#nonmatches에 추가

    for i in nonmatches: #nonmatches의 요소가 matches 안에 없을 때만 pi_arr에 추가
        if not (i in matches):
            pi_arr.append(i)

    if count == 0: #한 번도 묶이지 않았을 경우 여기서 while문 종료
        break

    dic = {}#dic을 비우고 pi_arr의 요소들을 같은 방식으로 다시 넣어줌
    for i in range(arg + 1):
        dic.update({i: None})
        arr = []
        for j in range(len(pi_arr)):
            if count_1(pi_arr[j]) == i:
                arr.append(pi_arr[j])
        dic[i] = arr

    pi_arr=[]#다음 반복을 위해 다 비워준다.
    nonmatches = []
    matches = []


print(pi_arr)

pi=[] #마지막으로 중복되는 것을 버리고 pi를 x1x2... 형태로 담을 리스트
for i in pi_arr:
    if i in pi_arr and not(i in pi):
        pi.append(i)

print(pi)
for i in range(len(pi)):
    pi[i] = convert(pi[i])

print(pi) # pi 도출

for i in range(len(pi)):
    print(i+1,"번째 pi는 ",pi[i],"\n")
