from django.shortcuts import render, redirect, get_list_or_404

def home_main(request):
    print("inside home of index")
    return redirect('/quiz_user/')
