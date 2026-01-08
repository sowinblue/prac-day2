# # section D - Create, Read, Update 조합
# # D-1 : 이름과 나이 입력받아 딕셔너리로 리스트에 추가
# name = input("이름")
# age = int(input("나이"))

# person = []

# for a in range(3):
#     human = {
#         "name": name,
#         "age" : age
#     }
#     person.append(human)
# print(person)

# # D-2 : 전체 목록 순회하며 이름만 출력

# person = []
# for a in range(3):
#     name = input("이름2")
#     age = int(input("나이"))
#     human = {
#         "name": name,
#         "age" : age
#     }
#     person.append(human)

# for member in person:
#     m_name = member["name"]
#     print(m_name)


# # D-3 : 특정 이름 검색하여 해당 딕셔너리 출력
# members = [
#     {"name": "윈블루", "age": 26},
#     {"name": "윈핑크", "age": 27},
#     {"name": "윈그린", "age": 28}
# ]

# for i in members:
#     if "블루" in i["name"]:
#         print(i)


# # D-4 : 특정 이름의 나이 수정
# target_name = input()
# new_age = int(input())

# for m in members:
#     if m["name"] == target_name:
#         m["age"]= new_age

# print(members) 


# # D-5 : 인덱스로 접근하여 값 수정
# # 닉네임 교체
# idx = int(input("숫자를 입력하시오"))
# new_nikname = input("닉네임을 적으시오")

# members[idx]["name"] = new_nikname

# print(members)

# # D-6 : 조건에 맞는 항목만 필터링하여 출력
# # 리스트 값 중에서 필터링 -> 다시 담아서 리스트 출력
# min_age = int(input())

# filter_age = []

# for i in members:
#     if i["age"] >= min_age:
#         filter_age.append(i)

# print(filter_age)

# # D-7 : 메뉴얼 선택에 따라 다른 동작 수행(if-elif-else)
# members = [
#     {"name": "윈블루", "age": 26},
#     {"name": "윈핑크", "age": 27},
#     {"name": "윈그린", "age": 28}
# ]

# menual = input("1,2,3")
# if menual == "1":
#     print(members)
# elif menual == "2":
#     print(len(members))
# else:
#     print("결정을 취소함")


# D-8 : 반복 입력과 조회를 while로 구성
members=[]

while True:
    cmd = input()
    if cmd == "q":
        break
    name = input("이름을 입력하시오: ")
    age=int(input("나이를 입력하시오: "))
    members.append({"name": name, "age": age})

print(members)