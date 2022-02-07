from django.core.exceptions import BadRequest
from django.http import HttpResponse, FileResponse
from django.views.decorators.csrf import csrf_exempt

from .models import CustomUser
from .utils import generate_points_create_csv, is_user_exists, Points


@csrf_exempt
def register(request):
    username = request.GET['username']
    password = request.GET['password']

    if request.method == 'POST':
        user = CustomUser.objects.create_user(username=username, password=password)
        csv_file_path, plot_file_path = generate_points_create_csv()
        user.generated_points.name = csv_file_path
        user.plot_with_points.name = plot_file_path
        user.save(update_fields=['generated_points', 'plot_with_points'])
        return HttpResponse('<h1>User was successfully register</h1>')
    else:
        raise BadRequest('Invalid request.')


def get_users_csv_file(request):
    username = request.GET['username']
    user_exists = is_user_exists(username)

    if request.method == 'GET' and user_exists:
        users_csv_file = CustomUser.objects.get(username=username).generated_points
        response = FileResponse(open(users_csv_file.path, 'rb'))
        return response
    else:
        raise BadRequest('The user does not register yet or invalid request method')


def get_users_plot(request):
    username = request.GET['username']
    user_exists = is_user_exists(username)

    if request.method == 'GET' and user_exists:
        users_plot = CustomUser.objects.get(username=username).plot_with_points
        return HttpResponse(users_plot, content_type="image/png")
    else:
        raise BadRequest('The user does not register yet or invalid request method')


@csrf_exempt
def regenerate_users_csv_file(request):
    username = request.GET['username']
    user_exists = is_user_exists(username)

    try:
        if request.method == 'POST' and user_exists:
            user = CustomUser.objects.get(username=username)

            csv_file_path = user.generated_points.path
            plot_file_path = user.plot_with_points.path
            Points.remove_files(csv_file_path, plot_file_path)

            user.generated_points = ''
            user.plot_with_points = ''
            user.save(update_fields=['generated_points', 'plot_with_points'])

            new_csv_file_path, new_plot_file_path = generate_points_create_csv()
            user.generated_points.name = new_csv_file_path
            user.plot_with_points.name = new_plot_file_path
            user.save(update_fields=['generated_points', 'plot_with_points'])
            return HttpResponse('<h1>User was successfully regenerated new points</h1>')
    except Exception:
        print("Oops! Something went wrong")
