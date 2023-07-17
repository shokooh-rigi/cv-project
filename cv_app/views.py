from rest_framework import viewsets

from cv_app.models import EducationHistory, Certificate
from cv_app.serializers import EducationSerializer, CertificateSerializer, SkillSerializer, BiographySerializer


class BiographyViewSet(viewsets.ModelViewSet):
    serializer_class = BiographySerializer

    def get_queryset(self):
        return EducationHistory.objects.filter(user__user_id=self.request.user.id)


class EducationViewSet(viewsets.ModelViewSet):
    serializer_class = EducationSerializer

    def get_queryset(self):
        return EducationHistory.objects.filter(user__user_id=self.request.user.id)


class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer

    def get_queryset(self):
        return EducationHistory.objects.filter(user__user_id=self.request.user.id)


class SkillListViewSet(viewsets.ModelViewSet):
    serializer_class = SkillSerializer

    def get_queryset(self):
        return EducationHistory.objects.filter(user__user_id=self.request.user.id)
