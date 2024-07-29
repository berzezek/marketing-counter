from django.urls import path

from counter.api.views import marketing_counter_list, marketing_counter_create


urlpatterns = [
    path('marketing-counters/', marketing_counter_list),
    path('marketing-counter-create/', marketing_counter_create),
]