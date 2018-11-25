var EditarEmpreendimento = Vue.component("editar-empreendimento-view", {
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
                    <h3 class="display-3">Editar Empreendimento</h3>

                    <span class="subheading">Edição dos dados da Empreendimento</span>
                    <v-divider class="my-3"></v-divider>
                    <ul v-if="errors && errors.length">
                        <li v-for="error of errors">
                        {{error.message}}
                        </li>
                    </ul>
                    <ul v-if="success && success.length">

                        <li style="list-style-type: none;" v-for="message of success">
                        <div class="alert alert-success">
                        {{message}}. <a href="#/empreendimentos" class="alert-link">Ver lista de empreendimentos</a>.
                        </div>

                        </li>
                    </ul>
                    <div v-if="schema.fields && schema.fields.length">
                    <vue-form-generator :schema="schema" :model="model" :options="formOptions"></vue-form-generator>
                    <v-btn large color="blue" class="mx-0" @click="send">Atualizar</v-btn>
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


        this.get_form_empreendimentos(this.$route.params.id)


    },
    methods: {
        get_form_empreendimentos(id) {
            axios.get(api_link + 'form_empreendimentos/' + id).then(response => {
            this.schema = response.data.schema;
            this.model = response.data.model;
        })},
        send() {
            var id = this.$route.params.id;
            this.loading = true;
            axios.post(api_link + 'form_empreendimentos/' + id, this.model)
            .then(response => {
                this.success.push('Empreendimento ' + response.data.nome + ' editada com sucesso!')
                this.schema = {};
                this.model = {};

            })
            .catch(e => {
              this.errors.push(e)
            })
    }}
});
