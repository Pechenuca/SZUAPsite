<template>
  <div>
    <TitleBlock label="Услуги компании" />
    <div class="services-block-wrapper">
      <div class="services-block-shortblocks wrapper-element">
          <ServiceBlock 
            v-for="(item, index) in servicesData[0]" :key="item.label"
            v-on:click="toggleModal(index)"
            :id="'serviceBlockId' + index"
            :label="item.label" 
            :icon="item.image" 
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
  import { ref, onBeforeUpdate  } from 'vue'
  import TitleBlock from "@/components/MainPage/TitleBlock.vue";
  import ServiceBlock from "@/components/MainPage/Services/ServiceBlock.vue"
  import Modal from "@/components/MainPage/Services/Modal.vue"

  export default {
    name: "Services",
    components: {TitleBlock, ServiceBlock, Modal},
    props: {
      servicesDataProp: {
        type: Array,
      }
    },
    setup(props) {
      const isModalHidden = ref(true)
      const modalTitle = ref('')
      const modalDescription = ref('')
      const servicesData = ref([])
      
      onBeforeUpdate(() => {
        servicesData.value = [props.servicesDataProp]
      })

      return {
        isModalHidden,
        modalTitle,
        modalDescription,
        servicesData
      }
    },
    methods: {
      toggleModal(index) {
        this.isModalHidden = false
        this.modalTitle = this.servicesData[0][index].label
        this.modalDescription = this.servicesData[0][index].description
      },
      closeModal() {
        this.isModalHidden = true
      },
    },
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