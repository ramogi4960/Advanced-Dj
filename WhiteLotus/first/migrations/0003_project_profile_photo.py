# Generated by Django 4.1.5 on 2023-03-30 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0002_tag_project_vote_ratio_project_vote_total_review_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='profile_photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]