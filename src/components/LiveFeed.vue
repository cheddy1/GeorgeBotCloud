<template lang="html">

  <section class="live-feed">
    >  {{ feedData }}
  </section>

</template>

<script>
// import axios from 'axios';

const baseUrl = process.env.NODE_ENV === 'production' ? 'http://george-env.eba-trrm37cn.us-east-2.elasticbeanstalk.com/' : 'http://127.0.0.1:5000/';

export default {
  name: 'live-feed',
  props: {
  },
  mounted() {
    // setInterval(this.fetchData, 3000); // save reference to the interval
    this.fetchData();
  },
  data() {
    return {
      feedData: 'Some fun data thing would go here.\n Maybe',
    };
  },
  methods: {
    fetchData() {
      this.$sse.create(`${baseUrl}listen`)
        .on('message', (msg) => { this.feedData = msg; })
        .on('error', (err) => console.error('Failed to parse or lost connection:', err))
        .connect()
        .catch((err) => console.error('Failed make initial connection:', err));
      // axios.get(`${baseUrl}api/lidar`)
      //   .then((response) => {
      //     this.feedData = response.data;
      //   });
    },
  },
  computed: {

  },
};

</script>

<style scoped>
  .live-feed {
    padding-left: 10px;
    padding-right: 10px;
    padding-top: 5px;
    bottom: 0;
  }
</style>
