<template>
  <div>
    <!-- 面包屑导航区域 -->
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/admin/home' }"
        >首页</el-breadcrumb-item
      >
      <el-breadcrumb-item>用户管理</el-breadcrumb-item>
      <el-breadcrumb-item>用户列表</el-breadcrumb-item>
    </el-breadcrumb>
    <!-- 卡片视图 -->
    <el-card class="box-card">
      <el-row :gutter="20">
        <el-col :span="10">
          <!-- 搜索与添加区域 -->
          <el-input placeholder="请输入学工号" v-model="input">
            <el-button slot="append" icon="el-icon-search"></el-button>
          </el-input>
        </el-col>
        <el-col :span="4">
          <el-button type="primary">添加用户</el-button>
        </el-col>
      </el-row>
    </el-card>
  </div>
</template>
<script>
export default {
  data() {
    return {
      input: '',
      userlist: {
        students: {
          list: [],
          total: 0,
        },
        teachers: {
          list: [],
          total: 0,
        },
        admin: {
          list: [],
          total: 0,
        },
      },
    }
  },
  created() {
    this.getUserList()
  },
  methods: {
    async getStudentList() {
      const { data: res } = await this.$http.get('admin/student/search/')
      if (res.status !== 200) return this.$message.error('获取用户列表失败')
      this.studentlist = res.data.Students
      this.studentTotal = res.data.total
      console.log(res)
    },
  },
}
</script>
<style lang="less" scoped>
</style>