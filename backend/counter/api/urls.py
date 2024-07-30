from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from counter.api.views import marketing_counter_list, marketing_counter_create

schema_view = get_schema_view(
    openapi.Info(
        title="Marketing counter API",
        default_version="v1",
        description="This app is counting of marketing activities",
        contact=openapi.Contact(email="nfakhritdinov@fortebank.com"),
    ),
    public=True,
)


urlpatterns = [
    path(
        "swagger<format>/", schema_view.without_ui(cache_timeout=0), name="schema-json"
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("marketing-counters/", marketing_counter_list),
    path("marketing-counter-create/", marketing_counter_create),
]
