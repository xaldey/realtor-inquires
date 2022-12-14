from django.shortcuts import render, redirect
from django.contrib import messages
from .fill_templates import fill_template


# from django.core.mail import send_mail    #отключил возможность отправки заявки по почте

from .models import Contact


def contact(request):
    if request.method == "POST":
        listing_id = request.POST["listing_id"]
        listing = request.POST["listing"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        message = request.POST["message"]
        user_id = request.POST["user_id"]
        realtor_email = request.POST["realtor_email"]

        # Check if user has made inquiry already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(
                listing_id=listing_id, user_id=user_id
            )
            if has_contacted:
                messages.error(
                    request, "Вы уже запросили информацию по этому объявлению."
                )
                return redirect("/listings/" + listing_id)

        contact = Contact(
            listing=listing,
            listing_id=listing_id,
            last_name=last_name,
            email=email,
            phone=phone,
            message=message,
            user_id=user_id,
        )
        contact.save()

        # Send mail
        """ send_mail(
            "Заявка по объявлению",
            "Пришла заявка по объявлению "
            + listing
            + ". Авторизуйтесь на сайте для получения более подробной информации.",
            "test_2004@mail.ru",
            [realtor_email, "test_2004@mail.ru"],
            fail_silently=False,
        ) """

        messages.success(
            request,
            "Ваш запрос направлен менеджеру. В ближайшее время он с вами свяжется.",
        )
        fill_template(request)

        return redirect("/listings/" + listing_id)
