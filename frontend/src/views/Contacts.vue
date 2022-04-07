<template>
  <div>
    <TitleBlock label="Контакты" />
    <div class="contacts-block-wrapper">
      <YandexMapWrapper 
        lon=37.64
        lat=55.76
        zoom=10
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