from indicadores.models import Resultado
count = 0
for e, r, i, ca, cl in Resultado.objects.all().values_list('empreendimento_id', 'referencia_id', 'indicador_id', 'campo_indicador_id', 'conferido_por_id').distinct():
    r = Resultado.objects.filter(
        conferido_por_id=cl,
        referencia_id=r,
        empreendimento_id=e,
        indicador_id=i,
        campo_indicador_id=ca,
    )
    if r.count()>1:
        r.exclude(id=r.last().id).delete()
        count +=1

print("Encontrados", count, 'dados duplicados.')
