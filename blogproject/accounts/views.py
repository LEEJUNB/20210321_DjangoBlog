from django.shortcuts import render

def login(request) : 
    # POST 요청이 들어오면 로그인 처리함
    if request.method == 'POST' : 
        pass
    # GET 요청이 들어오면 login form을 담고있는 login.html을 띄워주는 역할을 함
    else : 
        return render(request, 'login.html')


