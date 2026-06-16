from api.models import CategoryResource, CourseResource
from tastypie.api import Api
from django.urls import path, include

# For POST, DELETE add header
# Key: Authorization
# Value: ApiKey bogdan:asdh1kl2513413561

api = Api(api_name="v1")
api.register(CourseResource())
api.register(CategoryResource())


urlpatterns = [
    path('', include(api.urls), name="index"),
]
