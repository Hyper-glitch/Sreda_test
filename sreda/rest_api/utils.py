import csv
import os.path
import uuid

import numpy
import matplotlib.pyplot as plt

from .models import CustomUser
from numpy import ndarray


class Points:
    def __init__(self, mean_x1: float, mean_x2: float, standard_deviation: float, size: int):
        self.mean_x1 = mean_x1
        self.mean_x2 = mean_x2
        self.standard_deviation = standard_deviation
        self.size = size

    def generate_random_points(self) -> tuple:
        """
        This function generate random points with Mean of X1 distribution, Mean of X2 distribution, Standard derivation
        and Resultant shape.
        :return: x1, x2 - resulted ndarray with x1, x2 values
        """

        x1 = numpy.random.normal(loc=self.mean_x1, scale=self.standard_deviation, size=self.size)
        x2 = numpy.random.normal(loc=self.mean_x2, scale=self.standard_deviation, size=self.size)
        return x1, x2

    @staticmethod
    def join_ndarrays(minus_one_2d, plus_one_2d) -> ndarray:
        """
        Join two 2D arrays.
        :param minus_one_2d: 2D array of class-1 x1, x2 values
        :param plus_one_2d: 2D array of class+1 x1, x2 values
        :return: result_array - 2D array with all points
        """

        result_array = numpy.append(minus_one_2d, plus_one_2d, 0)
        return result_array

    @staticmethod
    def create_2d_arrays(minus_one_x1, minus_one_x2, plus_one_x1, plus_one_x2):
        """
        Create 2D arrays from 1D.
        :param minus_one_x1: 1D array of class-1 x1 values
        :param minus_one_x2: 1D array of class-1 x2 values
        :param plus_one_x1: 1D array of class+1 x1 values
        :param plus_one_x2: 1D array of class+1 x2 values
        :return: minus_one_2D, plus_one_2D - resulted 2D arrays
        """

        minus_one_2d = numpy.vstack((minus_one_x1, minus_one_x2)).T
        plus_one_2d = numpy.vstack((plus_one_x1, plus_one_x2)).T
        return minus_one_2d, plus_one_2d

    @staticmethod
    def create_points_csv(resulted_ndarray) -> tuple:
        """
        Create csv file with resulted points.
        :param resulted_ndarray: resulted 2D array with x1, x2 values
        :return: file_path, filename - path to media for downloading the file and name of the file
        """

        filename = str(uuid.uuid4())
        with open(f"./media/{filename}.csv", "w") as points_csv:
            writer = csv.writer(points_csv, delimiter=',')
            writer.writerows(resulted_ndarray)

        file_path = points_csv.name.split('media/')[1]

        return file_path, filename

    @staticmethod
    def remove_files(csv_file_path, plot_file_path):
        """
        Create csv file with resulted points.
        :param csv_file_path: path to csv file
        :param plot_file_path: path to plot
        """

        if os.path.exists(csv_file_path) and os.path.exists(plot_file_path):
            os.remove(csv_file_path)
            os.remove(plot_file_path)
        else:
            raise FileNotFoundError

    @staticmethod
    def create_points_plot(minus_one_x1, minus_one_x2, plus_one_x1, plus_one_x2, filename) -> str:
        """
        Create a plot with resulted points.
        :param minus_one_x1: 1D array of class-1 x1 values
        :param minus_one_x2: 1D array of class-1 x2 values
        :param plus_one_x1: 1D array of class+1 x1 values
        :param plus_one_x2: 1D array of class+1 x2 values
        :param filename - the name of the file
        :return: plot_path, a path to the plot
        """

        plt.scatter(minus_one_x1, minus_one_x2, c='red')
        plt.scatter(plus_one_x1, plus_one_x2, c='blue')
        plt.savefig(f"./media/{filename}.png")

        if os.path.exists(f"./media/{filename}.png"):
            plot_path = f"{filename}.png"
            return plot_path
        else:
            raise FileNotFoundError


def generate_points_create_csv():
    """
    This function make all actions from generate points up to create csv file and plot by points.
    :return: csv_file_path - path to generated csv file
             plot_file_path - path to generated plot
    """

    # instances initialization
    class_minus_one_points = Points(mean_x1=10.0, mean_x2=14.0, standard_deviation=4.0, size=50)
    class_plus_one_points = Points(mean_x1=20.0, mean_x2=18.0, standard_deviation=3.0, size=50)

    # generate random points
    minus_one_x1, minus_one_x2 = class_minus_one_points.generate_random_points()
    plus_one_x1, plus_one_x2 = class_plus_one_points.generate_random_points()

    # create 2D arrays from 1D
    minus_one_2d, plus_one_2d = Points.create_2d_arrays(minus_one_x1, minus_one_x2, plus_one_x1, plus_one_x2)

    # create one 2D array with 100 points
    resulted_ndarray = Points.join_ndarrays(minus_one_2d, plus_one_2d)

    # create a csv file
    csv_file_path, filename = Points.create_points_csv(resulted_ndarray)

    # create a plot
    plot_file_path = Points.create_points_plot(minus_one_x1, minus_one_x2, plus_one_x1, plus_one_x2, filename)

    return csv_file_path, plot_file_path


def is_user_exists(username):
    user_exists = CustomUser.objects.filter(username=username).exists()
    return user_exists


if __name__ == '__main__':
    generate_points_create_csv()
