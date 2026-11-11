# --- Example -------------------------------------------------------------------
# class SerializerExample(serializers.ModelSerializer):
#     parent_name = serializers.CharField(source="parent.name", read_only=True)  # from a relation
#     children = ChildSerializer(many=True, read_only=True)                      # nested
#
#     class Meta:
#         model = ModelExample
#         fields = ["id", "name", "kind", "parent", "parent_name", "children"]   # what goes in the JSON
#
#
# class InputExample(serializers.Serializer):                                    # input that is not a model
#     text = serializers.CharField(max_length=2000)
#     day = serializers.DateField(required=False)                                # optional
#     days = serializers.IntegerField(default=7, min_value=1, max_value=31)      # with limits
#
#
# class RowExample(serializers.Serializer):                                      # for plain dicts
#     parent = serializers.CharField()
#     days = serializers.IntegerField()
#     total = serializers.FloatField(allow_null=True)                            # null allowed
# -------------------------------------------------------------------------------
