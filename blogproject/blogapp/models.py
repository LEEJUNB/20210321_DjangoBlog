from django.db import models

class Blog(models.Model) :
    title = models.CharField(max_length=200,default = '') # 문자열, 괄호안은 제약사항
    body = models.TextField() # 대용량 문자열
    photo = models.ImageField(blank=True, null=True, upload_to='blog_photo') # 지정된 media폴더 > blog_photo 폴더에 저장
    date = models.DateTimeField(auto_now_add=True)

    # title이 DB 목록에 표현
    def __str__(self) : 
        return self.title