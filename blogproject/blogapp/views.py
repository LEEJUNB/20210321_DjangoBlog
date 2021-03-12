from django.shortcuts import render

def home(request) :
    return render(request, 'index.html')

# 블로그 글 작성 html
def new(request) :
    return render(request, 'new.html')

# 블로그 글 저장 함수
def create(request) :
    return render(request, 'create.html')