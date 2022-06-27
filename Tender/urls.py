from django.shortcuts import render
from django.urls import path
from . import views

from .views import (
    TradeListView,
    AuctionListView,
    DeleteAuctionView,
    AuctionDetailView,
)

address = [
    '', # null
    'auctions/', # список аукционов
    'auctions/<int:id>/auction-delete/', # удаление аукциона
    'auctions/<int:id>/auction-info/', # просмотр аукциона
    'trade/', # список торгов
]

urlpatterns = [
    path(address[0], views.tender, name='tender'),
    path(address[1], AuctionListView.as_view(), name='aucs'),
    path(address[2], DeleteAuctionView.as_view(), name='auc-delete'),
    path(address[3], AuctionDetailView.as_view(), name='auc-info'),
    path(address[4], TradeListView.as_view(), name='trade'),
]