from django.shortcuts import render,redirect
from .forms import ItemForm
from .models import Item


# Create your views here.
def home(request):
	return render(request, 'home.html', {})

def item_list(request):
	context = {'item_list': Item.objects.all()}
	return render(request, 'item_list.html',context)

def item_form(request, id=0):
	if request.method == "GET":
		if id==0:
			form = ItemForm()
		else:
			item = Item.objects.get(pk=id)
			form = ItemForm(instance=item)
		return render(request, 'item_form.html', {'form':form})
	else:
		if id == 0:
			form = ItemForm(request.POST)
		else:
			item = Item.objects.get(pk=id)
			form = ItemForm(request.POST,instance=item)
		if form.is_valid():
			form.save()
		return redirect('/list')

def item_delete(request,id):
	item = Item.objects.get(pk=id)
	item_delete()
	return redirect('/list')


