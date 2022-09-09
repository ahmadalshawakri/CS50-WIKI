from django.shortcuts import render
import markdown
import random

from . import util

markdowner = markdown.Markdown()

def check_entry(entry):
    content = util.get_entry(entry)
    if content == None:
        return None
    else:
        return markdowner.convert(content)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry (request, entry):
    entry_page = check_entry(entry)
    if entry_page is None:
        return render(request, "encyclopedia/error.html", {
            "title": entry,
            "message": "Error 404 the entry does not excist"
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "entry": entry_page,
            "title": entry
        })

def search(request):
    if request.method == "POST":
        entry_search = request.POST['q']
        entry_page = check_entry(entry)
        if entry_page is not None:
            return render(request, "encyclopedia/entry.html", {
                "entry": entry_page,
                "title": entry_search
        })
        else:
            entries = util.list_entries()
            recommendations = []
            for title in entries:
                if entry_search.lower() in title.lower():
                    recommendations.append(title)
            return render(request, "encyclopedia/search.html", {
                "entries": recommendations,
            })

def new_page(request):
    if request.method == "GET":
        return render(request, "encyclopedia/new_page.html")
    else:
        # Get the data that we stored in the form
        Title = request.POST.get('title')
        Content = request.POST.get('content')
        entries = util.list_entries()
        entries_lower = list((map(lambda x: x.lower(), entries)))
        if Title.lower() in entries_lower:
            return render(request, "encyclopedia/error.html", {
                "message": "The New Page you have created is already exist."
            })
        else:
             util.save_entry(Title, Content)
             return render(request, "encyclopedia/entry.html", {
                "title": Title,
                "entry": check_entry(Title)
            })

def edit(request):
    if request.method == "POST":
        entry_title = request.POST.get("entry_title")
        content = util.get_entry(entry_title)
        return render(request, "encyclopedia/edit.html", {
            "title": entry_title,
            "content": content
        })

def save_edit(request):
    if request.method == "POST":
        entry_title = request.POST.get("title")
        content = request.POST.get("content")
        util.save_entry(entry_title, content)
        return render(request, "encyclopedia/entry.html", {
                "title": entry_title,
                "entry": check_entry(entry_title)
            })

def random_page(request):
    entries = list(util.list_entries())
    random_title = random.choice(entries)
    return render(request, "encyclopedia/entry.html", {
                "title": random_title,
                "entry": check_entry(random_title)
            })
