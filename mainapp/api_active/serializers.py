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
    Candidate,
    AdaptationStatus,
    Award,
    AwardCandidate,
    Message,
    JobDirectoryCatalogs,
    CommentToStage,
    File
)


class BlockSerializer(serializers.ModelSerializer):
    json = serializers.JSONField(required=False)

    class Meta:
        model = Block
        fields = '__all__'


class BlockListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Block
        fields = ['json']


class AdaptationStageDetailSerializer(serializers.ModelSerializer):
    stage_name = serializers.CharField()
    illustration = serializers.CharField(required=False)
    tier = serializers.IntegerField(required=False)
    point = serializers.IntegerField(required=False)
    status = serializers.IntegerField(required=False)
    create_date = serializers.DateTimeField()
    id_employee = serializers.IntegerField(required=False)
    block = BlockListSerializer(read_only=True)

    class Meta:
        model = AdaptationStage
        fields = '__all__'


class AdaptationStageSerializer(serializers.ModelSerializer):
    stage_name = serializers.CharField()
    illustration = serializers.CharField(required=False)
    tier = serializers.IntegerField(required=False)
    point = serializers.IntegerField(required=False)
    status = serializers.IntegerField(required=False)
    create_date = serializers.DateTimeField()
    id_employee = serializers.IntegerField(required=False)
    block = BlockListSerializer(read_only=True)

    class Meta:
        model = AdaptationStage
        fields = '__all__'


class LevelSerializer(serializers.ModelSerializer):
    level_name = serializers.CharField()
    illustration = serializers.CharField(required=False)
    tier = serializers.IntegerField(required=False)
    status = serializers.IntegerField(required=False)
    create_date = serializers.DateTimeField()
    id_employee = serializers.IntegerField(required=False)
    stages = AdaptationStageSerializer(many=True, read_only=True)

    class Meta:
        model = Level
        fields = '__all__'


class LevelListSerializer(serializers.ModelSerializer):
    stages = AdaptationStageSerializer(many=True)

    class Meta:
        model = Level
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    last_name = serializers.CharField()
    first_name = serializers.CharField()
    middle_name = serializers.CharField(required=False)
    post = serializers.CharField(required=False)
    role = serializers.CharField(required=False)
    tier = serializers.IntegerField(required=False)
    status = serializers.IntegerField(required=False)
    illustration_link = serializers.CharField(required=False)
    create_date = serializers.DateTimeField()
    id_employee = serializers.IntegerField(required=False)

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


class CustomerSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField()
    city = serializers.CharField(required=False)
    address = serializers.CharField(required=False)
    status = serializers.IntegerField(required=False)
    create_date = serializers.DateTimeField()
    id_employee = serializers.IntegerField(required=False)
    programs = ProgramSerializerList(many=True, read_only=True)

    class Meta:
        model = Customer
        fields = '__all__'


class ProgramSerializer(serializers.ModelSerializer):
    status = serializers.IntegerField(required=False)
    create_date = serializers.DateTimeField(required=False)
    tier = serializers.IntegerField(required=False)
    description = serializers.CharField(required=False)

    class Meta:
        model = Program
        fields = '__all__'


class GoalSerializer(serializers.ModelSerializer):
    goal_name = serializers.CharField()
    description = serializers.CharField(required=False)
    tier = serializers.IntegerField(required=False)
    status = serializers.IntegerField(required=False)
    create_date = serializers.DateTimeField(required=False)
    id_employee = serializers.IntegerField(required=False)

    class Meta:
        model = Goal
        fields = '__all__'


class DocumentSerializer(serializers.ModelSerializer):
    document_name = serializers.CharField(required=False)
    tier = serializers.IntegerField(required=False)
    create_date = serializers.DateTimeField()
    id_employee = serializers.IntegerField(required=False)

    class Meta:
        model = Document
        fields = '__all__'


class DocumentSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'


class GoalsSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = '__all__'


class CustomerSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class ProgramDetailSerializer(serializers.ModelSerializer):
    status = serializers.IntegerField(required=False)
    create_date = serializers.DateTimeField(required=False)
    levels_detail = LevelListSerializer(many=True, read_only=True, source='levels')
    contacts_detail = ContactSerializerList(read_only=True, many=True, source='contact')
    documents_detail = DocumentSerializerList(many=True, read_only=True, source='documents')
    goals_detail = GoalsSerializerList(many=True, read_only=True, source='goals')
    customer_detail = CustomerSerializerList(read_only=True, many=True, source='customer')
    illustration = serializers.CharField(required=False)

    class Meta:
        model = Program
        fields = '__all__'


class ProgramDetailForCandidateSerializer(serializers.ModelSerializer):
    levels_detail = LevelListSerializer(many=True, read_only=True, source='levels')

    class Meta:
        model = Program
        fields = ('id', 'levels_detail')


