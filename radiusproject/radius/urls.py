from django.urls import path, include
from django.conf.urls import url
from django.views.generic import RedirectView
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.signin, name='signin'),
    path('maps/', views.default_map, name='maps'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', RedirectView.as_view(url='accounts/login/', permanent=True)),
    path('login', RedirectView.as_view(url='accounts/login/', permanent=True)),
    path('signup/', views.Signup.as_view()),
    path('signup', views.Signup.as_view()),
    path('create', views.create_activity),
    path('activity', views.activity),
    path('favourites', views.Favourites.as_view(), name='favourites'),
    path('history', views.history),
    path('about', views.about),
    path('activities/', views.ActivityListView.as_view(), name='activities'),
    path('activities/<str:pk>', views.ActivityDetailView.as_view(), name='activity-detail'),
    path('activity/create', views.create_activity, name='activity-creation'),
    path('longlat', views.longlat, name='longlattest'),
    path('avatar', views.avatar, name='avatar')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
