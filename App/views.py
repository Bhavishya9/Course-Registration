from django.shortcuts import render,render_to_response
from django.template import Context,RequestContext
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
from forms import *
from django.contrib.auth.models import Group
# Create your views here.

def homepageview(request):
    template = loader.get_template('homepage.html')
    return HttpResponse(template.render(None))

def testview(request):
    if "adminstrator" in str(request.path):
        url = '/App/admin/'
        return HttpResponseRedirect(url)
    if "studentlogin" in str(request.path):
        url = '/App/studentpage'
        return HttpResponseRedirect(url)
    if "facultylogin" in str(request.path):
        url = '/App/professorpage'
        return HttpResponseRedirect(url)

def adminview(request):
    template=loader.get_template('adminspage.html')
    return HttpResponse(template.render(None))

def studentview(request):
    stu=Student.objects.get(user=request.user)
    cats=Catelogue.objects.filter(branch=stu.dept)
    return render(request, 'app/student_page.html', {'catlist' : cats})

def confirm(request):
    template = loader.get_template('successful.html')
    return HttpResponse(template.render(None))

def addstudent(request,new_user):
    if request.method == "POST":
        studentform = StudentForm(request.POST)
        if studentform.is_valid():
            data=studentform.cleaned_data
            new_user1=User.objects.get(id=new_user)
            new_user1.groups.add(Group.objects.get(name='student'))
            new_student = Student(name=data['name'], pin=data['pin'],dept=data['dept'],section=data['section'],poll=False,
                                  user=new_user1)
            new_student.save()
            return HttpResponseRedirect('/App/successful/')
    else:
        studentform = StudentForm()
    return render(request, 'app/addstudent.html', {'form': studentform})

def addprofessor(request,new_user):
    if request.method == "POST":
        facultyform = FacultyForm(request.POST)
        if facultyform.is_valid():
            data=facultyform.cleaned_data
            new_user1=User.objects.get(id=new_user)
            new_user1.groups.add(Group.objects.get(name='professor'))
            new_faculty = Faculty(name=data['name'], pin=data['pin'],dept=data['dept'],user=new_user1)
            new_faculty.save()
            return HttpResponseRedirect('/App/successful/')
    else:
        facultyform = FacultyForm()
    return render(request, 'app/addprofessor.html', {'form': facultyform})


def adduser(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            id=new_user.id
            if "Student" in str(request.path):
                s='/App/addstudent/'+str(id)
                return HttpResponseRedirect(s)
            elif "Professor" in str(request.path):
                s = '/App/addprofessor/' + str(id)
                return HttpResponseRedirect(s)
    else:
        form = UserForm()
    return render(request, 'adduser.html', {'form': form})

def newCat(request):
        catform = CatelogueForm()
        if request.method == 'POST':
            catform = CatelogueForm(request.POST or None)
            if catform.is_valid():
                data = catform.cleaned_data
                cat = Catelogue(name=data['name'], branch=data['branch'], created_date=data['created_date'])
                cat.save()
                return HttpResponseRedirect('/App/catelogue/' + str(cat.id) + '/')
        return render(request, 'app/catelogue_form.html', {'form': catform})


def courseCreate(request, pk):
    courseform = CourseForm()
    if request.method == "POST":
        courseform = CourseForm(request.POST)
        if courseform.is_valid():
            data = courseform.cleaned_data
            new_course = Course(name=data['name'], code=data['code'], category=data['category'],
                                credits=data['credits'],
                                cat=Catelogue.objects.get(id=pk))
            new_course.save()
            if 'save' in request.POST:
                return HttpResponseRedirect('/App/catelogue/' + str(pk) + '/')
            else:
                return HttpResponseRedirect('/App/catelogue/course/'+str(pk)+'/new/')
    return render(request, 'app/course_form.html', {'form': courseform})

def add_vote(request,pk):
    catelogue=Catelogue.objects.get(id=pk)
    course=Course.objects.filter(cat=pk)
    if request.method=='POST':
        vote=request.POST.get('course')
        if Choice.objects.filter(catelogue_id=pk,user=request.user).exists():
            return HttpResponseRedirect('/App/catelogue/oops/')
        else:
            c=Course.objects.get(id=vote)
            v=Choice(catelogue=catelogue,course=c,user=request.user)
            v.save()
            return HttpResponseRedirect('/App/catelogue/votesuccesful/')
    return render_to_response('app/student_view_of_catelogue.html',{'course':course,'cat':catelogue},context_instance=RequestContext(request))

def success(request):
    template = loader.get_template('app/vote_successful.html')
    return HttpResponse(template.render(None))

def oops(request):
    return HttpResponse("You already voted honey!")