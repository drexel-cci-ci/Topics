import json

from django.core import serializers
from django.forms import model_to_dict
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from Topics.forms import TopicForm
from Topics.models import Topic


@csrf_exempt
@require_http_methods(["GET", "POST"])
def topics(request):
    if (request.method == "GET"):
        data = Topic.objects.all()
        response = serializers.serialize("json", data)
        return HttpResponse(response, content_type='application/json')
    else:
        form = TopicForm(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect(reverse('topics'))
        else:
            return HttpResponseBadRequest(str(form.errors))


@csrf_exempt
@require_http_methods(["GET", "POST"])
def topics_detail(request, topic_id):
    topic = get_object_or_404(Topic, name=topic_id)
    if (request.method == "GET"):
        return HttpResponse(json.dumps(model_to_dict(topic)), content_type='application/json')
    else:
        form = TopicForm(request.POST or None, instance=topic)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('topic_detail', args=[topic.name]))
        else:
            return HttpResponseBadRequest(str(form.errors))
