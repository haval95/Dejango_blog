from django.shortcuts import render
import pandas as pd
from geopy.geocoders import ArcGIS
import csv
from django.http import HttpResponse

arg = ArcGIS()
data = None

def SuperGeo_view(request):
    global data
    if request.method == 'POST':
        # file = request.POST["file"]
        file = request.FILES['my_file']
        df = pd.read_csv(file)
        df["cordinates"]= df["address"].apply(arg.geocode)
        df["Latitude"]=df["cordinates"].apply(lambda cordinate: cordinate.latitude)
        df["Longitude"]=df["cordinates"].apply(lambda cordinate: cordinate.longitude)
            
        table = df.to_dict('records')  
        data = df
        return render(request, "superGeo.html", {"table": table})
    else:
        return render(request, "superGeo.html")
    
    
def download():
    global data
    if data is None:
        # if data is not set, return an error response
        return HttpResponse('No data to download')
    else:
        # create a response object with the CSV file
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="data.csv"'
        response['Content-Type'] = 'text/csv'

        # write the DataFrame to the response as a CSV file
        data.to_csv(path_or_buf=response, index=False, quoting=csv.QUOTE_NONNUMERIC)
        
        return response