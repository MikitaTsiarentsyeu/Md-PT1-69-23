from django.shortcuts import render
import datetime

# Create your views here.
def test(request):
    # print("test view")
    now = datetime.datetime.now()
    items = [1,2.0,"three"]
    return render(request, 'test.html', {"current_time":now, "items":items})