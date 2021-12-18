from rest_framework import serializers

from ..models import (
    Program,
    Employee,
    Level,
    AdaptationStage,
    Block,
    Goal,
    Document,
    Contact,
    LnkLevelProgram
)


class AdaptationStageSerializer(serializers.ModelSerializer):
    stage_name = serializers.CharField()
    illustration = serializers.ImageField(required=False)
    tier = serializers.IntegerField()
    point = serializers.IntegerField()
    status = serializers.IntegerField()
    create_date = serializers.DateTimeField()
    id_employee = serializers.IntegerField()

    class Meta:
        model = AdaptationStage
        fields = '__all__'


class LevelSerializer(serializers.ModelSerializer):
    level_name = serializers.CharField()
    illustration = serializers.ImageField(required=False)
    tier = serializers.IntegerField()
    status = serializers.IntegerField()
    create_date = serializers.DateTimeField()
    id_employee = serializers.IntegerField()
    stages = AdaptationStageSerializer(many=True)

    class Meta:
        model = Level
        fields = '__all__'


class LevelListSerializer(serializers.ModelSerializer):
    stages = AdaptationStageSerializer(many=True)

    class Meta:
        model = Level
        fields = '__all__'


class ProgramSerializer(serializers.ModelSerializer):
    id_customer = serializers.IntegerField()
    status = serializers.IntegerField()
    create_date = serializers.DateTimeField()

    class Meta:
        model = Program
        fields = '__all__'


class ProgramDetailSerializer(serializers.ModelSerializer):
    id_customer = serializers.IntegerField()
    status = serializers.IntegerField()
    create_date = serializers.DateTimeField()
    levels = LevelListSerializer(many=True)

    class Meta:
        model = Program
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    last_name = serializers.CharField()
    first_name = serializers.CharField()
    middle_name = serializers.CharField()
    post = serializers.CharField()
    status = serializers.IntegerField()
    create_date = serializers.DateTimeField()

    class Meta:
        model = Employee
        fields = '__all__'


class BlockSerializer(serializers.ModelSerializer):
    block_name = serializers.CharField()
    description = serializers.CharField()
    tier = serializers.IntegerField()
    id_stage = serializers.IntegerField()
    status = serializers.IntegerField()
    create_date = serializers.DateTimeField()
    id_employee = serializers.IntegerField()

    class Meta:
        model = Block
        fields = '__all__'


class GoalSerializer(serializers.ModelSerializer):
    goal_name = serializers.CharField()
    description = serializers.CharField()
    tier = serializers.IntegerField()
    status = serializers.IntegerField()
    create_date = serializers.DateTimeField()
    id_employee = serializers.IntegerField()

    class Meta:
        model = Goal
        fields = '__all__'


class DocumentSerializer(serializers.ModelSerializer):
    document_name = serializers.CharField()
    document_link = serializers.URLField()
    tier = serializers.IntegerField()
    status = serializers.IntegerField()
    create_date = serializers.DateTimeField()
    id_employee = serializers.IntegerField()

    class Meta:
        model = Document
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    last_name = serializers.CharField()
    first_name = serializers.CharField()
    middle_name = serializers.CharField()
    post = serializers.CharField()
    role = serializers.CharField()
    tier = serializers.IntegerField()
    status = serializers.IntegerField()
    illustration_link = serializers.URLField()
    create_date = serializers.DateTimeField()
    id_employee = serializers.IntegerField()

    class Meta:
        model = Contact
        fields = '__all__'

