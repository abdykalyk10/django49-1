from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseBadRequest


class WorkAgeMiddleware(MiddlewareMixin):
    def process_requeВst(self, request):
        if request.path == '/register/' and request.method == 'POST':
            work_years = int(request.POST.get('work_years'))
            if 0 < work_years <= 2:
                request.salary = 30000
            elif 3 <= work_years <= 5:
                request.salary = 50000
            elif work_years >= 6:
                request.salary = 70000

        elif request.path == '/register/' and request.method == 'GET':
            setattr(request, 'club', 'Ошибка сервера')

