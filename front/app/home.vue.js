var final = Vue.component("reactive-chart", {
  data: function () {
      return {
        chart: {
      uuid: "um",
      traces: [
        {
          y: [1,5,4,5,5,4,5,6,5,1,2,1,0,2,3,5,4,1,8,5,12,1,5],
          line: {
            color: "#5e9e7e",
            width: 5,
            shape: "bar"
          }
        }
      ],
      layout: {},
      type: 'bar'
    }
      }
    },
  props: ["htrhr"],
  methods:{
    teste: function(){
      console.log(this.$refs);
    }
  },
  template: '<div  ref="um"></div>',
  mounted() {
    this.teste();
    var data = [
  {
    x: ['giraffes', 'orangutans', 'monkeys'],
    y: [20, 14, 23],
    type: 'bar'
  }
];

    Plotly.plot(this.$refs.um, data);
  },
  watch: {
    chart: {
      handler: function() {
        Plotly.react(
          this.$refs[this.chart.uuid],
          this.chart.traces,
          this.chart.layout,
          this.type
        );
      },
      deep: true
    }
  }
});

var Home = Vue.component("home-view", {
    data: function () {
        return {
          chart: {
        uuid: "123",
        traces: [
          {
            y: [],
            line: {
              color: "#5e9e7e",
              width: 4,
              shape: "line"
            }
          }
        ],
        layout: {}
      }
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
                    <reactive-chart></reactive-chart>
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
    },
    components: {
        "reactive-chart": final
      }

});
