# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-25 03:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutHd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_about', models.CharField(max_length=40, verbose_name='关于HD')),
                ('a_title', models.CharField(max_length=100, verbose_name='标题')),
                ('a_intro', models.TextField(verbose_name='HD简介')),
                ('a_image', models.ImageField(upload_to='static/img')),
            ],
            options={
                'verbose_name_plural': '关于HD',
                'verbose_name': '关于HD',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=30, verbose_name='客户姓名')),
                ('c_email', models.EmailField(max_length=254, verbose_name='客户邮箱')),
                ('c_message', models.TextField(blank=True, verbose_name='客户留言')),
                ('c_date', models.DateTimeField(auto_now=True, verbose_name='留言时间')),
            ],
            options={
                'verbose_name_plural': '联系我们',
                'verbose_name': '联系我们',
            },
        ),
        migrations.CreateModel(
            name='FocusPoints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_image', models.ImageField(upload_to='static/img')),
            ],
            options={
                'verbose_name_plural': '焦点',
                'verbose_name': '焦点',
            },
        ),
        migrations.CreateModel(
            name='ScienceBehind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_bigtitle', models.CharField(max_length=50, verbose_name='大标题')),
                ('s_title', models.CharField(max_length=50, verbose_name='标题')),
                ('s_image', models.ImageField(upload_to='static/img', verbose_name='image')),
                ('s_content', models.TextField(verbose_name='内容')),
            ],
            options={
                'verbose_name_plural': '背后的科学',
                'verbose_name': '背后的科学',
            },
        ),
        migrations.CreateModel(
            name='SideShow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_cover', models.ImageField(upload_to='static/img/fullscreen', verbose_name='图片路径')),
                ('s_title', models.CharField(max_length=30, verbose_name='轮播图标题')),
                ('s_idx', models.IntegerField(verbose_name='索引')),
                ('is_active', models.BooleanField(default=False, verbose_name='是否激活')),
            ],
            options={
                'verbose_name_plural': '轮播图',
                'verbose_name': '轮播图',
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_title', models.CharField(max_length=40, verbose_name='技术名称')),
                ('s_level', models.CharField(max_length=20, verbose_name='技術水平')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
            ],
            options={
                'verbose_name_plural': '技术',
                'verbose_name': '技术',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_name', models.CharField(max_length=30, verbose_name='工作人员姓名')),
                ('t_post', models.CharField(max_length=30, verbose_name='职位')),
                ('t_intro', models.TextField(verbose_name='人员简介')),
                ('t_picture', models.ImageField(upload_to='static/img', verbose_name='人员照片')),
                ('t_gender', models.BooleanField(default=False, verbose_name='性别,默认为女')),
                ('t_contribute', models.IntegerField(default=0, verbose_name='贡献值')),
            ],
            options={
                'verbose_name_plural': '团队',
                'verbose_name': '团队',
            },
        ),
        migrations.CreateModel(
            name='Us',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_content', models.TextField(verbose_name='contact us content')),
                ('u_tel', models.CharField(max_length=11, verbose_name='电话')),
                ('u_fax', models.CharField(max_length=20, verbose_name='传真')),
                ('u_email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('u_address', models.CharField(max_length=100, verbose_name='地址')),
            ],
            options={
                'verbose_name_plural': '公司信息',
                'verbose_name': '公司信息',
            },
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('w_title', models.CharField(max_length=30, verbose_name='产品标题')),
                ('w_image', models.ImageField(upload_to='static/img', verbose_name='产品')),
                ('w_describe', models.TextField(verbose_name='产品描述')),
                ('w_date', models.DateTimeField(auto_now=True, verbose_name='产品上传时间')),
            ],
            options={
                'verbose_name_plural': '产品',
                'verbose_name': '产品',
            },
        ),
        migrations.CreateModel(
            name='WorkCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wc_name', models.CharField(max_length=30, verbose_name='产品分类名称')),
            ],
            options={
                'verbose_name_plural': '产品分类',
                'verbose_name': '产品分类',
            },
        ),
        migrations.CreateModel(
            name='WorkCategoryTwo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wc_name', models.CharField(max_length=30, verbose_name='产品分类名称')),
            ],
            options={
                'verbose_name_plural': '产品分类二',
                'verbose_name': '产品分类二',
            },
        ),
        migrations.CreateModel(
            name='WorkPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wp_title', models.CharField(max_length=30, verbose_name='产品页标题')),
                ('wp_cintent', models.TextField(verbose_name='产品介绍')),
            ],
            options={
                'verbose_name_plural': '产品页',
                'verbose_name': '产品页',
            },
        ),
        migrations.CreateModel(
            name='WorkTwo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('w_class', models.CharField(max_length=30, verbose_name='类')),
                ('w_title', models.CharField(max_length=30, verbose_name='产品标题')),
                ('w_image', models.ImageField(upload_to='static/img', verbose_name='产品')),
                ('w_describe', models.TextField(verbose_name='产品描述')),
                ('w_date', models.DateTimeField(auto_now=True, verbose_name='产品上传时间')),
                ('w_category', models.ManyToManyField(to='aboutapp.WorkCategoryTwo', verbose_name='产品分类')),
            ],
            options={
                'verbose_name_plural': '产品大',
                'verbose_name': '产品大',
            },
        ),
        migrations.AddField(
            model_name='work',
            name='w_category',
            field=models.ManyToManyField(to='aboutapp.WorkCategory', verbose_name='产品分类'),
        ),
    ]
