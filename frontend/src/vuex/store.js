import { createStore } from "vuex";

export default createStore({
  state: {
    currentDivId: ''
  },
  mutations: {
    currentDiv(state, id) {
        state.currentDivId = id
    }
  },
  getters: {
    currentDiv: state => {
      return state.currentDivId
    }
  }
})