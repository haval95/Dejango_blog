from django.shortcuts import render
import pandas as pd


def SuperGeo_view(request):
    print(request.POST)
    if request.method == 'POST':
        # file = request.POST["file"]
        file = request.FILES['my_file']
        df = pd.read_csv(file)
        table = df.to_dict('records')
        print(df)
        return render(request, "superGeo.html", {"table": table})
    else:
        return render(request, "superGeo.html")