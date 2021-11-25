<template>
    <div class="main-block">
        <ImageTextBlock 
          :description="aboutBlockDescription" 
          :isImageAlignLeft="aboutBlockAlign"
          :image="aboutBlockImageUrl"
          id="about"
        />
        <Services
          id="services"
          :servicesDataProp="servicesData"
        />
        <News
          id="news"
          :postDataProp="newsData"
        />
        <News 
          id="audit"
          :isNews="false"
          :postDataProp="auditData"
        />
        <Contacts 
          id="contacts"
        />
    </div>
</template>

<script>
  import { ref } from 'vue'
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
      const aboutBlockAlign = ref(true)
      const aboutBlockImageUrl = ref('')
      const aboutBlockDescription = ref('')
      const servicesData = ref([])
      const newsData = ref([])
      const auditData = ref([])
      
      return {
        aboutBlockAlign,
        aboutBlockImageUrl,
        aboutBlockDescription,
        servicesData,
        newsData,
        auditData
      }
    },
    methods: {
      getBackendUrl() {
        return this.$store.getters.baseUrl
      },
      async getHelloPageData(url) {
        fetch(`${url}hello-page/`)
          .then((res) => {
            return res.json()
          })
          .then((data) => {
            let jsonData = data[0]
            this.aboutBlockAlign = (jsonData.imageAligin == 0) ? true : false
            this.aboutBlockImageUrl = jsonData.image
            this.aboutBlockDescription = jsonData.description
          })
      },
      async getServicesData(url) {
        fetch(`${url}services/`)
          .then((res) => {
            return res.json()
          })
          .then((data) => {
            this.servicesData = data
          })
      },   
      async getPostsData(url) {
        fetch(`${url}news/`)
          .then((res) => {
            return res.json()
          })
          .then((data) => {
            let audit = []
            let news = []

            data.forEach(el => {
              if (el.status) {
                el.content = el.content.replace(/<\/?[^>]+>/ig, " ")
                if (el.content.length >= 200) {
                  let slicedDescription = el.content.slice(0, 200) + ' ...'
                  el.content = slicedDescription
                }
                if (el.post_type) {
                  news.push(el)
                } else {
                  audit.push(el)
                }
              } 
            })
            this.auditData = audit
            this.newsData = news
          })
      },  
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
    },
    beforeMount () {
      smoothscroll.polyfill()

      this.getHelloPageData(this.getBackendUrl())
      this.getServicesData(this.getBackendUrl())
      this.getPostsData(this.getBackendUrl())
    },
    
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