from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import routers

from . import views


schema_view = get_schema_view(
    openapi.Info(
        title="CV Builder API",
        default_version='v1',
        description="API for managing CV data",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@cvbuilder.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register('biography', views.BiographyViewSet)
router.register('educations', views.EducationViewSet)
router.register('certificates', views.CertificateViewSet)
router.register('skills', views.SkillListViewSet)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
urlpatterns += router.urls
