from django.shortcuts import render
from portify.models import Portify
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from portify.forms import ExperienceForms, SkillsForms, PortifyForms


def portify_view(request):
    user = User.objects.filter(is_staff=True)
    portify = Portify.objects.get(user_id=user.id)
    return render(request, 'portify.html', {'portify': portify})


#        form_data_skills = SkillsForms(request.POST)
#        form_data_experience = ExperienceForms(request.POST)
@login_required
def portify_create(request):
    user = User.objects.get(id=request.user.id)
    if request.method == "POST":
        form_data_portify = PortifyForms(request.POST)
        if form_data_portify.is_valid():
            save_data_portify = form_data_portify.save(commit=False)
            save_data_portify.user_id = user
            save_data_portify.save()
        else:
            form_data_portify = PortifyForms(request.POST)
            context = {
                "portify": form_data_portify,

            }
            return render(request, 'form.html', context)

    else:
        form_data_portify = PortifyForms()
        context = {
            "portify": form_data_portify,

        }
        return render(request, 'form.html', context)

#Correction
#Correction
#Correction
@login_required
def portify_edit(request):
    user = User.objects.get(id=request.user.id)

    if request.method == "POST":
        form_data_portify = PortifyForms(request.POST)
        if form_data_portify.is_valid():
            save_data_portify = form_data_portify.save(commit=False)
            save_data_portify.user_id = user
            save_data_portify.save()
        else:
            form_data_portify = PortifyForms(request.POST)
            context = {
                "portify": form_data_portify,

            }
            return render(request, 'form.html', context)

    else:
        form_data_portify = PortifyForms()
        context = {
            "portify": form_data_portify,

        }
        return render(request, 'form.html', context)