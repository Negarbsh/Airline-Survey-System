# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Manager(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=150)
    password = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'manager'


class Airline(models.Model):
    airlineid = models.AutoField(primary_key=True)
    managerid = models.ForeignKey(to=Manager, to_field='userid', on_delete=models.DO_NOTHING, db_column='managerid')
    airlinename = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'airline'


class Flight(models.Model):
    flightnumber = models.AutoField(primary_key=True)
    airlineid = models.ForeignKey(to=Airline, to_field='airlineid', on_delete=models.DO_NOTHING, db_column='airlineid')
    flightdate = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'flight'


class Ticket(models.Model):
    ticketnumber = models.AutoField(primary_key=True)
    seatnumber = models.CharField(max_length=150)
    flightnumber = models.ForeignKey(Flight, models.CASCADE, db_column='flightnumber', to_field='flightnumber')
    firstname = models.CharField(max_length=150, blank=True, null=True)
    lastname = models.CharField(max_length=150, blank=True, null=True)
    passportnumber = models.CharField(max_length=150, blank=True, null=True)
    gender = models.TextField(blank=True, null=True)  # This field type is a guess.
    price = models.FloatField()

    class Meta:
        managed = False
        db_table = 'ticket'


class Voter(models.Model):
    userid = models.AutoField(primary_key=True)
    ticketnumber = models.ForeignKey(Ticket, models.CASCADE, db_column='ticketnumber', to_field='ticketnumber')
    flightnumber = models.ForeignKey(Flight, models.CASCADE, db_column='flightnumber', to_field='flightnumber')
    type = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'voter'
        unique_together = (('ticketnumber', 'flightnumber'),)


class Survey(models.Model):
    surveyid = models.AutoField(primary_key=True)
    activationinterval = models.DateTimeField()
    isactive = models.BooleanField()
    airlineid = models.ForeignKey(Airline, models.DO_NOTHING, db_column='airlineid', to_field='airlineid')

    class Meta:
        managed = False
        db_table = 'survey'


class Takesurvey(models.Model):
    id = models.BigAutoField(primary_key=True)
    voterid = models.OneToOneField(Voter, models.DO_NOTHING, db_column='voterid', to_field='userid')
    surveyid = models.ForeignKey(Survey, models.DO_NOTHING, db_column='surveyid', to_field='surveyid')
    starttime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'takesurvey'
        unique_together = (('voterid', 'surveyid'),)


class Question(models.Model):
    id = models.BigAutoField(primary_key=True)
    surveyid = models.OneToOneField(Survey, models.DO_NOTHING, db_column='surveyid',to_field='surveyid')
    questionnumber = models.IntegerField()
    questiontext = models.CharField(max_length=150)
    isobligatory = models.BooleanField()
    respondertype = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'question'
        unique_together = (('surveyid', 'questionnumber'),)


class Descriptivequestion(models.Model):
    id = models.BigAutoField(primary_key=True)
    surveyid = models.OneToOneField(Question, models.DO_NOTHING, db_column='surveyid', to_field='surveyid')
    questionnumber = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'descriptivequestion'
        unique_together = (('surveyid', 'questionnumber'),)


class Answers(models.Model):
    id = models.BigAutoField(primary_key=True)
    voterid = models.OneToOneField(Takesurvey, models.DO_NOTHING, db_column='voterid',to_field='voterid')
    surveyid = models.ForeignKey(Descriptivequestion, models.DO_NOTHING, db_column='surveyid', to_field='surveyid')
    questionnumber = models.IntegerField()
    answertext = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'answers'
        unique_together = (('voterid', 'surveyid', 'questionnumber'),)


class Assistancy(models.Model):
    id = models.BigAutoField(primary_key=True)
    mainmanagerid = models.OneToOneField(Manager, models.DO_NOTHING, db_column='mainmanagerid', to_field='userid')
    assistantmanagerid = models.ForeignKey(Manager, models.DO_NOTHING, db_column='assistantmanagerid', related_name='+',
                                           to_field='userid')
    surveyid = models.ForeignKey(Survey, models.DO_NOTHING, db_column='surveyid', to_field='surveyid')

    class Meta:
        managed = False
        db_table = 'assistancy'
        unique_together = (('mainmanagerid', 'assistantmanagerid', 'surveyid'),)


class Supervisor(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=150)
    password = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'supervisor'


class CheckQuestion(models.Model):
    id = models.BigAutoField(primary_key=True)
    surveyid = models.OneToOneField(Question, models.DO_NOTHING, db_column='surveyid', to_field='surveyid')
    questionnumber = models.IntegerField()
    supervisorid = models.ForeignKey(Supervisor, models.DO_NOTHING, db_column='supervisorid', to_field='userid')
    result = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'check_question'
        unique_together = (('surveyid', 'questionnumber', 'supervisorid'),)


class Multichoicequestion(models.Model):
    id = models.BigAutoField(primary_key=True)
    surveyid = models.OneToOneField(Question, models.DO_NOTHING, db_column='surveyid', to_field='surveyid')
    questionnumber = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'multichoicequestion'
        unique_together = (('surveyid', 'questionnumber'),)


class Choice(models.Model):
    id = models.BigAutoField(primary_key=True)
    surveyid = models.OneToOneField(Multichoicequestion, models.DO_NOTHING, db_column='surveyid', to_field='surveyid')
    questionnumber = models.IntegerField()
    choicenumber = models.IntegerField()
    choicetext = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'choice'
        unique_together = (('surveyid', 'questionnumber', 'choicenumber'),)


class Chooses(models.Model):
    id = models.BigAutoField(primary_key=True)
    voterid = models.OneToOneField(Takesurvey, models.DO_NOTHING, db_column='voterid', to_field='voterid')
    surveyid = models.ForeignKey(Choice, models.DO_NOTHING, db_column='surveyid')
    questionnumber = models.IntegerField()
    choicenumber = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'chooses'
        unique_together = (('voterid', 'surveyid', 'questionnumber', 'choicenumber'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
