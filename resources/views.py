from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Resources
from .forms import SuggestionForm


# Create your views here
class ResourcesList(generic.ListView):
    "Returns all published Resources and displays them"
    queryset = Resources.objects.filter(status=1)
    template_name = "resources/resources.html"


def resources_part(request):
    """
    Renders the Resources page
    """
    resources = Resources.objects.all().order_by('-created_on')
    suggestion_form = SuggestionForm()

    return render(
        request,
        "resources/resources.html",
        {
            "resources": resources,
            "suggestion_form": suggestion_form
        },
    )
