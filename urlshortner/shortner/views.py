from django.shortcuts import render, redirect
from .models import Link
from .forms import NewLinkForm
import random
import string
from django.contrib import messages

# Create your views here.
def shortner(request):

    if request.method == 'POST':
        form = NewLinkForm(request.POST)

        if form.is_valid():
            shortened = ''.join(random.choice(string.ascii_letters)
                           for x in range(10))
            original = form.cleaned_data["original"]
            shortened_url = Link(original=original,shortened=shortened)
            shortened_url.save()
            # print(dir(request.user))
            # request.user.shortner.add(shortened_url)

            messages.info(request, 'Your new url is: ' +shortened_url.shortened + "To access this add /"+shortened_url.shortened+" at the end of the website address,  i.e. 127.0.0.1:8000/"+shortened_url.shortened)

            return redirect('/')
    
    else:
        form = NewLinkForm()
    
    data = Link.objects.all()

    context = {
        'form':form,
        'data':data
    }


    return render(request, 'shortner.html', context)

def our_redirect(request, shortened_link):
    data = Link.objects.get(shortened=shortened_link)
    return redirect(data.original)





# ERROR HANDLING
def server_error_500(request):
    return render(request, '500.html')

def server_error_404(request, exception):
    return render(request, 'shortner.html')