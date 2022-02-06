import csv
import uuid

import numpy
from numpy import ndarray


class Points:
    def __init__(self, mean_x1: float, mean_x2: float, standard_deviation: float, size: int):
        self.mean_x1 = mean_x1
        self.mean_x2 = mean_x2
        self.standard_deviation = standard_deviation
        self.size = size

    def generate_random_points(self) -> ndarray:
        """
        This function generate random points with Mean of X1 distribution, Mean of X2 distribution, Standard derivation
        and Resultant shape.

        :return: points - resulted 2D array with x1, x2 values
        """
        x1 = numpy.random.normal(loc=self.mean_x1, scale=self.standard_deviation, size=self.size)
        x2 = numpy.random.normal(loc=self.mean_x2, scale=self.standard_deviation, size=self.size)
        points = numpy.vstack((x1, x2)).T
        return points

    @staticmethod
    def extend_ndarrays(first_array, second_array):
        result_array = numpy.append(first_array, second_array, 0)
        return result_array

    @staticmethod
    def create_points_csv(points):
        """
        This function create csv file with resulted points.

        :param points: resulted 2D array with x1, x2 values
        :return: file_path - path to media for downloading the file
        """
        filename = str(uuid.uuid4())
        with open(f"../media/{filename}.csv", "w") as points_csv:
            writer = csv.writer(points_csv, delimiter=',')
            writer.writerows(points)

        file_path = points_csv.name.split('media/')[1]

        return file_path

    def create_points_plot(self):
        # todo plots
        pass


def generate_points_create_csv() -> str:
    """
    This function make all actions from generate points up to create csv file.

    :return: path to generated csv file.
    """
    class_minus_one_points = Points(mean_x1=10.0, mean_x2=14.0, standard_deviation=4.0, size=50)
    class_plus_one_points = Points(mean_x1=20.0, mean_x2=18.0, standard_deviation=3.0, size=50)
    generated_first_points = class_minus_one_points.generate_random_points()
    generated_second_points = class_plus_one_points.generate_random_points()
    resulted_ndarray = Points.extend_ndarrays(generated_first_points, generated_second_points)
    csv_file_path = Points.create_points_csv(resulted_ndarray)
    return csv_file_path
