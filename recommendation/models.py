from django.db import models


class Recommendation(models.Model):
    date_of_recommendation = models.DateTimeField(auto_now=True, verbose_name="Дата рекомендации", null=True)
    patient_name = models.CharField(max_length=150, verbose_name="ФИО пациента")
    patient_dob = models.CharField(max_length=100, verbose_name="Дата рождения")
    diagnoses = models.CharField(max_length=500, verbose_name="Диагнозы", null=True)
    recommendations = models.TextField(verbose_name="Рекомендации")
    diet = models.TextField(verbose_name="Диета", null=True)

    def __str__(self):
        return f"Рекомендация для {self.patient_name} от {self.date_of_recommendation}"

    class Meta:
        verbose_name = "Рекомендация"
        verbose_name_plural = "Рекомендации"
