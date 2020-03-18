// const song = document.querySelector('#player');
// const progressBar = document.querySelector('#progress-bar'); // element where progress bar appears


function play() {
    document.getElementById('player').play();
    document.getElementById('played').style.visibility="hidden";
    document.getElementById('paused').style.visibility="visible";
  }

function pause() {
    document.getElementById('player').pause();
    document.getElementById('paused').style.visibility="hidden";
    document.getElementById('played').style.visibility="visible";
  }

function volup() {
    document.getElementById('player').volume+=0.1;
  }

function voldwn() {
    document.getElementById('player').volume-=0.1;
  }
// (".button").click(function() {
//       this.toggleClass("pause");
//       return false;
//     });
//   });


function convertElapsedTime(inputSeconds){
  var seconds = Math.floor(inputSeconds%60)
  if(seconds<10) {
    seconds = "0" + seconds
  }
  var minutes = Math.floor(inputSeconds/60)
  return minutes+":"+seconds
}

function updateBar(event){
  var canvasWidth = 603
  var canvas = document.getElementById("progress").getContext('2d')

  canvas.clearRect(0,0,canvasWidth,50)
  
  var currenttime = event.currentTime
  var duration = event.duration
  var percentage = (currenttime/duration)/2
  var progress = (canvasWidth*percentage)

  canvas.fillStyle = "green"
  canvas.fillRect(0,0,progress,50)

  

  document.getElementById("current-time").innerHTML = convertElapsedTime(currenttime)

  if (convertElapsedTime(currenttime)==convertElapsedTime(duration)){
    location.reload()
  }

  
  // canvas.fillStyle = "pink"
  // cavas.fillRect(0,0,progress,50)
}

function removecls() {
  var element = document.getElementById("played");
  var myAudio = document.getElementById("player");
  if (isPlaying){
  element.classList.remove("pause");
  element.classList.add('play');}
  else{
    element.classList.remove("play");
    element.classList.add('pause');

  }
}

// function updateProgressValue() {
//   progressBar.max = song.duration;
//   progressBar.value = song.currentTime;  
//   document.querySelector('.currentTime').innerHTML =  formatTime(song.currentTime); // See lines 85-92 for MM:SS formatting
//   document.querySelector('.durationTime').innerHTML = formatTime(song.duration); // See lines 85-92 for MM:SS formatting
// };

// function changeProgressBar() {
//   song.currentTime = progressBar.value;
// };