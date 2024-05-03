from drf_yasg import openapi

# Parámetros de paginación
page_size_openapi = openapi.Parameter(
    name='page_size',
    in_=openapi.IN_QUERY,
    type=openapi.TYPE_INTEGER,
    required=False,
    description='Tamaño de la página',
)
page_openapi = openapi.Parameter(
    name='page',
    in_=openapi.IN_QUERY,
    type=openapi.TYPE_INTEGER,
    required=False,
    description='Número de la página',
)
order_by_openapi = openapi.Parameter(
    name='order_by',
    in_=openapi.IN_QUERY,
    type=openapi.TYPE_STRING,
    required=False,
    description='Campo por el cual se ordenará la consulta',
)
oder_up_openapi = openapi.Parameter(
    name='order_up',
    in_=openapi.IN_QUERY,
    type=openapi.TYPE_BOOLEAN,
    required=False,
    description='Orden ascendente',
)
