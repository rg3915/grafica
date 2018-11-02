from django import forms
from .models import Cliente, Fornecedor


class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ('nome', 'email', 'telefone', 'cnpj')

    def save(self, commit=True):
        instance = super(ClienteForm, self).save(commit=False)
        instance.tipo = 'c'
        if commit:
            instance.save()
        return instance


class FornecedorForm(ClienteForm):

    class Meta:
        model = Fornecedor
        fields = ClienteForm.Meta.fields

    def save(self, commit=True):
        instance = super(ClienteForm, self).save(commit=False)
        instance.tipo = 'f'
        if commit:
            instance.save()
        return instance
