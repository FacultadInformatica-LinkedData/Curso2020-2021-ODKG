from django.shortcuts import render
from rdflib import Graph, Namespace
from rdflib.plugins.sparql import prepareQuery

from .models import RDFStore
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.views.generic.base import View
from django.core.paginator import Paginator
from .models import store


class Home(View):
    def get(self, request, *args, **kwargs):
        # res = store.allData()
        template = loader.get_template('index.html')
        context = {
            'name': "Mirfarzam",
        }
        return render(request, 'index.html', {})


class Country(View):
    def get(self, request, countryName, *args, **kwargs):
        caes = store.getCAEofCountry(countryName)
        paginator = Paginator(caes, 10)
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)

        return render(request, 'singleCountry.html', {
            "country": store.getCountry("http://eit-upm-opendata.com/ted/Country/" + countryName),
            'page_obj': page_obj,
        })


class Town(View):
    def get(self, request, townName, *args, **kwargs):
        caes = store.getCAEofTown(townName)
        paginator = Paginator(caes, 10)
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)

        return render(request, 'singleTown.html', {
            "town": store.getLocality("http://eit-upm-opendata.com/ted/Town/" + townName),
            'page_obj': page_obj,
        })


class ContractNoticeList(View):
    def get(self, request, *args, **kwargs):
        objects = store.getAllContractNotices(request.GET.get('pt', None), request.GET.get('ct', None))
        paginator = Paginator(objects, 10)
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)
        procedureTypes = store.getProcedureTypes()
        contractTypes = store.getContractTypes()
        return render(request, 'list.html',
                      {
                          'page_obj': page_obj,
                          'procedure_types': procedureTypes,
                          'contract_types': contractTypes,
                          'selected_pt': request.GET.get('pt', None),
                          'selected_ct': request.GET.get('ct', None)
                      })


class ContractNotice(View):
    def get(self, request, contractId, *args, **kwargs):
        template = loader.get_template('singleContractNotice.html')
        result = store.getContractNotice(str(contractId))
        context = {
            'contarctNotice': result,
        }
        return HttpResponse(template.render(context, request))


class ContractBodyList(View):
    def get(self, request, *args, **kwargs):
        objects = store.getAllContractBodies(request.GET.get('name', None))
        paginator = Paginator(objects, 10)
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)
        return render(request, 'list2.html',
                      {
                          'page_obj': page_obj,
                          'selected_name': request.GET.get('name', "")
                      })


class ContractBody(View):
    def get(self, request, contractId, *args, **kwargs):
        template = loader.get_template('singleContractBody.html')
        result = store.getContractBodies(str(contractId))
        context = {
            'contarctBody': result,
            'country': store.getCountry(result.addressCountry),
            'locality': store.getLocality(result.addressLocality)
        }
        return HttpResponse(template.render(context, request))
