from django.urls import path
# from watchlist_app.api.views import movie_list,movie_details
from watchlist_app.api.views import WatchListAV,WatchDetailAV,StreamPlatformListAV,StreamPlatformDetailAV

urlpatterns = [
    path('list/',WatchListAV.as_view()),
    path('<int:pk>',WatchDetailAV.as_view()),
    path('stream/',StreamPlatformListAV.as_view()),
    path('stream/<int:pk>',WatchDetailAV.as_view()),
]