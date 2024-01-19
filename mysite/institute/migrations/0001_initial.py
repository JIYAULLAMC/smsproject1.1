# Generated by Django 4.1.5 on 2024-01-16 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Curriculum",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("cclm_id", models.IntegerField(unique=True, verbose_name="cclm_id")),
                (
                    "cclm_name",
                    models.CharField(
                        help_text="like primary, high school, bachelor",
                        max_length=50,
                        unique=True,
                        verbose_name="cclm_name",
                    ),
                ),
                (
                    "cclm_duration_year",
                    models.IntegerField(default=0, verbose_name="cclm_duration_year"),
                ),
                (
                    "cclm_duration_month",
                    models.IntegerField(default=0, verbose_name="cclm_duration_month"),
                ),
                (
                    "cclm_duration_day",
                    models.IntegerField(default=0, verbose_name="cclm_duration_day"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Institute",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "inst_id",
                    models.CharField(
                        max_length=20, unique=True, verbose_name="inst_id"
                    ),
                ),
                (
                    "inst_name",
                    models.CharField(max_length=50, verbose_name="inst_name"),
                ),
                (
                    "inst_email",
                    models.EmailField(
                        blank=True, max_length=50, null=True, verbose_name="inst_email"
                    ),
                ),
                ("contact_no", models.BigIntegerField(verbose_name="inst_contact_no")),
                (
                    "address",
                    models.CharField(
                        blank=True,
                        max_length=250,
                        null=True,
                        verbose_name="inst_address",
                    ),
                ),
                (
                    "country",
                    models.IntegerField(
                        blank=True,
                        default="India",
                        null=True,
                        verbose_name="inst_country",
                    ),
                ),
                (
                    "state",
                    models.IntegerField(
                        blank=True,
                        choices=[
                            (1, "Andhra Pradesh"),
                            (2, "Arunachal Pradesh"),
                            (3, "Assam"),
                            (4, "Bihar"),
                            (5, "Chhattisgarh"),
                            (6, "Goa"),
                            (7, "Gujarat"),
                            (8, "Haryana"),
                            (9, "Himachal Pradesh"),
                            (10, "Jharkhand"),
                            (11, "Karnataka"),
                            (12, "Kerala"),
                            (13, "Madhya Pradesh"),
                            (14, "Maharashtra"),
                            (15, "Manipur"),
                            (16, "Meghalaya"),
                            (17, "Mizoram"),
                            (18, "Nagaland"),
                            (19, "Odisha"),
                            (20, "Punjab"),
                            (21, "Rajasthan"),
                            (22, "Sikkim"),
                            (23, "Tamil Nadu"),
                            (24, "Telangana"),
                            (25, "Tripura"),
                            (26, "Uttar Pradesh"),
                            (27, "Uttarakhand"),
                            (28, "West Bengal"),
                            (29, "Andaman and Nicobar Islands"),
                            (30, "Chandigarh"),
                            (31, "Dadra and Nagar Haveli and Daman and Diu"),
                            (32, "Lakshadweep"),
                            (33, "Delhi (National Capital Territory of Delhi)"),
                            (34, "Puducherry"),
                            (35, "Ladakh"),
                            (36, "Jammu and Kashmir"),
                        ],
                        null=True,
                        verbose_name="inst_state",
                    ),
                ),
                (
                    "city",
                    models.CharField(
                        blank=True, max_length=15, null=True, verbose_name="inst_city"
                    ),
                ),
                (
                    "pin_code",
                    models.CharField(
                        blank=True,
                        max_length=15,
                        null=True,
                        verbose_name="inst_pin_code",
                    ),
                ),
                ("curriculums", models.ManyToManyField(to="institute.curriculum")),
            ],
        ),
    ]
