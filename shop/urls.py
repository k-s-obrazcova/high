from django.urls import path
from rest_framework import routers
from .views import *

urlpatterns = [
    path('product/one-filter/', get_one_filter_product, name='get_one_filter_product'),
    path('product/all/', product_list, name='product_list'),
    path('product/more-filter/', get_more_filter_product, name='get_more_filter_product'),
    path('product/all-filter/', product_list_with_filter, name='product_filter_page'),
    path('product/detail/<int:id>/', get_one_product, name='get_one_product'),

    path('supplier/', ListSupplier.as_view(), name='supplier_list'),
    path('supplier/create/', CreateSupplier.as_view(), name='supplier_create'),
    path('supplier/detail/<int:pk>/', DetailSupplier.as_view(), name='supplier_detail'),
    path('supplier/update/<int:pk>/', UpdateSupplier.as_view(), name='supplier_update'),
    path('supplier/delete/<int:pk>/', DeleteSupplier.as_view(), name='supplier_delete'),

    path('order/<int:pk>/', OrderDetail.as_view(), name='order_detail'),

    path('api/', test_json, name='api_test'),
    path('api/orders/', order_api_list, name='api_order_list'),
    path('api/orders/<int:pk>/', order_api_detail, name='api_order_detail'),

]

router = routers.SimpleRouter()
router.register('api/products', ProductViewSet, basename='products')
router.register('api/products_small', ProductViewSetSmall, basename='products_small')
router.register('api/supplier', SupplierViewSet, basename='supplier')
router.register('api/supply', SupplyViewSet, basename='supply')
router.register('api/category', CategoryViewSet, basename='category')
router.register('api/tag', TagViewSet, basename='tag')
router.register('api/parametr', ParametrViewSet, basename='parametr')
router.register('api/warehouse', WarehouseViewSet, basename='warehouse')
router.register('api/inventory', InventoryViewSet, basename='inventory')
router.register('api/review', ReviewViewSet, basename='review')
router.register('api/supplier_filter', SupplierViewSetFilter, basename='supplier_filter')
urlpatterns += router.urls
