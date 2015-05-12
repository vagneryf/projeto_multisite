# -*- coding: utf-8 -*-
# Para rodar o comando colocar as configurações abaixo
import os, sys #, re, datetime
reload(sys)
sys.setdefaultencoding('utf-8')

# conf_location = 'settings.local' if sys.path[0][0:2].upper() == 'D:' else 'settings.remote'
conf_location = 'settings' if sys.path[0][0:2].upper() == 'D:'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", conf_location)

import django
django.setup()

from django.contrib.auth.models import User
from profiles.models import Profile
from artigos.models import Artigo, Categoria

p = User.objects.get(id=2)
print p

if p.profile:
    print p.profile.site
else:
    print u'Não tem profile'