from rest_framework import serializers
from note.models import NoteModel

class NoteSerializer(serializers.Serializer):
	"""docstring for NoteSerializer"""
	id = serializers.IntegerField(read_only=True)
	title = serializers.CharField(required=False, max_length=200)
	body = serializers.CharField()

	def create(self, validated_data):
		return NoteModel.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.title = validated_data.get('title', instance.title)
		instance.body = validated_data.get('body', instance.body)
		instance.save()	
		return instance
		
	class Meta:
		"""docstring for Meta"""
		model = NoteModel
		fields = ['id','title','body']				