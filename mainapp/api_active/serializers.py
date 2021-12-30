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
    LicensePack,
    Customer,
    License,
    UserCandidate,
    UserEmployee,
    Candidate,
    AdaptationStatus,
    Award,
    AwardCandidate,
    Message
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
    stages = AdaptationStageSerializer(many=True, read_only=True)

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


class ProgramSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = '__all__'


class CustomerSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField()
    city = serializers.CharField()
    address = serializers.CharField()
    status = serializers.IntegerField()
    create_date = serializers.DateTimeField()
    id_employee = serializers.IntegerField()
    programs = ProgramSerializerList(many=True, read_only=True)

    class Meta:
        model = Customer
        fields = '__all__'


class ProgramSerializer(serializers.ModelSerializer):
    status = serializers.IntegerField()
    create_date = serializers.DateTimeField()

    class Meta:
        model = Program
        fields = (
            'id',
            'tier',
            'duration_day',
            'create_date',
            'program_name',
            'status',
            'customer',
            'employee',
            'contact')


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
    create_date = serializers.DateTimeField()
    id_employee = serializers.IntegerField()

    class Meta:
        model = Document
        fields = '__all__'


class ProgramDetailSerializer(serializers.ModelSerializer):
    status = serializers.IntegerField()
    create_date = serializers.DateTimeField()
    levels = LevelListSerializer(many=True, read_only=True)
    contacts = ContactSerializerList(read_only=True, many=True, source='contact')
    documents = DocumentSerializer(many=True, read_only=True)
    goals = GoalSerializer(many=True, read_only=True)
    customer_detail = CustomerSerializerList(read_only=True)

    class Meta:
        model = Program
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    id_customer = serializers.IntegerField()
    last_name = serializers.CharField()
    first_name = serializers.CharField()
    middle_name = serializers.CharField()
    post = serializers.CharField()
    mobile_phone = serializers.CharField()
    email = serializers.CharField()
    status = serializers.IntegerField()
    create_date = serializers.DateTimeField()
    id_employee = serializers.IntegerField()

    class Meta:
        model = Employee
        fields = '__all__'


class EmployeeSerializerDetail(serializers.ModelSerializer):
    id_customer = serializers.IntegerField()
    last_name = serializers.CharField()
    first_name = serializers.CharField()
    middle_name = serializers.CharField()
    post = serializers.CharField()
    mobile_phone = serializers.CharField()
    email = serializers.CharField()
    status = serializers.IntegerField()
    create_date = serializers.DateTimeField()
    id_employee = serializers.IntegerField()
    programs = ProgramDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Employee
        fields = '__all__'


class EmployeeSerializerList(serializers.ModelSerializer):
    programs = ProgramDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Employee
        fields = '__all__'


class LicensePackSerializer(serializers.ModelSerializer):
    id_customer = serializers.IntegerField()
    users_count = serializers.IntegerField()
    users_spent = serializers.IntegerField()
    status = serializers.IntegerField()
    create_date = serializers.DateTimeField()
    id_employee = serializers.IntegerField()

    class Meta:
        model = LicensePack
        fields = '__all__'


class LicenseSerializer(serializers.ModelSerializer):
    id_license_pack = serializers.IntegerField()
    id_candidate = serializers.IntegerField()
    start_date = serializers.DateField()
    finish_date = serializers.DateField()
    create_date = serializers.DateTimeField()
    status = serializers.IntegerField()
    id_employee = serializers.IntegerField()

    class Meta:
        model = License
        fields = '__all__'


class UserCandidateSerializer(serializers.ModelSerializer):
    mobile_phone = serializers.CharField()
    status = serializers.IntegerField()
    create_date = serializers.DateTimeField()
    id_employee = serializers.IntegerField()

    class Meta:
        model = UserCandidate
        fields = '__all__'


class UserEmployeeSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField()
    status = serializers.IntegerField()
    create_date = serializers.DateTimeField()
    id_employee = serializers.IntegerField()

    class Meta:
        model = UserEmployee
        fields = '__all__'


class UserEmployeeDetail(serializers.ModelSerializer):
    user_name = serializers.CharField()
    status = serializers.IntegerField()
    create_date = serializers.DateTimeField()
    id_employee = serializers.IntegerField()
    employees = EmployeeSerializerList(read_only=True, many=True)

    class Meta:
        model = UserEmployee
        fields = '__all__'


class CandidateSerializer(serializers.ModelSerializer):
    id_customer = serializers.IntegerField()
    last_name = serializers.CharField()
    first_name = serializers.CharField()
    middle_name = serializers.CharField()
    post = serializers.CharField()
    mobile_phone = serializers.CharField()
    email = serializers.CharField()
    status = serializers.IntegerField()
    create_date = serializers.DateTimeField()
    id_employee = serializers.IntegerField()

    class Meta:
        model = Candidate
        fields = '__all__'


class ICandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ['id', 'candidate', 'program']


class AdaptationStatusSerializer(serializers.ModelSerializer):
    id_user_employee = serializers.IntegerField()
    id_stage = serializers.IntegerField()
    id_goal = serializers.IntegerField()
    point = serializers.IntegerField()
    create_date = serializers.DateTimeField()

    class Meta:
        model = AdaptationStatus
        fields = '__all__'


class AwardSerializer(serializers.ModelSerializer):
    award_name = serializers.CharField()
    illustration = serializers.CharField()
    tier = serializers.IntegerField()

    class Meta:
        model = Award
        fields = '__all__'


class AwardCandidateSerializer(serializers.ModelSerializer):
    award_name = serializers.CharField()
    id_candidate = serializers.IntegerField()
    create_date = serializers.DateTimeField()

    class Meta:
        model = AwardCandidate
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    text_message = serializers.CharField()
    id_candidate = serializers.IntegerField()
    create_date = serializers.DateTimeField()
    viewing_date = serializers.DateTimeField()
    status = serializers.IntegerField()

    class Meta:
        model = Message
        fields = '__all__'
