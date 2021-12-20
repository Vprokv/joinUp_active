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
)


class BlockSerializer(serializers.ModelSerializer):
    block_name = serializers.CharField()
    description = serializers.CharField()
    tier = serializers.IntegerField()
    status = serializers.IntegerField()
    create_date = serializers.DateTimeField()
    id_employee = serializers.IntegerField()

    class Meta:
        model = Block
        fields = '__all__'


class AdaptationStageDetailSerializer(serializers.ModelSerializer):
    stage_name = serializers.CharField()
    illustration = serializers.ImageField(required=False)
    tier = serializers.IntegerField()
    point = serializers.IntegerField()
    status = serializers.IntegerField()
    create_date = serializers.DateTimeField()
    id_employee = serializers.IntegerField()
    blocks = BlockSerializer(many=True)

    class Meta:
        model = AdaptationStage
        fields = '__all__'


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
        exclude = ('program',)


class ContactSerializer(serializers.ModelSerializer):
    last_name = serializers.CharField()
    first_name = serializers.CharField()
    middle_name = serializers.CharField()
    post = serializers.CharField()
    role = serializers.CharField()
    tier = serializers.IntegerField()
    status = serializers.IntegerField()
    illustration_link = serializers.URLField(required=False)
    create_date = serializers.DateTimeField()
    id_employee = serializers.IntegerField()

    class Meta:
        model = Contact
        fields = '__all__'


class ContactSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class ProgramSerializer(serializers.ModelSerializer):
    id_customer = serializers.IntegerField()
    status = serializers.IntegerField()
    create_date = serializers.DateTimeField()
    id_employee = serializers.IntegerField()

    class Meta:
        model = Program
        fields = (
        'id', 'tier', 'duration_day', 'create_date', 'program_name', 'status', 'id_customer', 'id_employee', 'contact')


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


class ProgramDetailSerializer(serializers.ModelSerializer):
    id_customer = serializers.IntegerField()
    status = serializers.IntegerField()
    create_date = serializers.DateTimeField()
    levels = LevelListSerializer(many=True, read_only=True)
    contacts = ContactSerializerList(read_only=True, many=True, source='contact')
    documents = DocumentSerializer(many=True, read_only=True)
    goals = GoalSerializer(many=True, read_only=True)

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
