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
                    <h3 class="display-3">Resultados gerais</h3>

                    <span class="subheading">Resultados gerais de janero a abril.</span>
                    <v-divider class="my-3"></v-divider>
                    <div ref="um"></div>
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
    mounted() {

        this.get_resultados()


    },
    methods: {
        get_resultados() {
            var data = [{
                x: ['A', 'B', 'C'],
                y: [20, 14, 23],
                name: 'Janeiro',
                type: 'bar',
                marker: {color: '#19d3f3'}
              },
              {
                x: ['A', 'B', 'C'],
                y: [12, 18, 29],
              name: 'Fevereiro',
              type: 'bar',
                marker: {color: '#ab63fa'}
              },
              {
                x: ['A', 'B', 'C'],
                y: [22, 20, 25],
              name: 'Março',
              type: 'bar',
                marker: {color: '#5463fa'}
              },
              {
                x: ['A', 'B', 'C'],
                y: [15, 25, 18],
              name: 'Abril',
              type: 'bar',
                marker: {color: '#bac3fa'}
              }
            ];

              var layout = {
                title: 'Reboco interno',
                plot_bgcolor: '#F5F7FA',
                paper_bgcolor: '#F5F7FA',
                width: "100%",
                xaxis: {
               title: 'empresas',
               titlefont: {
                 family: 'Arial',
                 size: 18,
                 color: '#7f7f7f'
               }
             },
             yaxis: {
               title: 'HH/m²',
               titlefont: {
                 family: 'Arial',
                 size: 18,
                 color: '#7f7f7f'
               }
             }
              };

              Plotly.plot(this.$refs.um, data, layout);
        }


}
});
