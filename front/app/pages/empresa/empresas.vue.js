var Empresas = Vue.component("home-view", {
    data: function () {
        return {
          empresas: [],
          success: [],
          errors: [],
        }
      },
    template: /*html*/`
            <v-layout align-left>
            <v-flex align-left>


                    <h3 class="display-3">Empresas Cadastradas

                    <v-tooltip float-right>
                      <v-btn
                        slot="activator"
                        href="#/nova-empresa"
                        icon
                        large

                      >
                        <v-icon large>add_box</v-icon>
                      </v-btn>
                      <span>Adicionar empresa</span>
                    </v-tooltip>

                    </h3>


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

<div class="p-2" v-for="(empresa, index) in empresas">
<v-flex py-2>
                    <v-card class="elevation-12">
                      <v-toolbar dark color="primary">
                        <v-toolbar-title>{{ empresa.nome }}</v-toolbar-title>


                        <v-spacer></v-spacer>
                        <v-tooltip bottom>
                          <v-btn
                            slot="activator"
                            href="#"
                            icon
                            large

                            @click="delete_empresa(empresa.url, index)"
                          >
                            <v-icon large>close</v-icon>
                          </v-btn>
                          <span>Remover</span>
                        </v-tooltip>

                        <v-tooltip bottom>
                          <v-btn
                            slot="activator"
                            :href="'#/editar-empresa/'+ empresa.id"
                            icon
                            large

                          >
                            <v-icon large>edit</v-icon>
                          </v-btn>
                          <span>Editar</span>
                        </v-tooltip>
                      </v-toolbar>
                      <v-card-text>


                      <h3>Contato:</h3>
                      <p>Telefone: {{ empresa.telefone }}</p>
                      <p>E-mail: {{ empresa.email }}</p>

                      </v-card-text>
                    </v-card>
                    </v-flex>

</div>


</v-flex>

            </v-layout>

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
            axios.get(api_link + 'empresas/').then(response => {
            this.empresas = response.data;
            console.log(this.empresas)
        })
        },
        delete_empresa(url, id) {
            axios.delete(url).then(response => {
            this.empresas.splice(id, 1)
        })
        }


}
});
