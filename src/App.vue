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

      let myInit = {
          headers: {
            Authorization: `Bearer ${(await Auth.currentSession())
              .getIdToken()
              .getJwtToken()}`
          }
        }; 

      const response = await API.get('minecraftserver', '/instance', myInit)
      this.items = response.data
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
