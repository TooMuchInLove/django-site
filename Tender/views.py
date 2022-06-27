#from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#from django.http import HttpResponse
#from django.conf import settings

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.shortcuts import render, redirect
from .models  import Tender, User, Region
from .forms   import TenderForm
from datetime import datetime


def tender(request):
    return render(request, 'main.html')


# СПИСОК АУКЦИОНОВ
class AuctionListView(ListView):
    # model = Tender

    template_name = 'auctions/tender.html'

    context_object_name = 'auctions'

    extra_context = {
        'site_title' : 'БСС.TENDER | АУКЦИОНЫ',
        'header_title' : 'АУКЦИОНЫ'
    }

    menu = [
        'Мои торги', 'Подкачка', 'Создать', 'Решения нет',
        'Ввести в 1С', 'Введено в 1С', 'Полный перечень',
    ]

    def get_context_data(self, *, object_list=None, **kwargs):
        # Берём уже существующий context из класса
        context = super().get_context_data(**kwargs)
        context['menu'] = self.menu
        context['users'] = User.objects.all()
        context['regions'] = Region.objects.all()

        return context

    def get_queryset(self):
        # users      = User.objects.all()
        # regs       = Region.objects.all()
        # count_recd = Tender.objects.all().count()
        # count_load = 5
        value      = 'all'
        auctions   = None

        if self.request.method == 'GET':
            user_form = self.request.GET.get('user', '')
            reg_form  = self.request.GET.get('region', '')
            num_form  = self.request.GET.get('num_auc', '')

            try:
                if user_form == value and reg_form == value and not num_form:
                    auctions = Tender.objects.all()# [:count_load]
                elif user_form == value and reg_form != value and not num_form:
                    reg = Region.objects.get(nameR=reg_form)
                    auctions = Tender.objects.filter(regionFK=reg).all()
                elif user_form != value and reg_form == value and not num_form:
                    user = User.objects.get(nameU=user_form)
                    auctions = Tender.objects.filter(userAddFK=user).all()
                elif user_form == value and reg_form == value and num_form:
                    auctions = Tender.objects.filter(id=num_form).all()
                elif user_form != value and reg_form == value and num_form:
                    user = User.objects.get(nameU=user_form)
                    auctions = Tender.objects.filter(id=num_form).filter(userAddFK=user).all()
                elif user_form == value and reg_form != value and num_form:
                    reg = Region.objects.get(nameR=reg_form)
                    auctions = Tender.objects.filter(id=num_form).filter(regionFK=reg).all()
                elif user_form != value and reg_form != value and not num_form:
                    user = User.objects.get(nameU=user_form)
                    reg = Region.objects.get(nameR=reg_form)
                    auctions = Tender.objects.filter(regionFK=reg).filter(userAddFK=user).all()
                elif user_form != value and reg_form != value and num_form:
                    user = User.objects.get(nameU=user_form)
                    reg = Region.objects.get(nameR=reg_form)
                    auctions = Tender.objects.filter(regionFK=reg).filter(userAddFK=user).filter(id=num_form).all()
            except:
                auctions = None

        elif self.request.method == 'POST':
            if self.request.POST.get('btn__add'):
                pass
        else: # not GET or POST
            pass

        return auctions


# УДАЛЯЕМ ЭЛЕМЕНТ ИЗ СПИСКА (АУКЦИОН)
class DeleteAuctionView(DeleteView):
    model = Tender

    # success_url = '/tender/auctions/'

    # по умолчанию используется pk для ключей (у меня id)
    pk_url_kwarg = 'id'

    template_name = 'auctions/tender.html'

    # context_object_name = 'auction'

    # extra_context = {
    #     'site_title': 'БСС.TENDER | АУКЦИОНЫ',
    #     'header_title': 'АУКЦИОНЫ'
    # }
    #
    # menu = [
    #     'Мои торги', 'Подкачка', 'Создать', 'Решения нет',
    #     'Ввести в 1С', 'Введено в 1С', 'Полный перечень',
    # ]

    def get_context_data(self, *, object_list=None, **kwargs):
        # Берём уже существующий context из класса
        context = super().get_context_data(**kwargs)
        # context['menu'] = self.menu

        # context['actions'] = kwargs.get('actions') # context['actions']
        # print(kwargs.get('actions'))
        # print(context['actions'])
        # print(self.context_object_name)

        return context

    def get_queryset(self):
        auction = Tender.objects.filter(id=self.kwargs.get('id')).all()
        # auction.delete()
        # print(auction, ': delete')

        return auction # redirect('/tender/auctions/')


