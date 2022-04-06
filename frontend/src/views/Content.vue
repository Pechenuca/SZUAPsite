<template>
  <div class="main-block">
    <h3 v-bind:style="cssData">Страницы, содержащие {{searchString}}, не найдены.</h3> 
    <News
      id="content"
      :postDataProp="contentProps"
      :isShort="false"
    />
  </div>
</template>

<script>
  import { ref } from 'vue'
  import News from "@/views/News"
  
  export default {
    name: "Content",
    components: {News},
    setup() {
      const contentProps = ref([])
      const cssData = 'display:none;'
      let searchString = ''
      return {
        cssData,
        contentProps,
        searchString
      }
    },
    methods: {
      getBackendUrl() {
        return this.$store.getters.baseUrl
      },
      async getPostsData(url, content_type, search) {
        let baseUrl = `${url}content/`
        if (content_type == 3) {
          baseUrl = `${baseUrl}?search=${search}`
        } else {
          baseUrl = `${baseUrl}?post_type=${content_type}&search=${search}`
        }
        fetch(baseUrl)
          .then((res) => {
            return res.json()
          })
          .then((data) => {
            let content = []

            if (data.length == 0) {
              this.cssData = 'display:block;'
              this.searchString = search
            }

            data.forEach(el => {
                el.content = el.content.replace(/<\/?[^>]+>/ig, " ").replace("&nbsp;", " ")
                if (el.content.length >= 200) {
                  let slicedDescription = el.content.slice(0, 200) + ' ...'
                  el.content = slicedDescription
                }
                content.push(el)
            })
            this.contentProps = content
          })
      },
    },
    beforeMount () {
      this.getPostsData(
        this.getBackendUrl(), 
        this.$route.params.type,
        (this.$route.params.search == undefined) ? '' : this.$route.params.search
      )
    },
  }
</script>

<style>
</style>