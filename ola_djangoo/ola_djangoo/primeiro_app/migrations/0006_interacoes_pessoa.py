import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primeiro_app', '0005_alter_pessoa_tipo_pessoa'),
    ]

    operations = [
        migrations.CreateModel(
            name='InteracoesPessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_hora', models.DateTimeField(auto_now_add=True)),
                ('mensagem', models.TextField()),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='primeiro_app.pessoa')),
            ],
        ),
    ]