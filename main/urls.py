from django.urls import path, include
from main.views import show_main, create_mood_entry, show_xml, show_json, register, login_user, logout_user, edit_mood, delete_mood, create_mood_entry_ajax

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-mood-entry', create_mood_entry, name='create_mood_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-mood/<uuid:id>', edit_mood, name='edit_mood'),
    path('delete/<uuid:id>', delete_mood, name='delete_mood'),
    path('create-ajax/', create_mood_entry_ajax, name='create_mood_entry_ajax'),
    path('news/', include('news.urls', namespace='news')),
]