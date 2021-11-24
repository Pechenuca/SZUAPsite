<template>
    <div class="main-block">
        <ImageTextBlock :description="aboutBlockDescription" :isImageAlignLeft="true" />
        <Services />
        <News />
    </div>
</template>

<script>
  import ImageTextBlock from "@/views/ImageTextBlock";
  import Services from "@/views/Services";
  import News from "@/views/News";
  export default {
    name: "MainPage",
    components: {
      ImageTextBlock,
      Services,
      News
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