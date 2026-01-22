# missions/forms.py
from django import forms
from .models import Mission


class MissionForm(forms.ModelForm):
    class Meta:
        model = Mission
        fields = [
            "title",
            "description",
            "xp_reward",
            "tecnica_pontuacao",
            "disciplina_pontuacao",
            "criatividade_pontuacao",
            "lideranca_pontuacao",
        ]
