import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primeiro_app', '0003_tipopessoa'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='tipo_pessoa',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='primeiro_app.tipopessoa'),
            preserve_default=False,
        ),
    ]
