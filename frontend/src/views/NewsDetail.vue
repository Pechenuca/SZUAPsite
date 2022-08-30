<template>
  <div class="main-block">
    <div class="content">
      <div class="image-wrapper">
        <img :src="contentData.image">
      </div>
      <div class="title-date">
        <h1>{{contentData.title}}</h1>
        <h2>{{new Date(contentData.created_on).toLocaleDateString('ru-ru')}}</h2>
      </div>
      <p v-html="contentData.content"></p>
      <p><a :href="contentData.file">Документы</a></p>
    </div>
  </div>
</template>

<script>
  import { ref } from 'vue'
  export default {
    name: "DetailContent",
    setup() {
      const contentData = ref({})
      return {
        contentData
      }
    },
    methods: {
      getBackendUrl() {
        return this.$store.getters.baseUrl
      },
      async getServicesData(url, id) {
        fetch(`${url}content/?id=${id}`)
          .then((res) => {
            return res.json()
          })
          .then((data) => {
            this.contentData = data[0]
        })
      }, 
    },
    beforeMount() {
      this.getServicesData(this.getBackendUrl(), this.$route.params.id)
    }
  }
</script>

<style>
  .image-wrapper {
    height: 200px;
  }
  .image-wrapper img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
  .content p {
    margin: 0;
    padding: 0;
    font-size: larger;
  }
  .title-date {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    flex-wrap: wrap;
    align-items: center;
  }
</style>