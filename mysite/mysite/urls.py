
from django.contrib import admin
from django.urls import include,path

urlpatterns = [
    path('myapp/', include("myapp.urls")),
    path("myapp_templates/", include("myapp_templates.urls")),
    path("myapp_templates2/", include("myapp_templates2.urls")),
    path("myapp_testmodel/", include("myapp_testmodel.urls"))
]
