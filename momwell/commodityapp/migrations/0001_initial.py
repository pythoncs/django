# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-18 03:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BigClassify',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_title', models.CharField(max_length=20, verbose_name='标题')),
                ('b_index', models.IntegerField(max_length=5, verbose_name='索引')),
                ('b_createTime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('b_updateTime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('b_isDelete', models.BooleanField(default=False, verbose_name='是否删除')),
            ],
            options={
                'verbose_name': '大分类',
                'verbose_name_plural': '大分类',
                'db_table': 'bigClassify',
            },
        ),
        migrations.CreateModel(
            name='BuyToday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_title', models.CharField(max_length=50, verbose_name='标题')),
                ('b_activityPrice', models.FloatField(max_length=10, verbose_name='活动价')),
                ('b_originalPrice', models.FloatField(max_length=10, verbose_name='原价')),
                ('b_reducedRate', models.FloatField(max_length=3, verbose_name='打折率')),
                ('b_image', models.ImageField(upload_to='buyToday/', verbose_name='团购图片')),
                ('b_createTime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('b_updateTime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('b_isDelete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('b_repertory', models.IntegerField(max_length=10, verbose_name='库存')),
                ('b_is_collect', models.BooleanField(default=False, verbose_name='是否收藏')),
            ],
            options={
                'verbose_name': '今日团购',
                'verbose_name_plural': '今日团购',
                'db_table': 'buyToday',
            },
        ),
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_title', models.CharField(max_length=50, verbose_name='商品标题')),
                ('c_current_price', models.FloatField(max_length=10, verbose_name='时价')),
                ('c_original_price', models.FloatField(max_length=10, verbose_name='原价')),
                ('c_image', models.ImageField(upload_to='commodity/', verbose_name='图片')),
                ('c_season', models.CharField(max_length=5, verbose_name='季节')),
                ('c_sales', models.IntegerField(max_length=10, verbose_name='销量')),
                ('c_createTime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('c_updateTime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('c_isDelete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('c_repertory', models.IntegerField(max_length=10, verbose_name='库存')),
                ('c_is_newProduct', models.BooleanField(default=True, verbose_name='是否新品')),
                ('c_is_collect', models.BooleanField(default=False, verbose_name='是否收藏')),
            ],
            options={
                'verbose_name': '商品',
                'verbose_name_plural': '商品',
                'db_table': 'commodity',
            },
        ),
        migrations.CreateModel(
            name='SmallClassify',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_title', models.CharField(max_length=20, verbose_name='标题')),
                ('s_index', models.IntegerField(max_length=5, verbose_name='索引')),
                ('s_createTime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('s_updateTime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('s_isDelete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('big_classify', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commodityapp.BigClassify')),
            ],
            options={
                'verbose_name': '小分类',
                'verbose_name_plural': '小分类',
                'db_table': 'smallClassify',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_phone', models.CharField(max_length=20, verbose_name='手机号')),
                ('u_password', models.CharField(max_length=20, verbose_name='密码')),
                ('u_name', models.CharField(max_length=10, verbose_name='昵称')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'db_table': 'user',
            },
        ),
        migrations.AddField(
            model_name='commodity',
            name='small_classify',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commodityapp.SmallClassify'),
        ),
    ]
