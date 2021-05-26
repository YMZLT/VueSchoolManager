<template>
  <div>
    <!-- 面包屑导航区域 -->
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/admin/home' }"
        >首页</el-breadcrumb-item
      >
      <el-breadcrumb-item>用户管理</el-breadcrumb-item>
      <el-breadcrumb-item>管理员</el-breadcrumb-item>
    </el-breadcrumb>
    <!-- 卡片视图 -->
    <el-card class="box-card">
      <!-- 搜索与添加区域 -->
      <el-row :gutter="20">
        <el-col :span="16">
          <!-- 搜索与添加区域 -->
          <el-input
            :placeholder="'请输入' + selected"
            v-model="input"
            clearable
          >
            <el-select
              v-model="selected"
              class="select"
              slot="prepend"
              placeholder="请选择"
            >
              <el-option
                v-for="item in options"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              >
              </el-option>
            </el-select>
            <el-button
              slot="append"
              icon="el-icon-search"
              @click="getAdminList(true)"
            ></el-button>
            <el-button
              slot="append"
              icon="el-icon-refresh-right"
              @click="getAdminList(false)"
            ></el-button>
          </el-input>
        </el-col>
        <el-col :span="4">
          <el-button type="primary" @click="addDialogVisible = true"
            >添加用户</el-button
          >
        </el-col>
      </el-row>
      <!-- 列表区域 -->
      <el-table :data="adminList" border stripe>
        <!-- 自定义索引 -->
        <el-table-column type="index"> </el-table-column>
        <el-table-column prop="user_id" label="工号"> </el-table-column>
        <el-table-column prop="user_name" label="姓名"></el-table-column>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button
              type="primary"
              icon="el-icon-edit"
              size="mini"
              @click="showEditDialog(scope.row.user_id)"
            >
            </el-button>
            <el-button
              type="danger"
              icon="el-icon-delete"
              size="mini"
              @click="deleteAdmin(scope.row.user_id)"
            >
            </el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-card>
    <!-- 添加用户对话框 -->
    <el-dialog
      title="添加管理员"
      :visible.sync="addDialogVisible"
      width="50%"
      @close="addDialogClosed"
    >
      <!-- 内容主题区域 -->
      <el-form label-position="left"
        :model="addForm"
        :rules="addFormRules"
        ref="addFormRef"
        label-width="70px"
      >
        <el-form-item label="工号" prop="user_id">
          <el-input
            v-model="addForm.user_id"
            placeholder="请输入工号"
            clearable
          ></el-input>
        </el-form-item>
        <el-form-item label="姓名" prop="user_name">
          <el-input
            v-model="addForm.user_name"
            placeholder="请输入姓名"
            clearable
          ></el-input>
        </el-form-item>
        <el-form-item label="密码" prop="password">
          <el-input
            v-model="addForm.password"
            placeholder="请输入密码"
            show-password
            clearable
          ></el-input>
        </el-form-item>
      </el-form>
      <!-- 底部区域 -->
      <span slot="footer" class="dialog-footer">
        <el-button @click="addDialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="addAdmin"> 确 定 </el-button>
      </span>
    </el-dialog>
    <!-- 修改用户对话框 -->
    <el-dialog
      title="修改管理员信息"
      :visible.sync="editDialogVisible"
      width="50%"
      @close="editDialogClosed"
    >
      <!-- 内容主题区域 -->
      <el-form label-position="left"
        :model="editForm"
        :rules="editFormRules"
        ref="editFormRef"
        label-width="70px"
      >
        <el-form-item label="工号" prop="user_id">
          <el-input v-model="editForm.user_id" disabled></el-input>
        </el-form-item>
        <el-form-item label="姓名" prop="user_name">
          <el-input
            v-model="editForm.user_name"
            placeholder="请输入姓名"
            clearable
          ></el-input>
        </el-form-item>
      </el-form>
      <!-- 底部区域 -->
      <span slot="footer" class="dialog-footer">
        <el-button @click="editDialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="editAdmin"> 确 定 </el-button>
      </span>
    </el-dialog>
  </div>
