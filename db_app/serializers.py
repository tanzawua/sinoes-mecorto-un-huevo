
from rest_framework import serializers

from .models import Servicio

class ServicioSerializer(serializers.ModelSerializer):
	class Meta:
		model = Servicio
		fields = ('id','referencia','nombre','apellido','precio','nuevo','descripcion','image','fecha')
		read_only_fields = ('fecha',)