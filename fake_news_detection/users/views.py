from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from .forms import NewsForm
from django.contrib.auth.decorators import login_required
from .models import FakeNews
import pandas as pd
# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def news(request):
    form = NewsForm(request.POST)
    if form.is_valid():
        form.save()
        form = NewsForm()
        user_fake_news = {}
        fake_news = []
        fake_news_objects = FakeNews.objects.all()
        for i in fake_news_objects:
            fake_news.append(i.news)
        label = ['False'] * len(fake_news)
        user_fake_news['news'] = fake_news
        user_fake_news['label'] = label
        fake_news_df = pd.DataFrame.from_dict(user_fake_news)
        fake_news_df.to_csv('static/user_fake_news.csv')
    return render(request, 'news.html', {'form':form})
    
