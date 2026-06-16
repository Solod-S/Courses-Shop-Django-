from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from shop.models import Category, Course
from .authentication import CustomAuthentication

# Create your resources here.


class CategoryResource(ModelResource):
    # /api/v1/categories                    GET
    # /api/v1/categories/?limit=1&offset=1  GET

    class Meta:
        queryset = Category.objects.all()
        resource_name = "categories"
        allowed_methods = ["get"]


class CourseResource(ModelResource):
    # /api/v1/courses                    GET, POST
    # /api/v1/courses/?limit=1&offset=1  GET,
    # /api/v1/courses/1/                 GET, DELETE

    class Meta:
        queryset = Course.objects.all()
        resource_name = "courses"
        allowed_methods = ["get", "post", "delete"]
        excludes = ["created_at"]
        authentication = CustomAuthentication()
        authorization = Authorization()

# hydrate - данные идут к серверу
# dehydrate - данные идут к клиенту

# для нормального приема category_id из body
    def hydrate(self, bundle):
        bundle.obj.category_id = bundle.data["category_id"]
        return bundle

# добавляем category_id и category  в тело ответа
    def dehydrate(self, bundle):
        bundle.data["category_id"] = bundle.obj.category_id
        bundle.data["category"] = bundle.obj.category
        return bundle

# добавляем все заголовки большими в тело ответа
    def dehydrate_title(self, bundle):
        return bundle.data["title"].upper()

# делаем все reviews_qty строками в тело ответа
    def dehydrate_reviews_qty(self, bundle):
        return str(bundle.data["reviews_qty"])
