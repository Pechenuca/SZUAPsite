<template>
    <div class="about-block-wrapper">
      <TitleBlock label="ООО “СЗУАП-АУДИТ”" />
      <div class="about-block" v-if="isImageAlignLeft">
        <div class="image-with-block">
          <div class="green-block">
            <img class="about-image" :src="image" alt="green-umbrella">
          </div>
        </div>
        <div class=description v-html="customizeDescription"></div>
      </div>
      <div class="about-block" v-else>
        <div>
          <p v-html="customizeDescription">
          </p>
        </div>
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
    },
    computed: {
      customizeDescription() {
        return this.description.substring(3, this.description.length - 4)
      }
        
    }
  }
</script>

<style>
  .about-block-wrapper {
    display: flex;
    flex-direction:column;
  }

  .description > p {
    overflow-wrap: break-word;
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
    max-width: 417px;
    max-height: 351px;
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

  @media (max-width: 375px) {
    .about-block {
        flex-direction: column;
        justify-content: center;       
    }
    .green-block {
      width: 85vw;
      height: 39.27vh;
    }
    .description {
      height: 8.6vw;
    }
    .about-image {
      width: 50vw;
      height: 23.1vh;
    }
  }
</style>