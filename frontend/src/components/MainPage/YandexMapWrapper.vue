<template>
  <div class="yandex-map">
    <div id='yandex-map'>
    </div>
  </div>
</template>

<script>
  import { ref } from 'vue'

  export default {
    name: "YandexMapWrapper",
    props: {
      lon: {
        type: String,
        required: true
      },
      lat: {
        type: String,
        required: true
      },
      zoom: {
        type: String,
        required: true
      }
    },
    setup(props) {
      let latlon = ref([])
      let rzoom = ref([])
      
      latlon.value = [
        props.lat, 
        props.lon
      ]

      rzoom.value = [props.zoom]
      return {
        latlon,
        rzoom
      }
    },
    methods: {
      loadMap() {
        const ymaps = window.ymaps
        ymaps.ready(() => {
          new ymaps.Map('yandex-map', {
              center: [
                this.latlon[0], 
                this.latlon[1]
              ],
              zoom: this.rzoom[0]
          }, {
              searchControlProvider: 'yandex#search'
          })
        })
      }
    },
    beforeMount () {
      if(this.$store.getters.isMapLoaded == false) {
       this.loadMap() 
       this.$store.commit("currentIsMapLoaded", true)  
      }
    }
  }
</script>

<style>
  
  .yandex-map {
    height: 650px;
    width: 1050px;
  }

  #yandex-map {
    width: 100%;
    height: 100%;
  }
</style>