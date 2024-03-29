from rest_framework import routers
from rental import views as rental_views


router = routers.DefaultRouter()
router.register('friends', rental_views.FriendModelViewSet)
router.register('belongings', rental_views.BelongingModelViewSet)
router.register('borrowed', rental_views.BorrowedModelViewSet)
#
