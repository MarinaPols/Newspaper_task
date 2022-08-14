from django import forms
from .models import Post, CategorySubscribers, PostCategory
from django.core.exceptions import ValidationError



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            #'author',
            'postCategory',
            'title',
            'text',
        ]

    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get("text")
        if text is not None and len(text) < 20:
            raise ValidationError({
                "text": "Описание не может быть менее 20 символов."
            })

        title = cleaned_data.get("title")
        if title == text:
            raise ValidationError(
                "Название не должно совпадать с основным текстом."
            )

        return cleaned_data


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = CategorySubscribers
        fields = ['category']