from django import forms
from .models import Empresa, Empreendimento

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['nome', 'email', 'cnpj', 'telefone']

class EmpreendimentoForm(forms.ModelForm):
    
    class Meta:
        model = Empreendimento
        fields = '__all__'




# Ewerton Escreve aqui em baixo:
from .models import Resultado 
class ResultadoForm(forms.ModelForm):
    class Meta:
        model = Resultado
        fields = ['empreendimento', 'referencia', 'conferido_por']
