from django.shortcuts import render
from django.http import HttpResponse, request

projectList = [
    {
        'id': 1,
        'title': 'Ecomm Website',
        'description': 'New Ecommerce project'
    },
    {
        'id': 2,
        'title': 'Movie Website',
        'description': 'New Ecommerce project'
    },
    {
        'id': 3,
        'title': 'OTT PLatform',
        'description': 'New Ecommerce project'
    },
]


def projects(req):
    context = {'projects': projectList}
    return render(
        req, 'projects/projects.html',
        context
    )


def project(req, id):
    projectObj = None
    for i in projectList:
        if i['id'] == id:
            projectObj = i

    return render(
        req, 'projects/single-projects.html',
        {'project': projectObj}
    )

# Create your views here.
