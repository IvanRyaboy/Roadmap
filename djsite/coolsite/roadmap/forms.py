from django import forms
from .models import *


class ChooseLearningLevel(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["skill_level"].empty_label = "Не выбрано"

    class Meta:
        model = Skill
        fields = ["skill_level"]

class MarkAsDone(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields[""]
