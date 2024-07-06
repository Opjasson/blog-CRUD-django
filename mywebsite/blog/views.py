from django.shortcuts import render,redirect
from .models import PostModel
from .forms import CreateForms
from django.http import HttpResponseRedirect

def update(request,id_update):
   form_update = PostModel.objects.get(id=id_update)
   
   data = {
       'judul' : form_update.judul,
       'body'  : form_update.body,
       'category' : form_update.category,
   }
   akun_form = CreateForms(request.POST or None,initial=data,instance=form_update)
   
   if request.method == 'POST':
        if akun_form.is_valid():
            akun_form.save()
            return HttpResponseRedirect('/blog')
    
   context = {
        'judul' : 'Update',
        'isi'   : 'Silahkan Update Postingan Anda',
        'form'  : akun_form,
        }
   return render(request,'create.html',context)
   

def delete(request,id_delete):
    PostModel.objects.filter(id=id_delete).delete()
    return redirect('blog:index')
    

def create(request):
    post = PostModel.objects.all()
    forms = CreateForms(request.POST or None)
    
    if request.method == 'POST':
        if forms.is_valid():
            forms.save()
            return HttpResponseRedirect('/blog')
    
    context = {
        'judul' : 'Create',
        'isi'   : 'Silahkan Buat Postingan Anda',
        'posts' : post,
        'form'  : forms,
    }
    return render(request,'create.html',context)

def index(request):
    post = PostModel.objects.all()
    
    context = {
        'judul' : 'Page Blog',
        'isi'   : 'Selamat Datang di MyBlog',
        'posts' : post
    }
    return render(request,'blog.html',context)
