from django.shortcuts import render
from .models import Tasks


def openMain(request):
    tasks = Tasks.objects.order_by('-sale')[0:50]
    return render(request, 'main/megamain.html', {'tasks': tasks})


def openMates(request):
    return render(request, 'main/aboutMatingPage.html')


def openAbout(request):
    return render(request, 'main/aboutPage.html')


def openCafes(request, page):
    st = 0; fn = 0;
    stA = 0; fnA = 0
    if page == 1:
        st = 0; fn = 50
    else:
        st = 50 * (page - 1)
        fn = st + 50
    tasks = Tasks.objects.filter(placeType='KR', ad=False)[st:fn]
    tasksAd = Tasks.objects.filter(placeType='KR', ad=True)[st:fn]
    tasksAll = Tasks.objects.filter(placeType='RECL')[st:fn]
    pageNext = 2
    pagePrev = 1
    if page != 1:
        pageNext = page + 1
        pagePrev = page - 1
    if len(tasks) == 0:
        pageNext = page
    return render(request, 'main/mainPage.html', {'Rec': tasksAd, 'adTasks': tasksAll, 'tasks': tasks, 'pages': page, 'type': 'cafes', 'pn': pageNext, 'pv': pagePrev, 'naming': 'Кафе и рестораны'})


def openTrevel(request, page):
    st = 0; fn = 0;
    if page == 1:
        st = 0; fn = 50
    else:
        st = 50 * (page - 1)
        fn = st + 50
    tasks = Tasks.objects.filter(placeType='P', ad=False)[st:fn]
    tasksAd = Tasks.objects.filter(placeType='P', ad=True)[st:fn]
    tasksAll = Tasks.objects.filter(placeType='RECL')
    pageNext = 2
    pagePrev = 1
    if page != 1:
        pageNext = page + 1
        pagePrev = page - 1
    if len(tasks) == 0:
        pageNext = page
    return render(request, 'main/mainPage.html', {'Rec': tasksAd, 'adTasks': tasksAll, 'tasks': tasks, 'pages': page, 'type': 'travels', 'pn': pageNext, 'pv': pagePrev, 'naming': 'Путешествия'})


def openShops(request, page):
    st = 0; fn = 0;
    if page == 1:
        st = 0; fn = 50
    else:
        st = 50 * (page - 1)
        fn = st + 50
    tasks = Tasks.objects.filter(placeType='M', ad=False)[st:fn]
    tasksAd = Tasks.objects.filter(placeType='M', ad=True)[st:fn]
    tasksAll = Tasks.objects.filter(placeType='RECL')
    pageNext = 2
    pagePrev = 1
    if page != 1:
        pageNext = page + 1
        pagePrev = page - 1
    if len(tasks) == 0:
        pageNext = page
    return render(request, 'main/mainPage.html', {'Rec': tasksAd, 'adTasks': tasksAll, 'tasks': tasks, 'pages': page, 'type': 'shops', 'pn': pageNext, 'pv': pagePrev, 'naming': 'Магазины'})


def openFun(request, page):
    st = 0; fn = 0;
    if page == 1:
        st = 0; fn = 50
    else:
        st = 50 * (page - 1)
        fn = st + 50
    tasks = Tasks.objects.filter(placeType='R', ad=False)[st:fn]
    tasksAd = Tasks.objects.filter(placeType='R', ad=True)[st:fn]
    tasksAll = Tasks.objects.filter(placeType='RECL')
    pageNext = 2
    pagePrev = 1
    if page != 1:
        pageNext = page + 1
        pagePrev = page - 1
    if len(tasks) == 0:
        pageNext = page
    return render(request, 'main/mainPage.html', {'Rec': tasksAd, 'adTasks': tasksAll, 'tasks': tasks, 'pages': page, 'type': 'fun', 'pn': pageNext, 'pv': pagePrev, 'naming': 'Развлечения'})


