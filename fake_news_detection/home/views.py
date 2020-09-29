from django.shortcuts import render
import pickle
from nltk import word_tokenize
from .forms import FactsForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    form = FactsForm(request.POST)
    result = ['']
    if form.is_valid():
        data = request.POST.copy()

        text = pickle.load(open('static/classification_model.sav','rb'))
        result = text.predict([data.get('fact')])
        #form.save()
        #form = FactsForm()
        #print("The given statement is ", result)
        #}
    return render(request, 'home.html', {'form':form ,'result': result[0] })

