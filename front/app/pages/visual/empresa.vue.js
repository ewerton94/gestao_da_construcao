var ResultadoIndicadoresParaEmpresa = Vue.component("home-view", {
    data: function () {
        return {
          resultados: [],
          loading: false,
          data: [{ x: [1, 3], y: [2, 4] }],
            layout: {},
            options: {},
            indicadores: [],
            indicador_atual: '',
            errors: []
        }
      },
    template: /*html*/`
    <div id="page-wrapper">


  
    
            <flex-box align-center sm>
                <v-responsive sm>
                    <h3 class="display-3">Resultados gerais </h3>


                    <span class="subheading">{{ indicador_atual }}</span>
                    <v-divider class="my-3"></v-divider>
                    <v-select
                      v-model="indicador_atual"
                      :items="indicadores"
                      :rules="[v => !!v || 'Item is required']"
                      label="Escolha o indicador"
                      required
                      
                      v-on:change="troca_resultados(indicador_atual)"
                    ></v-select>
                    <v-flex width="500" max-height="300"><div  ref="um"></div></v-flex>
                    
                </v-responsive>
            </flex-box>


    </div>
  `,
    props: ["title"],
    $_veeValidate: {
        validator: "new"
    },
    created() {
      this.get_resultados();
      


    },
    methods: {
      
      get_resultados(){
        this.loading = true;
            axios.get(api_link + 'resultados/por_referencia/', {})
            .then(response => {
                //app.success = [
                //    'Resposta enviada com sucesso!'
                //];
                //console.log(app.success)
                
                this.resultados = response.data;
                var that = this;
                this.resultados.forEach(function(r, index) {
                  that.indicadores.push(r.nome);
              });
          
                
                this.troca_resultados(this.resultados[0].nome);
                console.log(this.resultados);
                
            })
            .catch(e => {
              this.errors.push(e)
            })

      },
      troca_resultados(nome_indicador) {
        var that = this;
        if (that.indicador_atual.length){

          that.resultados.forEach(function(r, index) {
            var comp = r.nome + ' - ' + nome_indicador;
            console.log(comp)
            if (r.nome == nome_indicador){
              var resultado = r;
              that.plota_resultados(resultado, false);
                          
            }
        });

        } else {
          var resultado = this.resultados[0];
          this.plota_resultados(resultado, true)
        }
      },
        plota_resultados(resultado, novo) {
          
          console.log(window.innerWidth)
          
          var trace1 = {
            x: resultado.legendas,
            y: resultado.valores,
            mode: 'lines+markers',
            name: 'Média'
          };
          
          var trace2 = {
            x: resultado.legendas,
            y: resultado.tcpo,
            mode: 'lines',
            name: 'TCPO'
          };
          
        
          
          var data = [ trace1, trace2 ];
          
          

              var layout = {
                width: .9*window.innerWidth,
                title: resultado.nome,
                plot_bgcolor: '#F5F7FA',
                paper_bgcolor: '#F5F7FA',
      
                xaxis: {
               title: 'Empreendimentos',
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
              if (novo) {

                Plotly.plot(this.$refs.um, data, layout);

              } else {
                Plotly.newPlot(this.$refs.um, data, layout);
                Plotly.update(this.$refs.um, data, layout);
                
              }
              var that=this;
              window.onresize = function() {
                Plotly.relayout(that.$refs.um, {
                  width: .9*window.innerWidth
                })
              }
              

              
        }


}
});