# ИНФОРМАЦИЯ ОБ АУКЦИОНЕ
class AuctionDetailView(DetailView):
    # model = Tender

    # form_class = TenderForm()

    # по умолчанию используется pk для ключей (у меня id)
    pk_url_kwarg = 'id'

    template_name = 'auctions/auction_info.html'

    context_object_name = 'auction'

    extra_context = {
        'site_title' : 'БСС.TENDER | ИНФОРМАЦИЯ ОБ АУКЦИОНЕ',
        'header_title' : 'ИНФОРМАЦИЯ ОБ АУКЦИОНЕ'
    }

    menu = [
        'Информация об аукционе'
    ]

    def get_context_data(self, *, object_list=None, **kwargs):
        # Берём уже существующий context из класса
        context = super().get_context_data(**kwargs)
        context['menu'] = self.menu
        context['form'] = self.form_class
        context['message'] = self.msg

        return context

    def get_queryset(self):
        auctions = Tender.objects.filter(id=self.kwargs.get('id'))
        self.msg = (None, None)

        if self.request.method == 'GET':
            print('GET')
        elif self.request.method == 'POST':
            print('POST')
            if self.request.POST.get('btn__edit'): # edit records
                self.form_class = TenderForm(self.request.POST)
                if self.form_class.is_valid():
                    for auction in auctions:
                        auction.userAddFK  = self.form_class.cleaned_data['userAddFK']
                        auction.startsSumT = self.form_class.cleaned_data['startsSumT']
                        # Если даты нет, то ставим текущую;
                        if self.form_class.cleaned_data['dateAddT'] == None:
                            auction.dateAddT = datetime.now()
                        else:
                            auction.dateAddT = self.form_class.cleaned_data['dateAddT']
                        if self.form_class.cleaned_data['dateActionT'] == None:
                            auction.dateActionT = datetime.now()
                        else:
                            auction.dateActionT = self.form_class.cleaned_data['dateActionT']
                        if self.form_class.cleaned_data['dateDocT'] == None:
                            auction.dateDocT = datetime.now()
                        else:
                            auction.dateDocT = self.form_class.cleaned_data['dateDocT']
                        auction.numT     = self.form_class.cleaned_data['numT']
                        auction.regionFK = self.form_class.cleaned_data['regionFK']
                        # auction.save()
                        self.msg = ('Данные изменены!', 'green')
                else:
                    self.msg = ('Неверные данные!', 'red')
            else:
                pass
        else: # not GET or POST
            pass

        self.form_class = TenderForm()
        for auction in auctions:
            self.form_class.initial = {
                'userAddFK'   : auction.userAddFK,
                'startsSumT'  : auction.startsSumT,
                'dateAddT'    : auction.dateAddT.strftime("%Y-%m-%dT%H:%M"),
                'dateActionT' : auction.dateActionT.strftime("%Y-%m-%dT%H:%M"),
                'dateDocT'    : auction.dateDocT.strftime("%Y-%m-%dT%H:%M"),
                'numT'        : auction.numT,
                'regionFK'    : auction.regionFK,
            }

        return auctions # redirect('/tender/auctions/')


# СПИСОК ТОРГОВ
class TradeListView(ListView):
    # model = <ModelName>

    # pk_url_kwarg = 'id'

    template_name = 'auctions/trade.html'

    # context_object_name = '<trades>'

    extra_context = {
        'site_title' : 'БСС.TENDER | ТОРГИ',
        'header_title' : 'ТОРГИ'
    }

    menu = [
        'Торги 1', 'Торги 2', 'Торги 3', 'Торги 4', 'Торги 5'
    ]

    def get_context_data(self, *, object_list=None, **kwargs):
        # Берём уже существующий context из класса
        context = super().get_context_data(**kwargs)
        context['menu'] = self.menu

        return context

    def get_queryset(self):
        return 0