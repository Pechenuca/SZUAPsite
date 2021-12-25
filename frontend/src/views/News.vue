<template>
  <div>
    <TitleBlock label="Последние Новости" v-if="isNews && isShort" />
    <TitleBlock label="Последние Аудиторские Отчеты" v-if="!isNews && isShort" />
    <div class="news-short-block-wrapper">
        <NewsShort 
          class="news-short-item"
          v-for="(item) in postData[0]" :key="item.title"
          :detail_id="item.id"
          :label="item.title"
          :description="item.content"
          :img="item.image"
        />
        <NewsShort
          v-if="isShort"
          :type="isNews"
          class="news-short-item read-more"
          label="Смотреть Всё"
        />
    </div>
  </div>
</template>

<script>
  import { ref, onBeforeUpdate } from 'vue'
  import TitleBlock from "@/components/MainPage/TitleBlock.vue"
  import NewsShort from "@/components/MainPage/NewsShort.vue"

  export default {
    name: "News",
    components: {TitleBlock, NewsShort},
    props: {
      postDataProp: {
        type: Array,
      },
      isNews: {
        type: Boolean,
        default: true
      },
      isShort: {
        type: Boolean,
        default: true
      }
    },
    setup(props) {
      const postData = ref([])

      onBeforeUpdate(() => {
        postData.value = [props.postDataProp]
      })
      return {
        postData,
      }
    },
    methods: {
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
  .read-more {
    height: 50px;
  }
  .read-more > div > h3 {
    margin:auto;
  }
  @media (max-width: 576px) {
    .news-short-block-wrapper {
      flex-direction: column;
      justify-content: center;
    }
  }
</style>