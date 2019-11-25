from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('verify-mobile-number/', views.login, name='blog-login'),
    path('login/', views.login_form, name='blog-login_form'),
    path('forgetpass/', views.forgetpass, name='blog-forgetpass'),
    path('validateOTP/', views.validateOTP, name='blog-validateOTP'),
    path('sentotp/', views.sentotp, name='blog-sentotp'),
    path('newpassword/', views.newpassword, name='blog-newpassword'),
    path('resetpass/', views.resetpass, name='blog-resetpass'),
    path('signup/', views.register_form, name='blog-register_form'),
    path('registration/', views.registration, name='blog-registration'),
    path('verify_mobile_number/', views.verify_mobile_number, name='blog-verify_mobile_number'),
    path('minifacebook/', views.user_post, name='blog-user_post'),
    path('Share/', views.Share, name='blog-Share'),
    path('Save_notes/', views.Save_notes, name='blog-Save_notes'),
    path('Delete_notes/', views.Delete_notes, name='blog-Delete_notes'),
    # path('Logout', views.Logout, name='blog-Logout'),
    path('searchresults/', views.SearchUser, name='blog-SearchUser'),
    path('create/', views.create_session),
    path('access/', views.access_session),
    path('logout/', views.delete_session, name='blog-delete'),
    path('profile/<str:name>/<int:id>/', views.userprofile, name='blog-userprofile'),
    path('upadteprofile/', views.upadateprofile, name='blog-upadteprofile'),
    path('con_request/', views.con_request, name='blog-con_request'),
    path('conrequiestList/', views.conrequiestList, name='blog-conrequiestList'),
    path('friendlist/<int:id>/', views.friendlist, name='blog-friendlist'),
    path('comment_save/', views.comment_save, name='blog-comment_save'),
    path('like_post/', views.like_post, name='blog-like_post'),
    path('accept_reject_request/', views.accept_reject_request,
         name='blog-accept_reject_request'),
    path('likedby/', views.likedby, name='blog-likedby'),
    path('commentsby/', views.commentsby, name='blog-commentsby'),
    path('unfriend/', views.unfriend, name='blog-unfriend'),
    path('accept_reject/', views.accept_reject, name='blog-accept_reject'),
    path('cancel_req/', views.cancel_req, name='blog-cancel_req'),


]
