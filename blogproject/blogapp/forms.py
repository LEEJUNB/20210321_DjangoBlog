# django form을 저장
# HTML form의 models.py 역할 : 클래스 객체 생성

from django import forms
from .models import Blog, Comment # modelform에서 Blog, Comment 객체를 사용함

# forms의 Form을 상속받는 BlogForm 클래스
class BlogForm(forms.Form) : 
    # forms.Form의 형식에 맞게 지정한 입력값들
    title = forms.CharField() # 문자열 형식
    body = forms.CharField(widget=forms.Textarea) # Textarea : 더 많은 문자 받음

class BlogModelForm(forms.ModelForm) :
    class Meta : 
        model = Blog # form의 기반은 Blog 클래스
        fields= '__all__' # 모든 필드타입
        #fields = ['title','body'] # 입력받을 필드타입 설정

# 댓글 입력 공간
# detail.html에 찍기
class CommentForm(forms.ModelForm) : 
    class Meta : 
        model = Comment
        fields = ['comment']