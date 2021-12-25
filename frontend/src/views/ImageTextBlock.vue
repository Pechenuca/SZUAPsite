<template>
    <div class="about-block-wrapper">
      <TitleBlock label="ООО “СЗУАП-АУДИТ”" />
      <div class="about-block" v-if="isImageAlignLeft">
        <div class="image-with-block">
          <div class="green-block">
            <img class="about-image" :src="image" alt="green-umbrella">
          </div>
        </div>
        <div v-html="description"></div>
      </div>
      <div class="about-block" v-else>
        <div v-html="description"></div>
        <div class="image-with-block">
          <div class="green-block">
            <img class="about-image" :src="image" alt="green-umbrella">
          </div>
        </div>
      </div>
    </div>
</template>

<script>
  import TitleBlock from "@/components/MainPage/TitleBlock.vue";
  export default {
    name: "ImageTextBlock",
    components: {TitleBlock},
    props: {
      description: {
        type: String,
        default: '',
        required: true
      },
      isImageAlignLeft: {
        type: Boolean,
        default: null
      },
      image: {
        type: String,
        default: ''
      }
    },
    setup() {
      return {
      }
    }
  }
</script>

<style>
  .about-block-wrapper {
    display: flex;
    flex-direction:column;
  }
  
  .about-block {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-around;
  }

  .about-image {
    z-index: 0;
    margin-left: -20px;
    margin-top: -20px;
    border-radius: 15px;
    object-fit: cover;
  }
  
  .green-block {
    margin: 20px;
    z-index: 1;
    width: 417px;
    height: 351px;
    background: rgba(0, 198, 80, 0.56);
    border-radius: 15px;
  }

  .about-block p {
    max-width: 650px;
    word-break: break-all;
    font-style: normal;
    font-weight: normal;
    font-size: 28px;
    line-height: 35px;
  }

  @media (max-width: 915px) {
    .about-block {
        flex-direction: column;
        justify-content: center;
    }
  }
</style>