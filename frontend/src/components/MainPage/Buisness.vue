<template>
  <div class="buisness-block">
    <img :src="icon"/>
    <p>{{label}}</p>
  </div>
</template>

<script>
  export default {
    name: "buisnessBlock",
    props: {
      icon: {
        type: String,
        default: ""
      },
      label: {
        type: String,
        default: ""
      },
    },
  }
</script>

<style>
  .buisness-block {
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

  .buisness-block img {
    max-height: 116px;
    max-width: 113px;
    margin: auto;
  }

  .buisness-block p {
    text-align: center;
  }

  @media (max-width: 915px) {
    .buisness-block {
        margin: 5px;
        width: 199px;
        height: 195px;
    }
  }
</style>