from .models import AdminUIConfig


def global_navbar_style(request):
    config = AdminUIConfig.get_config()

    return {
        'global_navbar_style': config.navbar_style
    }

 