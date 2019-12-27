<template>
  <div>
    <el-tabs v-model="activeName" type="border-card">
        <el-tab-pane label="房屋" name="house">
            <HouseSearch></HouseSearch>
        </el-tab-pane>
        <el-tab-pane label="职位" name="job">职位</el-tab-pane>
    </el-tabs>
  </div>
</template>

<script>
import HouseSearch from '@/components/HouseSearch.vue'
export default {
    components: {
        HouseSearch
    },
    data() {
        return {
            activeName: 'house'
        }
    }
}
</script>

<style>

</style>