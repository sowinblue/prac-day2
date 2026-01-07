# section B - 딕셔너리를 담은 리스트
# B-1 : 딕셔너리 하나를 리스트에 추가

members = []
person = {"name":"블루윈","age":25}
members.append(person)
print(members)

#* gitbrach 사용하여 문제 풀기
# B-2 : 딕셔너리 여러 개를 리스트로 구성 

members = [{"name":"블루윈"}, {"age":25}, {"address":"지구"}]
print(members)


# members=[]
# for i in range(3):
#     name = input("이름")
#     age = input("나이")

#     member = {
#         "name" : name,
#         "age" : age
#     }

#     members.append(member)

# print(members)


# B-3 : 리스트 내 첫 번째 딕셔너리 접근

first = members[0]  # 접근 =  읽기
print(first)    # 출력

# B-4 : 리스트 내 딕셔너리의 특정 키 값 접근
# 키에 접근해서 값 도출
first = members[0]["name"]
print(first)

# B-5 : for문으로 딕셔너리 리스트 전체 순회
for member in members:
    print(member)


# B-6 : 순회하며 특정 키 값만 출력


# for member in members:
#     if "name" in member:
#         print(member["name"])

members = [
    {"name": "윈블루", "age": 26},
    {"name": "윈그린", "age": 27},
    {"name": "윈퍼플", "age": 28}
]

for member in members:
    print(member["name"])


# B-6 : 순회하며 특정 조건 딕셔너리만 출력
# for member in members:
#     if "블루" in member["name"]:
#         print(member["age"])


for member in members:
    if member["age"] < 28:
        print(member["name"])