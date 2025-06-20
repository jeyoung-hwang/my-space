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

age = int(input("나이를 입력하세요: "))
if age >= 20 and age < 30:
    print("20대입니다")
else:
    print("20대가 아닙니다")

result = (age >= 18 and age <30)
print(result)

animal  = str(input("강아지, 고양이 중에 아무거나 입력하세요: "))
if animal == '강아지' or animal == '고양이':
    print("잘했어요!")
else:
    print("ㅉㅉ")

# Day 4
## 조건문 if, elif, else
age =20
if age >= 18:
    print("성인입니다")
else:
    print("미성년자입니다")

score = 99
if score >= 98:
    print ("A학점")
elif score >= 90:
    print("B학점")

age = 25
is_student = True
if age >= 20:
    if is_student:
     print("성인인 학생입니다")
else:
     print("성인이지만 학생은 아닙니다")

num = int(input("숫자 입력: "))
if num % 2 == 0:
    print("짝수입니다")
else:
    print("홀수입니다")

price = int(input("가격(원): "))
menu = input(str("메뉴 선택(양갈비/랍스터/비프스테이크): "))
if price >= 57000 or menu == "양갈비" or menu == "랍스터":
     print("프리미엄 메뉴입니다")
else:
     print("캐주얼 메뉴입니다")

# Day 5
## 반복문 (for/while)
fruits = ["사과", "바나나", "포도"] # for 변수 in 반복할 자료:
for fruit in fruits:
    print(fruit)

for ch in "Python":
    print(ch)

for i in range(5): # range(5) -> 0, 1, 2, 3, 4
    print(i)

i = 1
while i <= 5: # while 조건:
    print(i)
    i += 1

for i in range(1, 6): # 1부터 5까지
    if i == 3:
        continue # break: 반복문 즉시 종료 / continue: 이번 반복 건너뛰고 다음 반복으로
    print(i) # 출력: 1, 2, 3, 4

# Day 6
## 반복문 심화 (중첩 반복, 구구단)
for i in range(1, 4): # 바깥 반복 (3번)
    for j in range(1, 4): # 안쪽 반복 (3번)
        print(i, j)

for dan in range(2, 10):
    print(f"\n[{dan}단]")
    for i in range(1, 10):
        print(f"{dan} x {i} = {dan * i}")

