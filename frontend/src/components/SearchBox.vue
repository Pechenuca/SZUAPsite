<template>
  <div class="search-box">
    <input class="search-input" type="text" />
    <img :src="search" />
  </div>
</template>

<script>
  import search from "@/assets/search.svg"
  export default {
    name: "SearchBox",
    setup() {
      return {
        search
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
    font-style: normal;
    font-size: 24px;
    line-height: 35px;
  }
  ::placeholder {
    color: black;
    font-family: AlkesLight;
    font-style: normal;
    font-size: 24px;
    line-height: 35px;
  }
  .search-input:focus {
    font-family: AlkesLight;
    font-style: normal;
    font-size: 24px;
    line-height: 35px;
  }
  .search-box img {
    margin-left: 20px;
  }
</style>