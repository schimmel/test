from django.http import HttpResponse
from worktime.models import Time

def index(request):
    latest_time_list = Time.objects.all().order_by('start')
    output = '<br> '.join([str(t.start) for t in latest_time_list])
    return HttpResponse(output)
