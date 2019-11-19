var Empreendimentos = Vue.component("listar-empreendimento-view", {
    data: function () {
        return {
          empreendimentos: [],
          errors: [],
          success: []
        }
      },
    template: /*html*/`


            <v-layout align-center>
                <v-flex >
                





























                    <h3 class="display-3">Empreendimentos Cadastrados

                    <v-tooltip float-right>
                      <v-btn
                        slot="activator"
                        href="#/novo-empreendimento"
                        icon
                        large

                      >
                        <v-icon large>add_box</v-icon>
                      </v-btn>
                      <span>Adicionar empreendimento</span>
                    </v-tooltip>
                    <v-tooltip float-right>
                    <v-btn
                        slot="activator"
                        @click="gerar_codigos" 
                        icon
                        large

                      >
                        <v-icon large>refresh</v-icon>
                      </v-btn>
                      <span>Gerar códigos</span>
                    </v-tooltip>

                    </h3>


                    <span class="subheading">Lista de empreendimentos cadastradas no projeto.</span>
                    <v-divider class="my-3"></v-divider>
                    <ul v-if="errors && errors.length" style="list-style-type:none;padding:0;">
                        <li v-for="error of errors">
                        {{error.message}}
                        </li>
                    </ul>
                    <ul v-if="success && success.length" style="list-style-type:none;padding:0;">
                        <li v-for="message of success">
                        <v-alert
                        :value="true"
                        type="success"
                        >
                        {{message}}.
                        </v-alert>
                        </li>
                    </ul>

<div class="p-2" v-for="(empreendimento, index) in empreendimentos">
<v-flex py-2>
                    <v-card class="elevation-12">
                      <v-toolbar dark color="primary">
                        <v-toolbar-title>{{ empreendimento.nome }} ({{ empreendimento.codigo }})</v-toolbar-title>


                        <v-spacer></v-spacer>
                        <v-tooltip bottom>
                          <v-btn
                            slot="activator"
                            href="#"
                            icon
                            large

                            @click="delete_empreendimento(empreendimento.id, index)"
                          >
                            <v-icon large>close</v-icon>
                          </v-btn>
                          <span>Remover</span>
                        </v-tooltip>

                        <v-tooltip bottom>
                          <v-btn
                            slot="activator"
                            :href="'#/editar-empreendimento/'+ empreendimento.id"
                            icon
                            large
                         
                          >
                            <v-icon large>edit</v-icon>
                          </v-btn>
                          <span>Editar</span>
                        </v-tooltip>
                      </v-toolbar>
                      <v-card-text>


                      <h3>Dados:</h3>
                        <p>Empresa: {{ empreendimento.empresa }}</p>
                        <p>Local: {{ empreendimento.empresa.nome }}</p>
                     
                        

                      </v-card-text>
                    </v-card>
                    </v-flex>

</div>


                </v-flex>
            </v-layout>
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
