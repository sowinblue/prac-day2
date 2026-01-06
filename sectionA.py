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