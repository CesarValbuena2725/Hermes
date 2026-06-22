from rest_framework import serializers
from .models import Developer, PR, Review, Comment
from collections import Counter

class PRSerializer(serializers.ModelSerializer):

    status = serializers.SerializerMethodField()

    class Meta:
        model = PR
        fields = '__all__'

    def get_status(self, obj):
        review_data = obj.review_set.all()

        #1. No data is found
        if not review_data:
            return 'OP'
        
        #2 Look for CH_RQ and return it if found 
        for review in review_data:
            if (review.status == 'CH_RQ'):
                return 'CH_RQ'
            
        # if no CH_RQ was found return acc
        return 'ACC'
    

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['pr','author','status']
        extra_kwargs = {
            'author' : {'read_only' : True}
        }


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['line_on_pr','review','content','author']
        extra_kwargs = {
            'author' : {'read_only' : True}
        }

    def validate(self, data):
        pr_data = data['review'].pr         #PrimaryKeyRelatedField - resolved from a PK to an object/model instance
        max_line_on_pr = len(pr_data.content.splitlines())

        if(data['line_on_pr'] < 1 or data['line_on_pr'] > max_line_on_pr):
            raise serializers.ValidationError("Invalid line to comment")
        return data