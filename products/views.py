from django.db.models import Min, Max
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
        sort = self.request.GET.get('sort')
        color = self.request.GET.get('color')
        size = self.request.GET.get('size')
        price = self.request.GET.get('price')
        if size:
            qs = qs.filter(sizes__id=size)

        if color:
            qs = qs.filter(colors__id=color)

        if price:
            price_from, price_to = price.split(';')
            qs = qs.filter(real_price__gte=price_from, real_price__lte=price_to)

        if sort:
            if sort == 'price':
                qs = qs.order_by('real_price')
            elif sort == '-price':
                qs = qs.order_by('-real_price')
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
        context['sizes'] = ProductSizeModel.objects.all()
        context['colors'] = ProductColorModel.objects.all()

        context['min_price'], context['max_price'] = ProductModel.objects.aggregate(
            Min('real_price'),
            Max('real_price')).values()
        return context


class ProductsDetailView(DetailView):
    template_name = 'shop-details.html'
    model = ProductModel
