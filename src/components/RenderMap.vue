<template lang="html">
  <section class="render-map">
    <img alt="render" class="render" src="../assets/preset_data.gif">
  </section>
</template>

<script lang="js">

export default {
  name: 'render-map',
  props: [],
  mounted() {

  },
  data() {
    return {

    };
  },
  methods: {

  },
  computed: {

  },
};

</script>

<style scoped>

.title {
  display: flex;
}
.render-map {
  display: flex;
  height: 100%;
}

.render {
  display: flex;
  margin: auto;
  align-items: center;
  justify-content: center;
  width: 65%;

}
</style>
