from django.shortcuts import render
import json

def index(request):
    """
    View function for home page of the site rendering index.html
    """

    # Parsing the guide json file and passing it as context variable
    guide = 'GLSProj//guide.json'
    with open(guide) as json_file:
        data = json.load(json_file)
        json_string = json.dumps(data)
        print(json_string)
    return render(request, 'index.html', {'guide': json_string})