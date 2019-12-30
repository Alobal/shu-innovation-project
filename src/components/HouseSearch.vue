<template>
    <div>
        <div class="search-form">
            <el-select v-model="form.platformValue" @change="handleSelect">
                <el-option label="贝壳" value="beike"></el-option>
                <el-option label="链家" value="lianjia"></el-option>
                <el-option label="自如" value="ziru"></el-option>
                <el-option label="房天下" value="fang"></el-option>
            </el-select>
            <el-select v-model="form.typeValue">
                <el-option label="二手房" value="二手房" :disabled="typeDisabled.sec"></el-option>
                <el-option label="新房" value="新房" :disabled="typeDisabled.new"></el-option>
                <el-option label="租房" value="租房" :disabled="typeDisabled.rent"></el-option>
            </el-select>
            <el-input placeholder="请输入城市名称" v-model="form.search"></el-input>
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
            showAlert: true,
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
            typeDisabled: {
                sec: false,
                new: false,
                rent: false
            },
            currentHeader: {},
            header: {
                新房: ['title', 'houseType', 'state', 'position', 'tags', 'unitPrice', 'totalPrice'],
                二手房: ['title', 'houseType', 'floor', 'buildTime', 'area', 'direction', 'position', 'tags', 'totalPrice', 'unitPrice'],
                租房: ['title', 'rentType', 'position', 'area', 'direction', 'tags', 'price'],
            }
        }
    },
    methods: {
        changePage(page) {
            let that = this;
            searchHouse({
                platform: that.form.platformValue,
                city: that.form.search,
                type: that.form.typeValue,
                page: page
            }).then(function(res){
                console.log(res);
                if(res.code == 404) {
                    that.$message.error(res.message);
                }
                that.currentHeader = that.header[that.form.typeValue];
                that.tableData = res.data;
                that.resultDetail.pageCount = res.pages;
            })
        },
        handleSelect(val) {
            let that = this;
            if(val == 'ziru') {
                this.form.typeValue = '租房';
                this.typeDisabled.sec = true;
                this.typeDisabled.new = true;
            }
            else if(val == 'fang') {
                this.form.typeValue = '二手房';
                this.typeDisabled.new = true;
            }
            else {
                 this.typeDisabled.sec = false;
                 this.typeDisabled.new = false;
                 this.typeDisabled.rent = false;
             }
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