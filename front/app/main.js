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
  { path: '/empresas', component: Empresas },
  { path: '/nova-empresa', component: NovaEmpresa },
  { path: '/editar-empresa/:id', component: EditarEmpresa, name: 'editar-empresa'},
  { path: '/empreendimentos', component: Empresas },
  { path: '/novo-empreendimento', component: NovoEmpreendimento },
  { path: '/editar-empreendimento/:id', component: EditarEmpresa, name: 'editar-empresa'}


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

const app = new Vue({
  router,
  components: {
    "vue-form-generator": VueFormGenerator.component
  },
}).$mount('#wrapper')

// Now the app has started!