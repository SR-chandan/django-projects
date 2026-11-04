from django.shortcuts import render
from django.http import HttpResponse

def app1(request):
    return HttpResponse("I am in firstapp")


from django.shortcuts import render
from django.http import HttpResponse

def app1(request):
    return HttpResponse("""
        <html>
        <head>
            <style>
                body {
                    background-color: lightblue;
                    text-align: center;
                    padding-top: 100px;
                }

                h1 {
                    color: darkblue;
                    font-size: 50px;
                    font-family: Arial;
                .first1{
                color: darkblue;
                    font-size: 50px;
                    font-family: Arial;
                    deco
                }
            </style>
        </head>

        <body>
            <h1 class='first'>I am in firstapp</h1>
            <h1 class='first1'>I am in firstapp</h1>
        </body>
        </html>
    """)