<template>
    <div class="title-block">
      <img class="title-block-item title-block-icon" :src="icon">
      <h1 class="title-block-item">{{label}}</h1>
    </div>
</template>

<script>
  import icon from "@/assets/umbrella-solid.svg"
  export default {
    name: "TitleBlock",
    props: {
      label: {
        type: String,
        default: ""
      },
    },
    setup() {
      return {
        icon,
      }
    },
  }
</script>

<style>
  .title-block {
    display: flex;
    flex-direction: row;
    margin: 0 -5px 25px 0;
    max-height: 60px;
  }
  .title-block-item {
    margin: 0 5px;
  }
  .title-block-icon {
     margin-right: 20px;
     width: 27px;
     height: 28px;
  }
</style>