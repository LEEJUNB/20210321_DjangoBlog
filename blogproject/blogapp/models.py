from django.db import models

class Blog(models.Model) :
    title = models.CharField(max_length=200,default = '') # 문자열, 괄호안은 제약사항
    body = models.TextField() # 대용량 문자열
    photo = models.ImageField(blank=True, null=True, upload_to='blog_photo') # 지정된 media폴더 > blog_photo 폴더에 저장
    date = models.DateTimeField(auto_now_add=True)

    # title이 DB 목록에 표현
    def __str__(self) : 
        return self.title

# Blog 객체에 종속적인 comment 객체
class Comment(models.Model) :
    comment = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    
    # 게시글에 댓글이 달리게 만드는 post 변수
    # 게시글 작성 역할인 Blog 객체에 종속. 
    # post 변수는 Blog 객체를 참조하는 칼럼 (참조키,ForeignKey)
    # 게시글(Blog 객체) 삭제시 댓글(comment 객체)도 삭제
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)

    # 댓글작성시 object(num)이 아닌 작성한 댓글 자체가 나타나도록
    def __str__(self) : 
        return self.comment