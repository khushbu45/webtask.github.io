from django.shortcuts import render

from contact.models import contactEnquiry
def home(request):
    return render(request,"index.html")
def contact (request):
    if request.method == 'POST':
        name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        en=contactEnquiry(name=name,email=email,phone=phone,message=message)
        en.save()
    return render(request, "index.html")