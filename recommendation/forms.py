from django import forms


class RecommendationForm(forms.Form):
    patient_name = forms.CharField(max_length=150, label="ФИО ", widget=forms.TextInput(attrs={
        "class": "form-control",
        "autocomplete": "off",
    }))
    patient_dob = forms.CharField(max_length=100, label="Дата рождения ", widget=forms.TextInput(attrs={
        "class": "form-control",
        "autocomplete": "off",
    }))
    diagnoses = forms.CharField(max_length=500, required=False, label="Диагнозы ", widget=forms.TextInput(attrs={
        "class": "form-control",
        "autocomplete": "off",
    }))
    recommendations = forms.CharField(label="Рекомендации ", widget=forms.Textarea(attrs={
        "class": "form-control",
        "rows": 5,
    }))
    diet = forms.CharField(required=False, label="Диета ", widget=forms.Textarea(attrs={
        "class": "form-control",
        "rows": 5,
    }))
