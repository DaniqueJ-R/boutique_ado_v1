from django.shortcuts import render

# Create your views here.


def view_bag(request):
    """ View to show bag template. """

    return render(request, "bag/bag.html")