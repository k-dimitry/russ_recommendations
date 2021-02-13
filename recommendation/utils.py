# from io import BytesIO
# from django.http import HttpResponse
# from django.template.loader import get_template
#
# from xhtml2pdf import pisa
#
#
# def render_to_pdf(template_src, context_dict={}):
#     template = get_template(template_src)
#     html = template.render(context_dict)
#     result = BytesIO()
#     pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
#     if not pdf.err:
#         return HttpResponse(result.getvalue(), content_type='application/pdf')
#     return None
#
# # outputFilename = "test.pdf"
# #
# #
# # def render_to_pdf(template_src, context_dict):
# #     pisa.showLogging()
# #     template = get_template(template_src)
# #     html = template.render(context_dict)
# #     with open(outputFilename, "w+b") as resultFile:
# #         pisa_status = pisa.CreatePDF(html, dest=resultFile, encoding='UTF-8')
# #     return pisa_status.error("oops")
