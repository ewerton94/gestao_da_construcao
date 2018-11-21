var ResultadoIndicadores = Vue.component("home-view", {
    data: function () {
        return {
          resultados: [],
          data: [{ x: [1, 3], y: [2, 4] }],
            layout: {},
            options: {}
        }
      },
    template: /*html*/`
    <div id="page-wrapper">

    
    <v-responsive color="grey lighten-2">
        <v-container fill-height>
            <v-layout align-center>
                <v-flex xs12>
                    <h3 class="display-3">Empresas Cadastradas <router-link class="btn btn-primary" to="/nova-empresa"><i class="fa fa-plus fa-fw"></i></router-link></h3>
               
                    <span class="subheading">Lista de empresas cadastradas no projeto.</span>
                    <v-divider class="my-3"></v-divider>
                    <vue-plotly :data="data" :layout="layout" :options="options"/>
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
    
        this.get_resultados()
    
    
    },
    components:{
        "vue-plotly": VuePlotly
    },
    methods: {
        get_resultados() {
            var data = [{
                x: ['giraffes', 'orangutans', 'monkeys'],
                y: [20, 14, 23], 
                name: 'SF Zoo',
                type: 'bar',
                marker: {color: '#19d3f3'}
              }, {
                x: ['giraffes', 'orangutans', 'monkeys'],
                y: [12, 18, 29], 
              name: 'LA Zoo', 
              type: 'bar',
                marker: {color: '#ab63fa'} 
              }];
              
              var layout = {
                plot_bgcolor: '#F5F7FA',
                paper_bgcolor: '#F5F7FA',
                width: 500
              };
              var graph = document.getElementById('myDiv');
              Plotly.plot(graph, data, layout);
        }


}
});

