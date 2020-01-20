from django.shortcuts import render

def home(request):
    return render(request, 'getmail/home.html')


def unos(request):
        if request.method == 'POST':
            print(request.POST)
            unet_website = request.POST['website']
            if "www" in unet_website and '.' in unet_website:
                return render(request, 'getmail/unos.html', {'unos': unet_website})
            else: 
                error_message = 'pogresan unos'
                return render(request, 'getmail/home.html', {"error": error_message})