# Create your views here.
from wiki.models      import Page
from django.shortcuts import render_to_response
from django.http      import HttpResponseRedirect
import markdown

def view_page(request, page_name): #from URL
  '''Views a page XXX retrieving it from DB'''
  try:
    page = Page.objects.get(pk=page_name) # takes this from model 
  except Page.DoesNotExist:
    return render_to_response("create.html", {"page_name": page_name} )
  content=page.content
  return render_to_response("view.html", {"page_name": page_name, "content": markdown.markdown(content)} )

def edit_page(request, page_name):
  """Creates/Edits page calles 'page_name'. this var comes from urls.py"""
  try:
    page = Page.objects.get(pk=page_name) # takes this from model
    content = page.content # maybe typo?
  except Page.DoesNotExist:
    content = "No content"
  return render_to_response("edit.html", {"page_name": page_name, "content": content} )

def save_page(request, page_name):
  """A form from EDIT redirects to save_page with a content and a page_name"""
  content = request.POST['content']
  try:
    page = Page.objects.get(pk=page_name) # takes this from model
    page.content = content
  except Page.DoesNotExist:
    page = Page(name=page_name, content=content)
  page.save()
  return HttpResponseRedirect("/wikicamp/" + page_name + "/" )

def view_home(request):
    return HttpResponseRedirect("/wikicamp/Home/")