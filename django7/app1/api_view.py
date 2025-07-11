from .models import Student
from .serializers import StudentSerializer, StudentListSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination
#viewset, genericviewset,modelviewset,readOnlymodelviewset


@api_view(['GET'])
def student_list(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)

class StudentViewSet(viewsets.GenericViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    
    filterset_fields = {
        "dept": ["exact"],
        "courses__id": ["in"]
    }
    
    search_fields = ['user__first_name', 'user__username'] 
    ordering_fields = ['id', 'roll_no']     
    
    # def get_serializer(self, *args, **kwargs):
    #     if self.action == 'list':
    #         return StudentListSerializer(*args, **kwargs)
    #     return super().get_serializer(*args, **kwargs)

    def get_queryset(self):
        return Student.objects.all().distinct()

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True, context={'request': request})
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True, context={'request': request})
            return self.get_paginated_response(serializer.data)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        student = self.get_object()
        serializer = self.get_serializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, pk=None):
        student = self.get_object()
        student.delete()
        return Response({"message": "Student delete Successfully"})
    
    def partial_update(self, request, pk=None): 
        student = self.get_object()
        serializer = self.get_serializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)