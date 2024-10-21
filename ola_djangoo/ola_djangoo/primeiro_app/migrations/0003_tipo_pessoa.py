from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primeiro_app', '0002_pessoa_delete_novamodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoPessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=45)),
                ('descricao', models.CharField(max_length=60)),
            ],
        ),
    ]
