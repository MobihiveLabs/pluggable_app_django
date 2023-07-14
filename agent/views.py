from django.shortcuts import render
from .forms import AgentCompositeForm
from django.http import HttpResponse

def agent_form_view(request):
    if request.method == 'POST':
        form = AgentCompositeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Form Saved!")
    else:
        form = AgentCompositeForm()

    return render(request, 'forms.html', {'form': form})
