from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('upload/', views.upload_file, name='upload'),
    path('preview/', views.data_preview, name='preview'),
    path("ai-insights/", views.ai_insights, name="ai_insights"),
    path('forecast/', views.forecast, name='forecast'),
    path("reports/", views.reports, name="reports"),
    path("download-report/", views.download_report, name="download_report"),
    path("datasets/",views.dataset_list,name="datasets"),
    path("datasets/use/<int:dataset_id>/",views.use_dataset,name="use_dataset",),
    path("datasets/delete/<int:dataset_id>/",views.delete_dataset,name="delete_dataset",),
    path("chat/",views.chatbot,name="chatbot"),
    path("chat/clear/", views.clear_chat, name="clear_chat"),
]