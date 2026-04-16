from django import forms
from . import models


class CreatePost(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ["title", "body", "slug", "banner"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        base_input_class = (
            "w-full px-4 py-2 border border-gray-300 rounded-lg "
            "focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
        )

        textarea_class = (
            "w-full px-4 py-2 border border-gray-300 rounded-lg "
            "h-40 resize-none focus:outline-none focus:ring-2 focus:ring-blue-500"
        )

        file_class = (
            "w-full text-sm text-gray-600 file:mr-4 file:py-2 file:px-4 "
            "file:rounded-lg file:border-0 file:bg-blue-50 file:text-blue-700"
        )

        for name, field in self.fields.items():

            if name == "body":
                field.widget.attrs.update({"class": textarea_class})

            elif name == "banner":
                field.widget.attrs.update({"class": file_class})

            else:
                field.widget.attrs.update({"class": base_input_class})
