from typing import Any, List
from ninja_simple_jwt.auth.views.api import mobile_auth_router
from ninja import NinjaAPI
from .models import User, CourseMember, CourseContent, Comment, Course
from ninja.pagination import paginate, PaginationBase
from ninja import Schema
from ninja import ModelSchema
from django.contrib.auth.models import User

apiv2 = NinjaAPI(version="2.0.0")
apiv2.add_router("/auth/", mobile_auth_router)
apiAuth = mobile_auth_router.auth

class UserSchema(ModelSchema):
    class Meta:
        model = User
        fields = ["id", "username", "email"]

class CourseMemberSchema(Schema):
    id: int
    user_id: int
    course_id: int
    roles: str

class CommentCreateSchema(Schema):
    content_id: int
    comment: str

class CustomPagination(PaginationBase):
    class Input(Schema):
        skip: int

    class Output(Schema):
        items: List[Any]
        total: int
        per_page: int

    def paginate_queryset(self, queryset, pagination: Input, **params):
        skip = pagination.skip
        return {
            'items': queryset[skip : skip + 5],
            'total': queryset.count(),
            'per_page': 5,
        }

@apiv2.get("/users", response=List[UserSchema])
@paginate(CustomPagination, page_size=50)
def users(request):
    return User.objects.all()

@apiv2.get("mycourses/", auth=apiAuth, response=List[CourseMemberSchema])
def mycourses(request):
    queryset = CourseMember.objects.filter(user_id=request.user)\
                                    .select_related('user_id', 'course_id') 
    return [
        CourseMemberSchema(
            id=m.id,
            user_id=m.user_id.id, 
            course_id=m.course_id.id,
            roles=m.roles,
        ) for m in queryset
    ]

@apiv2.post('course/{id}/enroll/', auth=apiAuth, response=CourseMemberSchema)
def courseEnrollment(request, id:int):
    user = request.user
    course = Course.objects.get(pk=id)

    enrollment = CourseMember.objects.create(
        user_id=user,
        course_id=course,
        roles="std"
    )

    return CourseMemberSchema(
        id=enrollment.id,
        user_id=enrollment.user_id.id,
        course_id=enrollment.course_id.id,
        roles=enrollment.roles
    )

@apiv2.post('comments/', auth=apiAuth)
def postComment(request, data: CommentCreateSchema):
    user = request.user
    content_id = CourseContent.objects.get(id=data.content_id)
    coursemember = CourseMember.objects.filter(user_id=user, course_id=content_id.course_id).first()

    if coursemember:
        Comment.objects.create(comment=data.comment, member_id=coursemember, content_id=content_id)
        return "berhasil"
    else:
        return apiv2.create_response(request, {"error": "Tidak boleh komentar di sini"}, status=403)