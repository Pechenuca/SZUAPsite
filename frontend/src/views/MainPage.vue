<template>
    <div class="main-block">
        <ImageTextBlock :description="aboutBlockDescription" :isImageAlignLeft="true" href="about" />
        <Services href="services" />
    </div>
</template>

<script>
  import ImageTextBlock from "@/components/MainPage/ImageTextBlock";
  import Services from "@/components/MainPage/Services";
  export default {
    name: "MainPage",
    components: {
      ImageTextBlock,
      Services
    },
    setup() {
      return {
        aboutBlockDescription: "В нашей компании только профессионалы, разделяющие высокие требования к качеству результатов нашей работы для Вашего бизнеса"
      }
    }
  }
</script>

<style scoped>
    .main-block {
        padding: 10px;
        flex: 1 1 auto;
        overflow: auto;
    }
</style>