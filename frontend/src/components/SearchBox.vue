<template>
  <div class="search-box">
    <input class="search-input" type="text" placeholder="Поиск" v-model="searchString" />
    <img :src="search" v-on:click="findPosts" />
  </div>
</template>

<script>
  import { ref } from 'vue'
  import search from "@/assets/search.svg"
  export default {
    name: "SearchBox",
    setup() {
      const searchString = ref('')
      return {
        searchString,
        search
      }
    },
    methods: {
      findPosts() {
        if (this.searchString != '') {
          this.$router.push(`/content/3/${this.searchString}`)
          this.searchString = ''
        }
      }
    }
  }
</script>

<style>
   .search-input {
    border: 0.7px solid black;
    border-radius: 5px;
    width: 130px;
    height: 35px;
    font-family: ZenKakuGothicAntique-Light;
    font-style: normal;
    font-size: 24px;
    line-height: 35px;
    color: black;
  }
  ::placeholder {
    color: black;
    font-family: ZenKakuGothicAntique-Light;
    font-style: normal;
    font-size: 24px;
    line-height: 35px;
  }
  .search-input:focus {
    font-family: ZenKakuGothicAntique-Light;
    font-style: normal;
    font-size: 24px;
    line-height: 35px;
  }
  .search-box img {
    margin-left: 20px;
  }
</style>