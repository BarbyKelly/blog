from django.shortcuts import render
from .models import Resources


# Create your views here.
def resources_part(request):
    """
    Renders the Resources page
    """
    resources = Resources.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "resources/resources.html",
        {"resources": resources},
    )
