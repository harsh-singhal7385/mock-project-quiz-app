from django.shortcuts import render, redirect, get_list_or_404

def home_main(request):
    return render(request,'index.html')
