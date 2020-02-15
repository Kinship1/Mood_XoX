from django.shortcuts import render
from gesture import handsignal
import random
# Create your views here.
def index(request):
    ansi = handsignal()
    song_name = ['01 Ae Dil Hai Mushkil (Future Bass Remix By DJ Khushi) 190Kbps.mp3','01 Afghan Jalebi (Ya Baba) Phantom (Asrar n Pritam) 192Kbps.mp3','01 Chalti Hai Kya 9 Se 12 - Judwaa 2 - 190Kbps.mp3','01 - O Heeriye (Ayushmann Khurrana) - DownloadMing.SE.mp3',
                '02 Haareya - Arijit Singh - 190Kbps.mp3'    ]
    context = {
                'emotion' : "Arijit_Singh",
                'song_nam': 'media/'+str(ansi)+'.mp3',
                'range': ansi
              }
    print(context['song_nam'])
    return render(request, 'index.html',context)
