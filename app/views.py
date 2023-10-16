from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import ContactForm
from app.models import *

def index(request):
	return render(request,'index.html')



def upload_contacts(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_contacts')
    else:
        form = ContactForm()
    return render(request, 'contactsupload.html', {'form': form})

def view_contacts(request):
    data = Contact.objects.all()
    return render(request,'viewcontacts.html',{'data':data})
from django.shortcuts import render, get_object_or_404
from .models import Contact  # Import the Contact model

def view_video(request, contact_id):
    selected_contact = get_object_or_404(Contact, id=contact_id)

    context = {
        'selected_contact': selected_contact,
    }
    return render(request, 'app.html', context)