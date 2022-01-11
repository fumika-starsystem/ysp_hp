from django import forms
from django.core.mail import EmailMessage
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse


class InquiryForm(forms.Form):
    name = forms.CharField(label='お名前', max_length=30)
    subject = forms.CharField(label='タイトル', max_length=30)
    message = forms.CharField(label='メッセージ', widget=forms.Textarea)
    from_email = forms.EmailField(label='メールアドレス')
    recipient_list = ["ysp.southaichi1006@gmail.com"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control col-9'
        self.fields['name'].widget.attrs['placeholder'] = 'お名前をここに入力してください。'

        self.fields['from_email'].widget.attrs['class'] = 'form-control col-11'
        self.fields['from_email'].widget.attrs['placeholder'] = 'メールアドレスをここに入力してください。'

        self.fields['subject'].widget.attrs['class'] = 'form-control col-11'
        self.fields['subject'].widget.attrs['placeholder'] = 'タイトルをここに入力してください'

        self.fields['message'].widget.attrs['class'] = 'form-control col-12'
        self.fields['message'].widget.attrs['placeholder'] = 'メッセージをここに入力してください'

    def send_email(self):
        if self.is_valid():
            subject = self.cleaned_data['subject']
            message = self.cleaned_data['message']
            from_email = self.cleaned_data['from_email']
            recipient_list = ["ysp.southaichi1006@gmail.com"]

        try:
            send_mail(subject, message, from_email, recipient_list)

        except BadHeaderError:
            return HttpResponse('無効なヘッダーが見つかりました。')


        # name = self.cleaned_data['name']
        # from_email = self.cleaned_data['from_email']
        # subject = self.cleaned_data['subject']
        # message = self.cleaned_data['message']
        # recipient_list = ["ysp.southaichi1006@gmail.com"]
        # send_mail(subject, message, from_email, recipient_list)

        #
        # subject = 'お問い合わせ　{}'.format(subject)
        # message = '送信者名:{0}\nメールアドレス:{1}\nメッセージ:\n{2}'.format(name, from_email, message)
        # from_email = 'ysp.southaichi1006@gmail.com'
        # to_list = [
        #     'ysp.southaichi1006@gmail.com'
        # ]
        # cc_list = [
        #     from_email
        # ]
        #
        # message = EmailMessage(subject=subject, body=message, from_email=from_email, to=to_list, cc=cc_list)
        # message.send()

