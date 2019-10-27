var RespostaIndicadores = Vue.component("resposta-indicadores-view", {
    data: function () {
        return {
            forms: [],    
            model: {},   
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
                <v-flex class="col-md-12">
                    <h3 class="display-3">Respoder com informações de indicadores</h3>
               
                    <span class="subheading">Resposta mensal</span>
              
                    <v-divider class="my-3"></v-divider>
                    <ul v-if="errors && errors.length">
                        <li v-for="error of errors">
                        {{error.message}}
                        </li>
                    </ul>
                    <ul v-if="success && success.length">
                        
                        <li style="list-style-type: none;" v-for="message of success">
                        <div class="alert alert-success">
                        {{message}}. <a href="#/" class="alert-link">Voltar ao início</a>.
                        </div>
                        
                        </li>
                    </ul>
                    <div v-if=" !success.length">
                    <div v-for="form of forms" class="my-5">
                    <template >
  <div v-if="form.titulo">
    <v-toolbar color="blue darken-1" dark>
      <v-toolbar-title>{{ form.titulo }}</v-toolbar-title>

      <div class="flex-grow-1"></div>

     

      
    </v-toolbar>
  </div>
  </template>
                    <vue-form-generator :schema="form.schema" :model="model" :options="formOptions"></vue-form-generator>

                    </div>
                    <v-btn large color="blue" class="mx-0" @click="send">Enviar</v-btn>
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
    
        this.get_form()
    
    
    },
    methods: {
        get_form() {
            axios.get(api_link + 'form_indicadores/').then(response => {
                this.forms = response.data
            //this.schema = response.data.schema;
            console.log(this.forms);
            //this.model = response.data.model;
        })},
        send() {
            this.loading = true;
            axios.post(api_link + 'form_indicadores/', this.model)
            .then(response => {
                app.success = [
                    'Resposta enviada com sucesso!'
                ];
                console.log(app.success)
                this.success.push('Resposta enviada com sucesso!')
                this.schema = {};
                this.model = {};
                
            })
            .catch(e => {
              this.errors.push(e)
            })
    }}
});








