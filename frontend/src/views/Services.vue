<template>
  <div>
    <TitleBlock label="Услуги компании" />
    <div class="services-block-wrapper">
      <div v-for="item in servicesData" :key="item.lable">
        <ServiceBlock 
          :lable="item.lable" 
          :icon="item.img" 
          :description="item.description"
        />
      </div>
    </div>
  </div>
</template>

<script>
  import TitleBlock from "@/components/MainPage/TitleBlock.vue";
  import ServiceBlock from "@/components/MainPage/Services/ServiceBlock.vue"
  
  import audit from "@/assets/services/audit.png";
  import sud from "@/assets/services/sud.png";
  import tax from "@/assets/services/tax.png";
  import ur_cons from "@/assets/services/ur_cons.png";

  export default {
    name: "Services",
    components: {TitleBlock, ServiceBlock},
    setup() {
      return {
        servicesData: [
          {
            lable: "Аудит отчетности РСБУ",
            description: "Аудит отчетности РСБУ description",
            img: audit
          },
          {
            lable: "Налоговый консалтинг",
            description: "Налоговый консалтинг description",
            img: tax
          },
          {
            lable: "Судебные споры",
            description: "Судебные споры description",
            img: sud
          },
          {
            lable: "Юрилический консалтинг",
            description: "Юрилический консалтинг description",
            img: ur_cons
          } 
        ]
      }
    }
    
  }
</script>

<style>
  .services-block-wrapper {
    display: flex;
    flex-direction:row;
    justify-content: center;
  }
</style>