from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'ex_template/index.html')

def ex01(request):
    n1 = 100
    lst = [1,2,3]
    tup = (4,5,6)
    dic = {'a':1, 'b':2, 'c':3}
    
    context = {
        'n1' : n1,
        'lst' : lst,
        'tup' : tup,
        'dic' : dic,
    }
    # 값을 준비하고 한 곳으로 묶어 렌더를 통해서 템플릿 파일에 데이터를 이용할 수 있게 context를 통해 데이터를 담아 보낸다.
    return render(request, 'ex_template/ex01.html', context)


def ex02(request):
    val1 = 'hello<world><br>'
    lst = ['hO', 'Hi', 'weLCome']
    tup = (1,2,3)
    dic = {'aa':10, 'bb':20, 'cc':30,}
    bio = 'hi1 hi2 hi3 hi4 hi5 hi6 hi7 hi8 hi9 hi10'
    ls = [100]
    lss = [100,200]
    data = { 'val1' : val1, 'lst' : lst, 'tup' : tup,
              'dic' : dic , 'bio' : bio, 'ls' : ls, 'lss' : lss}
    return render(request, 'ex_template/ex02.html', data)

class Info:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Info[name={self.name}, age={self.age}]'

def ex03(request):
    name_list = ['홍길동', '이순신', '김동우' , '김초코']
    info_list = [
        Info('홍길동', 33),
        Info('이순신', 34),
        Info('김동우', 23),
        Info('김초코', 16),
    ]
    context = {
        'name_list': name_list,
        'info_list': info_list,
    }
    return render(request, 'ex_template/ex03.html', context)
    