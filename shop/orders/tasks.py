from celery import shared_task
from django.core.mail import send_mail

from orders.models import Order
from shop.celery import app


@app.task
def order_created(order_id):
    print('==========В ТАСКУ ЧТО-ТО ПРИШЛО ==========')
    order = Order.objects.get(id=order_id)
    subject = f'Order {order_id}'
    message = f'Dear {order.first_name}\n\n You have successfully placed an order.' \
              f'Your order {order.id}'
    mail_sent = send_mail(subject, message,
                          'admin@eshop.com',
                          [order.email], )
    print('EMAIL УЛЕТЕЛ --------->>>>>>')
    return mail_sent
