# Generated by Django 4.2.16 on 2024-10-25 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0002_bout_fighter_fighterstats_delete_todoitem_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="fighter", old_name="birthdate", new_name="dob",
        ),
        migrations.RemoveField(model_name="bout", name="event_date",),
        migrations.RemoveField(model_name="bout", name="event_name",),
        migrations.RemoveField(model_name="bout", name="round_fought",),
        migrations.RemoveField(model_name="fighter", name="nationality",),
        migrations.RemoveField(model_name="fighter", name="nickname",),
        migrations.RemoveField(model_name="fighter", name="no_contests",),
        migrations.RemoveField(model_name="fighter", name="team",),
        migrations.RemoveField(model_name="fighterstats", name="control_time",),
        migrations.RemoveField(model_name="fighterstats", name="knockdowns",),
        migrations.RemoveField(model_name="fighterstats", name="strikes_attempted",),
        migrations.RemoveField(model_name="fighterstats", name="strikes_landed",),
        migrations.RemoveField(model_name="fighterstats", name="submission_attempts",),
        migrations.RemoveField(model_name="fighterstats", name="takedowns_attempted",),
        migrations.RemoveField(model_name="fighterstats", name="takedowns_landed",),
        migrations.AddField(
            model_name="fighterstats",
            name="sig_strikes_abs",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=2, null=True
            ),
        ),
        migrations.AddField(
            model_name="fighterstats",
            name="sig_strikes_perMin",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=2, null=True
            ),
        ),
        migrations.AddField(
            model_name="fighterstats",
            name="strike_def",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=2, null=True
            ),
        ),
        migrations.AddField(
            model_name="fighterstats",
            name="strikes_accuracy",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=2, null=True
            ),
        ),
        migrations.AddField(
            model_name="fighterstats",
            name="sub_avg",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=2, null=True
            ),
        ),
        migrations.AddField(
            model_name="fighterstats",
            name="takedown_average_per15",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=2, null=True
            ),
        ),
        migrations.AddField(
            model_name="fighterstats",
            name="takedown_defense",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=2, null=True
            ),
        ),
        migrations.AddField(
            model_name="fighterstats",
            name="takedowns_accuracy",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=2, null=True
            ),
        ),
        migrations.AlterField(
            model_name="fighter",
            name="height",
            field=models.DecimalField(
                blank=True, decimal_places=0, max_digits=3, null=True
            ),
        ),
        migrations.AlterField(
            model_name="fighter",
            name="weight",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=3, null=True
            ),
        ),
    ]