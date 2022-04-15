<template>
    <div class="aboutUs-block-wrapper">
      <TitleBlock label="О нас"/>
      <div class="aboutUs-block">
        <!-- <div v-html="label"></div> -->
        <div v-html="description"></div>
      </div>
    </div>
</template>

<script> 
  import TitleBlock from "./TitleBlock.vue";
  export default {
    name: "aboutUsBlock",
    components: {TitleBlock},
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
      
      },
    setup() {
      return {
      }
    }
    }
</script>

<style>
  .aboutUs-block {
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
  .aboutUs-block-wrapper {
    display: flex;
    flex-direction:column;
  }

  .aboutUs-block > p {
    text-align: center;
  }
  .aboutUs-block > div {
    text-align: center;
  }
  @media (max-width: 375px) {
    .aboutUs-block {
        /* width: 50vh;
        height: 25vw;
        flex-direction: absolute;
        justify-content: center;
        flex-wrap: wrap; */
        font-size: 12px;
    }
  }

</style>