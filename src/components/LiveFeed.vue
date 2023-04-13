<template lang="html">
  <section class="live-feed">
    <div v-if="isFeedEmpty" class="loading-text"> Waiting on controller data...</div>
    <div v-else>
      <ul class="demo" style="list-style-type: >">
        <li v-for="item in feedArray" :key="item">
          {{ item }}
        </li>
      </ul>
    </div>
  </section>
</template>

<script>
// import axios from 'axios';

const baseUrl = process.env.NODE_ENV === 'production' ? 'http://george-env.eba-trrm37cn.us-east-2.elasticbeanstalk.com/' : 'http://127.0.0.1:5000/';

export default {
  name: 'live-feed',
  props: {},
  mounted() {
    // setInterval(this.fetchData, 3000); // save reference to the interval
    this.fetchData();
  },
  data() {
    return {
      isFeedEmpty: true,
      feedArray: [],
    };
  },
  methods: {
    initFeed() {
      this.feed = '<ul class="demo" style="list-style-type: >"> <li v-for="item in feedArray" :key="item">{{ item }}</li></ul>';
    },
    fetchData() {
      this.$sse.create(`${baseUrl}api/data-feed`)
        .on('message', (msg) => { this.feedArrayHandler(msg); })
        .on('error', (err) => console.error('Failed to parse or lost connection:', err))
        .connect()
        .catch((err) => console.error('Failed make initial connection:', err));
      // axios.get(`${baseUrl}api/lidar`)
      //   .then((response) => {
      //     this.feedData = response.data;
      //   });
    },
    feedArrayHandler(rawLog) {
      const log = rawLog.replace('{\'log\': \'', '').replace('\'}', '');
      this.isFeedEmpty = false;
      if (this.feedArray.length > 50) {
        this.feedArray.pop();
        this.feedArray.unshift(log);
      } else {
        this.feedArray.unshift(log);
      }
    },
  },
  computed: {

  },
};

</script>

<style scoped>
.live-feed {
  padding-right: 10px;
  padding-top: 5px;
  padding-bottom: 10px;
  color: whitesmoke;
  display: flex;
  height: 100%;
}

ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

li {
  padding-left: 16px;
}

li::before {
  content: ">";
  padding-right: 8px;
}

</style>
