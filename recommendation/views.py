from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.http import HttpResponse

from .utils import render_to_pdf
from recommendation.forms import RecommendationForm
from recommendation.models import Recommendation


def index(request):
    if request.method == "POST":
        form = RecommendationForm(request.POST)
        if form.is_valid():
            Recommendation.objects.create(**form.cleaned_data)
            return redirect("recommendation")
    else:
        form = RecommendationForm()

    context = {
        "form": form
    }

    return render(request, template_name="recommendation/index.html", context=context)


def show_recommendation(request):
    patient = Recommendation.objects.order_by("-pk")[0]
    context = {
        "patient": patient
    }
    # Recommendation.objects.all().delete()
    return render(request, "recommendation/show_recommendation.html", context)

#
# def get(request, *args, **kwargs):
#     template = get_template('recommendation/show_recommendation.html')
#     patient = Recommendation.objects.order_by("-pk")[0]
#     context = {
#         "patient": patient
#     }
#     html = template.render(context)
#     pdf = render_to_pdf('recommendation/show_recommendation.html', context)
#     if pdf:
#         response = HttpResponse(pdf, content_type='application/pdf')
#         filename = f"recommendation_{patient.patient_name}.pdf"
#         content = f"inline; filename='{filename}'"
#         download = request.GET.get("download")
#         if download:
#             content = f"attachment; filename='{filename}'"
#         response['Content-Disposition'] = content
#         return response
#     return HttpResponse("Not found")
