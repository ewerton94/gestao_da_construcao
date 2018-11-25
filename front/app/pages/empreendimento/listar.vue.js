var Empreendimentos = Vue.component("home-view", {
    data: function () {
        return {
          empreendimentos: [],
          errors: [],
          success: []
        }
      },
    template: /*html*/`
    <div id="page-wrapper">


    <v-responsive color="grey lighten-2">
        <v-container fill-height>
            <v-layout align-center>
                <v-flex >
                <div class="col-md-10">
                    <h3  class="display-3">Empreendimentos Cadastrados <router-link class="btn btn-primary" to="/novo-empreendimento"><i class="fa fa-plus fa-fw"></i></router-link></h3>

                    <span class="subheading">Lista de empreendimentos cadastrados no projeto.</span>
                    <v-divider class="my-3"></v-divider>
                    <ul v-if="errors && errors.length">
                        <li v-for="error of errors">
                        {{error.message}}
                        </li>
                    </ul>
                    <ul v-if="success && success.length">
                        <li v-for="message of success">
                        <v-alert
                        :value="true"
                        type="success"
                        >
                        {{message}}.
                        </v-alert>
                        </li>
                    </ul>


                    <div id="example-1" >
                    <div class="panel panel-primary p-0 m-0" v-for="(empreendimento, index) in empreendimentos">
                        <div class="panel-heading">
                            {{ empreendimento.nome }}
                            <a href="#" class="pull-right" @click="delete_empresa(empresa.id, index)"><i class="fa fa-close fa-fw"></i></a>
                            <router-link class="pull-right"  :to="'/editar-empreendimento/'+ empreendimento.id"><i class="fa fa-edit fa-fw"></i></router-link>




                        </div>
                        <div class="panel-body">
                        <h3>Contato:</h3>
                        <p>Local: {{ empreendimento.nome }}</p>
                        <p>Local: {{ empreendimento.empresa.nome }}</p>
                        </div>
                        <div class="panel-footer">
                            Panel Footer
                        </div>
                    </div>



    </div>
                    <v-btn large color="blue" class="mx-0">See more</v-btn>
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
    created() {

        this.get_empreendimento()


    },
    methods: {
        get_empreendimento() {
            axios.get(api_link + 'empreendimentos/').then(response => {
            this.empreendimentos = response.data;
        })
        },
        delete_empreendimento(url, id) {
            axios.delete(url).then(response => {
            this.empreendimentos.splice(id, 1)
        })
        }


}
});
