from django.contrib import admin
from .models import Auction_list,User,comment,Category,bids,Watch_list
# Register your models here.

admin.site.register(User)
admin.site.register(Auction_list)
admin.site.register(bids)
admin.site.register(Category)
admin.site.register(comment)
admin.site.register(Watch_list)