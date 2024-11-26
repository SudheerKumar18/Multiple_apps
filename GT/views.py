from django.shortcuts import render
from django.http import HttpResponse

def GT(request):
    return HttpResponse("""
        <h1>GT is a RoyalEnfield model 650cc</h1>
        <img src="https://tse3.mm.bing.net/th?id=OIP.QDpjPy25SaXom-TWrCy8gQHaFj&pid=Api&P=0&h=220" alt="Royal Enfield GT 650cc"
                        width="500" height="280">
    """)
