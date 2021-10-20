from django.db import models


class BookInfo(models.Model):
    name = models.CharField(max_length=20, verbose_name='书名')
    pub_date = models.DateField(verbose_name='发行日期')
    readcount = models.IntegerField(verbose_name='阅读量', default=0)
    commentcount = models.IntegerField(verbose_name='评论量', default=0)
    is_delete = models.BooleanField(verbose_name='逻辑删除', default=False)

    class Meta:
        db_table = 'bookinfo'
        verbose_name = '图书'

    def __str__(self):
        return self.name


class PeopleInfo(models.Model):
    GENDER_CHOICE = ((0, 'male'), (1, 'female'))
    name = models.CharField(max_length=20, verbose_name='姓名')
    gender = models.SmallIntegerField(choices=GENDER_CHOICE, verbose_name='性别', default=0)
    description = models.CharField(max_length=200, verbose_name='人物描述')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')
    book = models.ForeignKey(to=BookInfo,on_delete=models.SE,verbose_name='图书')
    class Meta:
        db_table = 'peopleinfo'
        verbose_name = '人物'

    def __str__(self):
        return self.name
