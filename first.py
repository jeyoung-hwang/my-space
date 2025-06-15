print ("Welocme to black parade")
print ("Github에 올라간 파일을 변경하면 line 옆에 초록줄이 생겨요")
print ("그리고 파일 이름 자체도 노락색으로 바뀝니다")

# 숫자 자료형
100

# Day 1
## input(), print()
name = input("young")
print(f"{name}님, 파이썬에 오신 것을 환영합니다")

name = input("young")
age = input(21)
print(f"{name}님은 {age}살입니다")


# Day 2
## 변수와 자료형
name = "young"
age = 21
is_student = True

print("이름", name)

print(type(name))

print(type(10)) # int 정수: 나이, 수량
print(type(3.14)) # float 실수: 소수점 있는 숫자
print(type("hello")) # str 문자열: 글자 데이터
print(type(True)) # bool 불리언: 참/거짓

# Day 3
## 연산자 (산술, 문자열, 비교, 논리)
a = 3
b = 5
print(a + b)

first = "케이크"
second = "사와"
print(first + " " + "맛있는 거" + " " + second + "!")

age = 20
is_adult = age >= 18
print("성인인가요?", is_adult)
print(age >= 18 and age < 65)
