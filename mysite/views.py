#from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import render

def index(request):
    now = timezone.now()
    context = {
        'now' : now,
        'name' : '홍길동',
    }
    return render(request, 'index.html') # 따로 경로를 지정하지 않고 템플릿 이름을 적으면 settings에 있는 'DIRS': [template_dir] 을 통해 templates 폴더에서 파일을 찾는다