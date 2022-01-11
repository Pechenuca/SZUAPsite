import { createStore } from "vuex";

export default createStore({
  state: {
    currentDivId: '',
    backendBaseUrlDev: 'http://127.0.0.1:8000/api/v1/',
    backendBaseUrlProd: 'http://127.0.0.1/api/v1/',
    isMapLoaded: false
  },
  mutations: {
    currentDiv(state, id) {
        state.currentDivId = id
    },
    currentIsMapLoaded(state, isMapLoaded) {
      state.isMapLoaded = isMapLoaded
    }
  },
  getters: {
    currentDiv: state => {
      return state.currentDivId
    },
    baseUrl: state => {
      //return state.backendBaseUrlDev
      return state.backendBaseUrlProd
    },
    isMapLoaded: state => {
      return state.isMapLoaded
    }
  }
})