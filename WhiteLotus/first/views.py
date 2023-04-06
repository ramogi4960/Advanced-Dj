from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm

# Create your views here.

# project_list = [
#     {
#         'id': '1',
#         'title': 'Ecommerce Website',
#         'description': 'This is a wide database web app for businesses',
#     },
#     {
#         'id': '2',
#         'title': 'Portfolio',
#         'description': 'This describes my skill-base',
#     },
#     {
#         'id': '3',
#         'title': 'Social Network',
#         'description': 'This is a social web app for connecting people',
#     },
# ]


def index(request):
    project = Project.objects.all()
    context = {'proj': project, }
    return render(request, 'first/base.html', context)


def dynamic(request, pk):
    # project_object = None
    # for i in project_list:
    #     if i['id'] == pk:
    #         project_object = i
    project = Project.objects.get(id=pk)
    tags = project.tags.all()
    context = {'p': project, 'tag': tags}
    return render(request, 'first/dynamic.html', context)


def forms(request):
    form = ProjectForm()
    if request.method == 'POST':
        # print(request.POST)
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form, }
    return render(request, 'first/forms.html', context)


def update_forms(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        # print(request.POST)
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form, }
    return render(request, 'first/forms.html', context)


def delete_forms(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('home')
    context = {'object': project, }
    return render(request, 'first/delete.html', context)
