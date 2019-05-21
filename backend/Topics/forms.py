from django import forms

from Topics.models import Topic


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ('name', 'description')
