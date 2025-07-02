# from app1.models import Profile
# from django.contrib.auth.models import User

## Create
# user = User.objects.create(username = 'testuser', password='password123', first_name ='Test', last_name='User', email='user@gmail.com' )
# print("User Created: ", user)
# obj = Profile(
#     user = user,
#     phone = '0176538892',
#     address = '123 Test St, Test City, TC 123',
#     profile_pic = 'path/to/profile_pic.webp'
# )
# obj.save()
# print("Profile Created Successfully")

## Read 
# all_profile = Profile.objects.all()
# print("All Profile:", all_profile)
# for profile in all_profile:
#     pic = profile.profile_pic.url if profile.profile_pic else None
#     print("Profile:", profile.user.username, profile.full_name, profile.phone, pic)

# singla model data featch or dakar jonno "get()" function used kora.
# profile = Profile.objects.get(id=2,user__username='testuser')
# print("Profile Get:", profile)

# profile = Profile.objects.filter(id=2,user__username='testuser')
# print("Profile Filter: ", profile)
# print(Profile.objects.filter(id=2,user__username='testuser').exists())

# profile = Profile.objects.exclude(id=2,user__username='testuser')
# print("Profile Exclude: ", profile)

# ----> Read ar ai gula Query: 
# Field Lookup
# i = insensitive --> capital, small, upper, lower - X
# exact, contains,iexact, icontains, gt/gte/lt/lte(tim,date,claculation), range, startwith,istartwith 
# ......> Read ar update Query  = Aggregate, Queue,


# Update: 
#  Update korta Must Get() used korta hoba: 

# profile = Profile.objects.get(id=1)
# profile.phone = "5681544423"
# profile.save()
# profile = Profile.objects.get(id=2)
# profile.user.first_name = 'updatedFirstName'
# profile.user.save()
# print("Successfully Updated.")


# way-2: profile.objects.filter(user__username = 'testuser').update(phone='111111111')

# Delete:
# profile = Profile.objects.get(id=1)
# profile.delete()
# print("Profile Delete Succesfully")

# Profile.objects.filter(user__username='testuser').delete()






