<template>
  <div class="service-block">
    <img :src="icon"/>
    <p>{{lable}}</p>
  </div>
</template>

<script>
  export default {
    name: "ServiceBlock",
    props: {
      icon: {
        type: String,
        default: ""
      },
      lable: {
        type: String,
        default: ""
      },
    },
  }
</script>

<style>
  .service-block {
    /* margin: 0px 34px; */
    cursor: pointer;
    min-width: 199px;
    min-height: 195px;
    background: #FFFFFF;
    box-shadow: 0px 0px 4px rgba(0, 0, 0, 0.25);
    border-radius: 15px;
    display: flex;
    flex-direction: column;
    justify-content:center;
  }

  .service-block img {
    max-height: 116px;
    max-width: 113px;
    margin: auto;
  }

  .service-block p {
    text-align: center;
  }
</style>