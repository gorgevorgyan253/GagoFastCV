from django.shortcuts import render , redirect 

# Create your views here.

from .models import Resume, Skill, Experience, Education, Language, Certification
from django.core.files.storage import FileSystemStorage

def resume_step_1(request):
    if request.method == 'POST':
        # Save personal info in session
        request.session['first_name'] = request.POST.get('first_name')
        request.session['last_name'] = request.POST.get('last_name')
        request.session['phone_number'] = request.POST.get('phone_number')
        request.session['email'] = request.POST.get('email')
        request.session['address'] = request.POST.get('address')
        request.session['linkedin'] = request.POST.get('linkedin')
        request.session['website'] = request.POST.get('website')
        return redirect('resume_step_2')
    return render(request, 'resume_step_1.html')

def resume_step_2(request):
    if request.method == 'POST' and request.FILES.get('photo'):
        # Save photo in session
        photo = request.FILES.get('photo')
        fs = FileSystemStorage()
        filename = fs.save(photo.name, photo)
        request.session['photo'] = filename
        return redirect('resume_step_3')
    return render(request, 'resume_step_2.html')

def resume_step_3(request):
    if request.method == 'POST':
        # Save skills in session
        skills = request.POST.getlist('skills')
        request.session['skills'] = skills
        return redirect('resume_step_4')
    return render(request, 'resume_step_3.html')

def resume_step_4(request):
    if request.method == 'POST':
        # Save work experience in session
        job_title = request.POST.get('job_title')
        company_name = request.POST.get('company_name')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        description = request.POST.get('description')
        request.session['experience'] = {
            'job_title': job_title,
            'company_name': company_name,
            'start_date': start_date,
            'end_date': end_date,
            'description': description
        }
        return redirect('resume_step_5')
    return render(request, 'resume_step_4.html')

def resume_step_5(request):
    if request.method == 'POST':
        # Save education info in session
        degree = request.POST.get('degree')
        school_name = request.POST.get('school_name')
        graduation_year = request.POST.get('graduation_year')
        major = request.POST.get('major')
        gpa = request.POST.get('gpa')
        request.session['education'] = {
            'degree': degree,
            'school_name': school_name,
            'graduation_year': graduation_year,
            'major': major,
            'gpa': gpa
        }
        return redirect('resume_step_6')
    return render(request, 'resume_step_5.html')

def resume_step_6(request):
    if request.method == 'POST':
        # Save language info in session
        language_name = request.POST.get('language_name')
        proficiency = request.POST.get('proficiency')
        request.session['languages'] = {
            'language_name': language_name,
            'proficiency': proficiency
        }
        return redirect('resume_step_7')
    return render(request, 'resume_step_6.html')

def resume_step_7(request):
    if request.method == 'POST':
        # Save certifications info in session
        cert_name = request.POST.get('cert_name')
        issuing_org = request.POST.get('issuing_org')
        date_obtained = request.POST.get('date_obtained')
        expiry_date = request.POST.get('expiry_date')
        request.session['certifications'] = {
            'cert_name': cert_name,
            'issuing_org': issuing_org,
            'date_obtained': date_obtained,
            'expiry_date': expiry_date
        }
        return redirect('resume_review')
    return render(request, 'resume_step_7.html')

def resume_review(request):
    if request.method == 'POST':
        # Retrieve all session data
        resume = Resume(
            first_name=request.session.get('first_name'),
            last_name=request.session.get('last_name'),
            phone_number=request.session.get('phone_number'),
            email=request.session.get('email'),
            address=request.session.get('address'),
            linkedin=request.session.get('linkedin'),
            website=request.session.get('website'),
            photo=request.session.get('photo')
        )
        resume.save()

        # Save other details (skills, experience, education, etc.)
        for skill in request.session.get('skills', []):
            Skill.objects.create(resume=resume, name=skill)
        
        exp = request.session.get('experience', {})
        Experience.objects.create(
            resume=resume,
            job_title=exp.get('job_title'),
            company_name=exp.get('company_name'),
            start_date=exp.get('start_date'),
            end_date=exp.get('end_date'),
            description=exp.get('description')
        )
        
        edu = request.session.get('education', {})
        Education.objects.create(
            resume=resume,
            degree=edu.get('degree'),
            school_name=edu.get('school_name'),
            graduation_year=edu.get('graduation_year'),
            major=edu.get('major'),
            gpa=edu.get('gpa')
        )
        
        lang = request.session.get('languages', {})
        Language.objects.create(
            resume=resume,
            name=lang.get('language_name'),
            proficiency=lang.get('proficiency')
        )
        
        cert = request.session.get('certifications', {})
        Certification.objects.create(
            resume=resume,
            name=cert.get('cert_name'),
            issuing_organization=cert.get('issuing_org'),
            date_obtained=cert.get('date_obtained'),
            expiry_date=cert.get('expiry_date')
        )

        # Clear session data
        request.session.flush()

        return redirect('resume_success')

    return render(request, 'resume_review.html')

def resume_success(request):
    return render(request, 'resume_success.html')