from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm


def profile(request):
    """
    Displays the user's profile
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    # When updating profile info
    if request.method == 'POST':
        # instance of profile defined in method
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserProfileForm(instance=profile)
    # Get user's associated orders and return them to template
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)
