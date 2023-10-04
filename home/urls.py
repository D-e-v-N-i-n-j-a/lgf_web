from django.urls import path
from .views.home_view import home,home_details
from .views.about_views import aboutUs
from .views.donate_views import donate
from .views.blog_views import blog_details,blogs
from .views.partner_views import partnerForm,partnership
from .views.fun_raising_views import funRaising
from .views.volunteer import volunteer
from .views.library_views import community_library
from .views.book_talk_views import bookTalk




app_name = 'home'
urlpatterns = [
    path('',home,name='home'),
    # path('work/<int:id>/', home_details, name='work_details'),
    path('about',aboutUs,name='about'),
    path('donate',donate,name='donate'),
    path('blog',blogs,name='blog'),
    # path('partnership',partnership,name='partnership'),
    # path('partnerForm',partnerForm,name='partnerForm'),
    path('blog/<int:blog_id>/', blog_details, name='blog-details'),
    path('volunteer',volunteer,name="volunteer"),
    # path('funRaising',funRaising,name='fun_raising'),
    # path('community_library',community_library,name='community_library'),
    # path('book_talk',bookTalk,name='book_talk')
]

 




