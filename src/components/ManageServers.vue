<template>
    <div>
        <h3>Serverlist: {{label}}</h3>
        <ul id="demo">
            <li v-repeat="instances" :class="instances-$index">
                {{$index}} - {{childMsg}}
            </li>
        </ul>
    </div>
</template>

<script>
export default {
  name: 'ManageServers',
  props: {
      label: {require: true, type: String},
      instances: {require: true, type: String},
  }
}

//const instances = await API.get('minecraftserver', '/instances');
</script>
