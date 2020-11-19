import markdown as md
import random
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django import forms
from django.urls import reverse

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request, title):
    if util.get_entry(title):
        content=util.get_entry(title)
        return render(request,"encyclopedia/content.html",{
            "title": title,
            "content":md.markdown(content),
        })
    else:
        return render(request,"encyclopedia/error.html")


## for the page to create a new page
def newpage(request):
    return render(request, "encyclopedia/newpage.html")
## this is for the entry of your title
def save(request):
    title = request.POST.get("title")
    text = request.POST.get("markdown")
    if util.get_entry(title):
        return render(request,"encyclopedia/pageexists.html",{
            "entry":title
        })
    else:
        util.save_entry(title,text)
        return redirect('title', title=title)
        ## the given below line if for the redirect to the page
        # return HttpResponseRedirect(reverse("index"))

# for the search option
def search(request):
    query=request.POST.get("q") # here q is the name of input in search option
    new=[]
    if util.get_entry(query):
        return redirect('title',title=query)
    else:
        all_entries=util.list_entries()
        for l in all_entries:
            s1=str(query).lower()
            s2=str(l).lower()
            if(s2.find(s1)!=-1):
                new.append(l)
        if len(new)==0:
            return render(request,"encyclopedia/error.html")
        else:
            return render(request, "encyclopedia/search.html", {
        "entries": new
    })

    # for the going to the edit page
def editpage(request,title):
        return render(request,"encyclopedia/edit.html",{
        "title":title.capitalize(),
        "content":util.get_entry(title)
    }) # where we have used the edit page

def edit(request,title):
    content=request.POST.get("markdown")
    ti=title.capitalize()
    util.save_entry(ti,content)
    return redirect('title',title=ti)

def randompage(request):
    all_entries=util.list_entries()
    l=len(all_entries)
    i=random.randint(0,l-1)
    return redirect('title',title=all_entries[i])