from django.http import JsonResponse,HttpResponse
from django.contrib.auth.models import User
from django.db.models import Max, Min, Avg, Count
from .models import Course, CourseContent, CourseMember  
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist

def create_test_user(request):
    user = User.objects.create_user(
        username="rizal",
        email="rizalram100@gmail.com",
        password="rizal_2004",
    )
    return JsonResponse({"id": user.id, "username": user.username})

def create_course_from_query(request):
    row = {
        "name": request.GET.get("name", "Nama Default"),
        "description": request.GET.get("description", "-"),
        "price": int(request.GET.get("price", 10000)),
    }

    teacher = User.objects.get(pk=1)
    course = Course.objects.create(
        name=row["name"],
        description=row["description"],
        price=row["price"],
        teacher=teacher,
    )
    return JsonResponse({"id": course.id, "name": course.name})

def allCourse(request):
    allCourse = Course.objects.all()
    result = []
    for course in allCourse:
        record = {
            'id': course.id, 
            'name': course.name,
            'description': course.description,
            'price': course.price,
            'teacher': {
                'id': course.teacher.id,
                'username': course.teacher.username,
                'email': course.teacher.email,
                'fullName': f"{course.teacher.first_name} {course.teacher.last_name}"
            }
        }
        result.append(record)
    return JsonResponse(result, safe=False)

def userCourses(request):
    user = User.objects.get(pk=3)
    courses = Course.objects.filter(teacher=user.id)
    
    course_data = []
    for course in courses:
        record = {
            'id': course.id, 
            'name': course.name,
            'description': course.description, 
            'price': course.price
        }
        course_data.append(record)
        
    result = {
        'id': user.id, 
        'username': user.username, 
        'email': user.email,
        'fullName': f"{user.first_name} {user.last_name}",
        'courses': course_data
    }
    
    return JsonResponse(result, safe=False)

def courseStat(request):
    courses = Course.objects.all()
    stats = courses.aggregate(max_price=Max('price'),
                              min_price=Min('price'),
                              avg_price=Avg('price'))
    
    cheapest = Course.objects.filter(price=stats['min_price'])
    expensive = Course.objects.filter(price=stats['max_price'])
    
    popular = Course.objects.annotate(member_count=Count('coursemember')) \
        .order_by('-member_count')[:5]
        
    unpopular = Course.objects.annotate(member_count=Count('coursemember')) \
        .order_by('member_count')[:5]
    
    result = {
        'course_count': len(courses), 
        'courses': stats,
        'cheapest': serializers.serialize('python', cheapest),
        'expensive': serializers.serialize('python', expensive),
        'popular': serializers.serialize('python', popular),
        'unpopular': serializers.serialize('python', unpopular)
    }
    
    return JsonResponse(result, safe=False)

def courseDetail(request, course_id):
    course = Course.objects.annotate(
        member_count=Count('coursemember'),
        content_count=Count('coursecontent'),
        comment_count=Count('coursecontent__comment')
    ).get(pk=course_id)

    contents = CourseContent.objects.filter(course_id=course.id) \
        .annotate(count_comment=Count('comment')) \
        .order_by('-count_comment')[:3]

    result = {
        'name': course.name,
        'description': course.description,
        'price': course.price,
        'member_count': course.member_count,
        'content_count': course.content_count,
        'teacher': {
            'username': course.teacher.username,
            'email': course.teacher.email,
            'fullname': f"{course.teacher.first_name} {course.teacher.last_name}"
        },
        'comment_stat': {
            'comment_count': course.comment_count,
            'most_comment': [
                {
                    'name': content.name, 
                    'comment_count': content.count_comment
                } 
                for content in contents
            ],
        },
    }
    return JsonResponse(result)

def courseMemberStat(request):
    courses = Course.objects.filter(description__contains='python') \
        .annotate(member_num=Count('coursemember'))
    
    course_data = []
    for course in courses:
        record = {'id': course.id, 'name': course.name, 'price': course.price,
                  'member_count': course.member_num}
        course_data.append(record)
        
    result = {'data_count': len(course_data), 'data': course_data}
    return JsonResponse(result)

def home(request):
    """Menampilkan pesan selamat datang di halaman utama."""
    return HttpResponse("<h1>Selamat Datang di SimpleLMS!</h1><p>Akses /admin/ atau /core/ untuk melihat fitur.</p>")

