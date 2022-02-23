from django.shortcuts import render

# Create your views here.
def test_templates1(request):
    templates_var = {
        "name" : "มานี",
        "surname" : "ใจกล้า",
        "tel" : "0816548686"
    }
    return render(request, "MyTemplatesVar.html", templates_var)

def test_templates2(request):
    templates_var2 = {
        "sport" : ["Basketball", "Tennis", "Table Tennis", "Volleyball"],
        "subject" : {"Math" : 98, "English" : 80, "Scince" : 79}
    }
    return render(request, "MyTemplatesVar2.html", templates_var2)