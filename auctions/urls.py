from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create/",views.create, name="create"),
    path("save/", views.save, name="save"),
    path("display/<item_id>", views.display, name="display"),
    path("newbid/<item_bid>", views.newbid, name="newbid"),
    path("comments/<item_id>", views.comments, name="comments"),
    path("watchcreate/<item_id>", views.watchcreate, name="watchcreate"),
    path("watchlist/", views.watchlist, name="watchlist"),
    path("removewatch/<item_id>", views.removewatch, name="removewatch"),
    path("cate/", views.cate, name="cate"),
    path("filter/", views.filter, name="filter"),
    path("close/<item_id>", views.close, name="close")
]
