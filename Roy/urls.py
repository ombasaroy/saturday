from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("my_app.urls")),
    path('second/', include("second_app.urls"))
]
