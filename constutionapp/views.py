from django.shortcuts import render, get_object_or_404
from .models import Section, Chapter

def index(request):
    sections = Section.objects.all()
    return render(request, 'constitution/index.html', {'sections': sections})

def section_detail(request, section_id):
    section = get_object_or_404(Section, id=section_id)
    return render(request, 'constitution/section_detail.html', {'section': section})

def chapter_detail(request, chapter_id):
    chapter = get_object_or_404(Chapter, id=chapter_id)
    return render(request, 'constitution/chapter_detail.html', {'chapter': chapter})
