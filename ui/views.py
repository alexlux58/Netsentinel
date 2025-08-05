from django.shortcuts import render


def home(request):
    """Render the main dashboard."""
    return render(request, 'ui/home.html')
