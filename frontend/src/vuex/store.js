import { createStore } from "vuex";

export default createStore({
  state: {
    currentDivId: '',
    backendBaseUrlDev: 'http://127.0.0.1:8000/api/v1/',
    backendBaseUrlProd: 'http://127.0.0.1/api/v1/'
  },
  mutations: {
    currentDiv(state, id) {
        state.currentDivId = id
    }
  },
  getters: {
    currentDiv: state => {
      return state.currentDivId
    },
    baseUrl: state => {
      //return state.backendBaseUrlDev
      return state.backendBaseUrlProd
    }
  }
})