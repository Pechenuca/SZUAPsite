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
        type: Float32Array,
        required: true
      },
      lat: {
        type: Float32Array,
        required: true
      },
      zoom: {
        type: Int8Array,
        required: true
      }
    },
    setup(props) {
      let latlon = ref([])
      let zoom = ref([])
      
      latlon.value = [
        props.lat, 
        props.lon
      ]

      zoom.value = [props.zoom]


      const ymaps = window.ymaps
        ymaps.ready(() => {
          console.log('Map loaded')
          new ymaps.Map('yandex-map', {
              center: [
                latlon.value[0], 
                latlon.value[1]
              ],
              zoom: zoom.value[0]
          }, {
              searchControlProvider: 'yandex#search'
          })
        })

      return {
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