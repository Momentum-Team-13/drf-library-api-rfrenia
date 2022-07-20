"""django_library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from library import views as library_views
import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", library_views.BookListView.as_view(), name="homepage"),
    # path("books", library_views.book_list, name="book_list"),
    # path("books/<int:pk>", library_views.book_detail, name="book_detail"),
    # path("books/new", library_views.add_book, name="add_book"),
    path("accounts/", include("registration.backends.simple.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path("books", library_views.BookListCreateView.as_view(), name="book_list"),
    path("books/<int:pk>", library_views.BookDetailView.as_view(), name="book_detail"),
    path("books/<int:pk>/tracker", library_views.BookTrackerView.as_view(), name="add_tracker"),
]

if settings.DEBUG:
    urlpatterns.append(path(r'__debug__/', include(debug_toolbar.urls)))
