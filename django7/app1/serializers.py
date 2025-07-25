from rest_framework import serializers
from .models import Student, Course
from django.contrib.auth.models import User
#serializers,modelserializers,hyperlinkModelSerializer

class CourseSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Course
        fields = ['id', 'name', 'code', 'description', 'credits', 'semester', 'dept']
        extra_kwargs = {
            'id': {'required': False},
            'name': {'required': False},
            'code': {'required': False},
            'description': {'required': False},
            'credits': {'required': False},
            'semester': {'required': False},
            'dept': {'required': False}
        }
        # def validate(self, data):
        #     if 'id' not in data:
        #         if 'name' not in data:
        #             raise serializers.ValidationError({"message: Name is required"})
        #     return data
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']
        extra_kwargs = {
            'username': {'read_only': True}
        }

class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    courses = CourseSerializer(required=False, many=True)
    class Meta:
        model = Student 
        fields = "__all__"
    
    def create(self, validated_data):        # Students [User,Courses] models value created.
        try:
            user = validated_data.pop('user')
            firstname = user.get('first_name')
            lastname = user.get('last_name')
            phone = validated_data.get('phone')
            user['username'] = f"{firstname}_{lastname}_{phone[-2:]}"
            user_instance = User.objects.create(**user)
            
            course = validated_data.pop('courses', None)
            course_list = []
            for data in course:
                if 'id' in data:
                    course_instance = Course.objects.get(id=data['id'])
                    course_list.append(course_instance)
                else:
                    course_instance = Course.objects.create(**data)
                    course_list.append(course_instance)
            student = Student.objects.get(user=user_instance)
            student.courses.set(course_list)
            student.save()
            for key, value in validated_data.items():
                if key == 'courses':
                    continue 
                setattr(student, key, value)
            student.save()
            return student
        except Exception as e:
            print(e)
            raise serializers.ValidationError({"message : Error creating student"})
   
    def update(self, instance, validated_data):
        
        user_data = validated_data.pop('user', None)
        if user_data:
            for attr, value in user_data.items():
                setattr(instance.user, attr, value)
            instance.user.save()
        course = validated_data.pop('courses', None)
        if course:
            course_list = []
            for data in course:
                if 'id' in course:
                    course_instance = Course.objects.get(id=data['id'])
                    course_list.append(course_instance)
                else:
                    course_instance = Course.objects.create(**data)
                    course_list.append(course_instance)
            instance.courses.set(course_list)
        
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['courses'] = CourseSerializer(instance.courses.all(), many=True).data
        data['extra'] = "Hudai Ja iccha Tai"
        data['phone_number'] = instance.phone
        del data['phone']
        return data
class StudentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student 
        fields = "__all__"