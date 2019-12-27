<template>
    <div>
        <div class="search-form">
            <el-select v-model="form.platformValue" @change="handleSelect">
                <el-option label="前程无忧" value="51"></el-option>
                <el-option label="拉钩网" value="lagou"></el-option>
                <el-option label="智联招聘" value="zhilian"></el-option>
            </el-select>
            <el-input v-model="form.search"></el-input>
            <el-button @click="changePage(1)" type="primary">搜索</el-button>
        </div>
        <el-divider></el-divider>
        <div class="result">
            <el-table :data="tableData" :header="currentHeader">
                <el-table-column  :key="h" v-for="h in currentHeader" :label="h" :prop="h" width="100px;"/>
            </el-table>
            <el-pagination
            background
            layout="pager"
            :page-count="resultDetail.pageCount"
            @current-change="changePage"
            >
            </el-pagination>
        </div>
    </div>
</template>


<script>
export default {

}
</script>

<style>

</style>