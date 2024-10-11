from rest_framework.decorators import api_view
from rest_framework import status
from .models import Category
from .serializers import CategorySerializer, CharackterstickSerializer, ProductSerializer, ProductаSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from rest_framework.generics import RetrieveAPIView
from .serializers import ProductDetailSerializer

@api_view(['GET'])
def get_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_characteristics(request, category_id):
    category = Category.objects.get(id_category=category_id)
    serializer = CharackterstickSerializer(category.charackterstick)
    return Response(serializer.data)

@api_view(['POST'])
def add_product(request):
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductSearchView(APIView):
    permission_classes = []
    def get(self, request):
        query = request.GET.get('query', '')
        products = Product.objects.filter(name__icontains=query)
        serializer = ProductаSerializer(products, many=True)
        return Response(serializer.data)
class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_field = 'id_product'
    permission_classes = []