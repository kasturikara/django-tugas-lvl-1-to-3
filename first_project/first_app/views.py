from django.shortcuts import render
from first_app.models import Topic, WebPage, AccessRecord


def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    return render(request, "first_app/index.html", context=date_dict)
