<template lang="html">
    <div v-if="isFeedEmpty" class="loading-text"> Waiting on the ROS data feed...</div>
    <div v-else>
        <div class="title sticky-top">ROS Feed</div>
        <div class="live-feed">
            <ul style="list-style-type: >">
                <li v-for="item in feedArray" :key="item">
                    {{ item }}
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
// import axios from 'axios';

export default {
  name: 'ROS-live-feed',
  props: [
    'feedArray',
    'isFeedEmpty',
  ],
  mounted() {
  },
  methods: {
  },
  computed: {
  },
};

</script>

<style scoped>
.live-feed {
    padding-right: 10px;
    padding-top: 2px;
    color: whitesmoke;
    height: 100%;
    overflow: wrap;
    word-break: break-all;
}

ul {
    list-style: none;
    padding: 0;
    margin: 0;
    font-size: 14px;
}

li {
    padding-left: 16px;
}

li::before {
    content: ">";
    padding-right: 8px;
}
</style>
