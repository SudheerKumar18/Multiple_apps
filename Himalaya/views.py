from django.shortcuts import render
from django.http import HttpResponse

def Himalaya(request):
    return HttpResponse("""
        <h1>RoyalEnfield model Himalaya 450CC</h1>
        <img src="https://www.rushlane.com/wp-content/uploads/2022/04/2023-royal-enfield-himalayan-450-official-teaer.jpeg" alt="Royal Enfield Himalayan 450CC"
                        width="500" height="280">>
                        
    """)
