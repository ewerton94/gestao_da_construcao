var NovoIndicador = Vue.component("novo-indicador-view", {
    data: function () {
        return {
            model: {},
            schema: {},           
            formOptions: {
                validateAfterLoad: false,
                validateAfterChanged: false
            },
            errors: [],
            success: []
            
        }
      },
    template: /*html*/`
    <div id="page-wrapper">

    
    <v-responsive color="grey lighten-2">
        <v-container fill-height>
            <v-layout align-center>
                <v-flex xs12>
                    <h3 class="display-3">Novo Indicador</h3>
               
                    <span class="subheading">Cadastro de novo indicador</span>
                    <v-divider class="my-3"></v-divider>
                    <ul v-if="errors && errors.length">
                        <li v-for="error of errors">
                        {{error.message}}
                        </li>
                    </ul>
                    <ul v-if="success && success.length">
                        
                        <li style="list-style-type: none;" v-for="message of success">
                        <div class="alert alert-success">
                        {{message}}. <a href="#/indicadores" class="alert-link">Ver lista de indicadores</a>.
                        </div>
                        
                        </li>
                    </ul>
                    <div v-if="schema.fields && schema.fields.length">
                    <vue-form-generator :schema="schema" :model="model" :options="formOptions"></vue-form-generator>
                    <v-btn large color="blue" class="mx-0" @click="send">Criar</v-btn>
                    </div>
                </v-flex>
            </v-layout>
        </v-container>
    </v-responsive>
    </div>
  `,
    props: ["title"],
    $_veeValidate: {
        validator: "new"
    },
    components:{
        "vue-form-generator": VueFormGenerator.component
    },
    created() {
    
        this.get_form_empresas()
    
    
    },
    methods: {
        get_form_empresas() {
            axios.get(api_link + 'criar_indicador/').then(response => {
            this.schema = response.data.schema;
            this.model = response.data.model;
        })},
        send() {
            this.loading = true;
            axios.post(api_link + 'criar_indicador/', this.model)
            .then(response => {
                app.success = [
                    'Indicador ' + response.data.nome + ' criada com sucesso!'
                ];
                console.log(app.success)
                this.success.push('Indicador ' + response.data.nome + ' criada com sucesso!')
                this.schema = {};
                this.model = {};
                
            })
            .catch(e => {
              this.errors.push(e)
            })
    }}
});








