<template>
  <div class="service-modal" v-if="!isHidden">
    <div class="service-modal-title">
      <h3>{{title}}</h3>
      <img :src="close" v-on:click="closeModal">
    </div>
    <p>{{description}}</p>
  </div>
</template>

<script>
  import close from "@/assets/times-circle-regular.svg"

  export default {
    name: "ServiceModal",
    props: {
      isHidden: {
        type: Boolean,
        default: true
      },
      title: {
        type: String,
        default: "",
      },
      description: {
        type: String,
        default: "",
      }
    },
    setup() {
      return {
        close
      }
    },
    methods: {
      closeModal() {
        this.$emit('child-hide-event')
      },
    }
  }
</script>

<style>
  .service-modal {
      background: #FFFFFF;
      box-shadow: 0px 0px 4px rgba(0, 0, 0, 0.25);
      border-radius: 15px;
      display: flex;
      justify-content: flex-start;
      flex-direction: column;
    }
  
  .service-modal .service-modal-title, p {
    margin: 20px;
  }
  
  .service-modal-title {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
  }

  .service-modal-title h3 {
    margin: 0px;
  }

  .service-modal-title img {
    widows: 20px;
    height: 20px;
    cursor: pointer;
  }
</style>