from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets

# this code is for viewset class
# class StudentViewSet(viewsets.ViewSet):

#     def list(self, request):
#         stu = Student.objects.all()
#         serializer = StudentSerializer(stu, many = True)
#         return Response(serializer.data)

#     def create(self, request):
#         serializer = StudentSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status = status.HTTP_201_CREATED)
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

#     def retrieve(self, request, pk=None):
#         id = pk
#         if id is not None:
#             stu = Student.objects.get(id = id)
#             serializer = StudentSerializer(stu)
#             return Response(serializer.data)

#     def update(self, request, pk=None):
#         id = pk
#         stu = Student.objects.get(pk = id)
#         serializer = StudentSerializer(stu, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
#     def partial_update(self, request, pk=None):
#         id = pk
#         stu = Student.objects.get(pk = id)
#         serializer = StudentSerializer(stu, data = request.data, partial = True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

#     def destroy(self, request, pk=None):
#         id = pk
#         stu = Student.objects.get(pk = id)
#         stu.delete()
#         return Response('Deleted')
    
# this code is for ModelViewSet class
# for crud operations we need to write one modelviewset class
# class StudentViewSet(viewsets.ModelViewSet):
#     serializer_class = StudentSerializer
#     queryset = Student.objects.all()

# this code is for ReadOnlyModelViewSet class
# for crud operations we need to write one modelviewset class
class StudentViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()