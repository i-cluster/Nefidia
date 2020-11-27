<template>
  <div>
    <h3>CommentList</h3>
      <div v-for="(comment, idx) in comments" :key="idx">
        {{ comment.user.username }} : {{ comment.content }}
      </div>
  </div>
</template>

<script>
export default {
  name: 'CommentList',
  props: {
    comments: {
      type: Array
    }
  }
}
</script>

<style>

</style>