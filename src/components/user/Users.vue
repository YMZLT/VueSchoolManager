<template>
  <div>
    <!-- 面包屑导航区域 -->
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>用户管理</el-breadcrumb-item>
      <el-breadcrumb-item>用户列表</el-breadcrumb-item>
    </el-breadcrumb>
    <!-- 卡片视图区域 -->
    <el-card>
      <!-- 搜索与添加区域 -->
      <el-row :gutter="20">
        <el-col :span="7">
          <el-input v-model="user_id" placeholder="请输入学工号">
            <el-button slot="append" icon="el-icon-search"></el-button>
          </el-input>
        </el-col>
        <el-col :span="4">
          <el-button type="primary">添加用户</el-button>
        </el-col>
      </el-row>
      <!-- 用户列表区域 -->
      <el-table :data="userSubList" border stripe>
        <el-table-column type="index"></el-table-column>
        <el-table-column label="学工号" prop="user_id"></el-table-column>
        <el-table-column label="姓名" prop="user_name"></el-table-column>
        <el-table-column label="身份" prop="user_type"></el-table-column>
        <el-table-column label="院系" prop="college_id"></el-table-column>
        <el-table-column
          label="英语等级"
          prop="English_class"
        ></el-table-column>
        <el-table-column label="职位" prop="position"></el-table-column>
        <el-table-column label="管理员" prop="is_admin">
          <template slot-scope="scope">
            <el-switch
              v-model="scope.row.is_admin"
              @change="userStateChange(scope.row)"
              :disabled="scope.row.user_type == 'S'"
            >
            </el-switch>
          </template>
        </el-table-column>
        <el-table-column label="操作">
          <template>
            <el-button
              type="primary"
              icon="el-icon-edit"
              size="mini"
              circle
            ></el-button>
            <el-button
              type="danger"
              icon="el-icon-delete"
              size="mini"
              circle
            ></el-button>
            <el-tooltip
              class="item"
              effect="dark"
              content="分配角色"
              placement="top"
              :enterable="false"
            >
              <el-button
                type="warning"
                icon="el-icon-setting"
                size="mini"
                circle
              ></el-button>
            </el-tooltip>
          </template>
        </el-table-column>
      </el-table>
      <!-- 分页功能 -->
      <div class="block">
        <el-pagination
          @size-change="handleSizeChange"
          @current-change="handleCurrentChange"
          :current-page="pagination.currentPage"
          :page-sizes="[5, 8, 10, 15]"
          :page-size="pagination.pageSize"
          layout="total, sizes, prev, pager, next, jumper"
          :total="pagination.total"
        >
        </el-pagination>
      </div>
    </el-card>
  </div>
</template>


<script>
export default {
  data() {
    return {
      // 全部用户列表
      userList: [],
      // 部分用户列表
      userSubList: [],
      // 分页管理
      pagination: {
        total: 0,
        pageSize: 5,
        currentPage: 1,
      },
      // 学工号（搜索）
      user_id: '',
    }
  },
  created() {
    this.getUserList()
  },
  methods: {
    // 获取用户列表
    async getUserList() {
      const data = await this.$http.get('user')
      // console.log(data)
      // const { data: res } = await this.$http.get('users', {
      //   params: this.queryInfo,
      // })
      if (data.status !== 200) return this.$message.error('获取用户列表失败！')
      this.userList = data.data
      this.pagination.total = data.data.length

      var start = (this.pagination.currentPage - 1) * this.pagination.pageSize
      this.userSubList = data.data.slice(
        start,
        start + this.pagination.pageSize
      )
    },
    handleSizeChange(val) {
      // console.log(`每页 ${val} 条`)
      let start = (this.pagination.currentPage - 1) * val
      let end = start + val
      this.userSubList = this.userList.slice(start, end)
    },
    handleCurrentChange(val) {
      // console.log(`当前页: ${val}`)
      let start = (val - 1) * this.pagination.pageSize
      let end = start + this.pagination.pageSize
      this.userSubList = this.userList.slice(start, end)
    },
    async userStateChange(userInfo)
    {
      console.log(userInfo)
      const data = await this.$http.put(`user/${userInfo.user_id}/`,userInfo)
      console.log(data)
    }
  },
}
</script>

<style lang="less" scoped>
.block {
  padding-top: 10px;
}
</style>