from django.shortcuts import render
from gesture import handsignal
import random
from howsthexp.forms import RegisterForm,LoginForm,ResetPassForm,ForgotPassForm
from django.http import HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from howsthexp.models import Song,UserRegister
from hashing import *
import eyed3
import predict
from os import listdir
import keras.backend as K
# Create your views here.
def Index(request):
    ansi = predict.emotion_detect()
    # ansi = random.choice(['sad','neutral','happy'])
    songname = random.choice(listdir('howsthexp/static/media/'+ansi))
    print(songname)
    path = "howsthexp/static/media/"+ansi+"/"+songname
    audiofile = eyed3.load(path)
    # save("/static/image/coverart.jpg")

    
    # image = Image.frombytes("RGBA", (500, 500), audiofile.tag.images[0])
    # b, g, r, _ = image.split()
    # image = Image.merge("RGB", (r, g, b))

    # image.save("/static/image/coverart.jpg")





    # coverart.save("cover.jpg")
    # release_group_ID = audiofile.tag.images[0]
    # artwork = mb.get_release_group_image_front(release_group_ID)

    # result_file = 'result_file'
    # with open(result_file, 'wb') as file_handler:
    #     file_handler.write(artwork)
    # Image.open(result_file).save("/static/image/coverart" + '.jpg')
    # os.remove(result_file)


    # for kl in list(audiofile.tag.images.get(None)):
    #   print(7,kl)
    print(audiofile.tag.images[0],"Image Frame")
    print( audiofile.tag.artist)
    print( audiofile.tag.album)
    print (audiofile.tag.title)
    context = {
                'emotion' : ansi,
                'song_name': songname,
                'song_title': audiofile.tag.title,
                'artist': audiofile.tag.artist,
                'coverart': audiofile.tag.images[0],
                #'range': ansi
              }
    return render(request, 'index.html',context)



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


def Player(request):
  ansi = predict.emotion_detect()
  # ansi = random.choice(['sad','neutral','happy'])
  songname = random.choice(listdir('howsthexp/static/media/'+ansi))
  path = "howsthexp/static/media/"+ansi+"/"+songname
  audiofile = eyed3.load(path)
  context = {
                'emotion' : ansi,
                'song_name': songname
                #'range': ansi
              }
  return render(request, 'musicplayer.html',context)
