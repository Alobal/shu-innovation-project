<template>
    <div>
        <div class="search-form">
            <el-select v-model="form.platformValue">
                <el-option label="前程无忧" value="51"></el-option>
                <el-option label="拉钩网" value="lagou"></el-option>
                <el-option label="智联招聘" value="zhilian"></el-option>
                <el-option label="猎聘" value="liepin"></el-option>
            </el-select>
            <el-input class="city" placeholder="城市名称" v-model="form.city"></el-input>
            <el-input class="job" placeholder="工作名称" v-model="form.job"></el-input>
            <el-button @click="changePage(1)" type="primary">搜索</el-button>
        </div>
        <el-divider></el-divider>
        <div class="result">
            <el-table :data="tableData" :header="header">
                <el-table-column  :key="h" v-for="h in header" :label="h" :prop="h" width="100px;"/>
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
import {searchJob} from '@/api/search.js'
export default {
    data() {
        return {
            form: {
                platformValue: '51',
                city: '',
                job: ''
            },
            tableData: [],
            resultDetail: {
                pageCount: 1
            },
            header: ['jobName', 'company', 'position', 'salary']
        }
    },

    methods: {
        changePage(page) {
            let that = this;
            searchJob({
                platform: this.form.platformValue,
                city: this.form.city,
                job: this.form.job,
                page: page
            }).then(function(res){
                if(res.code == 404) {
                    that.$message.error(res.message);
                }
                that.tableData = res.data;
                that.resultDetail.pageCount = res.pages;
            })
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