from django.shortcuts import render
from .models import Subscriber
from .forms import SubscribePostForm

def subscriber_form(request):
    subscribed = False
    if request.method == 'POST':
        form = SubscribePostForm(request.POST)
        if form.is_valid():            
            human = True
            new_subscriber = form.save(commit=False)
            new_subscriber.save()

            # form.save()
            subscribed = True
    else:
        form = SubscribePostForm()
    context = {'form':form, 'subscribed':subscribed}
    return render(request, 'emailmarketing/subscribe.html', context)



