from django.shortcuts import render
from gesture import handsignal
import random
from howsthexp.forms import RegisterForm,LoginForm,ResetPassForm,ForgotPassForm
from django.http import HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from howsthexp.models import Song,UserRegister
from hashing import *
import eyed3
from predict import emotion_detect
import keras.backend as K
# Create your views here.
def Index(request):
    # ansi = handsignal()
    # song_name = ['01 Ae Dil Hai Mushkil (Future Bass Remix By DJ Khushi) 190Kbps.mp3','01 Afghan Jalebi (Ya Baba) Phantom (Asrar n Pritam) 192Kbps.mp3','01 Chalti Hai Kya 9 Se 12 - Judwaa 2 - 190Kbps.mp3','01 - O Heeriye (Ayushmann Khurrana) - DownloadMing.SE.mp3',
    #             '02 Haareya - Arijit Singh - 190Kbps.mp3'    ]
    # context = {
    #             'emotion' : "Arijit_Singh",
    #             'song_nam': 'media/'+str(ansi)+'.mp3',
    #             'range': ansi
    #           }
    # print(context['song_nam'])
    return render(request, 'index.html')



def Register(request):
    if request.method == 'POST':
        #save the form and got to login page
        form = RegisterForm(request.POST)

        if form.is_valid():
            user=UserRegister()
            user.name = form.cleaned_data['Name']
            user.username = form.cleaned_data['username']
            user.email = form.cleaned_data['Email']
            pas = form.cleaned_data['password']
            user.password = hash_password(pas)

            user.save()
            return HttpResponseRedirect(reverse('login_user'))



        # print("here")
    else:
        form = RegisterForm()

    context = {
    'form':form,
    }


    return render(request,'register.html',context)


def Login(request):
    if request.method == 'POST':
        #save the form and got to login page
        form = LoginForm(request.POST)

        print("here")
        if form.is_valid():
            username = form.cleaned_data['username']
            request.session['name'] = username
            return HttpResponseRedirect(reverse('user_dashboard',args=(username,)))

    else:
        form = LoginForm()

    context = {
    'form':form,
    }

    return render(request,'login.html',context)


def Dashboard(request,user):
    if request.session.get('name') == user:
        if request.method=='POST':
            emotion = emotion_detect()
            K.clear_session()
            print("detected emotion {}".format(emotion))

            return HttpResponseRedirect(reverse('play_song',args=(user,emotion,)))
        context={
        'username':user,
        }
        return render(request,'dashboard.html',context)

    else:
        return HttpResponseRedirect(reverse('login_user'))



def Play(request,user,emotion):

    print("emotion {}".format(emotion))
    return render(request,'play_song.html')






def Logout(request,user):
    try:
        del request.session['name']
        print("user deleted")
        print(request.session['name'])
    except :
          pass
    return HttpResponseRedirect(reverse('login_user'))
