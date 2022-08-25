from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
   pass

class Category(models.Model):
    list_category = models.CharField(max_length=25)
    
    def __str__(self) -> str:
        return f"{self.list_category}"


class Auction_list(models.Model):
    title = models.CharField(max_length=79,null=False)
    description = models.TextField(null=False)
    image = models.URLField()
    auction_status = models.BooleanField()
    time_create = models.DateTimeField()
    creator_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user")
    category_list = models.ForeignKey(Category,on_delete=models.CASCADE ,related_name="type", null=True)
    start_bid = models.FloatField(null=False)

    def __str__(self) -> str:
        return f"{self.id}"

class bids(models.Model):
    item = models.ForeignKey(Auction_list,on_delete=models.CASCADE ,related_name="item")
    value = models.FloatField()
    user_bid = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_name")
    user_time_bid = models.DateTimeField()

    def __str__(self) -> str:
        return f"{self.value}"

class comment(models.Model):
    items = models.ForeignKey(Auction_list,on_delete=models.CASCADE ,related_name="items") 
    content = models.TextField()
    comment_time = models.DateTimeField()
    user_comment = models.ForeignKey(User,on_delete=models.CASCADE ,related_name="time")

    def __str__(self) -> str:
        return f"{self.items},{self.user_comment},{self.comment_time},{self.content}"

class Watch_list(models.Model):
    item = models.ForeignKey(Auction_list, on_delete=models.CASCADE, related_name="watch")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user1")

    def __str__(self) -> str:
        return f"{self.id}"