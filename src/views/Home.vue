<template>
  <div class="home">
    <Header></Header>
  </div>
</template>

<script>
// @ is an alias to /src
import Header from '@/components/Header.vue'

export default {
  name: 'home',
  components: {
    Header
  }
}
</script>

<style lang="scss" scoped>
  .home {
    margin: 0 auto;
    padding: 20px;
    min-height: 300px;
    display: flexbox;
    justify-content: center;
    width: 70%;
    border: 1px solid #e6e6e6;
  }
</style>