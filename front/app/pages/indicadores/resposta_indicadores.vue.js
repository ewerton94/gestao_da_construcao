function makeid (length) {
    var result = ''
    var characters =
      'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    var charactersLength = characters.length
    for (var i = 0; i < length; i++) {
      result += characters.charAt(Math.floor(Math.random() * charactersLength))
    }
    return result
  }

var RespostaIndicadores = Vue.component("resposta-indicadores-view", {
    data: function () {
        return {
            forms: [],    
            model: {codigo: makeid(15)},   
            formOptions: {
                validateAfterLoad: false,
                validateAfterChanged: false
            },
            errors: [],
            success: [],
            loading: true,
            
            
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
                    <ul v-if="errors && errors.length" style="list-style-type:none;padding:0;">
                        <li v-for="error of errors">
                        <v-alert
                        :value="true"
                        type="error"
                        >
                        {{error.message}}
                        </v-alert>
                        </li>
                    </ul>

                    <ul v-if="success && success.length" style="list-style-type:none;padding:0;">
                        <li v-for="message of success">
                        <v-alert
                        :value="true"
                        type="success"
                        >
                        {{message}}. <a href="#/" class="alert-link">Voltar ao início</a>.
                        </v-alert>
                        </li>
                    </ul>
                    <v-flex
               
                v-if="loading"
              >
                Carregando... <v-progress-circular
                indeterminate
                color="primary"
                
              ></v-progress-circular>
              </v-flex>
                    
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
                    <v-btn v-if="!loading" large color="blue" class="mx-0" @click="send">Enviar</v-btn>
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
    async created() {
    
        await this.get_form()
    
    
    },
    methods: {
        async get_form() {
            await axios.get(api_link + 'form_indicadores/').then(async response => {
                this.forms = await response.data
                this.loading = false;
          
        })},
        async send() {
            this.loading = true;
            await axios.post(api_link + 'form_indicadores/', this.model)
            .then(response => {
                this.loading = false;
                app.success = [
                    'Resposta enviada com sucesso!'
                ];
                console.log(app.success)
                this.errors = []
                this.success.push('Resposta enviada com sucesso!')
                this.schema = {};
                this.model = {};
                $("html, body").animate({ scrollTop: 0 }, "slow");
                
            })
            .catch(async e => {
                this.loading = false;
                let data = await e.response.data;
                console.log(data)
              this.errors = [data]
              $("html, body").animate({ scrollTop: 0 }, "slow");
            })
    }}
});








