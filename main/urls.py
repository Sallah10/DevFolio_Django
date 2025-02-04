from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
	path('', views.IndexView.as_view(), name="home"),
	path('contact/', views.ContactView.as_view(), name="contact"),
	path('portfolio/', views.PortfolioView.as_view(), name="portfolio"),
	path('portfolio/<slug:slug>', views.PortfolioDetailView.as_view(), name="portfolio-details"),
	path('blog/', views.BlogView.as_view(), name="blogs"),
	path('blog/<slug:slug>', views.BlogDetailView.as_view(), name="blog-details"),
	]