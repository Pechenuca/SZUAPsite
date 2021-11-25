<template>
    <div class="main-block">
        <ImageTextBlock 
          :description="aboutBlockDescription" 
          :isImageAlignLeft="true"
          id="about"
        />
        <Services
          id="services"
        />
        <News
          id="news"
        />
        <News 
          id="audit"
          :isNews="false" 
        />
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
    },
    computed: {
      currentDiv() {
        return this.$store.getters.currentDiv
      }
    },
    watch: {
      currentDiv (newDiv, oldDiv) {
        console.log(`Old div ${oldDiv}`)
        console.log(`Current div ${newDiv}`)
        if (document.getElementById(newDiv) != null) {
          document.getElementById(newDiv).scrollIntoView()
        }
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
    .main-block div:nth-child(n) {
      margin-top: 45px;
    }
    .main-block div:nth-child(1) {
      margin-top: 0px;
    }
</style>