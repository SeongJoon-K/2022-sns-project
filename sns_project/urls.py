from django.contrib import admin
from django.urls import path, include
from main import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "main"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.showmain, name="showmain"),
    path('intro/', views.intro, name="intro"),
    path('<int:id>', views.detail, name="detail"),
    path('new', views.new, name="new"),
    path('create', views.create, name="create"),
    path('edit/<str:id>', views.edit, name="edit"),
    path('update/<str:id>', views.update, name="update"),
    path('delete/<str:id', views.delete, name="delete"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
