from Ipython.display import display, Javascript
from google.colab.output import eval_js
from base64 import b64decode, b64encode
import numpy as np

def init_camera():
  """Creates objects and functions in HTML/Javascript to access local web camera"""
  js = Javascript('''

  // global variables to use in both functions
  var div = null;
  var video = null; // video to display stream from local webcam
  var stram = null; // stream from local webcam
  var canvas = null;  // for single frame from video and convert frame to JPG
  var img = null;  // to display jpg after processing with 'cv2'

  async function initCamera() {
  // place for video 
  div = document.createElement('div');
  document.body.appendChild(div);

  // To display video
  video = document.createElement('video');
  video.style.display = 'block';
  div.appendChild(video);

  // get webcam stream and assing to <video>
  stream = await navigator.mediaDevices.getUserMedia({video: true});
  video.srcObject = stream;
  
  // start playing stream from webcam in <video>
  await video.play();

  // Resize the output to fit the video element.
  google.colab.output.setIframeHeight(document.documentElement.scrollHeight, true);

  // <canvas> for frame from <video>
  canvas = document.createElement('canvas');
  canvas.width = video.videoWidth;
  canvas.height = video.videoHeight;
  //div.appendChild(input_canvas); // there is no need to display to get image (but you can display it for test)

  // <img> for image after processing with <cv2>
  img = document.createElement('img');
  img.width = video.videoWidth;
  img.height = video.videoHeight;
  div.appendChild(img);

  }

  
  
  
