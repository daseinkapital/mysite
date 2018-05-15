from django.shortcuts import render
from django.urls import reverse

def generic_home_context():
    context = {}
    home_items = []

    about_items = []

    music_items = []

    photo_items = []

    food_items = []

    pages = [
        {'name': 'Home', 'items': home_items, 'link': '#collapse1', 'id': 'collapse1'},
        {'name': 'About', 'items': about_items, 'link': reverse('about'), 'id': 'collapse2'},
        {'name': 'Music', 'items': music_items, 'link': '/music', 'id': 'collapse2'},
        {'name': 'Photography', 'items': photo_items, 'link': '/photography', 'id': 'collapse3'},
        {'name': 'Food', 'items': food_items, 'link': '/food', 'id': 'collapse4'}
    ]

    context.update({'pages': pages})
    return context

def generic_about_context():
    context = {}
    home_items = []

    about_items = [
        {'name': 'About', 'link': '#about'},
        {'name': 'Experience', 'link': '#experience'},
        {'name': 'Education', 'link': '#education'},
        {'name': 'Skills', 'link': '#skills'},
        {'name': 'Interests', 'link': '#interests'},
        {'name': 'Awards', 'link': '#awards'},
    ]

    music_items = []

    photo_items = []

    food_items = []

    pages = [
        {'name': 'Home', 'items': home_items, 'link': reverse('home'), 'id': 'collapse1'},
        {'name': 'About', 'items': about_items, 'link': '#collapse2', 'id': 'collapse2'},
        {'name': 'Music', 'items': music_items, 'link': '/music', 'id': 'collapse2'},
        {'name': 'Photography', 'items': photo_items, 'link': '/photography', 'id': 'collapse3'},
        {'name': 'Food', 'items': food_items, 'link': '/food', 'id': 'collapse4'}
    ]

    context.update({'pages': pages})
    return context

def home(request):
    context = generic_home_context()
    return render(request, 'mysite/home.html', context)

def about(request):
    context = generic_about_context()
    return render(request, 'mysite/about.html', context)