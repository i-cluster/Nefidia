<template>
  <div class="profile">
    <h1>This is 프 로 필 그리고 하위컴포넌트는 프 로 필 디 테 일</h1>
    <ProfileDetail />
  </div>
</template>

<script>
// @ is an alias to /src
import ProfileDetail from '@/components/accounts/ProfileDetail'

export default {
  name: 'Profile',
  components: {
    ProfileDetail,
  }
}
</script>

<style>

</style>