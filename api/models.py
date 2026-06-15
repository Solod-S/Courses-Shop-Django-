from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from shop.models import Category, Course
from .authentication import CustomAuthentication

# Create your resources here.


class CategoryResource(ModelResource):
    # /api/v1/categories
    # /api/v1/categories/?limit=1&offset=1
    class Meta:
        queryset = Category.objects.all()
        resource_name = "categories"
        allowed_methods = ["get"]


class CourseResource(ModelResource):
    # /api/v1/courses
    # /api/v1/courses/?limit=1&offset=1

    class Meta:
        queryset = Course.objects.all()
        resource_name = "courses"
        allowed_methods = ["get", "post", "delete"]
        authentication = CustomAuthentication()
        authorization = Authorization()
