<template>
  <div id="app">
    <AppHeader v-if="!isHidden"></AppHeader>
    <router-view></router-view>
    <AppFooter v-if="!isHidden"></AppFooter>
  </div>
</template>

<script>
import AppFooter from './components/AppFooter.vue';
import AppHeader from './components/AppHeader.vue';

export default {
  name: 'App',
  components: {
    AppHeader,
    AppFooter
  },
  computed: {
    isHidden() {
      return this.$route.path === '/register/agency' || 
             this.$route.path === '/register/users' || 
             this.$route.path === '/enter'; 
    }
  }
}
</script>