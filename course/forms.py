from django import forms

# from ckeditor.widgets import CKEditorWidget                   # 일반적 처리가능
from ckeditor_uploader.widgets import CKEditorUploadingWidget  # image 포함 처리가능

from .models import Course

class CourseForm(forms.ModelForm):

    # content = forms.CharField(widget=CKEditorWidget())
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Course
        fields = ('subject', 'content', )
        # fields = '__all__'

