from rest_framework import routers

from bullet.items.views import ItemViewSet
from bullet.signifiers.views import SignifierViewSet

router = routers.DefaultRouter()
router.register(r'items', ItemViewSet)
router.register(r'signifiers', SignifierViewSet)
