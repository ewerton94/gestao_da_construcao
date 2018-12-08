// 0. If using a module system (e.g. via vue-cli), import Vue and VueRouter
// and then call `Vue.use(VueRouter)`.

// 1. Define route components.
// These can be imported from other files

Vue.use(VueRouter);

const Bar = { template: '<div id="page-wrapper"><div>bar</div></div>' }

// 2. Define some routes
// Each route should map to a component. The "component" can
// either be an actual component constructor created via
// `Vue.extend()`, or just a component options object.
// We'll talk about nested routes later.
const routes = [
  { path: '/', component: Home },
  { path: '/bar', component: Bar },
  { path: '/resposta-indicadores', component: RespostaIndicadores },
  { path: '/resultados-indicadores', component: ResultadoIndicadores },
  { path: '/empresas', component: Empresas, name:'empresas' },
  { path: '/nova-empresa', component: NovaEmpresa },
  { path: '/editar-empresa/:id', component: EditarEmpresa, name: 'editar-empresa'},
  { path: '/empreendimentos', component: Empreendimentos },
  { path: '/novo-empreendimento', component: NovoEmpreendimento },
  { path: '/editar-empreendimento/:id', component: EditarEmpreendimento, name: 'editar-empreendimento'},
  { path: '/clientes', component: Clientes },
  { path: '/novo-cliente', component: NovoCliente },
  { path: '/editar-cliente/:id', component: EditarCliente, name: 'editar-cliente'},
  { path: '/users', component: Users },
  { path: '/novo-user', component: NovoUser },
  { path: '/editar-user/:id', component: EditarUser, name: 'editar-user'},
  { path: '/referencias', component: Referencias },
  { path: '/novo-referencia', component: NovoReferencia },
  { path: '/editar-referencia/:id', component: EditarReferencia, name: 'editar-referencia'},
  { path: '/indicadores', component: Indicadores },
  { path: '/novo-indicador', component: NovoIndicador },
  { path: '/editar-indicador/:id', component: EditarIndicador, name: 'editar-indicador'},
  { path: '/tipoindicadores', component: TipoIndicadores },
  { path: '/novo-tipoindicador', component: NovoTipoIndicador },
  { path: '/editar-tipoindicador/:id', component: EditarTipoIndicador, name: 'editar-tipoindicador'},
  { path: '/resultados', component: Resultados },
  { path: '/novo-resultado', component: NovoResultado },
  { path: '/editar-resultado/:id', component: EditarResultado, name: 'editar-resultado'},
  { path: '/pesquisadors', component: Pesquisadors },
  { path: '/novo-pesquisador', component: NovoPesquisador },
  { path: '/editar-pesquisador/:id', component: EditarPesquisador, name: 'editar-pesquisador'},


]

// 3. Create the router instance and pass the `routes` option
// You can pass in additional options here, but let's
// keep it simple for now.
const router = new VueRouter({
  routes // short for `routes: routes`
})

// 4. Create and mount the root instance.
// Make sure to inject the router with the router option to make the
// whole app router-aware.




store = new Vuex.Store({
  state: {
    authUser: {},
    isAuthenticated: false,
    jwt: localStorage.getItem('token'),
    endpoints: {
      // TODO: Remove hardcoding of dev endpoints
      obtainJWT: api_link+'obtain_token/',
      refreshJWT: api_link + 'refresh_token/',
      baseUrl: api_link
    }
  },

  mutations: {
    setAuthUser(state, {
      authUser,
      isAuthenticated
    }) {
      Vue.set(state, 'authUser', authUser)
      Vue.set(state, 'isAuthenticated', isAuthenticated)
    },
    updateToken(state, newToken) {
      // TODO: For security purposes, take localStorage out of the project.
      localStorage.setItem('token', newToken);
      state.jwt = newToken;
    },
    removeToken(state) {
      // TODO: For security purposes, take localStorage out of the project.
      localStorage.removeItem('token');
      state.jwt = null;
    }
  }
})









const app = new Vue({
  router,
  store,
  data:{
    errors: [],
    model:{},
    success: [],
    user: {'username': ''},
    pronto: false
  },
  created(){
    console.log(this.user.username);
    this.get_usuario_logado();

  },
  components: {
    "vue-form-generator": VueFormGenerator.component
  },
  methods: {
    get_usuario_logado(){

        axios.defaults.withCredentials = true;

          axios.get(api_link + 'obtem_usuario_logado/', ).then(response => {
          this.user = response.data.user;
          this.pronto = true;

          console.log('ai')
      }).catch(e => {

        console.log(e)
        this.pronto = true;
      })

    },
    login(){
      console.log('login')
      axios.post(api_link + 'entrar/', this.model)
      .then(response => {
          this.success.push('Cliente ' + response.data.nome + ' editada com sucesso!')
          console.log(response.data)
          localStorage.setItem('user-token', response.data.token);
          window.location.reload();

      })
      .catch(e => {
        console.log()
        this.errors.push(e)
        localStorage.removeItem('user-token');
      })

    },
    logout(){
      axios.get(api_link + 'sair/')
      .then(response => {
          console.log(response.data)
          localStorage.removeItem('user-token');
          window.location.reload();


      })
      .catch(e => {
        console.log()
        this.errors.push(e)
        localStorage.removeItem('user-token');
        window.location.reload();
      })




    }
  }
}).$mount('#app')

// Now the app has started!
