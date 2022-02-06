from django.db import models

from sreda.rest_api.utils import generate_points_create_csv


class CustomUser(models.Model):
    generated_points = models.FileField(null=True, upload_to='csv_points')
    plot_with_points = models.ImageField(null=True, upload_to='plots')

    def save(self, *args, **kwargs):
        super(CustomUser, self).save(*args, **kwargs)

        csv_path = generate_points_create_csv()
        self.generated_points.name = csv_path