class EmployeeSerializer(serializers.ModelSerializer):
    id_customer = serializers.IntegerField()
    last_name = serializers.CharField()
    first_name = serializers.CharField()
    middle_name = serializers.CharField(required=False)
    post = serializers.CharField(required=False)
    mobile_phone = serializers.CharField(required=False)
    email = serializers.CharField(required=False)
    status = serializers.IntegerField(required=False)
    create_date = serializers.DateTimeField(required=False)
    id_employee = serializers.IntegerField(required=False)
    illustration = serializers.CharField(required=False)

    class Meta:
        model = Employee
        fields = '__all__'


class EmployeeSerializerDetail(serializers.ModelSerializer):
    id_customer = serializers.IntegerField(required=False)
    last_name = serializers.CharField()
    first_name = serializers.CharField()
    middle_name = serializers.CharField(required=False)
    post = serializers.CharField(required=False)
    mobile_phone = serializers.CharField(required=False)
    email = serializers.CharField(required=False)
    status = serializers.IntegerField(required=False)
    create_date = serializers.DateTimeField()
    id_employee = serializers.IntegerField(required=False)
    illustration = serializers.CharField(required=False)

    class Meta:
        model = Employee
        exclude = ('password',)


class EmployeeSerializerList(serializers.ModelSerializer):
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


class AdaptationStatusSerializerDetail(serializers.ModelSerializer):
    class Meta:
        model = AdaptationStatus
        fields = '__all__'


class CommentToStageSerializerDetail(serializers.ModelSerializer):
    class Meta:
        model = CommentToStage
        fields = '__all__'


class CandidateSerializer(serializers.ModelSerializer):
    id_customer = serializers.IntegerField(required=False)
    last_name = serializers.CharField()
    first_name = serializers.CharField()
    middle_name = serializers.CharField(required=False)
    post = serializers.CharField(required=False)
    mobile_phone = serializers.CharField(required=False)
    email = serializers.CharField(required=False)
    status = serializers.IntegerField(required=False)
    create_date = serializers.DateTimeField()
    id_employee = serializers.IntegerField(required=False)
    program_details = ProgramDetailForCandidateSerializer(many=True, read_only=True, source='program')
    adaptation_status = AdaptationStatusSerializerDetail(many=True, read_only=True)
    comment = CommentToStageSerializerDetail(many=True, read_only=True)
    illustration = serializers.CharField(required=False)

    class Meta:
        model = Candidate
        fields = (
            'id',
            'last_name',
            'first_name',
            'middle_name',
            'post',
            'salary',
            'mobile_phone',
            'email',
            'status',
            'create_date',
            'release_date',
            'id_employee',
            # 'candidate',
            'program',
            'id_customer',
            'program_details',
            'adaptation_status',
            'comment',
            'illustration'
        )


class CandidateSerializerDetail(serializers.ModelSerializer):
    last_name = serializers.CharField()
    first_name = serializers.CharField()
    middle_name = serializers.CharField()
    post = serializers.CharField(required=False)
    mobile_phone = serializers.CharField(required=False)
    email = serializers.CharField(required=False)
    status = serializers.IntegerField(required=False)
    program_details = ProgramDetailSerializer(many=True, read_only=True, source='program')
    adaptation_status = AdaptationStatusSerializerDetail(many=True, read_only=True)
    comment = CommentToStageSerializerDetail(many=True, read_only=True)
    illustration = serializers.CharField(required=False)

    class Meta:
        model = Candidate
        fields = '__all__'


class CandidateSerializerList(serializers.ModelSerializer):
    program_details = ProgramDetailSerializer(many=True, read_only=True, source='program')

    class Meta:
        model = Candidate
        fields = '__all__'


class ICandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ['id', 'candidate', 'program']


class AdaptationStatusSerializer(serializers.ModelSerializer):
    id_stage = serializers.IntegerField()
    id_goal = serializers.IntegerField(required=False)
    point = serializers.IntegerField(required=False)
    create_date = serializers.DateTimeField()

    class Meta:
        model = AdaptationStatus
        fields = '__all__'


class CommentToStageSerializer(serializers.ModelSerializer):
    id_stage = serializers.IntegerField()
    comment = serializers.CharField(required=False)

    class Meta:
        model = CommentToStage
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


class JobDirectorySerializer(serializers.ModelSerializer):
    directory = serializers.CharField()

    class Meta:
        model = JobDirectoryCatalogs
        fields = '__all__'


class FileSerializer(serializers.ModelSerializer):
    file = serializers.FileField()

    class Meta:
        model = File
        fields = ('file', 'remark', 'timestamp')
