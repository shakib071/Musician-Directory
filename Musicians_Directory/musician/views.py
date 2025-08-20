from django.shortcuts import render,redirect
from .models import MusicianModel 
from .forms import MusicianForm
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy

# Create your views here.

# def show_musician_list(request):

#     musician_list = MusicianModel.objects.all()
#     print(musician_list)
#     return render(request,'show_musician_list.html',{'musician_list': musician_list})




# def add_musician(request):

#     if request.method == "POST":
#         form = MusicianForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("homepage")
        
#     else:
#         form =  MusicianForm()
#     return render(request,'add_musician.html',{'form' : form})





class MusicianCreateView(CreateView):
    model = MusicianModel
    form_class = MusicianForm
    template_name = 'add_musician.html'
    success_url = reverse_lazy('homepage')





# def edit_musician(request,id):
#     musician  = MusicianModel.objects.get(pk=id)
#     musician_form = MusicianForm(instance=musician)
#     if request.method == "POST":
#         musician_form = MusicianForm(request.POST,instance=musician)
#         if musician_form.is_valid():
#             musician_form.save()
#             return redirect('homepage')
    
#     return render(request,'add_musician.html',{'form': musician_form})


class MusicianUpdateView(UpdateView):
    model = MusicianModel
    form_class = MusicianForm
    template_name = 'add_musician.html'
    success_url = reverse_lazy('homepage')

