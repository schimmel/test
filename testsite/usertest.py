from django.contrib.auth.models import User,Group

first_name = 'tobias'
last_name = 'ofdeaf'

import unicodedata
user_name = '%s.%s'[:30] %('tobias'.lower(),'ofdeaf'.lower())
#user_name = user_name[:30]
#user_name =  unicodedata.normalize('NFKD', user_name).encode('ASCII', 'ignore')

print user_name

userex = User.objects.get(username=user_name)
if userex:
    print "User exists "
    user_exists = True
    #i = 0

while user_exists and i < 10:
    i+=1
    user_name_new = str(i) + user_name
    user_name_new = user_name_new[:30]
    print str(i)
    print user_name_new
    try:
       User.objects.get(username=user_name_new)
    except:
       user_exists = False

print "Anzuglegender Benutzername %s " % user_name_new

try:
    user = User.objects.create_user(user_name_new, '')
except:
    print "Fehler beim anlegen"

user.is_staff = False
user.is_active = False
user.first_name = first_name
user.last_name = last_name
group = Group.objects.get(name='cme_manual')
user.groups.add(group)
user.save()
