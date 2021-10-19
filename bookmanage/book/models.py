from django.db import models

# Create your models here.
class BookInfo(models.Model):
    b_title = models.CharField(max_length=20,verbose_name='书名')
    pub_date = models.DateField(verbose_name='发行日期',null=True)
    readcount = models.IntegerField(verbose_name='阅读量',default=0)
    commentcount = models.IntegerField(verbose_name='评论量',default=0)
    is_delete = models.BooleanField(default=False,verbose_name='逻辑删除')

    class Meta:
        db_table = 'bookinfo'
        verbose_name = '图书'

    def __str__(self):
        return self.b_title

class People_Info(models.Model):
    GENDER_CHIOCE = ((0,'male'),(1,'female'))
    name = models.CharField(max_length=20,verbose_name='姓名')
    gender = models.SmallIntegerField(choices=GENDER_CHIOCE,default=0,verbose_name='性别')
    description = models.CharField(max_length=200,null=True,verbose_name='描述信息')
    book = models.ForeignKey(to=BookInfo,on_delete=models.CASCADE,verbose_name='图书')
    is_delete = models.BooleanField(verbose_name='逻辑删除',default=False)

    class Meta:
        db_table = 'people_info'
        verbose_name ='人物'
    def __str__(self):
        return self.name


