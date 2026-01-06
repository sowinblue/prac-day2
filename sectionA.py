#section A - 빈 딕셔너리 선언
# A-1 : 빈 딕셔너리  선언
person = {}
print(person)


# A-2 : 키-값 쌍이 있는 딕셔너리 선언
person = {"name":"블루윈","age":25}
print(person)


# A-3: 딕셔너리에서 특정 키로 값 접근
# 딕셔너리는 키 하나당 값 하나 -> 값이 리스트(또는 다른 컨테이너)이면 여러 내용을 담을 수 있다.
person2 = person["name"]
print(person2)


# A-4 : 딕셔너리에 새 키-값 추가
person["favorite"] = "음악 듣기"
print(person)


# A-5 : 딕셔너리 특정 키의 값 수정
person["age"]= 26
print(person)


# A-6 : 딕셔너리 키 존재 여부 확인
# 불리언 값을 반환하는 표현식으로 제어문이 아니더라도 True/False 표시
result = "name" in person
print(result)

# A-7 : 딕셔너리 키-값 삭제
del person["favorite"]
print(person)


# A-8 : 딕셔너리 전체 키 목록 확인
# .keys 메서드를 이용해서 person 딕셔너리의 키 값을 추출
# 키 목록을 list로 변환해 목록 확인
keys = list(person.keys())
print(keys)

values = list(person.values())
print(values)

items = list(person.items())
print(items)
# [('name', '블루윈'), ('age', 26)]  리스트 안에 튜플 형태로 출력