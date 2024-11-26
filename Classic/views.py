from django.shortcuts import render
from django.http import HttpResponse

def Clasic(request):
    return HttpResponse("""
        <h1>Basic model of RoyalEnfield 350cc</h1>
        <img src="https://imgd.aeplcdn.com/1280x720/n/cw/ec/49318/royalenfield-classic-exterior5.jpeg?wm=2" alt="Royal Enfield Classic 350"
                        width="500" height="280">
    """)
