<template>
  <div>
    <LoginForm @login="login" />
  </div>
</template>

<script>
import LoginForm from '@/components/accounts/LoginForm'
export default {
  name: 'Login',
  components: {
    LoginForm,
  },
  methods: {
    login: function () {
      this.$emit('login')
    }
  }
}
</script>

<style>
</style>