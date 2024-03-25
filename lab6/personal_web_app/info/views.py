from django.shortcuts import render, redirect
from .models import DataInfo
from .forms import DataInfoForm
from django.views.generic import UpdateView, DeleteView


def info_index(request):
    receipt = DataInfo.objects.all().order_by('-date')
    return render(request, 'info/info.html', {'receipt': receipt})


def info_sort_price_index(request):
    receipt = DataInfo.objects.all().order_by('price')
    return render(request, 'info/info_sort_price.html', {'receipt': receipt})


def info_sort_name_index(request):
    receipt = DataInfo.objects.all()
    return render(request, 'info/info_sort_product_name.html', {'receipt': receipt})


def create_receipt(request):
    error = ''
    if request.method == 'POST':
        form = DataInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/info')

        else:
            error = 'Check the data for correct input'

    form = DataInfoForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'info/create.html', data)


class InfoUpdateView(UpdateView):
    model = DataInfo
    template_name = 'info/update.html'
    form_class = DataInfoForm


class InfoDeleteView(DeleteView):
    model = DataInfo
    success_url = '/info'
    template_name = 'info/delete.html'


