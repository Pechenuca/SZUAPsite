<template>
    <div class="carier-block-wrapper">
      <TitleBlock label="Карьера"/>
      <div class="carier-block">
        <div v-html="label"></div>
        <div v-html="description"></div>
      </div>
    </div>
</template>

<script>
  import TitleBlock from "./TitleBlock.vue";

  export default {
    components: {TitleBlock},
    name: "carierBlock",
    props: {
      // label: {
      //   type: String,
      //   default: '',
      //   required: true
      // },
      description: {
        type: String,
        default: '',
        required: true
      },
    setup() {
        return {
        }
      }
      }
    }
</script>

<style>
  .carier-block {
    /* margin: 0px 34px; */
    /* cursor: pointer; */
    min-width: 199px;
    min-height: 195px;
    background: #FFFFFF;
    /* box-shadow: 0px 0px 4px rgba(0, 0, 0, 0.25); */
    border-radius: 15px;
    display: flex;
    flex-direction: column;
    justify-content:center;
  }
  .carier-block-wrapper {
    display: flex;
    flex-direction:column;
  }
  .carier-block p {
    text-align: center;
  }
  @media (max-width: 375px) {
    .carier-block {
        /* flex-direction: initial;
        justify-content: center;
        flex-wrap: wrap;
        margin: 5px;
        width: 50vh;
        height: 25vw; */
        font-size: 12px;
    }
  }
</style>