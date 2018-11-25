var Empreendimentos = Vue.component("listar-empreendimento-view", {
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
                    <h3  class="display-3">Empreendimentos Cadastrados <router-link class="btn btn-primary" to="/novo-empreendimento"><i class="fa fa-plus fa-fw"></i></router-link> <a class="btn btn-primary" @click="gerar_codigos"><i class="fa fa-refresh fa-fw"></i></a></h3>

                    <span class="subheading">Lista de empreendimentos cadastrados no projeto.</span>
                    <v-divider class="my-3"></v-divider>
                    <ul v-if="errors && errors.length">
                        <li v-for="error of errors">
                        {{error.message}}
                        </li>
                    </ul>
                    <ul v-if="success && success.length">
                    <li style="list-style-type: none;" v-for="message of success">
                    <div class="alert alert-success">
                    {{message}}.
                    </div>

                    </li>
                    </ul>


                    <div v-if="empreendimentos && empreendimentos.length">
                    <div class="panel panel-primary p-0 m-0" v-for="(empreendimento, index) in empreendimentos">
                        <div class="panel-heading">
                            {{ empreendimento.nome }}
                            <a href="#" class="pull-right" @click="delete_empreendimento(empreendimento.id, index)"><i class="fa fa-close fa-fw"></i></a>
                            <router-link class="pull-right"  :to="'/editar-empreendimento/'+ empreendimento.id"><i class="fa fa-edit fa-fw"></i></router-link>




                        </div>
                        <div class="panel-body">
                        <h3>Dados:</h3>
                        <p>Empresa: {{ empreendimento.empresa }}</p>
                        <p>Local: {{ empreendimento.empresa.nome }}</p>
                        </div>
                        <div class="panel-footer">
                            {{ empreendimento.codigo }}
                        </div>
                    </div>



                    </div>

                    <div v-else>
                    <div class="alert alert-danger">
                    Sem empreendimentos.
                    </div>
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
    created() {

        this.get_empreendimento()


    },
    methods: {
        get_empreendimento() {
            axios.get(api_link + 'empreendimentos/').then(response => {
            this.empreendimentos = response.data;
        })
        },
        gerar_codigos() {
          console.log('Tentando gerar_codigos')
            axios.post(api_link + 'criar_codigos/', {gerar: 'ok'}).then(response => {
            this.success.push(response.data.message);
            this.get_empreendimento()
        })
        },
        delete_empreendimento(id, idx) {
            axios.delete(api_link + 'empreendimentos/' + id).then(response => {
            this.empreendimentos.splice(idx, 1)
        })
        }


}
});