</template>
<script>
export default {
  data() {
    return {
      options: [
        {
          value: '工号',
          label: '工号',
        },
        {
          value: '姓名',
          label: '姓名',
        },
      ],
      selected: '工号', // 搜索选择
      input: '', // 搜索输入框
      adminList: [], // 用户列表
      total: 0, // 用户列表总数
      // 控制添加对话框显示与隐藏
      addDialogVisible: false,
      // 添加用户的表单数据
      addForm: {
        user_id: '',
        user_name: '',
        password: '',
      },
      // 添加表单的验证规则
      addFormRules: {
        user_id: [
          { required: true, message: '请输入工号', trigger: 'blur' },
          {
            min: 4,
            max: 4,
            message: '工号长度为4个字符',
            trigger: 'blur',
          },
        ],
        user_name: [
          { required: true, message: '请输入姓名', trigger: 'blur' },
          {
            min: 3,
            max: 10,
            message: '姓名长度在3~10个字符之间',
            trigger: 'blur',
          },
        ],
        password: [
          { required: true, message: '请输入密码', trigger: 'blur' },
          {
            min: 6,
            max: 10,
            message: '密码长度在6~10个字符之间',
            trigger: 'blur',
          },
        ],
      },
      // 控制修改对话框显示与隐藏
      editDialogVisible: false,
      // 查询到的用户信息
      editForm: {},
      // 修改表单的验证规则
      editFormRules: {
        user_name: [
          { required: true, message: '请输入姓名', trigger: 'blur' },
          {
            min: 3,
            max: 10,
            message: '姓名长度在3~10个字符之间',
            trigger: 'blur',
          },
        ],
        password: [
          { required: true, message: '请输入密码', trigger: 'blur' },
          {
            min: 6,
            max: 10,
            message: '密码长度在6~10个字符之间',
            trigger: 'blur',
          },
        ],
      },
    }
  },
  created() {
    this.getAdminList()
  },
  methods: {
    // 获取管理员列表
    async getAdminList(search) {
      var query = {}
      if (search) {
        if (this.selected === '工号') {
          query = { user_id: this.input }
        } else if (this.selected === '姓名') {
          query = { user_name: this.input }
        }
      }
      const { data: res } = await this.$http.get('admin/superuser/search/', {
        params: query,
      })
      if (res.status !== 200) return this.$message.error('获取用户列表失败')
      this.adminList = res.data.SuperUsers
      this.total = res.data.total
      console.log(res)
    },
    // 监听对话框关闭事件
    addDialogClosed() {
      // 重置表单
      this.$refs.addFormRef.resetFields()
    },
    // 添加管理员
    addAdmin() {
      this.$refs.addFormRef.validate(async (valid) => {
        if (!valid) return
        // 校验正确则发起请求
        const { data: res } = await this.$http.post('admin/superuser/create/', [
          this.addForm,
        ])
        if (res.status === 200) this.$message.success('添加成功！')
        else this.$message.error('添加失败！\n' + res.detail[0])
        this.addDialogVisible = false
        // 重新获取用户列表
        this.getAdminList()
      })
    },
    // 修改管理员信息
    async showEditDialog(id) {
      this.editDialogVisible = true
      const { data: res } = await this.$http.get('admin/superuser/search/', {
        params: { user_id: id },
      })
      if (res.status !== 200) return this.$message.error('获取用户列表失败')
      this.editForm = res.data.SuperUsers[0]
      console.log(res)
    },
    // 监听修改对话框的关闭事件
    editDialogClosed() {
      this.$refs.editFormRef.resetFields()
    },
    // 修改管理员信息
    editAdmin() {
      this.$refs.editFormRef.validate(async (valid) => {
        // console.log(valid)
        if (!valid) return
        // 校验正确则发起请求
        const { data: res } = await this.$http.put(
          'admin/superuser/edit/' + this.editForm.user_id,
          { user_name: this.editForm.user_name }
        )
        if (res.status !== 200)
          this.$message.error('修改失败！\n' + res.detail[0])
        this.$message.success('更新成功！')
        this.editDialogVisible = false
        // 重新获取用户列表
        this.getAdminList()
      })
    },
    // 删除管理员
    deleteAdmin(id) {
      // 弹框提示
      this.$confirm('此操作将永久删除该用户, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning',
      })
        .then(async () => {
          // 确定删除
          const { data: res } = await this.$http.delete(
            'admin/superuser/edit/' + id
          )
          if (res.status != 200)
            return this.$message({
              type: 'error',
              message: '删除失败!',
            })

          this.$message({
            type: 'success',
            message: '删除成功!',
          })
          // 刷新用户列表
          this.getAdminList()
        })
        .catch(() => {
          this.$message({
            type: 'info',
            message: '已取消删除',
          })
        })
    },
  },
}
</script>
<style lang="less" scoped>
.select {
  width: 120px;
}
</style>