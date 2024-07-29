from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime


def index(request):

    partners = [
        {'name': 'Partner 1', 'image': 'https://production.egspec.org/assets/images/Accredited/award2.webp'},
        {'name': 'Partner 2', 'image': 'https://production.egspec.org/assets/images/Accredited/award5.webp'},
        {'name': 'Partner 3', 'image': 'https://production.egspec.org/assets/images/Accredited/award2.webp'},
        {'name': 'Partner 4', 'image': 'https://production.egspec.org/assets/images/Accredited/award5.webp'},
        {'name': 'Partner 5', 'image': 'https://production.egspec.org/assets/images/Accredited/award2.webp'}
    ]

    current_year = datetime.now().year

    return render(request, 'index.html', {'partners': partners, 'current_year': current_year})