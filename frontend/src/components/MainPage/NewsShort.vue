<template>
    <div class="news-short">
      <img :src="img" />
      <div class="news-text">
        <h3>{{label}}</h3>
        <p>{{description}}</p>
      </div>
    </div>
</template>

<script>
  export default {
    name: "NewsShort",
    props: {
      img: {
        type: String,
      },
      label: {
        type: String,
      },
      description: {
        type: String,
      }
    }
  }
</script>

<style>
  .news-short {
    width: 304px;
    height: 422px;
    background: #FFFFFF;
    box-shadow: 0px 0px 4px rgba(0, 0, 0, 0.25);
    border-radius: 15px;
    cursor: pointer;
  }

  .news-short img {
    width: 304px;
    height: 169px;
    border-radius: 15px 15px 0px 0px;
  }

  .news-text p, h3 {
    padding: 10px;
    margin: 0px;
  }

  .news-short h3 {
    font-size: 24px;
    line-height: 35px;
  }

  .news-short p {
    font-size: 18px;
    line-height: 26px;
    word-break: break-all;
  }
  @media (max-width: 626px) {
    .news-short {
      margin: auto;
      width: 90%;
    }

    .news-short img {
      width: 100%;
    }
  }
</style>