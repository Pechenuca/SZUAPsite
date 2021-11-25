<template>
  <div>
    <TitleBlock label="Новости" v-if="isNews" />
    <TitleBlock label="Аудиторские отчеты" v-else />
    <div class="news-short-block-wrapper">
        <NewsShort 
          class="news-short-item"
          v-for="(item) in newsShortData" :key="item.label"
          :label="item.label"
          :description="item.description"
          :img="item.image"
        />
    </div>
  </div>
</template>

<script>
  import TitleBlock from "@/components/MainPage/TitleBlock.vue"
  import NewsShort from "@/components/MainPage/NewsShort.vue"
  import imgPreview from "@/assets/testNewsShortImg.jpg"

  export default {
    name: "News",
    components: {TitleBlock, NewsShort},
    props: {
      isNews: {
        type: Boolean,
        default: true
      }
    },
    setup() {
      return {
        newsShortData: [
          {
            image: imgPreview,
            label: "Hello world",
            description: "test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test testtest test test test test test test test test test test test test test test testtest test test test test test test test test test test test test test test test"
          },
          {
            image: imgPreview,
            label: "Hello world",
            description: "test test test test test test test test test test test test test test test test "
          },
          {
            image: imgPreview,
            label: "Hello world",
            description: "test test test test test test test test test test test test test test test test "
          },
          {
            image: imgPreview,
            label: "Hello world",
            description: "test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test testtest test test test test test test test test test test test test test test testtest test test test test test test test test test test test test test test test"
          },
          {
            image: imgPreview,
            label: "Hello world",
            description: "test test test test test test test test test test test test test test test test "
          },
          {
            image: imgPreview,
            label: "Hello world",
            description: "test test test test test test test test test test test test test test test test "
          }
        ]
      }
    },
    created() {
        this.newsShortData.forEach(el => {
          if (el.description.length >= 250) {
            let slicedDescription = el.description.slice(0, 250) + ' ...'
            el.description = slicedDescription
          }
        })
      }
    
  }
</script>

<style>
  .news-short-block-wrapper {
    max-width: 1200px;
    margin-left: auto;
    margin-right: auto;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    flex-wrap: wrap;
  }
  .news-short-item {
    margin-top: 15px;
  }
</style>