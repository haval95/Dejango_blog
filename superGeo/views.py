from django.shortcuts import render


def SuperGeo_view(request):
    if request.method == 'POST':
        file = request.POST["file"]
        with open(file, "r") as f:
            print(f.read())
        return render(request, "superGeo.html", {"out_put": "success" })
    else:
        return render(request, "superGeo.html")