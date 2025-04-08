from django.http import JsonResponse

def api_root(request):
    return JsonResponse({
        "message": "Welcome to the OctoFit API!",
        "url": "https://[REPLACE-THIS-WITH-YOUR-CODESPACE-NAME]-8000.app.github.dev"
    })