from django import forms
from .models import Cliente, User, Empresa, Empreendimento, Referencia, TipoIndicador, Pesquisador, Indicador, Resultado

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['nome', 'email', 'cnpj', 'telefone']

class EmpreendimentoForm(forms.ModelForm):

    class Meta:
        model = Empreendimento
        fields = ['nome', 'empresa', 'endereco']

class EmpreendimentoRestritoForm(forms.ModelForm):

    class Meta:
        model = Empreendimento
        fields = ['nome', 'endereco']

class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = '__all__'

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = '__all__'

class ReferenciaForm(forms.ModelForm):

    class Meta:
        model = Referencia
        fields = '__all__'

class IndicadorForm(forms.ModelForm):

    class Meta:
        model = Indicador
        fields = '__all__'

class TipoIndicadorForm(forms.ModelForm):

    class Meta:
        model = TipoIndicador
        fields = '__all__'

class ResultadoForm(forms.ModelForm):

    class Meta:
        model = Resultado
        fields = '__all__'

class PesquisadorForm(forms.ModelForm):

    class Meta:
        model = Pesquisador
        fields = '__all__'



# Ewerton Escreve aqui em baixo:
from .models import Resultado
class ResultadoForm(forms.ModelForm):
    class Meta:
        model = Resultado
        fields = ['empreendimento', 'referencia']

    def __init__(self, empresa, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if empresa is not None:
            self.fields['empreendimento'].queryset = self.fields['empreendimento'].queryset.filter(empresa=empresa)
