var Empresas = Vue.component("home-view", {
    data: function () {
        return {
          empresas: [],
          success: [],
          errors: [],
        }
      },
    template: /*html*/`
    <div id="page-wrapper">


    <v-responsive color="grey lighten-2">
        <v-container fill-height>
            <v-layout align-center>
                <v-flex class="col-md-12">
                <div class="col-md-10">
                {{ user }}
                    <h3 class="display-3">Empresas Cadastradas <router-link class="btn btn-primary" to="/nova-empresa"><i class="fa fa-plus fa-fw"></i></router-link></h3>

                    <span class="subheading">Lista de empresas cadastradas no projeto.</span>
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


                    <div id="example-1">
                    <div class="panel panel-primary" v-for="(empresa, index) in empresas">
                        <div class="panel-heading">
                            {{ empresa.nome }}
                            <a href="#" class="pull-right" @click="delete_empresa(empresa.url, index)"><i class="fa fa-close fa-fw"></i></a>
                            <router-link class="pull-right"  :to="'/editar-empresa/'+ empresa.id"><i class="fa fa-edit fa-fw"></i></router-link>




                        </div>
                        <div class="panel-body">
                        <h3>Contato:</h3>
                        <p>Telefone: {{ empresa.telefone }}</p>
                        <p>E-mail: {{ empresa.email }}</p>
                        </div>
                        <div class="panel-footer">
                            Panel Footer
                        </div>
                    </div>



    </div>

                    </div>
                </v-flex>
            </v-layout>
        </v-container>
    </v-responsive>
    </div>
  `,
    props: [],
    $_veeValidate: {
        validator: "new"
    },
    created() {

        this.get_empresas();



    },
    methods: {
        get_empresas() {
            axios.get('http://localhost:8000/empresas/').then(response => {
            this.empresas = response.data;
            console.log(this.user)
        })
        },
        delete_empresa(url, id) {
            axios.delete(url).then(response => {
            this.empresas.splice(id, 1)
        })
        }


}
});
