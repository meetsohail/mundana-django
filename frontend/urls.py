from django.urls import path
from frontend import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="home"),
    path('category', views.category, name="category"),
    path('post', views.post, name="post"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
