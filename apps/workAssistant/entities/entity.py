from django.db import models


# Create your models here.


# 任务表
class MyTask(models.Model):
	pid = models.IntegerField()
	flow_task_no = models.CharField(max_length=100)
	order_code = models.CharField(max_length=100)
	mtype = models.IntegerField()
	flow_branch = models.IntegerField(blank=True, null=True)
	flow_id = models.IntegerField(blank=True, null=True)
	flow_code = models.CharField(max_length=100, blank=True, null=True)
	flow_name = models.CharField(max_length=100, blank=True, null=True)
	task_id = models.IntegerField(blank=True, null=True)
	task_code = models.CharField(max_length=100, blank=True, null=True)
	task_name = models.CharField(max_length=100, blank=True, null=True)
	step = models.IntegerField()
	status = models.IntegerField(blank=True, null=True)
	flow_status = models.IntegerField(blank=True, null=True)
	result = models.CharField(max_length=5000, blank=True, null=True)
	description = models.CharField(max_length=2000, blank=True, null=True)
	create_id = models.IntegerField(blank=True, null=True)
	create_name = models.CharField(max_length=200, blank=True, null=True)
	receive_id = models.IntegerField(blank=True, null=True)
	receive_name = models.CharField(max_length=100, blank=True, null=True)
	submit_role = models.CharField(max_length=255, blank=True, null=True)
	receive_time = models.DateTimeField(blank=True, null=True)
	finish_time = models.DateTimeField(blank=True, null=True)
	flow_finish_time = models.DateTimeField(blank=True, null=True)
	city = models.IntegerField(blank=True, null=True)
	ext1 = models.CharField(max_length=45, blank=True, null=True)
	ext2 = models.CharField(max_length=45, blank=True, null=True)
	ext3 = models.CharField(max_length=45, blank=True, null=True)
	ext4 = models.CharField(max_length=45, blank=True, null=True)
	ext5 = models.CharField(max_length=45, blank=True, null=True)
	ext6 = models.CharField(max_length=45, blank=True, null=True)
	ext7 = models.CharField(max_length=45, blank=True, null=True)
	ext8 = models.CharField(max_length=100, blank=True, null=True)
	ext9 = models.CharField(max_length=45, blank=True, null=True)
	ext10 = models.CharField(max_length=45, blank=True, null=True)
	ext11 = models.CharField(max_length=45, blank=True, null=True)
	ext12 = models.CharField(max_length=45, blank=True, null=True)
	ext13 = models.CharField(max_length=45, blank=True, null=True)
	ext14 = models.CharField(max_length=45, blank=True, null=True)
	ext15 = models.CharField(max_length=45, blank=True, null=True)
	ext16 = models.CharField(max_length=45, blank=True, null=True)
	ext17 = models.CharField(max_length=45, blank=True, null=True)
	ext18 = models.CharField(max_length=100, blank=True, null=True)
	ext19 = models.CharField(max_length=45, blank=True, null=True)
	ext20 = models.CharField(max_length=45, blank=True, null=True)
	ext21 = models.CharField(max_length=100, blank=True, null=True)
	ext22 = models.CharField(max_length=45, blank=True, null=True)
	ext23 = models.CharField(max_length=45, blank=True, null=True)
	ext24 = models.CharField(max_length=45, blank=True, null=True)
	ext25 = models.CharField(max_length=45, blank=True, null=True)
	ext26 = models.CharField(max_length=45, blank=True, null=True)
	ext27 = models.CharField(max_length=45, blank=True, null=True)
	ext28 = models.CharField(max_length=45, blank=True, null=True)
	ext29 = models.CharField(max_length=45, blank=True, null=True)
	is_interview = models.IntegerField(blank=True, null=True)
	return_reason = models.CharField(max_length=2000, blank=True, null=True)
	return_name = models.CharField(max_length=200, blank=True, null=True)
	return_time = models.DateTimeField(blank=True, null=True)
	is_material_complete = models.IntegerField(blank=True, null=True)
	is_reconsider = models.IntegerField(blank=True, null=True)
	is_audit_pass = models.IntegerField(blank=True, null=True)
	task_flag = models.IntegerField(blank=True, null=True)
	first_handle_time = models.DateTimeField(blank=True, null=True)
	create_time = models.DateTimeField(blank=True, null=True)
	create_by = models.CharField(max_length=64, blank=True, null=True)
	update_time = models.DateTimeField(blank=True, null=True)
	update_by = models.CharField(max_length=64, blank=True, null=True)
	delete_flag = models.CharField(max_length=1, blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'my_task'


# 员工表
class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    login_name = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    password = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    sex = models.IntegerField()
    age = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    referrer_mobile = models.CharField(max_length=40, blank=True, null=True)
    position = models.CharField(max_length=1000, blank=True, null=True)
    user_type = models.IntegerField()
    status = models.IntegerField()
    corp_code = models.CharField(max_length=64, blank=True, null=True)
    organization_id = models.IntegerField(blank=True, null=True)
    city = models.IntegerField(blank=True, null=True)
    user_property = models.IntegerField(blank=True, null=True)
    is_logginer = models.IntegerField(blank=True, null=True)
    user_source = models.IntegerField(blank=True, null=True)
    is_inquiry = models.IntegerField(blank=True, null=True)
    wx_logname = models.CharField(max_length=255, blank=True, null=True)
    openid = models.CharField(max_length=255, blank=True, null=True)
    has_qrcode = models.CharField(max_length=1, blank=True, null=True)
    create_time = models.DateTimeField()
    create_by = models.CharField(max_length=64, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=64, blank=True, null=True)
    delete_flag = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'