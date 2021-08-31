import Vue from 'vue'
import App from './App.vue'
//import '@aws-amplify/ui-vue';

import Amplify, * as AmplifyModules from 'aws-amplify';
import { AmplifyPlugin } from '@aws-amplify/ui-vue';
import aws_exports from './aws-exports';
Amplify.configure(aws_exports);
//Vue.use(AmplifyPlugin, AmplifyModules);

Vue.config.productionTip = false
Vue.use(AmplifyPlugin, AmplifyModules);

new Vue({
  render: h => h(App),
}).$mount('#app')