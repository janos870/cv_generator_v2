from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserProfileForm
from .models import UserProfile
from django.template.loader import get_template
from xhtml2pdf import pisa
import base64


def create(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user_profile = form.save()
            return redirect('preview', user_id=user_profile.id)
    else:
        form = UserProfileForm()

    return render(request, 'cv_app/create.html', {'form': form})

def preview(request, user_id):
    user_profile = UserProfile.objects.get(id=user_id)
    return render(request, 'cv_app/preview.html', {'user_profile': user_profile})


def cv_list(request):
    user_profiles = UserProfile.objects.all()
    return render(request, 'cv_app/cv_list.html', {'user_profiles': user_profiles})

#-------------------------------------CONVERT TO PDF-----------------------------------------#

def convert_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def render_to_pdf(template_path, context_dict):
    template: object = get_template(template_path)
    html = template.render(context_dict)

    # Replace image paths with base64 encoded images
    profile_picture_path = context_dict.get('user_profile').profile_picture.path
    profile_picture_base64 = convert_image_to_base64(profile_picture_path)

    html = html.replace('{{ profile_picture.url }}', f'data:image/jpeg;base64,{profile_picture_base64}')
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="profile_preview.pdf"'

    # Create a PDF object and write the HTML content to it
    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse('Error during PDF generation.')

    return response

def convert_to_pdf(request, user_id):
    user_profile = UserProfile.objects.get(id=user_id)
    context = {'user_profile': user_profile}

    # Image conversation base64-be
    profile_picture_path = user_profile.profile_picture.path
    profile_picture_base64 = convert_image_to_base64(profile_picture_path)

    context['user_profile'].profile_picture_base64 = f'data:image/jpeg;base64,{profile_picture_base64}'
    pdf = render_to_pdf('cv_app/pdf.html', context)
    return pdf




