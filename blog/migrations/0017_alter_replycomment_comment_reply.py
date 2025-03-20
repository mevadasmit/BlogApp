# Generated by Django 4.2.1 on 2025-02-10 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0016_replycomment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="replycomment",
            name="comment_reply",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reply_comments",
                to="blog.blogcomment",
            ),
        ),
    ]
