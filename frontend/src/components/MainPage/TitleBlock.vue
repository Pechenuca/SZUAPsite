<template>
    <div class="title-block">
      <img class="title-block-item title-block-icon" :src="icon">
      <h1 :href="hrefHoock" class="title-block-item">{{label}}</h1>
    </div>
</template>

<script>
  import icon from "@/assets/umbrella-solid 2.svg"
  export default {
    name: "TitleBlock",
    props: {
      label: {
        type: String,
        default: ""
      },
      pHref: {
        type: String,
        default: null
      }
    },
    setup(props) {
      return {
        icon,
        hrefHoock: "#" + props.pHref
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
  }
</style>