from asyncio.windows_events import NULL
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import  HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import datetime
from .models import Auction_list, Category, User, Watch_list, comment,bids


def index(request):
    x = []
    x = Auction_list.objects.filter(auction_status = 1)
    items = []
    for item in reversed(x):
        items.append(item)
    return render(request, "auctions/index.html",{
        "items":items
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def create(request):
    category = []
    category = Category.objects.all()
    return render(request,"auctions/create.html",{
        "category":category
    })

def save(request):
    if request.method == "POST": 
        title = request.POST["title"]
        description = request.POST["description"]
        start_bid = request.POST["start_bid"]
        image = request.POST["image"]
        category = Category.objects.filter(list_category=request.POST["category"]).first()
        user = request.user
        time = datetime.datetime.now()
        content = Auction_list.objects.create(title=title,creator_id=user,category_list=category,description=description,start_bid=start_bid,image=image,auction_status=1,time_create=time)
        item_id = content.pk
    return display(request,item_id)

def display(request,item_id):
    winner = None
    test = Watch_list.objects.filter(user = request.user, item = item_id)
    item = Auction_list.objects.get(id = item_id)
    comms =[]
    comms = comment.objects.filter(items = item_id) 
    last = bids.objects.filter(item = item.id).last()
    if last is None:
        last = 0
    else:    
      winner = last.user_bid

    if comms is NULL:
        return render(request, "auctions/display.html", {
            "item" : item,
            "test":test,
            "winner":winner
        })
    else:    
        return render(request,"auctions/display.html",{
        "item":item,
        "comms":comms,
        "test":test,
        "winner":winner
    })


def newbid(request,item_bid):
    list = Auction_list.objects.get(id = item_bid)
    new =int(request.POST["bid"]) 
    oldbid = list.start_bid
    user = request.user
    if new > oldbid:
         content = bids.objects.create(
        item = list,
        value = new,
        user_bid = user,
        user_time_bid = datetime.datetime.now(),
        )
         list.start_bid = new
         list.save(update_fields=['start_bid'])
         return display(request,item_bid)


def comments(request,item_id):
    item = Auction_list.objects.get(id = item_id)
    comments = request.POST["comments"]
    time = datetime.datetime.now()
    user = request.user
    contents = comment.objects.create(
        items = item,
        content =comments,
        comment_time = time,
        user_comment = user
    )
    comm = contents.content
    return display(request,item_id)


def watchlist(request):
    user1 = request.user.id
    auctions = []
    auctions = Watch_list.objects.filter(user = user1)
    item = []
    for y in auctions:
        yyy = y.item
        item.append(yyy)
    return render(request, "auctions/watch.html",{
        "items" : item,
    })


def watchcreate(request,item_id):
    us = request.user
    list = Auction_list.objects.get(id = item_id)  
    content = Watch_list.objects.create(
        item = list,
        user = us,
    )
    return display(request,item_id)
    
def removewatch(request,item_id):
    us = request.user
    list = Auction_list.objects.get(id = item_id)
    watch = Watch_list.objects.get(user=us, item=list)
    watch.delete()
    return display(request,item_id)

def cate(request):
    name = []
    name = Category.objects.all() 
    return render(request,"auctions/cate.html",{
        "name":name
    })
            
def filter(request):
    categories = []
    categories = Category.objects.all()
    select = request.POST.get("option")
    if select is None:

        return render(request,"auctions/cate.html",{
            "categories" : categories,
        })
    else:
        se = Category.objects.get(list_category=select)
        sel = se.id
        auctions = Auction_list.objects.filter(category_list = sel)
        return render(request,"auctions/cate1.html",{
            "categories" : categories,
            "auctions" : auctions,
        })

def close(request,item_id):
    status = Auction_list.objects.get(id = item_id)
    status.auction_status = 0
    status.save(update_fields=['auction_status'])
    return display(request,item_id)   





