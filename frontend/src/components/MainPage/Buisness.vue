<template>
    <div class="buisness-block-wrapper">
      <TitleBlock label="О деятельности"/>
      <div class="buisness-block">
        <div v-html="description"></div>
      </div>
    </div>
</template>

<script>
  import TitleBlock from "./TitleBlock.vue";
  export default {
    name: "buisnessBlock",
    components: {TitleBlock},
    props: {
      description: {
        type: String,
        default: '',
        required: true
        },
      },
    setup() {
      return {
      }
    }
    }
</script>

<style>
  .buisness-block {
    /* margin: 0px 34px; */
    /* cursor: pointer; */
    min-width: 199px;
    min-height: 195px;
    background: #FFFFFF;
    /* box-shadow: 0px 0px 4px rgba(0, 0, 0, 0.25); */
    border-radius: 5px;
    display: flex;
    flex-direction: column;
    justify-content:center;
  }

 .buisness-block-wrapper {
    display: flex;
    flex-direction:column;
  }
  
  .buisness-block p {
    text-align: center;
  }

  @media (max-width: 375px) {
    .buisness-block {
        /* flex-direction: initial;
        justify-content: center;
        flex-wrap: wrap;
        margin: 0;
        width: 50vh;
        height: 25vw; */
        font-size: 12px;
    }
  }
</style>