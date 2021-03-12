# django form을 저장
# HTML form의 models.py 역할 : 클래스 객체 생성

from django import forms
# from .models import Blog

# forms의 Form을 상속받는 BlogForm 클래스
class BlogForm(forms.Form) : 
    # forms.Form의 형식에 맞게 지정한 입력값들
    title = forms.CharField() # 문자열 형식
    body = forms.CharField(widget=forms.Textarea) # Textarea : 더 많은 문자 받음