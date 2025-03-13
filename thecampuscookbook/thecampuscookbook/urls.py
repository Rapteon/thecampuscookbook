"""
URL configuration for thecampuscookbook project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from home.views import index as home_index
from login.views import index as login_index
from register.views import index as register_index
from category.urls import urlpatterns as category_urls
from account.urls import urlpatterns as account_urls
from django.conf.urls.static import static
from thecampuscookbook import settings


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_index, name="home"),
    path("login/", login_index, name="login"),
    path("register/", register_index, name="register"),
    path("category/", include(category_urls), name="category"),
    path("profile/", include(account_urls), name="account"),  # profile = account
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)