def openMed(request, page):
    st = 0; fn = 0;
    if page == 1:
        st = 0; fn = 50
    else:
        st = 50 * (page - 1)
        fn = st + 50
    tasks = Tasks.objects.filter(placeType='Z', ad=False)[st:fn]
    tasksAd = Tasks.objects.filter(placeType='Z', ad=True)[st:fn]
    tasksAll = Tasks.objects.filter(placeType='RECL')[st:fn]
    pageNext = 2
    pagePrev = 1
    if page != 1:
        pageNext = page + 1
        pagePrev = page - 1
    if len(tasks) == 0:
        pageNext = page
    return render(request, 'main/mainPage.html', {'Rec': tasksAd, 'adTasks': tasksAll, 'tasks': tasks, 'pages': page, 'type': 'med', 'pn': pageNext, 'pv': pagePrev, 'naming': 'Красота и здоровье'})


def openOther(request, page):
    st = 0; fn = 0;
    if page == 1:
        st = 0; fn = 50
    else:
        st = 50 * (page - 1)
        fn = st + 50
    tasks = Tasks.objects.filter(placeType='O', ad=False)[st:fn]
    tasksAd = Tasks.objects.filter(placeType='O', ad=True)[st:fn]
    tasksAll = Tasks.objects.filter(placeType='RECL')
    pageNext = 2
    pagePrev = 1
    if page != 1:
        pageNext = page + 1
        pagePrev = page - 1
    if len(tasks) == 0:
        pageNext = page
    return render(request, 'main/mainPage.html', {'Rec': tasksAd, 'adTasks': tasksAll, 'tasks': tasks, 'pages': page, 'type': 'other', 'pn': pageNext, 'pv': pagePrev, 'naming': 'Остальное'})


def openCar(request, page):
    st = 0; fn = 0;
    if page == 1:
        st = 0; fn = 50
    else:
        st = 50 * (page - 1)
        fn = st + 50
    tasks = Tasks.objects.filter(placeType='Car', ad=False)[st:fn]
    tasksAd = Tasks.objects.filter(placeType='Car', ad=True)[st:fn]
    tasksAll = Tasks.objects.filter(placeType='RECL')
    pageNext = 2
    pagePrev = 1
    if page != 1:
        pageNext = page + 1
        pagePrev = page - 1
    if len(tasks) == 0:
        pageNext = page
    return render(request, 'main/mainPage.html', {'Rec': tasksAd, 'adTasks': tasksAll, 'tasks': tasks, 'pages': page, 'type': 'car', 'pn': pageNext, 'pv': pagePrev, 'naming': 'Авто'})


def openStudy(request, page):
    st = 0; fn = 0;
    if page == 1:
        st = 0; fn = 50
    else:
        st = 50 * (page - 1)
        fn = st + 50
    tasks = Tasks.objects.filter(placeType='Study', ad=False)[st:fn]
    tasksAd = Tasks.objects.filter(placeType='Study', ad=True)[st:fn]
    tasksAll = Tasks.objects.filter(placeType='RECL')
    pageNext = 2
    pagePrev = 1
    if page != 1:
        pageNext = page + 1
        pagePrev = page - 1
    if len(tasks) == 0:
        pageNext = page
    return render(request, 'main/mainPage.html', {'Rec': tasksAd, 'adTasks': tasksAll, 'tasks': tasks, 'pages': page, 'type': 'study', 'pn': pageNext, 'pv': pagePrev, 'naming': 'Учёба'})


def openOneShop(request, page):
    st = 0; fn = 0;
    if page == 1:
        st = 0; fn = 50
    else:
        st = 50 * (page - 1)
        fn = st + 50
    tasks = Tasks.objects.filter(placeType='OneShop', ad=False)[st:fn]
    tasksAd = Tasks.objects.filter(placeType='OneShop', ad=True)[st:fn]
    tasksAll = Tasks.objects.filter(placeType='RECL')
    pageNext = 2
    pagePrev = 1
    if page != 1:
        pageNext = page + 1
        pagePrev = page - 1
    if len(tasks) == 0:
        pageNext = page
    return render(request, 'main/mainPage.html', {'Rec': tasksAd, 'adTasks': tasksAll, 'tasks': tasks, 'pages': page, 'type': 'oneshop', 'pn': pageNext, 'pv': pagePrev, 'naming': 'Отдельные товары'})



def openPageAboutMate(request, pk):
    task = Tasks.objects.filter(id=pk)[0]
    return render(request, 'main/matePage.html', {'task': task})
