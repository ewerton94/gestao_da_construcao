var NovoEmpreendimento = Vue.component("novo-empreendimento-view", {
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
            <v-flex class="col-md-12">
            <div class="col-md-10">
                    <h3 class="display-3">Novo Empreendimento</h3>

                    <span class="subheading">Cadastro de novo empreendimento</span>
                    <v-divider class="my-3"></v-divider>
                    <ul v-if="errors && errors.length" style="list-style-type:none;padding:0;">
                        <li v-for="error of errors">
                        <v-alert
                        :value="true"
                        type="error"
                        >
                        {{error.message}}
                        </li>
                    </ul>

                    <ul v-if="success && success.length" style="list-style-type:none;padding:0;">
                        <li v-for="message of success">
                        <v-alert
                        :value="true"
                        type="success"
                        >
                        {{message}}. <a href="#/empreendimentos" style="color:white;">Ver lista de empreendimentos</a>.
                        </v-alert>
                        </li>
                    </ul>
                    
                    <div v-if="schema.fields && schema.fields.length">
                    <vue-form-generator :schema="schema" :model="model" :options="formOptions"></vue-form-generator>
                    <v-btn large color="blue" class="mx-0" @click="send">Criar</v-btn>
                    </div>
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
            axios.get(api_link + 'criar_empreendimento/').then(response => {
            this.schema = response.data.schema;
            this.model = response.data.model;
        })},
        send() {
            this.loading = true;
            axios.post(api_link + 'criar_empreendimento/', this.model)
            .then(response => {
                app.success = [
                    'Empreendimento ' + response.data.nome + ' criada com sucesso!'
                ];
                console.log(app.success)
                this.success.push('Empreendimento ' + response.data.nome + ' criada com sucesso!')
                this.schema = {};
                this.model = {};

            })
            .catch(e => {
              this.errors.push(e)
            })
    }}
});
