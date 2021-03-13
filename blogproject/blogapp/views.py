# redirect : 함수 실행시 특정 html,url로 이동하도록함  
# get_object_or_404() : pk값(프라이머리키값)을 이용해 특정 모델 객체 하나만 갖고오거나 없다면 404 띄우기
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Blog # models.py의 Blog객체(HTML Form)는 .models를 상속받았음
from .forms import BlogForm # forms.py의 BlogForm객체(Django Form)는 .forms를 상속받았음
from .forms import BlogModelForm # forms.py의 BlogModelForm객체(Django Model Form)는 .forms를 상속받았음

def home(request) :
    # posts = Blog.objects.all() # 블로그 객체들을 모두 띄우는 코드
    posts = Blog.objects.filter().order_by('-date') # 필터를 통해 최신순으로 정렬가능
    return render(request, 'index.html', {'posts' : posts})

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

# models.py에 있는 Blog객체 기반으로 제작
def modelformcreate(request) : 
    # POST
    # 입력 내용 DB에 저장
    if request.method == 'POST' or request.method == 'FILES':
        form = BlogModelForm(request.POST, request.FILES)
        # 유효한 데이터 타입이라면
        if form.is_valid() : 
            form.save() # model객체.save()를 통해 모델 객체를 DB에 저장
            return redirect('home')
    # GET
    # 입력 내용 불러오기
    else : 
        form = BlogModelForm() # form를 form_create.html에 보내주기
    # 3번째 인자로 views.py내의 데이터를 html에 dict type으로 넘기기 가능
    return render(request, 'form_create.html', {'form':form} )

# 몇 번째(id) 블로그글인지를 인자로 받음
def detail(request, blog_id) : 
    # blog_id번째 블로그 글을 DB로 가지고와서 detail.html로 띄움
    # pk값이 blog_id인 Blog에 해당되는 객체 1개 가져올것
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    # blog_id 번째 블로그 글을 detail.html로 띄워주는 코드
    return render(request, 'detail.html', {'blog_detail':blog_detail})
    
