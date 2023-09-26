from django.urls import path, include
from rest_framework import routers 


#Vi
#from .views import OwnersViewSet
from .views import ( ListOwnersAPIView,
                    RetrieveOwnersAPIView,
                    CreateOwnersAPIView,
                    UpdateOwnersAPIView, 
                    DeleteOwnersAPIView,
                    OwnersListCreateView,
                    OwnersRetrieveUpdateDestroyAPIView,)
from . import views

# Router

#router = routers.DefaultRouter()
#router.register(r"owners", OwnersViewSet)
#router.register()




# owners/ --> POST
# owners/ --> GET
# owners/id --> GET
# owners/id --> PUT
# owners/id --> DELETE
urlpatterns = [#path("", include(router.urls))
               path('', views.home),
               #path("owners/",ListOwnersAPIView.as_view(), name="owners_list"),
               #path("owners/<int:pk>/", RetrieveOwnersAPIView.as_view(), name="owners_detail"),
               #path("owners/add", CreateOwnersAPIView.as_view(), name="owners_create"),
               #path("owners/<int:pk>/", UpdateOwnersAPIView.as_view(), name="owners_update"),
               #path("owners/<int:pk>/", DeleteOwnersAPIView.as_view(), name="owners_delete"),
               path("owners/",OwnersListCreateView.as_view(),name= "Create_data"),
               path("owners/<int:pk>/",OwnersRetrieveUpdateDestroyAPIView.as_view(), name = "Retrieve_Update_Destroy")
               ]