from django_vueformgenerator.schema import Schema

SCHEMA_DICT = {
    'number': 'input',
    'text': 'input'
}

EXTRA_FIELDS_DICT = {
    'email': 'email'
}

def get_schema(form):
    schema = Schema().render(form)
    for field in schema['schema']['fields']:
        field['inputType'] = EXTRA_FIELDS_DICT.get(field['model'], field['type'])
        field['type']= SCHEMA_DICT[field['type']]
    return schema