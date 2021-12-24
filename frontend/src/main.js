import { createApp } from 'vue'
import App from './App.vue'
import store from "./vuex/store"
import router from "./router/"

const app = createApp(App)

app.component('App', App)
app
  .use(store)
  .use(router)
app.mount('#app')