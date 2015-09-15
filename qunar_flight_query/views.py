# This Python file uses the following encoding: utf-8

from django.shortcuts import render
from django.http import HttpResponse
import xml.etree.ElementTree as etree
import urllib
import sys
import time
import json

reload(sys)
sys.setdefaultencoding('utf8')

# Create your views here.
def index(request):
    return render(request, 'index.html')

def query(request):
    c1 = request.GET["c1"]
    c2 = request.GET["c2"]
    selDate = request.GET["date"]
    places = c1 + "-" +c2
    #times =  time.strftime('%Y年-%m月-%d日 %H时:%M分:%S秒',time.localtime())
    
    context = urllib.urlopen('http://ws.qunar.com/holidayService.jcp?lane=%s' %places.encode("utf-8"))
    tree = etree.parse(context)
    root = tree.getroot()
    ret = "["
    for node in root[0]:
        if node.attrib["date"] == selDate or selDate=="0":
            if len(node) != 0:
                for child in node:
                    if child.attrib["type"] == "go" and int(child.attrib["price"])!=0:
                        ret = ret+'{'+\
                        '"date":'+ '"'+ node.attrib["date"][5:]+ '"'+","+\
                        '"places":'+'"'+places+ '"'+","+\
                        '"discount":'+'"'+child.attrib["discount"]+ '"'+","+\
                        '"price":'+'"'+child.attrib["price"]+ '"'+","+\
                        '"company":'+'"'+node.attrib["go_avc"]+ '"'+","+\
                        '"start":'+'"'+node.attrib["go_start"]+ '"'+","+\
                        '"expires":'+'"'+node.attrib["go_expires"]+ '"'+"},"
                        #ret = ret+"<tr><td>"+node.attrib["date"]+"</td>"\
                        #+"<td>"+places+"</td>"\
                        #+"<td>"+child.attrib["discount"]+"</td>"\
                        #+"<td>"+child.attrib["price"]+u"元"+"</td>"\
                        #+"<td>"+node.attrib["go_avc"]+"</td>"\
                        #+"<td>"+node.attrib["go_start"]+"</td>"\
                        #+"<td>"+node.attrib["go_expires"]+"</td></tr>"
    ret= ret[:-1]+']'
    return HttpResponse(ret)        