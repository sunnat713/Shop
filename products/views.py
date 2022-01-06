
from django.views.generic import ListView, DetailView
from .models import *


class ProductsListView(ListView):
    template_name = 'shop.html'
    paginate_by = 3

    def get_queryset(self):

        qs = ProductModel.objects.order_by('-pk')
        q = self.request.GET.get('q')
        cat = self.request.GET.get('cat')
        brand = self.request.GET.get('brand')
        tag = self.request.GET.get('tag')
        if tag:
            qs = qs.filter(tags__id=tag)

        if q:
            qs = qs.filter(title__icontains=q)

        if cat:
            qs = qs.filter(category_id=cat)

        if brand:
            qs = qs.filter(brand_id=brand)

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CategoryModel.objects.all()
        context['brands'] = BrandModel.objects.all()
        context['tags'] = ProductTagModel.objects.all()
        return context


class ProductsDetailView(DetailView):
    model = ProductModel
