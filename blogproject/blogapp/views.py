from django.shortcuts import render, redirect # redirect : 함수 실행시 특정 html,url로 이동하도록함  
from .models import Blog
from django.utils import timezone

def home(request) :
    return render(request, 'index.html')

# 블로그 글 작성 html
def new(request) :
    return render(request, 'new.html')

# 블로그 글 저장 함수. 작성한 글이 DB에 반영
# new.html에서 버튼을 눌렀을 때 실행되는 함수
# 렌더링을 해서 특정 html을 보여주는 함수가 아님
def create(request) :
    if(request.method == "POST") :
        post = Blog() # post변수에 Blog객체생성
        
        # Blog 객체는 title, body, date로 이뤄짐
        post.title = request.POST['title'] # title에 해당되는 것을 post.title에 담음
        post.body = request.POST['body']
        post.date = timezone.now()
        
        post.save() # model객체.save()를 통해 모델 객체를 DB에 저장
    return redirect('home')