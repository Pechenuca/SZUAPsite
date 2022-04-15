<template>
  <div>
    <TitleBlock label="Контакты" />
    <div class="contacts-block-wrapper">
      <YandexMapWrapper 
        lat=59.94
        lon=30.32
        zoom=12
        class="yandex-map"
        
        
      />
    </div>
  </div>
</template>

<script>
  import TitleBlock from "@/components/MainPage/TitleBlock.vue"
  import YandexMapWrapper from "@/components/MainPage/YandexMapWrapper.vue"

  export default {
    name: "Contacts",
    components: {TitleBlock, YandexMapWrapper},
    setup() {
      return {
      }
    },
  }
</script>

<style>
  .contacts-block-wrapper {
    display: flex;
    flex-direction: row;
    justify-content: space-around;
  }
</style>