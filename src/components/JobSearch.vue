<template>
    <div>
        <div class="search-form">
            <el-select v-model="form.platformValue">
                <el-option label="前程无忧" value="51"></el-option>
                <el-option label="拉钩网" value="lagou"></el-option>
                <el-option label="智联招聘" value="zhilian"></el-option>
            </el-select>
            <el-input class="city" placeholder="城市名称" v-model="form.city"></el-input>
            <el-input class="job" placeholder="工作名称" v-model="form.job"></el-input>
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
        <el-backtop target=".page-component__scroll .el-scrollbar__wrap"></el-backtop>
    </div>
</template>


<script>
export default {
    data() {
        return {
            form: {
                platformValue: '51',
                city: '',
                job: ''
            },
            currentHeader: {},
            tableData: [],
            resultDetail: {
                pageCount: 1
            },
            header: {
                '51': [],
                'zhilian': [],
                'lagou':[]
            }
        }
    },

    methods: {
        changePage(page) {

        },

    }
}
</script>

<style lang="scss" scoped>
.search-form {
    display: flexbox;
    justify-content: space-between;
    .job {
        width: 30%;
    }
    .city {
        width: 10%;
    }
}
</style>