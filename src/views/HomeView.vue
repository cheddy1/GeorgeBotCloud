<template>
  <div class="container-fluid no-mp">
    <div class="row no-mp">
      <div class="col no-mp">
        <div class="left">
          <RenderMap />
        </div>
      </div>
      <div class="col no-mp">
        <div class="top-right box">
          <!-- eslint-disable-next-line max-len -->
          <ControllerLiveFeed :feedArray="controllerFeedArray" :isFeedEmpty="controllerIsFeedEmpty"/>
        </div>
        <div class="bot-right box">
          <ROSLiveFeed :feedArray="rosFeedarray" :isFeedEmpty="rosIsFeedEmpty"/>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
// @ is an alias to /src
import ControllerLiveFeed from '@/components/ControllerLiveFeed.vue';
import RenderMap from '@/components/RenderMap.vue';
import ROSLiveFeed from '@/components/ROSLiveFeed.vue';

const baseUrl = process.env.NODE_ENV === 'production' ? 'http://george-env.eba-trrm37cn.us-east-2.elasticbeanstalk.com/' : 'http://127.0.0.1:5000/';

export default {
  name: 'HomeView',
  components: {
    ControllerLiveFeed,
    RenderMap,
    ROSLiveFeed,
  },
  mounted() {
    this.fetchData();
  },
  methods: {
    fetchData() {
      this.$sse.create(`${baseUrl}api/data-feed-receive`)
        .on('message', (msg) => { this.feedArrayHandler(msg); })
      // eslint-disable-next-line
        .on('error', (err) => console.error('Failed to parse or lost connection:', err))
        .connect()
      // eslint-disable-next-line
        .catch((err) => console.error('Failed make initial connection:', err));
    },
    feedArrayHandler(rawLog) {
      const jsonLog = JSON.parse(rawLog.replace(/'/g, '"'));
      let log;
      if ('controller-log' in jsonLog) {
        this.controllerIsFeedEmpty = false;
        log = JSON.stringify(jsonLog['controller-log']);
        log = log.replace(/{|}|"/g, '').replace(/:/g, ': ').replace(/,/g, ', ');
        if (this.controllerFeedArray.length > 50) {
          this.controllerFeedArray.pop();
          this.controllerFeedArray.unshift(log);
        } else {
          this.controllerFeedArray.unshift(log);
        }
      } else {
        this.rosIsFeedEmpty = false;
        log = JSON.stringify(jsonLog['ros-log']);
        log = log.replace(/{|}|"/g, '').replace(/:/g, ': ').replace(/,/g, ', ');
        if (this.rosFeedarray.length > 50) {
          this.rosFeedarray.pop();
          this.rosFeedarray.unshift(log);
        } else {
          this.rosFeedarray.unshift(log);
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
  height: 46vh;
  border-left: 2px;
  border-bottom: 2px;
  border-right: 0px;
  border-top: 0px;
  overflow: auto;
  border-color: #494949;
  border-style: solid;
  display: flex;
  flex-direction: column;
}

.left {
  height: 92vh;
  display: flex;
  flex-direction: column;
}

.bot-right {
  height: 46vh;
  border-left: 2px;
  border-right: 0px;
  border-top: 0px;
  border-color: #494949;
  border-style: solid;
  width: 50vw;
  bottom: 0px;
  overflow: auto;
  display: flex;
  flex-direction: column;
}

.feed-title {
  font-size: 20px;
  color: whitesmoke;
}

.box {
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
