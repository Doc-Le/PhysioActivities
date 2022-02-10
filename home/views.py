from django.shortcuts import render
from user.models import UserProfile

def index(request):
    """ A view to return the index page """
    current_user = request.user
    try:
        profile = UserProfile.objects.get(user_id=current_user.id)
    except UserProfile.DoesNotExist:
        profile = None
    context = {'profile': profile}
    return render(request, 'home/index.html', context)