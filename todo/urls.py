from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("api/v1/", include("users.api.v1.urls")),
    path("api/v1/", include("task.api.v1.urls")),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),

]


admin.site.site_header = "ToDo"
admin.site.site_title = "ToDo Admin Portal"
admin.site.index_title = "ToDo Admin"

# swagger
schema_view = get_schema_view(
    openapi.Info(
        title="ToDo API",
        default_version="v1",
        description="API documentation for ToDo App",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns += [
    path("api-docs/", schema_view.with_ui("swagger", cache_timeout=0), name="api_docs")
]

