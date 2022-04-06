<template>
    <div class="main-block"> 
        <ImageTextBlock 
          :description="aboutBlockDescription" 
          :isImageAlignLeft="aboutBlockAlign"
          :image="aboutBlockImageUrl"
          id="about"
        />
        <AboutUs
          id="aboutUs"
          :aboutUsDataProp="aboutUsData"
          />
        <Buisness
          id="buisness"
          :buisnessDataProp="buisnessData"
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
        <Carier
          id="carier"
          :carierDataProp="carierData"
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
  import AboutUs from '@/components/MainPage/AboutUs.vue'
  import Carier from '@/components/MainPage/Carier.vue'
  import Buisness from '@/components/MainPage/Buisness.vue'

  export default {
    name: "MainPage",
    components: {
      ImageTextBlock,
      Services,
      News,
      Contacts,
      AboutUs,
      Carier, 
      Buisness
    },
    setup() {
      const aboutBlockAlign = ref(true)
      const aboutBlockImageUrl = ref('')
      const aboutBlockDescription = ref('')
      const servicesData = ref([])
      const newsData = ref([])
      const auditData = ref([])
      const carierData = ref([])
      const aboutUsData = ref([])
      const buisnessData = ref([])
      
      return {
        aboutBlockAlign,
        aboutBlockImageUrl,
        aboutBlockDescription,
        servicesData,
        newsData,
        auditData,
        carierData,
        buisnessData,
        aboutUsData
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
      async getAboutUsData(url) {
        fetch(`${url}aboutus/`)
          .then((res) => {
            return res.json()
          })
          .then((data) => {
            this.aboutUsData = data
          })
      },   
      async getBuisnessData(url) {
        fetch(`${url}buisness/`)
          .then((res) => {
            return res.json()
          })
          .then((data) => {
            this.buisnessData = data
          })
      },   
      async getCarierData(url) {
        fetch(`${url}carier/`)
          .then((res) => {
            return res.json()
          })
          .then((data) => {
            this.carierData = data
          })
      },   
      async getPostsData(url, content_type) {
        fetch(`${url}content/?post_type=${content_type}&short=1`)
          .then((res) => {
            return res.json()
          })
          .then((data) => {
            let content = []

            data.forEach(el => {
                el.content = el.content.replace(/<\/?[^>]+>/ig, " ").replace("&nbsp;", " ")
                if (el.content.length >= 200) {
                  let slicedDescription = el.content.slice(0, 200) + ' ...'
                  el.content = slicedDescription
                }
                content.push(el)
            })
            if (content_type == 1) {
              this.auditData = content
            } else {
              this.newsData = content
            }
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
      this.getPostsData(this.getBackendUrl(), 1)
      this.getPostsData(this.getBackendUrl(), 0)
      // this.getAboutUsData(this.getBackendUrl())
      // this.getBuisnessData(this.getBackendUrl())
      // this.getCarierData(this.getBackendUrl())
    },
    
  }
</script>

<style scoped>
    .main-block div:nth-child(n) {
      margin-top: 45px;
    }
    .main-block div:nth-child(1) {
      margin-top: 0px;
    }
    .main-block div:last-child {
      margin-bottom: 200px;
    }
    @media (max-width: 1191px) {
      .main-block {
        display: block;
      }
      .main-block div:last-child  {
        margin-bottom: 0px;
      }
    }
</style>