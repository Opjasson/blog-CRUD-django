from django import forms
from .models import PostModel



class CreateForms(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = [
            'judul',
            'body',
            'category',
        ]
        
        widgets = {
            "judul": forms.TextInput(
                attrs= {
                    "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 ",
                    "placeholder": "Post title"
                }
            ),
            
            "body": forms.Textarea(
                attrs= {
                    "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 ",
                    "placeholder": "Masukan isi"
                }
            ),
            
            "category": forms.TextInput(
                attrs= {
                    "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 ",
                    "placeholder": "Masukan Category"
                }
            ),
        }