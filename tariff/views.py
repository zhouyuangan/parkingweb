import csv
from djqscsv import render_to_csv_response
from django.shortcuts import render
from django.http import HttpResponse
from tariff.models import Tariffs
# Create your views here.

def index(request):
    return HttpResponse(u'这里是票务中心')

def download_csv(request):
    # Create the HttpResponse object with the appropriate CSV header.
    # response = HttpResponse(content_type='text/csv')
    # response['Content-Disposition'] = 'attachment; filename="费用用度.csv"'

    # writer = csv.writer(response)
    # writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    # writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])
    # qs = Tariffs.objects.values('user_name','car_number')
    qs = Tariffs.objects.all()
    return render_to_csv_response(qs,filename=u'tariffs.csv')