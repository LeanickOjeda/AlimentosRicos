from rest_framework import serializers
from core.models import MenuSemana
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuSemana
        fields =['nrocatalogo','dia','platofondo','Ensalada','Postre']