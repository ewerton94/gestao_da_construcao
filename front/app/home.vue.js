var Home = Vue.component("home-view", {
    data: function () {
        return {
          pesquisador: localStorage.getItem('user-pesquisador'),
          cliente: localStorage.getItem('user-cliente'),
          success: [],
          errors: [],
          user: JSON.parse(localStorage.getItem('user')) || {}
        }
      },
    template: /*html*/`
    <div id="page-wrapper">


    <v-responsive color="grey lighten-2">
        <v-container fill-height>
            <v-layout align-center>
                <v-flex>
                    <h3 class="display-3">Indicadores de Qualidade de obras</h3>

                    <span class="subheading">Este site foi criado com o objetivo de facilitar a alimentação e processamento de dados de Benchmarking de empresas da Construção Civil de Maceió.</span>
                    <v-divider class="my-3"></v-divider>
                    <h1>Ações</h1>
                    
                    <ul v-if="pesquisador > 0 | cliente > 0">


                    <v-card
                    class="mx-auto"
                    max-width="100%"
                    tile
                  >
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
                  <v-list dense>

                  <v-list-tile v-if="user.add_permissions.indexOf('empresa')!=-1" :href="'#/empresas'">
                  <v-list-tile-action>
                    <v-icon>store</v-icon>
                  </v-list-tile-action>
                  <v-list-tile-content>
                    <v-list-tile-title>Gerenciar empresas</v-list-tile-title>
                  </v-list-tile-content>
                </v-list-tile>
                <v-list-tile v-if="user.add_permissions.indexOf('empreendimento')!=-1" :href="'#/empreendimentos'">
                  <v-list-tile-action>
                    <v-icon>business</v-icon>
                  </v-list-tile-action>
                  <v-list-tile-content>
                    <v-list-tile-title>Gerenciar Empreendimentos</v-list-tile-title>
                  </v-list-tile-content>
                </v-list-tile>

                <v-list-tile v-if="pesquisador > 0" @click="atualizar_calculos">
                  <v-list-tile-action>
                    <v-icon>refresh</v-icon>
                  </v-list-tile-action>
                  <v-list-tile-content>
                    <v-list-tile-title>Atualziar cálculos</v-list-tile-title>
                  </v-list-tile-content>
                </v-list-tile>



                <v-list-tile v-if="cliente > 0" :href="'#/resposta-indicadores'">
                  <v-list-tile-action>
                    <v-icon>send</v-icon>
                  </v-list-tile-action>
                  <v-list-tile-content>
                    <v-list-tile-title>Enviar resultados</v-list-tile-title>
                  </v-list-tile-content>
                </v-list-tile>



                <v-list-tile v-if="cliente > 0":href="'#/resultados-indicadores'">
                  <v-list-tile-action>
                    <v-icon>multiline_chart</v-icon>
                  </v-list-tile-action>
                  <v-list-tile-content>
                    <v-list-tile-title>Ver resultados (benchmarking)</v-list-tile-title>
                  </v-list-tile-content>
                </v-list-tile>

                <v-list-tile v-if="cliente > 0":href="'#/resultados-indicadores-internos'">
                  <v-list-tile-action>
                    <v-icon>bar_chart</v-icon>
                  </v-list-tile-action>
                  <v-list-tile-content>
                    <v-list-tile-title>Ver resultados internos</v-list-tile-title>
                  </v-list-tile-content>
                </v-list-tile>


                </v-list>
                    </v-card>


                        

                    </ul>






                </v-flex>
            </v-layout>
        </v-container>
    </v-responsive>
    </div>
  `,
    props: ["ff"],
    $_veeValidate: {
        validator: "new"
    },
    mounted() {
      console.log(this.user)
    },
    methods: {

        atualizar_calculos(){
            axios.get(api_link + 'atualizar_calculos', {})
            .then(response => {
                //app.success = [
                //    'Resposta enviada com sucesso!'
                //];
                //console.log(app.success)
                
                this.success = [response.data];
       
                
            })
            .catch(e => {
              console.log(e)
              this.errors.push(e)
            })
        }
    }


});
