from django.shortcuts import render
from myapp_testmodel.models import Cust
from django.contrib import messages

def cust_profile(request):
    var = {
                "firstname" : "มานี",
                "lastname" : "ใจกล้า",
    }
    custrecord = Cust()
    custrecord.firstname = "มานี"
    custrecord.lastname = "ใจกล้า"
    try:
        custrecord.save()
        messages.success(request, "บันทึกข้อมูลสำเร็จ!!!")
    except:
        messages.success(request, "บันทึกข้อมูลไม่สำเร็จ!!!")
    finally:
        return render(request, "MyCust.html",var)

