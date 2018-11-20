var Home = Vue.component("home-view", {
    data: function () {
        return {
          empresas: []
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
                    <div class="title mb-3">Veja resultados!</div>
                    
                    <ul id="example-1">
  <li v-for="item in empresas">
    {{ item.cnpj }}
  </li>
</ul>
                    <v-btn large color="blue" class="mx-0">See more</v-btn>
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
    
        this.get_empresas()
    
    
    },
    methods: {
        get_empresas() {
            axios.get('http://localhost:8000/empresas/').then(response => {
            this.empresas = response.data;
        })}
    }

});

