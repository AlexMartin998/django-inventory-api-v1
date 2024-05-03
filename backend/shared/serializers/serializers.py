from rest_framework import serializers


class FiltersBaseSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(FiltersBaseSerializer, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False


class NotFoundSerializer(serializers.Serializer):
    error = serializers.CharField()
    status = serializers.IntegerField()


class BadRequestSerializer(serializers.Serializer):
    error = serializers.CharField()
    status = serializers.IntegerField()
    missing_fields = serializers.ListField(child=serializers.CharField(), required=False)




# ### Swagger
class OptionalFieldsModelSerializer(serializers.ModelSerializer):
    def get_fields(self, *args, **kwargs):
        fields = super(OptionalFieldsModelSerializer, self).get_fields(*args, **kwargs)
        for field in fields.values():
            field.required = False
        return fields

