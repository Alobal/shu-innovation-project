<template>
    <div>
        <div class="search-form">
            <el-select v-model="form.platformValue">
                <el-option label="贝壳" value="beike"></el-option>
                <el-option label="链家" value="lianjia"></el-option>
            </el-select>
            <el-select v-model="form.typeValue">
                <el-option label="二手房" value="二手房"></el-option>
                <el-option label="新房" value="新房"></el-option>
                <el-option label="租房" value="租房"></el-option>
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
import {searchHouse} from '@/api/search.js'
export default {
    data() {
        return {
            form: {
                platformValue: 'beike',
                typeValue: '二手房',
                search: ''
            },
            resultDetail: {
                pageCount: 1,
                currentPage: 1,
            },
            tableData: [],
            currentHeader: {},
            header: {
                新房: ['title', 'state', 'type', 'position', 'tags', 'totalPrice', 'unitPrice'],
                二手房: ['title', 'floor', 'buildTime', 'roomType', 'area', 'direction', 'position', 'viewNum', 'time', 'tags', 'totalPrice', 'unitPrice'],
                租房: ['title', 'rentType', 'position', 'area', 'direction', 'roomType', 'floor', 'tags', 'brand', 'time', 'price'],
            }
        }
    },
    methods: {
        changePage(page) {
            let that = this;
            searchHouse({
                platform: this.form.platformValue,
                city: this.form.search,
                type: this.form.typeValue,
                page: page
            }).then(function(res){
                that.currentHeader = that.header[that.form.typeValue];
                that.tableData = res.data.data;
                that.resultDetail.pageCount = res.data.pages;
            }).catch(function(err) {
                console.log(err)
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