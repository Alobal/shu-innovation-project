<template>
    <div>
        <div class="search-form">
            <el-select v-model="form.platformValue">
                <el-option label="京东" value="jingdong"></el-option>
                <el-option label="苏宁" value="suning"></el-option>
            </el-select>

            <el-input placeholder="请输入商品名称" v-model="form.search"></el-input>
            <el-button @click="changePage(1)" type="primary">搜索</el-button>
        </div>
        <el-divider></el-divider>
        <div class="result">
            <el-table :data="tableData" :header="header">
                <el-table-column  :key="h" v-for="h in header" :label="h" :prop="h" width="250px;"/>
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
import {searchGoods} from '@/api/search.js'
export default {
    data() {
        return {
            showAlert: true,
            form: {
                platformValue: 'jingdong',
                search: ''
            },
            resultDetail: {
                pageCount: 1,
                currentPage: 1,
            },
            tableData: [],
            header: ['title', 'price', 'shop', 'tags']
        }
    },
    methods: {
        changePage(page) {
            let that = this;
            searchGoods({
                platform: that.form.platformValue,
                keyword: that.form.search,
                page: page
            }).then(function(res){
                if(res.code == 404) {
                    that.$message.error(res.message);
                }
                that.currentHeader = that.header;
                that.tableData = res.data;
                that.resultDetail.pageCount = res.pages;
            })
        }
    }
}
</script>

<style lang="scss" scoped>
    .search-form {
        display: flexbox;
        justify-content: space-between;
        .el-input {
            width: 30%;
        }
    }
</style>