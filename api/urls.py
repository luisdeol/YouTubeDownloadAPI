from django.conf.urls import url

urlpatterns = [
    url(r'^download_videos', 'api.views.download_videos')
]