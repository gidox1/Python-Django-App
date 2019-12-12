from django.urls import path, include
from rest_framework.routers import DefaultRouter 
from test_rest_api_app import views


router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet),
router.register('feed', views.UserProfileFeedViewSet)

urlpatterns = [
    path('hello-view', views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls))##retrieves all urls registered to the router.
]