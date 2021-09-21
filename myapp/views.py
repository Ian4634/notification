from django.shortcuts import render
from django.http import HttpResponse
from win10toast import ToastNotifier
import asyncio

async def count():
    for i in range(10):
        print(i)
        await asyncio.sleep(1)

# Create your views here.
def index(request):
    asyncio.run(count())
    hr = ToastNotifier()
    hr.show_toast("alarm", "this is the massage")
    return HttpResponse("hi")