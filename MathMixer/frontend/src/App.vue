<template>
  <div>
    <h1>Usernames</h1>
    <ul>
      <li v-for="user in users" :key="user.username">{{ user.username }}</li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      users: []
    }
  },

  created() {
    axios.get('http://localhost:8000/api/users/')
      .then(response => {
        this.users = response.data
      })
      .catch(error => {
        console.error(error)
      })
  }
}
</script>