from django.shortcuts import render, redirect # redirect : 함수 실행시 특정 html,url로 이동하도록함  
from django.utils import timezone
from .models import Blog # models.py의 Blog객체(HTML Form)는 .models를 상속받았음
from .forms import BlogForm # forms.py의 BlogForm객체(Django Form)는 .forms를 상속받았음

def home(request) :
    return render(request, 'index.html')

# 블로그 글 작성 html
def new(request) :
    return render(request, 'new.html')

# HTML Form
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

# django Form
# 장고는 하나의 URL에서 GET, POST 요청 모두를 처리하는 함수 가능
def djangocreate(request) :
    # POST
    # 입력 내용 DB에 저장
    if request.method == 'POST':
        form = BlogForm(request.POST)
        # 유효한 데이터 타입이라면
        if form.is_valid() : 
            post = Blog()
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.save() # model객체.save()를 통해 모델 객체를 DB에 저장
            return redirect('home')
    # GET
    # 입력 내용 불러오기
    else : 
        form = BlogForm() # form를 form_create.html에 보내주기
    # 3번째 인자로 views.py내의 데이터를 html에 dict type으로 넘기기 가능
    return render(request, 'form_create.html', {'form':form} ) 

    