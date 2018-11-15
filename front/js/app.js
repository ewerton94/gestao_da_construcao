const NotFound = { template: '<p>Página não encontrada</p>' }
const Home = { template: '<p>Página Inicial</p>' }
const About = { template: '<p>Sobre</p>' }

const routes = {
  '/': Home,
  '/sobre': About
}

new Vue({
  el: '#app',
  data: {
    currentRoute: window.location.pathname
  },
  computed: {
    ViewComponent () {
      return routes[this.currentRoute] || NotFound
    }
  },
  render (h) { return h(this.ViewComponent) }
})

var app = new Vue({
    el: '#app',
    data: {
        results: [],
        message: 'Hello Vue!',
        currentRoute: window.location.pathname
        
    },
    methods: {
        get_empresas: function(){
            axios.get('http://localhost:8000/empresas/').then(response => {
            this.results = response.data;
        })
        }


    },
    computed: {
        ViewComponent () {
          return routes[this.currentRoute] || NotFound
        }
      },
    mounted() {
    
       this.get_empresas()


    },
    render (h) { return h(this.ViewComponent) }
    


});

 setInterval( () => app.get_empresas(), 3000)