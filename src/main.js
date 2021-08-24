import Vue from 'vue'
import App from './App.vue'
import '@aws-amplify/ui-vue';
import Amplify, { Auth } from 'aws-amplify';

Amplify.configure({
  Auth: {
      // REQUIRED - Amazon Cognito Region
      region: 'eu-central-1',

      // OPTIONAL - Amazon Cognito User Pool ID
      userPoolId: 'eu-central-1_UgVKzLuC9',

      // OPTIONAL - Amazon Cognito Web Client ID (26-char alphanumeric string)
      userPoolWebClientId: '2o58tunop1au1cvo2ku7fo749p',

      // OPTIONAL - Enforce user authentication prior to accessing AWS resources or not
      mandatorySignIn: false,
  }
});
Auth.configure();

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')
