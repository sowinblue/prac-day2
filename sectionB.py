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


print(members)


# B-3 : 리스트 내 첫 번째 딕셔너리 접근

first = members[0]  # 접근 =  읽기
print(first)    # 출력