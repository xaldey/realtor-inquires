from docxtpl import DocxTemplate, InlineImage
from docx.shared import Mm
from datetime import datetime
import qrcode


def fill_template(request):

    tstamp = datetime.now()

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    nomDogFull = "КС10-123"
    zakazSummaReal = 8000

    link_QR = (
        "ST00012|Name=ИП+Бондарь+Виктор+Михайлович|PersonalAcc=40802810826060000842|BankName=ФИЛИАЛ+РОСТОВСКИЙ+АО+АЛЬФА-БАНК|BIC=046015207|CorrespAcc=30101810500000000207|PayeeINN=232800397040|Purpose="
        + nomDogFull
        + "|Sum="
        + str(zakazSummaReal * 100)
    )

    img = qr.add_data(link_QR)
    # type(img)  # qrcode.image.pil.PilImage
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("media/qr_for_invoice.png")
    doc = DocxTemplate("templates/template.docx")

    qr_image = InlineImage(
        doc, image_descriptor="media/qr_for_invoice.png", width=Mm(28)
    )

    data = {
        "name": "Имя",
        "phone": "8-918-103-2344",
        "listing": "Title of listing",
        "message": "Big message",
        "timestamp": tstamp,
        "dog_num": "КС10-",
        "aparts_num": 27,
        "link_QR": link_QR,
        "qr_image": qr_image,
    }

    # paragraph = doc.add_paragraph("Lorem ipsum dolor sit amet.")
    doc.render(data)
    doc.save("%Y/%m/%d/" + str(nomDogFull) + "_new.docx")


# fill_template()
