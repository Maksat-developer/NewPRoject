from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



from .models import Bboard, Rubric
from .forms import BboardForm
from .serializers import RubricSerializer, BboardSerializer


# def index(request):
#     message = "Список обьявлений\r\n\r\n\r\n"
#     for bboard in Bboard.objects.order_by('-published'):
#         message += bboard.title + '\r\n' + bboard.content + '\r\n\r\n'
#     return HttpResponse(message, content_type='text/plain; charset=utf-8')
#


def index(request):
    bbs = Bboard.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs': bbs, 'rubrics': rubrics}
    return render(
        request=request,
        template_name='bboard/index.html',
        context=context)


def by_rubric(request, rubric_id):
    bbs = Bboard.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {
        'bbs': bbs,
        'rubrics': rubrics,
        'current_rubric': current_rubric}
    return render(
        request=request,
        template_name='bboard/by_rubric.html',
        context=context)




class BboardCreateView(CreateView):
    template_name = 'bboard/create.html'
    form_class = BboardForm
    success_url = reverse_lazy('index')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context
    


@api_view(['GET', 'POST'])
def api_rubrics(request):
    if request.method == 'GET':
        rubrics = Rubric.objects.all()
        serializer = RubricSerializer(rubrics, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = RubricSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def api_rubric_detail(request, pk):
    rubric = Rubric.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = RubricSerializer(rubric)
        return Response(serializer.data)
    elif request.method == 'PUT' or request.method == 'PATCH':
        serializer = RubricSerializer(rubric, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        rubric.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
