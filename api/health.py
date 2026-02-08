import json

def handler(request):
    return (
        json.dumps({"status": "ok"}),
        200,
        {"Content-Type": "application/json"},
    )
