from django import forms


class ContactFormOne(forms.Form):
    first_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={'placeholder': 'Name', 'class': 'input inp-inp'}
        )
    )
    email_address = forms.EmailField(
        max_length=150,
        min_length=4,
        help_text='Укажите ваш действующий Email',
        widget=forms.EmailInput(
            attrs={'placeholder': 'E-mail', 'class': 'input inp-inp'}
        )
    )
    phone = forms.CharField(
        max_length=70,
        min_length=11,
        help_text='Укажите в формате: +7 000 000-00-00',
        widget=forms.TextInput(
            attrs={'placeholder': 'Phone', 'class': 'input inp-inp'}
        )
    )
    message = forms.CharField(
        max_length=2000,
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': 'Message', 'class': 'input-wrapper-textarea', 'cols': '30', 'rows': '10'}
        )
    )


class ContactFormTwo(forms.Form):
    first_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={'placeholder': 'Name', 'class': 'input _req'}
        )
    )
    email_address = forms.EmailField(
        max_length=150,
        min_length=4,
        help_text='Укажите ваш действующий Email',
        widget=forms.EmailInput(
            attrs={'placeholder': 'E-mail', 'class': 'input _req _email'}
        )
    )
    phone = forms.CharField(
        max_length=70,
        min_length=11,
        help_text='Укажите в формате: +7 000 000-00-00',
        widget=forms.TextInput(
            attrs={'placeholder': 'Phone', 'class': 'input _req'}
        )
    )
    message = forms.CharField(
        max_length=2000,
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': 'Message', 'cols': '30', 'rows': '10'}
        )
    )

