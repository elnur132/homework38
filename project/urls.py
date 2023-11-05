
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from app.views import CarCreate, CarList, CarDelete

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", CarList.as_view(), name='list'),
    path("create/", CarCreate.as_view(), name='create'),
    path("delete/<int:car_id>", CarDelete.as_view(), name='delete')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
