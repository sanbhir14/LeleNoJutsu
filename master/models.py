from django.db import models
import uuid
from django.dispatch import receiver
from django_cas_ng.signals import cas_user_authenticated
import json
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
LANG = settings.SSO_UI_ORG_DETAIL_LANG
ORG_CODE = {}
with open(settings.SSO_UI_ORG_DETAIL_FILE_PATH, 'r') as ORG_CODE_FILE:
    ORG_CODE.update(json.load(ORG_CODE_FILE))

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    id = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False)
    nama = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    no_induk = models.CharField('Nomor Induk', max_length=10, blank=True)
    faculty = models.CharField('fakultas', max_length=128, blank=True)
    role = models.CharField(max_length=100)
    study_program = models.CharField('program studi', max_length=128, blank=True)
    educational_program = models.CharField('program pendidikan', max_length=128, blank=True)
    no_hp = models.CharField(max_length=50, blank=True, null=True)
    foto_profil = models.CharField(max_length=5000, blank=True, null=True)

    class Meta:
        verbose_name = 'profile'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nama

@receiver(cas_user_authenticated)
def save_user_attributes(user, attributes, **kwargs):
    print(attributes)
    user.save()
    print(user)
    if attributes['peran_user'] == 'mahasiswa':
        org_code = attributes['kd_org']
        record = ORG_CODE[LANG][org_code]
        profileInDb =Profile.objects.filter(no_induk = attributes['npm']).exists()
        if not profileInDb:
            profile = Profile(user = user, nama = attributes['nama'], faculty = record['faculty'], study_program = record['study_program'],
            educational_program = record['educational_program'], email = f'{user.username}@ui.ac.id', no_induk = attributes['npm'])
            profile.save()
            user.profile = profile
            user.save()

    if attributes['peran_user'] == 'staff':
        profileInDb = Profile.objects.filter(no_induk = attributes['nip']).exists()
        if not profileInDb:
            profile = Profile(user = user, nama = attributes['nama'], nip = attributes['nip'], email = f'{user.username}@ui.ac.id')
            profile.save()
            user.profile = profile
            user.save()

