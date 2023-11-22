from django.shortcuts import render
from django.http.response import StreamingHttpResponse
from streaming.camera import RtspCam

# Create your views here.
def index(request):
    return render(request, 'streaming/index.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        if frame:
            yield  (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        else:
            pass

def video_feed(request):
    return StreamingHttpResponse(gen(RtspCam()), 
                                content_type='multipart/x-mixed-replace; boundary=frame')