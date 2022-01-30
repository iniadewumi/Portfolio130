from django.http.response import HttpResponse
from django.shortcuts import render, redirect
import requests, json
from pandas import DataFrame
from datetime import datetime, timedelta
from .models import Ceres_Report
# Create your views here.
from django.views.generic import ListView
from datetime import datetime, timedelta
from urllib.parse import unquote

def homepage(request):
    return render(request, 'Pages/Home.html')

def profile(request):
    return render(request, 'Pages/About.html')

def contact(request):
    return render(request, 'Pages/Contact.html')

def fields(request):
    return render(request, 'Pages/Fields.html')

def resumes(request):
    return render(request, 'Pages/Resumes.html')


def text_to_speech_demo(request):
    return render(request, 'Pages/dummy_build.html')


def article_radar(request):
    return render(request, 'Pages/ArticleRadar.html')
def form_improvements(request):
    return render(request, 'Pages/form-improvements.html')

def article_results(request):
    import json
    keyword = request.GET.get('search_keyword')
    api_key = "302b75560a5d49efb89d07e1524b6be3"

    yest = str(datetime.now()-timedelta(days=1)).split()[0] 
    
    response = requests.get(f"https://newsapi.org/v2/everything?q={keyword}&apiKey={api_key}&from={yest}&sortBy=relevancy&pageSize=20")
    r_json = response.json()
    articles = r_json['articles']
    df = DataFrame.from_records(articles)
    for char in ['{', '}', "'id': ", '<ol>','<p class="p1">', "</li>", "</p>",  "<p>", "<li>", "</li>", ""]:
        df = df.replace(char, "")
    
    df['content'] = df['content'].astype("str").apply(lambda x: " ".join(x.split(" ")[:30])+"...")

    df.columns = [x.upper() for x in df.columns]
    for char in ['{', '}', "'id': ", 'None', ", 'name':", "'"]:
        df["SOURCE"] = df['SOURCE'].astype("str").replace(char, "", regex=True)
    
    out_articles = df.head(10).to_html(index=False, col_space='50px').replace('class="dataframe"', 'id="dataframe"').replace("<td>", '<td style="max-width: 150px;">').replace("\n", "").replace("\r", "").replace("\\", "").replace("<ol>", "").replace("{", "").replace("}", "").replace("<p>", "").replace("<li>", "").replace("</li>", "")
    context = {'out_articles':out_articles}
    return render(request, 'Pages/ArticleResult.html', context=context)
# yesterday = str(datetime.now()-timedelta(days=1))


def ceres_demo(request):
    reports = Ceres_Report.objects.all()
    context = {'reports': reports}
    print(context)
    return render(request, template_name='Pages/ceres.html', context=context)
def ceres_report_view(request, ceres_report_id):
    report = Ceres_Report.objects.get(pk=ceres_report_id)
    context = {'report': report}
    return render(request, template_name='Pages/ceres-report.html', context=context)

def ceres_report_update(request):
    data = unquote(request.body.decode('utf-8')).replace("+", " ").replace("report=<", "<")
    if len(data.split("&date=")) > 1:
        report, date = data.split("&date=")
        Ceres_Report.objects.create(text=report, created_at=date, modified_at=date)
        print("Created")
    elif data:
        print("ELSE IS BEING USED\n\n")
        Ceres_Report.objects.create(text=data)
        return HttpResponse("New Article Added")
    return HttpResponse("Access Denied!")


def projects(request):
    return render(request, 'Pages/Projects.html')

def scorepred(request):
    return render(request, 'Pages/ScorePred.html')

def imageclass(request):
    return render(request, 'Pages/ImageClass.html')

def doctrina(request):
    return render(request, 'Pages/Doctrina.html')
def emailgenerator(request):
    return render(request, 'Pages/EmailGenerator.html')

def bi_final(request):
    return render(request, 'Pages/final.html')
    # return redirect('https://public.tableau.com/app/profile/ini.adewumi/viz/test_16334777638670/ImpactofCovid19onUSAstates#1')

def tester(request):
    return render(request, 'Pages/delete.html')


def flappybird(request):
    return render(request, 'Pages/flappybird.html')

def vehicle_detector(request):
    return render(request, 'Pages/VehicleDetector.html')