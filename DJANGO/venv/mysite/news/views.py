from django.shortcuts import render, redirect
from .models import Articles # импортируме для вывода данных из таблицы
from .forms import ArticlesForm # импортируем для ввода данных в таблицу
from django.views.generic import DetailView, UpdateView, DeleteView # динамические страницы



def news_home(request):
    news = Articles.objects.order_by('-date')[:3] # получаем последние 3 записи из таблицы артиклс
    # сортируем по уменьшающей по дате, 
    # рендерим их ниже
    return render(request, 'news/news_home.html', {'news': news})

class NewsDetailView(DetailView):
    model = Articles 
    template_name = 'news/details_view.html'
    context_object_name = 'article'

class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'
    form_class = ArticlesForm

class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news/'
    template_name = 'news/news_delete.html'

def create(request):
    error = ""
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = "Проверьте данные"

    form = ArticlesForm()
    data = {'form' : form, 'error': error}
    return render( request, 'news/create.html', data)