<template>
  <div>
    <el-tabs v-model="activeName" type="border-card">
        <el-tab-pane label="房屋" name="house">
            <HouseSearch></HouseSearch>
        </el-tab-pane>
        <el-tab-pane label="职位" name="job">
            <JobSearch></JobSearch>
        </el-tab-pane>
        <el-tab-pane label="商品" name="goods">
            <GoodsSearch></GoodsSearch>
        </el-tab-pane>  
    </el-tabs>
  </div>
</template>

<script>
import HouseSearch from '@/components/HouseSearch.vue'
import JobSearch from '@/components/JobSearch.vue'
import GoodsSearch from '@/components/GoodsSearch.vue'

export default {
    components: {
        HouseSearch,
        JobSearch,
        GoodsSearch
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