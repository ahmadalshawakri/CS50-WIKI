from django.shortcuts import render
import markdown

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


