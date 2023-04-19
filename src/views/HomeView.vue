<template>
  <div class="container-fluid no-mp">
    <div class="row no-mp">
      <div class="col no-mp">
        <div class="top-left box">
          <RenderMap />
        </div>
      </div>
      <div class="col no-mp">
        <div class="top-right box">
          <!-- eslint-disable-next-line max-len -->
          <ControlllerLiveFeed :feedArray="controllerFeedArray" :isFeedEmpty="controllerIsFeedEmpty"/>
        </div>
      </div>
    </div>
    <div class="row no-mp">
      <div class="col no-mp">
        <div class="bot-left box">
          <div class="loading-text"> Waiting on 3D data...</div>
        </div>
      </div>
      <div class="col no-mp">
        <div class="bot-right box">
          <ROSLiveFeed :feedArray="rosFeedarray" :isFeedEmpty="rosIsFeedEmpty"/>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
// @ is an alias to /src
import ControlllerLiveFeed from '@/components/ControlllerLiveFeed.vue';
import RenderMap from '@/components/RenderMap.vue';
import ROSLiveFeed from '@/components/ROSLiveFeed.vue';

const baseUrl = process.env.NODE_ENV === 'production' ? 'http://george-env.eba-trrm37cn.us-east-2.elasticbeanstalk.com/' : 'http://127.0.0.1:5000/';

export default {
  name: 'HomeView',
  components: {
    ControlllerLiveFeed,
    RenderMap,
    ROSLiveFeed,
  },
  mounted() {
    this.fetchData();
  },
  methods: {
    fetchData() {
      this.$sse.create(`${baseUrl}api/data-feed`)
        .on('message', (msg) => { this.feedArrayHandler(msg); })
      // eslint-disable-next-line
        .on('error', (err) => console.error('Failed to parse or lost connection:', err))
        .connect()
      // eslint-disable-next-line
        .catch((err) => console.error('Failed make initial connection:', err));
    },
    feedArrayHandler(rawLog) {
      const jsonLog = JSON.parse(rawLog);
      if ('controller-log' in jsonLog) {
        this.controllerIsFeedEmpty = false;
        if (this.controllerFeedArray.length > 50) {
          this.controllerFeedArray.pop();
          this.controllerFeedArray.unshift(jsonLog['controller-log']);
        } else {
          this.controllerFeedArray.unshift(jsonLog['controller-log']);
        }
      } else {
        this.rosIsFeedEmpty = false;
        if (this.rosFeedarray.length > 50) {
          this.rosFeedarray.pop();
          this.rosFeedarray.unshift(jsonLog['ros-log']);
        } else {
          this.rosFeedarray.unshift(jsonLog['ros-log']);
        }
      }
      this.isFeedEmpty = false;
    },
  },
  data() {
    return {
      controllerFeedArray: [],
      controllerIsFeedEmpty: true,
      rosFeedarray: [],
      rosIsFeedEmpty: true,
    };
  },
};
</script>

<style>

.title {
  background-color: #323232;
  height: 30px;
  font-size: 16px;
  color: #9ec0e1;
  display: flex;
  align-items: center;
  justify-content: center;
}

.top-right {
  border-left: 0px;
  border-bottom: 2px;
  border-right: 0px;
  border-top: 0px;
  overflow: auto;
}

.top-left {
  border-left: 0px;
  border-bottom: 2px;
  border-right: 2px;
  border-top: 0px;
}

.bot-right {
  border: 0px;
  width: 50vw;
  bottom: 0px;
  overflow: auto;
}

.bot-left {
  width: 50vw;
  border-left: 0px;
  border-bottom: 0px;
  border-right: 2px;
  border-top: 0px;
  bottom: 0px;
}

.feed-title {
  font-size: 20px;
  color: whitesmoke;
}

.box {
  height: 46vh;
  border-color: #494949;
  border-style: solid;
  display: flex;
  flex-direction: column;
}

.no-mp {
  margin: 0 !important;
  padding: 0 !important;
}

.loading-text {
  display: flex;
  width: 100%;
  height: 100%;
  align-items: center;
  justify-content: center;
  color: #9ec0e1;
  opacity: 70%;
  font-size: 22px;
}

::-webkit-scrollbar {
  width: 20px;
}

::-webkit-scrollbar-track {
  background-color: transparent;
}

::-webkit-scrollbar-thumb {
  background-color: #cdcdcd;
  border-radius: 20px;
  border: 6px solid transparent;
  background-clip: content-box;
}
</style>
