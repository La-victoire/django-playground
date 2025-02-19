from django.shortcuts import render, redirect
from django.contrib import messages 
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Room , Topic
from .forms import RoomForm

# Create your views here.

#  rooms = [
#   {"id" : 1, 'name': 'sup bitches'},
#   {"id" : 2, 'name': 'lets get started'},
#   {"id" : 3, 'name': 'gyatttt bitches'},
#   ] 

def loginPage(request):

  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    if username is None or password is None:
     print(f"username: {username}")
     print(f"password: {password}")
     return
    try:
        user = User.objects.get(username=username)
    except:
        messages.error(request, 'User does not exist')
        return render(request, 'crudapp/login_register.html', {})
    
    user = authenticate(request, username=username, password=password)

    if user is not None:
      login(request, user)
      return redirect('home')
    else:
      messages.error(request, 'username or password does not exist')
      return render(request, 'crudapp/login_register.html')
     
  context ={}
  return render(request, 'crudapp/login_register.html',context)

def home(request):
  q = request.GET.get('q') if request.GET.get('q') != None else ''

  rooms = Room.objects.filter(
    Q(topic__name__icontains=q) |
    Q(name__icontains=q) |
    Q(description__icontains=q)
    )

  topics = Topic.objects.all()
  room_count = rooms.count()

  context = {'rooms': rooms, 'topics':topics, 'room_count': room_count}
  return render(request, 'crudapp/home.html', context )

def room(request, pk):
  room = Room.objects.get(id=pk )
  context = {'room': room}    
  return render(request, 'crudapp/Room.html', context)

def createRoom(request):
  form = RoomForm()
  if request.method == 'POST':
    form = RoomForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('home')

  context = {'form':form}
  return render(request, 'crudapp/room_form.html',context)

def updateRoom(request, pk):
  room = Room.objects.get(id=pk)
  form = RoomForm(instance=room)
  if request.method == 'POST':
    form = RoomForm(request.POST, instance=room)
    if form.is_valid():
      form.save()
      return redirect('home')
    
  context = {'form': form}
  return render(request, 'crudapp/room_form.html', context)

def deleteRoom(request, pk):
  room = Room.objects.get(id=pk)
  if request.method == 'POST':
    room.delete()
    return redirect('home')
  context = {'obj':room}
  return render(request, 'crudapp/delete.html', context)