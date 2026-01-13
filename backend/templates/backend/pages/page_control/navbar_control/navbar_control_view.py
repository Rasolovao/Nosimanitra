from django.shortcuts import render
from backend.models import AdminUIConfig

def navbar_control(request):


    config = AdminUIConfig.get_config()
    if request.method == 'POST':
        navbar_style = request.POST.get('navbar_style')
        valid_styles = [choice[0] for choice in AdminUIConfig.NAVBAR_CHOICES]
        if navbar_style in valid_styles:
            config.navbar_style = navbar_style
            config.save()


  



    context = {'config': config , 'navbar_styles': AdminUIConfig.NAVBAR_CHOICES}

    return render(request, 'backend/pages/page_control/navbar_control/navbar_control.html', context)

  