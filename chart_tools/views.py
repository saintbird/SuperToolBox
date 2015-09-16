from django.shortcuts import render

# Create your views here.
def index(request):
    print "chart.index"
    return render(request, 'chart_tools/index.html')