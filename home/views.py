from django.shortcuts import render,redirect
from django.views import View
from .forms import CommentForm
from django.contrib import messages
from .models import News
# Create your views here.
from django.shortcuts import render,get_object_or_404
class HomeView(View):
    form_class=CommentForm
    def get(self,request):
        form=self.form_class
        modelnew=get_object_or_404(News)
        return render(request,'index.html',{'form':form,'model':modelnew})
    def post(self,request):
       form=self.form_class(request.POST)
       modelnew=get_object_or_404(News)
       if form.is_valid():
           form.save()
           messages.success(request, 'پیام ارسال شد ', 'success')
           return redirect('home:home_index')
       return render(request,'index.html',{'form':form,'model':modelnew})