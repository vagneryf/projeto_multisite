# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from profiles.models import Profile
from artigos.models import Artigo, Categoria

p = User.objects.get(id=2)
print p

if p.profile:
    print p.profile.site
else:
    print u'Não tem profile'