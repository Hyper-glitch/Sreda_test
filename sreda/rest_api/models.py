from django.db import models

from rest_api.utils import generate_points_create_csv


class CustomUser(models.Model):
    generated_points = models.FileField(null=True, blank=True, upload_to='csv_points')
    plot_with_points = models.ImageField(null=True, blank=True, upload_to='plots')

    def save(self, *args, **kwargs):
        super(CustomUser, self).save(*args, **kwargs)

        csv_file_path, plot_file_path = generate_points_create_csv()
        self.generated_points.name = csv_file_path
        self.plot_with_points.name = plot_file_path

