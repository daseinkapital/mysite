from django.shortcuts import render

def home(request):
    context = {}
    items = [
        {'name': 'About', 'link': '#about'},
        {'name': 'Experience', 'link': '#experience'},
        {'name': 'Education', 'link': '#education'},
        {'name': 'Skills', 'link': '#skills'},
        {'name': 'Interests', 'link': '#interests'},
        {'name': 'Awards', 'link': '#awards'},
    ]
    additional_pages = [
        {'name': 'Photography', 'link': 'photography'},
        {'name': 'Music', 'link': 'music'}
    ]
    context.update({'items': items})
    return render(request, 'mysite/home.html', context)