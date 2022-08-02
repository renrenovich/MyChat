from django.urls import path


from User.views import ListUsersView, CreateUserView

urlpatterns = [
    path('user/all/', ListUsersView.as_view()),
    path('user/signup/', CreateUserView.as_view()),
    path('user/login/', CreateUserView.as_view()),

]
