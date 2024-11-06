from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.routers import SimpleRouter
from django.urls import path, include, re_path
from .views import AttributeViewSet, HeroViewSet, RoleViewSet, HeroRolesViewSet, AspectsViewSet, \
    SkillsViewSet, NewsViewSet, HeroListView, GetCurrentHero, GetCurrentHeroSkills

router = SimpleRouter()
router.register(r'attributes', AttributeViewSet, basename='attribute')
router.register(r'heroes', HeroViewSet, basename='hero')
router.register(r'roles', RoleViewSet, basename='role')
router.register(r'hero-roles', HeroRolesViewSet, basename='hero-role')
router.register(r'aspects', AspectsViewSet, basename='aspect')
router.register(r'skills', SkillsViewSet, basename='skill')
router.register(r'news', NewsViewSet, basename='news')

schema_view = get_schema_view(
    openapi.Info(
        title="Ruslan Fans",
        default_version="v1",
        description="Ruslan Fans API",
    ),
    public=True,
    permission_classes=([permissions.AllowAny]),
)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),

    path("", include(router.urls)),

    re_path(r'^auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('heroes-list/', HeroListView.as_view()),
    path('hero/<str:name>/', GetCurrentHero.as_view()),
    path('hero-skill/<int:id>/', GetCurrentHeroSkills.as_view())
]
