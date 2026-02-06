from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login
from django.contrib import messages
from .models import Franchise,Players,Stadium,Profile
from .forms import PlayerForm,StadiumForm,ProfileForm,UserRegiterForm

# Create your views here.
def home(request):
    context={
        'msg':"This is IPL Home page",
        'title':"IPL HOME"
    }
    return render(request,'home.html',context)

def register(request):
    if request.method =="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirmPassword')
        print(username,email,password,confirm_password)
        return HttpResponse("Registerd successfully")
    else:
        return render(request,'register.html')
    
def login_pr(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
        return HttpResponse("LOGIN SUCCESSFUL")
    return render(request,'login.html')


def register_franchise(request):
    if request.method=="POST":
        name=request.POST.get("name")
        short_name=request.POST.get("short_name")
        founded_year=request.POST.get("founded_year")
        no_of_trophies= request.POST.get("no_of_trophies")
        city=request.POST.get("city")
        owner=request.POST.get("owner")
        coach=request.POST.get("coach")
        logo=request.POST.get("logo")

        Franchise.objects.create(
            name=name,
            short_name=short_name,
            founded_year=founded_year,
            no_of_trophies=no_of_trophies,
            city=city,
            owner=owner,
            coach=coach,
            logo=logo,
        )
        return HttpResponse("REGISTERD Succesfully")
    else:
        return render(request,'register_franchise.html')
    
def franchise_list(request):
    franchise=Franchise.objects.all()
    context={
        "franchise":franchise,
    }
    return render(request,"franchise_list.html",context)

def fr_details(request,id):
    franchise = Franchise.objects.get(id=id)
    return render(request,'franchise_details.html',{'franchise':franchise})

def fr_update(request,id):
    franchise = Franchise.objects.get(id=id)
    if request.method=="POST":
        franchise.name=request.POST.get("name")
        franchise.short_name=request.POST.get("short_name")
        franchise.founded_year=request.POST.get("founded_year")
        franchise.no_of_trophies=request.POST.get("no_of_trophies")
        franchise.city=request.POST.get("city")
        franchise.owner=request.POST.get("owner")
        franchise.coach=request.POST.get("coach")

        if request.FILES.get('logo'):
            franchise.logo = request.FILES.get("logo")
        
        franchise.save()
        return redirect('ipl_app:franchise_list')
    else:
        return render(request,'Update_franchise.html',{'franchise':franchise})
    
def fr_delete(request,id):
    franchise = Franchise.objects.get(id=id)
    if request.method=="POST":
        franchise.delete()
        return redirect('ipl_app:franchise_list')
    
def register_player(request):
    if request.method == "POST":
        form = PlayerForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ipl_app:register_player')
        else:
            return HttpResponse("INVALID RESPONSE", status=400)
    else:
        form= PlayerForm()
        return render(request,'register_players.html',{'form': form})

def player_list(request):
    players = Players.objects.all()
    return render(request,'players_list.html',{'players':players})

def delete_player(request,id):
    player= Players.objects.get(id=id)
    if request.method=="POST":
        player.delete()
        return redirect('ipl_app:players_list')
    
def update_player(request,id):
    player= Players.objects.get(id=id)
    if request.method=="POST":
        form = PlayerForm(request.POST,request.FILES,instance=player)
        if form.is_valid():
            form.save()
            return redirect('ipl_app:players_list')
    else:
        form = PlayerForm(instance=player)
        return render(request,'update_player.html',{'form':form, 'player':player})

def register_stadium(request):
    if request.method=="POST":
        form = StadiumForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Saved sUccessfully')
    else:
        form = StadiumForm()
        return render(request,'stadium.html',{'form':form})
    
def stadium_list(request):
    stadiums = Stadium.objects.all()
    return render(request,'stadium_list.html',{'stadiums':stadiums})

def stadium_delete(request,id):
    stadium = Stadium.objects.get(id=id)
    if request.method=='POST':
        stadium.delete()
        return redirect('ipl_app:stadium_list')
    
def stadium_update(request,id):
    stadium = Stadium.objects.get(id=id)
    if request.method=="POST":
        form = StadiumForm(request.POST, instance=stadium)
        if form.is_valid():
            form.save()
            return redirect('ipl_app:stadium_list')
    else:
        form = StadiumForm(instance=stadium)
        franchises = Franchise.objects.all()
        return render(request,'stadium_update.html',{'stadium':stadium, 'form':form, 'franchises':franchises})
    

def register_user(request):
    if request.method=='POST':
        user_form = UserRegiterForm(request.POST)
        profile_form = ProfileForm(request.POST,request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            #create user
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()

            #create profile
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            return HttpResponse('Your account has been created ,You can login now')
    else:    
        user_form=UserRegiterForm()
        profile_form = ProfileForm()
        return render(request,'register_user.html',{'user_form':user_form,'profile_form':profile_form})


def login_user(request):
    if request.method=='POST':
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']

            user  = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,'LOGIN USER SUCCESSFUL')
            else:
                messages.error(request,'ENTERED DETAILS ARE NOT VALID')
    else:
        login_form = AuthenticationForm()
    return render(request,'login_user.html',{'login_form':login_form})