<template>
  <div>
    <TitleBlock label="Услуги компании" />
    <div class="services-block-wrapper">
      <div class="services-block-shortblocks wrapper-element">
          <ServiceBlock 
            v-for="(item, index) in servicesData" :key="item.lable"
            v-on:click="toggleModal(index)"
            :id="'serviceBlockId' + index"
            :lable="item.lable" 
            :icon="item.img" 
          />
      </div>
      <Modal
        @child-hide-event="closeModal"
        class="wrapper-element"
        :isHidden="isModalHidden"
        :title="modalTitle"
        :description="modalDescription"
      />
    </div>
  </div>
</template>

<script>
  import { ref } from 'vue'
  import TitleBlock from "@/components/MainPage/TitleBlock.vue";
  import ServiceBlock from "@/components/MainPage/Services/ServiceBlock.vue"
  import Modal from "@/components/MainPage/Services/Modal.vue"
  
  import audit from "@/assets/services/audit.png"
  import sud from "@/assets/services/sud.png"
  import tax from "@/assets/services/tax.png"
  import ur_cons from "@/assets/services/ur_cons.png"

  export default {
    name: "Services",
    components: {TitleBlock, ServiceBlock, Modal},
    setup() {
      const isModalHidden = ref(true)
      const modalTitle = ref('')
      const modalDescription = ref('')
      
      return {
        isModalHidden,
        modalTitle,
        modalDescription,
        servicesData: [
          {
            lable: "Аудит отчетности РСБУ",
            description: "Аудит отчетности РСБУ description. Аудит отчетности РСБУ description. Аудит отчетности РСБУ description. Аудит отчетности РСБУ description.",
            img: audit
          },
          {
            lable: "Налоговый консалтинг",
            description: "Налоговый консалтинг description. Налоговый консалтинг description. Налоговый консалтинг description. Налоговый консалтинг description.",
            img: tax
          },
          {
            lable: "Судебные споры",
            description: "Судебные споры description. Налоговый консалтинг description. Налоговый консалтинг description. Налоговый консалтинг description.",
            img: sud
          },
          {
            lable: "Юрилический консалтинг",
            description: "Юрилический консалтинг description. Налоговый консалтинг description. Налоговый консалтинг description. Налоговый консалтинг description.",
            img: ur_cons
          } 
        ]
      }
    },
    methods: {
      toggleModal(index) {
        this.isModalHidden = false
        this.modalTitle = this.servicesData[index].lable
        this.modalDescription = this.servicesData[index].description
      },
      closeModal() {
        this.isModalHidden = true
      }
    }
    
  }
</script>

<style>
  .services-block-wrapper {
    display: flex;
    flex-direction: column;
    justify-content: center;
    margin-left: auto;
    margin-right: auto;
    max-width: 1200px;
  }

  .services-block-shortblocks {
    display: flex;
    flex-direction:row;
    justify-content: space-between;
  }

  .wrapper-element {
    margin-top: 25px;
  }
</style>