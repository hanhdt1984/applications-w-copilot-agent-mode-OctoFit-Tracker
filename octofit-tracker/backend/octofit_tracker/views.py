from django.http import JsonResponse

def api_root(request):
    return JsonResponse({
        "message": "Welcome to the OctoFit API!",
        "url": "https://shiny-waddle-v94jw569p72xrrr-8000.app.github.dev"
    })