import { createApp } from 'vue';
import { BootstrapVue3 } from 'bootstrap-vue-3';
import App from './App.vue';
import router from './router';

// Import Bootstrap and BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue-3/dist/bootstrap-vue-3.css';

createApp(App).use(router).use(BootstrapVue3).mount('#app');
