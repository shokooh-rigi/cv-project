import datetime
import string

import factory
from factory import fuzzy

from cv_app import enums
from cv_app import models


class UniversityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.University

    class Params:
        town = factory.Faker('state', locale='fa')

    name = factory.LazyAttribute(lambda a: ' دانشگاه {}'.format(a.town))
    university_id = fuzzy.FuzzyInteger(111, 999)


class EducationHistoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.EducationHistory

    user = factory.SubFactory('cv_app.factories.User.Factory')
    university = factory.SubFactory(UniversityFactory)
    institution = factory.fuzzy.FuzzyText(prefix='آموزشگاه', length=15, chars=string.ascii_lowercase)
    major = factory.fuzzy.FuzzyText(prefix='رشته تحصیلی', length=15, chars=string.ascii_lowercase)
    education_orientation = factory.fuzzy.FuzzyText(prefix='گرایش', length=15, chars=string.ascii_lowercase)
    education_place = factory.fuzzy.FuzzyText(prefix='محل تحصیل', length=15, chars=string.ascii_lowercase)
    start_date = datetime.date(year=2022, month=4, day=12)
    end_date = datetime.date(year=2023, month=4, day=12)
    study_level = factory.fuzzy.FuzzyChoice([x[0] for x in enums.StudyLevel.choices])


class BiographyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Biography

    first_name = factory.Faker('first_name', locale='fa')
    last_name = factory.Faker('last_name', locale='fa')
    birth_date = datetime.date(year=1988, month=5, day=12)


class CertificateFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Certificate


class SkillFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Skill


class JobExperienceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.JobExperience
