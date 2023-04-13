from django.core.mail import send_mail

from item.models import Item
from lovely_checker import settings
from useraccount.models import BecomeOwnerQuestionnaire


def send_city_mail(*args, **kwargs):
    mail_subject = "It`s Lovely Checker`s moderator info!"
    send_mail(
        subject=mail_subject,
        message=kwargs['message'],
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[kwargs['email']],
        fail_silently=False,
    )


def send_item_mail(*args, **kwargs):
    mail_subject = "It`s Lovely Checker`s moderator info!"
    item = Item.objects.select_related('author').get(pk=kwargs['pk'])
    send_mail(
        subject=mail_subject,
        message=f'Ваш объект "{item.title}" не прошел модерацию.\n'
                f'Описание проблемы: \n'
                f'{kwargs["message"]}\n'
                f'С уважением, Lovely Checker!',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[item.author.email],
        fail_silently=False,
    )
    Item.objects.get(pk=kwargs['pk']).delete()


def send_item_success_mail(*args, **kwargs):
    mail_subject = "Поздравляю! Ваш объект прошел модерацию"
    item = Item.objects.select_related('author').get(pk=kwargs['pk'])
    send_mail(
        subject=mail_subject,
        message=f'Ваш объект "{item.title}" прошел модерацию и стал доступным.\n'
                f'С уважением, Lovely Checker!',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[item.author.email],
        fail_silently=False,
    )


def send_user_failure_mail(*args, **kwargs):
    mail_subject = "Вы не прошли модерацию!"
    send_mail(
        subject=mail_subject,
        message=f'Ваша заявка не прошла модерацию. Попробуйте снова!\n'
                f'По данной причине:\n'
                f'{kwargs["message"]}\n'
                f'С уважением, Lovely Checker!',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[kwargs['email']],
        fail_silently=False,
    )
