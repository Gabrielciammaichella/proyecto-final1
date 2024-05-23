from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from mysite.blog import views as blog_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog_views.post_list, name='post_list'),  # Ruta para la lista de posts
    path('post/<int:pk>/', blog_views.post_detail, name='post_detail'),  # Ruta para detalles de post
    path('post/new/', blog_views.post_new, name='post_new'),  # Ruta para crear nuevo post
    path('post/<int:pk>/edit/', blog_views.post_edit, name='post_edit'),  # Ruta para editar post existente
    path('post/<int:pk>/delete/', blog_views.post_delete, name='post_delete'),  # Ruta para eliminar post
    path('about/', blog_views.about, name='about'),  # Ruta para la página "about"
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),  # Ruta para iniciar sesión
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),  # Ruta para cerrar sesión
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
