<template>
  <div id="app">
    <amplify-authenticator>
      <amplify-sign-in header-text="My Custom Sign In Text" slot="sign-in"></amplify-sign-in>
      <div>
        <img alt="Vue logo" src="./assets/logo.png" />
        
        <manage-servers label="Minecraft"></manage-servers>
        
        <div id="amplify-signout">
          <amplify-sign-out></amplify-sign-out>
        </div>
      </div>
    </amplify-authenticator>
  </div>
</template>

<script>
import ManageServers from './components/ManageServers.vue'
import Amplify, {API, Auth} from 'aws-amplify';
import awsconfig from './aws-exports';
Amplify.configure(awsconfig);

export default {
  components: { ManageServers },
  name: 'App',
  async created() {
    // You may have saved off the JWT somewhere when the user logged in.
    // If not, get the token from aws-amplify:
    this.retrieveInstances();
  },
  commponents: {
    ManageServers,
  },
  data() {
    return {
      items: []
    }
  },
  methods: {
    async retrieveInstances() {

      const user = await Auth.currentAuthenticatedUser();
      const token = user.signInUserSession.idToken.jwtToken;

      API.get('minecraftserver', '/instance/', {
        headers: {
          Authorization: `Bearer ${token}`
        }
      }).then(response => {
        this.items = response.data;
      });
    }
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
