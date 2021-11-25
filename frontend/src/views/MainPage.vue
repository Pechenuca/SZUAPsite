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
        <Contacts 
          id="contacts"
        />
    </div>
</template>

<script>
  import ImageTextBlock from "@/views/ImageTextBlock"
  import Services from "@/views/Services"
  import News from "@/views/News"
  import Contacts from "@/views/Contacts"
  import smoothscroll from 'smoothscroll-polyfill'

  export default {
    name: "MainPage",
    components: {
      ImageTextBlock,
      Services,
      News,
      Contacts
    },
    setup() {
      smoothscroll.polyfill()
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
      currentDiv (newDiv) {
        if (document.getElementById(newDiv) != null) {
          document.getElementById(newDiv).scrollIntoView({ behavior: 'smooth' })
          this.$store.commit("currentDiv", '')  
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
    .main-block div:last-child {
      margin-bottom: 200px;
    }
</style>