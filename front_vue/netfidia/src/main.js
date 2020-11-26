import '@fortawesome/fontawesome-free/css/all.min.css'
import 'bootstrap-css-only/css/bootstrap.min.css'
import 'mdbvue/lib/css/mdb.min.css'
import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'
import { NavbarPlugin } from 'bootstrap-vue'

Vue.use(NavbarPlugin)

Vue.config.productionTip = false

new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')

// import * as mdbvue from 'mdbvue'
// for (const component in mdbvue) {
//   Vue.component(component, mdbvue[component])
// }