import json

from rest_framework import serializers

from apps.GameInfo.models import GameBuylist, GameType, BJLGoodRecord

class BJLGoodRecordSerializer(serializers.ModelSerializer):
    pk = serializers.IntegerField()
    content = serializers.JSONField(
        required=False, allow_null=True)
    filter_len = serializers.IntegerField()
    filter_single = serializers.IntegerField()
    filter_double = serializers.IntegerField()
    cut_start = serializers.IntegerField()
    cut_end = serializers.IntegerField()
    created_at = serializers.DateTimeField()
    name = serializers.CharField()

    def to_representation(self, instance):
        ret = super(BJLGoodRecordSerializer, self).to_representation(instance)
        ret['content'] = json.loads(ret['content'])
        return ret
    
    class Meta:
        model = BJLGoodRecord
        fields = ['pk', 'content', 'filter_len', 'filter_single', 'filter_double', 'cut_start', 'cut_end', 'created_at', 'name']

