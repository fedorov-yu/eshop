from django import template
from mysite.models import Category

register = template.Library()


@register.inclusion_tag('mysite/list_categories.html')
def show_categories():
    categories = Category.objects.all()
    return {'categories': categories}
