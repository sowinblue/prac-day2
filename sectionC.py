# section C - 조건문 기초 
# C-1 : if문 단독 사용
name = "윈블루"

if "윈" in name:
    print(name)


# C-2 : if-else 사용
age = int(input("나이를 입력하시오"))
if age < 50:
    print("50대 이하")

else: 
    print("50대 이상")


# C-3 : if-elif-else 사용
# if/ elif 둘 중 하나가 작동되면 끝남
age = int(input("나이"))
if age <20:
    print("10대")
elif age < 30 :
    print("20대")
else :
    print("30대 이상")


# C-4 : 숫자 비교 조건문

age = int(input("나이2"))
result = ""
if age > 26:
    result = "나보다 나이 많음"
elif age ==26:
    result = "나랑 동갑"
else:
    result = "나보다 어림"

print(result)

# C-5 : 문자열 비교 조건문
name = input("이름은 무엇?")

result = ""
if name == "윈블루":
    result = "너구나"
elif name == "윈그린":
    result = "넌아니야"
else:
    result = "누구세요"

print(result)

# C-6 : in 연산자로 포함 여부 확인
keyword=input("이름을 적으시오")
members = ["윈그린", "윈블루","윈퍼플"]
result = ""
if keyword in members:
    result = "존재한다."
else:
    result =  "존재하지 않는다." 

print(result)

# C-7 : and 조건 사용
name = "윈블루"
age = 26

if name == "윈블루" and not age ==26 :
    print("맞습니다")

# C-8 :  or 조건 사용
name = input('이름 뭐야')

for n in name:
    if "윈" in n or "루" in n:
        print("오서오세요")