var Home = Vue.component("home-view", {
    data: function () {
        return {
          pesquisador: localStorage.getItem('user-pesquisador'),
          cliente: localStorage.getItem('user-cliente')
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
                    <ul>

{{ pesquisador }}{{ cliente }}
                        <div v-if="pesquisador.length"><li><router-link class="" to="/empresas">Gerenciar empresas</router-link></li></div>
                        <div v-if="pesquisador.length"><li><router-link class="" to="/empreendimentos">Gerenciar Empreendimentos</router-link></li></div>
                        <div v-if="cliente.length"><li><router-link class="" to="/resposta-indicadores">Enviar resultados</router-link></li></div>
                        <div ><li><router-link class="" to="/resultados-indicadores">Ver resultados</router-link></li></div>


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
    },
    methods: {}


});
