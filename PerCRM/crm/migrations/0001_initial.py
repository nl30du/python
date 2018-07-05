# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-25 06:38
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.ASCIIUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'verbose_name': '\u8d26\u6237\u8868',
                'verbose_name_plural': '\u8d26\u6237\u8868',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('addr', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': '\u6821\u533a\u8868',
                'verbose_name_plural': '\u6821\u533a\u8868',
            },
        ),
        migrations.CreateModel(
            name='ClassList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.PositiveSmallIntegerField(verbose_name='\u5b66\u671f')),
                ('class_type', models.PositiveSmallIntegerField(choices=[(0, '\u9762\u6388(\u8131\u4ea7)'), (1, '\u9762\u6388(\u5468\u672b)'), (2, '\u7f51\u7edc')], verbose_name='\u73ed\u7ea7\u7c7b\u578b')),
                ('start_date', models.DateField(verbose_name='\u5f00\u73ed\u65e5\u671f')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='\u6bd5\u4e1a\u65e5\u671f')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Branch', verbose_name='\u6821\u533a')),
            ],
            options={
                'verbose_name': '\u73ed\u7ea7\u8868',
                'verbose_name_plural': '\u73ed\u7ea7\u8868',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('price', models.PositiveIntegerField()),
                ('period', models.PositiveSmallIntegerField(verbose_name='\u5468\u671f(\u6708)')),
                ('outline', models.TextField(verbose_name='\u5927\u7eb2')),
            ],
            options={
                'verbose_name': '\u8bfe\u7a0b\u8868',
                'verbose_name_plural': '\u8bfe\u7a0b\u8868',
            },
        ),
        migrations.CreateModel(
            name='CourseRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_num', models.PositiveSmallIntegerField(verbose_name='\u7b2c\u51e0\u8282(\u5929)')),
                ('has_homework', models.BooleanField(default=True)),
                ('homework_title', models.CharField(blank=True, max_length=32, null=True)),
                ('outline', models.TextField(verbose_name='\u672c\u8282\u8bfe\u5927\u7eb2')),
                ('date', models.DateField(auto_now_add=True)),
                ('from_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.ClassList', verbose_name='\u73ed\u7ea7')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u4e0a\u8bfe\u8bb0\u5f55',
                'verbose_name_plural': '\u4e0a\u8bfe\u8bb0\u5f55',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=32, null=True)),
                ('qq', models.CharField(max_length=64, unique=True)),
                ('qq_name', models.CharField(blank=True, max_length=64, null=True)),
                ('phone', models.CharField(blank=True, max_length=64, null=True)),
                ('source', models.PositiveSmallIntegerField(choices=[(0, '\u8f6c\u4ecb\u7ecd'), (1, 'QQ\u7fa4'), (2, '\u5b98\u7f51'), (3, '\u767e\u5ea6\u63a8\u5e7f'), (4, '51CTO'), (5, '\u5e02\u573a\u63a8\u5e7f')])),
                ('referral_from', models.CharField(blank=True, max_length=64, null=True, verbose_name='\u8f6c\u4ecb\u7ecd\u4ebaQQ')),
                ('content', models.TextField(verbose_name='\u54a8\u8be2\u8bfe\u7a0b')),
                ('note', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('consult_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Course', verbose_name='\u54a8\u8be2\u8bfe\u7a0b')),
                ('consultant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u54a8\u8be2\u4eba')),
            ],
            options={
                'verbose_name': '\u5ba2\u6237\u8868',
                'verbose_name_plural': '\u5ba2\u6237\u8868',
            },
        ),
        migrations.CreateModel(
            name='CustomerFollowUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='\u8ddf\u8fdb\u5185\u5bb9')),
                ('intention', models.PositiveSmallIntegerField(choices=[(0, '2\u5468\u5185\u62a5\u540d'), (1, '\u4e00\u4e2a\u6708\u5185\u62a5\u540d'), (2, '\u8fd1\u671f\u65e0\u62a5\u540d\u8ba1\u5212'), (3, '\u5df2\u5728\u5176\u4ed6\u673a\u6784\u62a5\u540d'), (4, '\u5df2\u62a5\u540d'), (0, '\u5df2\u62c9\u9ed1')])),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('consultant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u8ddf\u8fdb\u4eba')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Customer')),
            ],
            options={
                'verbose_name': '\u5ba2\u6237\u8ddf\u8fdb\u8868',
                'verbose_name_plural': '\u5ba2\u6237\u8ddf\u8fdb\u8868',
            },
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_agreed', models.BooleanField(default=False, verbose_name='\u5b66\u5458\u5df2\u540c\u610f\u5408\u540c\u6761\u6b3e')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('consultant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u8bfe\u7a0b\u987e\u95ee')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Customer')),
                ('enrolled_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.ClassList', verbose_name='\u6240\u62a5\u73ed\u7ea7')),
            ],
            options={
                'verbose_name': '\u62a5\u540d\u8868',
                'verbose_name_plural': '\u62a5\u540d\u8868',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(default=500, verbose_name='\u6570\u989d')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('consultant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Course', verbose_name='\u6240\u62a5\u8bfe\u7a0b')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Customer')),
            ],
            options={
                'verbose_name': '\u7f34\u8d39\u8868',
                'verbose_name_plural': '\u7f34\u8d39\u8868',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
            ],
            options={
                'verbose_name': '\u89d2\u8272\u8868',
                'verbose_name_plural': '\u89d2\u8272\u8868',
            },
        ),
        migrations.CreateModel(
            name='StudyRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance', models.PositiveSmallIntegerField(choices=[(0, '\u5df2\u7b7e\u5230'), (1, '\u8fdf\u5230'), (2, '\u7f3a\u52e4'), (3, '\u65e9\u9000')], default=0)),
                ('score', models.SmallIntegerField(choices=[(100, 'A+'), (90, 'A'), (85, 'B+'), (80, 'B'), (75, 'B-'), (70, 'C+'), (60, 'C'), (40, 'C-'), (-50, 'D'), (-100, 'copy'), (0, 'N/A')])),
                ('note', models.TextField(blank=True, null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('course_record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.CourseRecord')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Enrollment')),
            ],
            options={
                'verbose_name': '\u5b66\u4e60\u8bb0\u5f55\u8868',
                'verbose_name_plural': '\u5b66\u4e60\u8bb0\u5f55\u8868',
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
            ],
            options={
                'verbose_name': '\u6807\u7b7e\u8868',
                'verbose_name_plural': '\u6807\u7b7e\u8868',
            },
        ),
        migrations.AddField(
            model_name='customer',
            name='flags',
            field=models.ManyToManyField(blank=True, null=True, to='crm.Tags'),
        ),
        migrations.AddField(
            model_name='classlist',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Course', verbose_name='\u73ed\u7ea7\u8bfe\u7a0b'),
        ),
        migrations.AddField(
            model_name='classlist',
            name='teachers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='roles',
            field=models.ManyToManyField(blank=True, null=True, to='crm.Role'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AlterUniqueTogether(
            name='studyrecord',
            unique_together=set([('student', 'course_record', 'score')]),
        ),
        migrations.AlterUniqueTogether(
            name='enrollment',
            unique_together=set([('customer', 'enrolled_class')]),
        ),
        migrations.AlterUniqueTogether(
            name='courserecord',
            unique_together=set([('from_class', 'day_num')]),
        ),
        migrations.AlterUniqueTogether(
            name='classlist',
            unique_together=set([('branch', 'course', 'semester')]),
        ),
    ]
