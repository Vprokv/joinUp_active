from .models import PhoneCode

@app.task
def send_sms_async(identifier: int):
    code = PhoneCode.objects.filter(pk=identifier).first()
    if code:
        provider: SMSProviderBase = Test()
        provider.send_private_sms(code.phone, code.code)