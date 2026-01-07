# section D - Create, Read, Update 조합
# D-1 : 이름과 나이 입력받아 딕셔너리로 리스트에 추가
name = input("이름")
age = int(input("나이"))

person = []

for a in range(3):
    human = {
        "name": name,
        "age" : age
    }
    person.append(human)
print(person)

# D-2 : 전체 목록 순회하며 이름만 출력

person = []
for a in range(3):
    name = input("이름2")
    age = int(input("나이"))
    human = {
        "name": name,
        "age" : age
    }
    person.append(human)

for member in person:
    m_name = member["name"]
    print(m_name)


# D-3 : 특정 이름 검색하여 해당 딕셔너리 출력
members = [
    {"name": "윈블루", "age": 26},
    {"name": "윈핑크", "age": 27},
    {"name": "윈그린", "age": 28}
]

for i in members:
    if "블루" in i["name"]:
        print(i)


# D-4 : 특정 이름의 나이 수정
target_name = input()
new_age = int(input())

for m in members:
    if m["name"] == target_name:
        m["age"]= new_age

print(members) 


# D-5 : 인덱스로 접근하여 값 수정
