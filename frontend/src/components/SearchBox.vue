<template>
    <input class="search-input" type="text" :placeholder="label" />
</template>

<script>

  export default {
    name: "SearchBox",
    props: {
      label: {
        type: String,
        default: ''
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
    font-style: normal;
    font-size: 24px;
    line-height: 35px;
  }
  .search-input:focus {
    font-style: normal;
    font-size: 24px;
    line-height: 35px;
  }
</style>