from django.shortcuts import render, redirect   # Add import redirect at this line
from main.forms import MoodEntryForm
from main.models import MoodEntry
from django.http import HttpResponse
from django.core import serializers

def show_main(request):
    mood_entries = MoodEntry.objects.all()

    context = {
        'npm' : '2306256356',
        'name': 'Heinrich',
        'class': 'KKI',
        'mood_entries' : mood_entries
    }

    return render(request, "main.html", context)

def show_xml(request):
    data = MoodEntry.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def create_mood_entry(request):
    form = MoodEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_mood_entry.html", context)