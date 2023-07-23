from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_id')
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    create_by = models.IntegerField()
    update_at = models.DateTimeField(auto_now=True)
    update_by = models.IntegerField()

    class Meta:
        db_table = 'user_info'


class UserRelation(models.Model):
    relation_name = models.CharField(max_length=10,help_text="相對的關係")
    related = models.ForeignKey(User, on_delete=models.CASCADE, related_name="related_user_id")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_relation_user_id")

    class Meta:
        db_table = 'user_relation'


class NeederInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="needer_info_user_id")
    age = models.IntegerField()
    birth_date = models.DateTimeField()
    heath_status = models.IntegerField()
    location = models.CharField(max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)
    create_by = models.IntegerField()
    update_at = models.DateTimeField(auto_now=True)
    update_by = models.IntegerField()

    class Meta:
        db_table = 'needer_info'


class AllergicList(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "allergic_list"


class Allergic(models.Model):
    allergic = models.ForeignKey(AllergicList, on_delete=models.CASCADE, related_name='allergic_list_id')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='allergic_user_id')

    class Meta:
        db_table = 'allergic'


class SkillList(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'skill_list'


class GiverInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='giver_info_user_id')
    skill = models.ForeignKey(SkillList, on_delete=models.CASCADE, related_name='skill_list_id')
    location = models.CharField(max_length=5)

    class Meta:
        db_table = 'giver_info'


class UserNeed(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_need_user_id')
    need_category = models.CharField(max_length=100)
    need_time = models.JSONField()
    solved = models.BooleanField(default=False)
    status = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    create_by = models.IntegerField()
    update_at = models.DateTimeField(auto_now=True)
    update_by = models.IntegerField()

    class Meta:
        db_table = 'user_need'


class GiverTime(models.Model):
    need_user = models.ForeignKey(NeederInfo, on_delete=models.CASCADE, related_name='need_user_id')
    giver = models.ForeignKey(GiverInfo, on_delete=models.CASCADE, related_name='giver_id')
    need_pair_time = models.DateTimeField()

    class Meta:
        db_table = 'need_pair_time'


class OrderInfo(models.Model):
    need_pair_id = models.IntegerField()
    order_price = models.IntegerField()
    order_date = models.DateTimeField()

    class Meta:
        db_table = 'order_info'