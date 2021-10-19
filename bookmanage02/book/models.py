from django.db import models


# Create your models here.
class BookInfo(models.Model):
    class Meta:
        db_table = 'bookinfo'
        verbose_name = '图书'

    name = models.CharField(max_length=20, verbose_name='书名')
    pub_date = models.DateField(verbose_name='发行日期')
    readcount = models.IntegerField(verbose_name='阅读量', default=0)
    commentcount = models.IntegerField(verbose_name='评论量', default=0)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class PeopleInfo(models.Model):
    GENDER_CHOICE = ((0, 'male'), (1, 'female'))

    class Meta:
        db_table = 'peopleinfo'
        verbose_name = '人物'
    def __str__(self):
        return self.name
    name = models.CharField(max_length=20, verbose_name='姓名')
    gender = models.SmallIntegerField(choices=GENDER_CHOICE, default=0,verbose_name='性别')
    description = models.CharField(max_length=200, null=True,verbose_name='描述')
    book = models.ForeignKey(to=BookInfo,on_delete=models.CASCADE,verbose_name='图书')
    is_delete = models.BooleanField(default=False,verbose_name='逻辑删除')
