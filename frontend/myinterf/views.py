from django.conf import settings
import requests
from django.shortcuts import render, redirect

def persona_list(request):
    response = requests.get(f'{settings.BACKEND_API_URL}/api/personas/')
    if response.status_code == 200:
        personas = response.json()
        return render(request, 'persona_list.html', {'personas': personas})
    else:
        return render(request, 'error.html', {'message': 'Error fetching personas'})

def persona_detail(request, pk):
    response = requests.get(f'{settings.BACKEND_API_URL}/api/personas/{pk}/')
    if response.status_code == 200:
        persona = response.json()
        return render(request, 'persona_detail.html', {'persona': persona})
    else:
        return render(request, 'error.html', {'message': 'Error fetching persona'})

def persona_create(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        response = requests.post(f'{settings.BACKEND_API_URL}/api/personas/', data={'nombre': nombre, 'apellido': apellido})
        if response.status_code == 201:
            return redirect('persona_list')
        else:
            return render(request, 'error.html', {'message': 'Error creating persona'})
    return render(request, 'persona_form.html')

def persona_update(request, pk):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        response = requests.put(f'{settings.BACKEND_API_URL}/api/personas/{pk}/', data={'nombre': nombre, 'apellido': apellido})
        if response.status_code == 200:
            return redirect('persona_list')
        else:
            return render(request, 'error.html', {'message': 'Error updating persona'})
    response = requests.get(f'{settings.BACKEND_API_URL}/api/personas/{pk}/')
    if response.status_code == 200:
        persona = response.json()
        return render(request, 'persona_form.html', {'persona': persona})
    else:
        return render(request, 'error.html', {'message': 'Error fetching persona'})

def persona_delete(request, pk):
    if request.method == 'POST':
        response = requests.delete(f'{settings.BACKEND_API_URL}/api/personas/{pk}/')
        if response.status_code == 204:
            return redirect('persona_list')
        else:
            return render(request, 'error.html', {'message': 'Error deleting persona'})
    response = requests.get(f'{settings.BACKEND_API_URL}/api/personas/{pk}/')
    if response.status_code == 200:
        persona = response.json()
        return render(request, 'persona_confirm_delete.html', {'persona': persona})
    else:
        return render(request, 'error.html', {'message': 'Error fetching persona'})
