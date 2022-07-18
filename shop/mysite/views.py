from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import F
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.cache import cache_page
from django.views.generic import ListView, DetailView
from django.core.mail import send_mail, BadHeaderError

# Create your views here.
from cart.forms import CartAddProductForm
from mysite.models import Product, Category
from orders.forms import ContactForm


def index(request):
    products = Product.objects.all()
    title = 'Moschino'
    context = {
        'products': products,
        'title': title,
    }
    return render(request, 'mysite/index.html', context=context)


def product_by_category(request, slug):
    if request.GET.get('orderby') is None:
        ordering = '-name'
    else:
        ordering = request.GET.get('orderby')
    products = Product.objects.filter(category__slug=slug).all().order_by(ordering)
    count_of_products = products.count()
    title = str(Category.objects.filter(slug=slug).first())
    context = {
        'products': products,
        'title': title,
        'count_of_products': count_of_products,
    }
    return render(request, 'mysite/shop.html', context=context)


def shop(request):
    # Сортировка. Если не назначена, то по имени
    if request.GET.get('orderby') is None:
        ordering = '-name'
    else:
        ordering = request.GET.get('orderby')
    products = Product.objects.all().order_by(ordering)
    title = 'Shop'
    count_of_products = products.count()
    ''' не знаю как не дублировать код пагинатора без классов
    при создании отдельной функции не выходит обработать исключения
    а без них пагинация не работает
    '''
    paginator = Paginator(products, 8)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    context = {
        'page_obj': page_obj,
        'products': products,
        'title': title,
        'count_of_products': count_of_products,
    }
    return render(request, 'mysite/shop.html', context=context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart_product_form = CartAddProductForm()
    product.views += 1
    product.save()
    product.refresh_from_db()
    # print(product.views)
    context = {
        'product': product,
        'cart_product_form': cart_product_form
    }
    return render(request, 'mysite/single_product.html', context=context)


def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'mysite/about.html', context=context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = 'ТЕСТОВОЕ СООБЩЕНИЕ'
            body = {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())
            try:
                send_mail(subject, message, 'asdma@mail.com', ['uxax4@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Некорректный заголовок')
            # messages.add_message(request, messages.SUCCESS, 'Ваше сообщение отправлено')
            redirect('contact')
    form = ContactForm()
    return render(request, "mysite/contact.html", {'form': form})

# class IndexView(ListView):
#     model = Product
#     template_name = 'mysite/index.html'
#     paginate_by = 6
#     context_object_name = 'products'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Moschino'
#         # print(context)
#         return context
#
#
# class ProductByCategory(ListView):
#     model = Product
#     template_name = 'mysite/shop.html'
#     context_object_name = 'products'
#     paginate_by = 8
#     allow_empty = False
#
#     def get_queryset(self):
#         return Product.objects.filter(category__slug=self.kwargs['slug'])
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = str(context['products'][0].category)
#         return context
#
#
# class ProductDetailView(DetailView):
#     model = Product
#     template_name = 'mysite/single_product.html'
#     context_object_name = 'product'
#     allow_empty = False
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         self.object.views = F('views') + 1
#         self.object.save()
#         self.object.refresh_from_db()
#         print(context)
#         return context
#
#     def post(self, request, *args, **kwargs):
#         return self.get(request, *args, **kwargs)
#
#
# class ShopView(ListView):
#     model = Product
#     template_name = 'mysite/shop.html'
#     paginate_by = 8
#     context_object_name = 'products'
#
#     def get_ordering(self):
#         ordering = self.request.GET.get('orderby')
#         return ordering
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Shop'
#         return context
