<template>
  <div>
    <!-- 面包屑导航区域 -->
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/admin/home' }"
        >首页</el-breadcrumb-item
      >
      <el-breadcrumb-item>信息管理</el-breadcrumb-item>
      <el-breadcrumb-item>开课列表</el-breadcrumb-item>
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
              @click="getOpenList(true)"
            ></el-button>
            <el-button
              slot="append"
              icon="el-icon-refresh-right"
              @click="getOpenList(false)"
            ></el-button>
          </el-input>
        </el-col>
        <el-col :span="4">
          <el-button type="primary" @click="addDialogVisible = true">
            添加开课
          </el-button>
        </el-col>
      </el-row>
      <!-- 列表区域 -->
      <el-table :data="OpenListShow" border stripe>
        <!-- 自定义索引 -->
        <el-table-column type="index"> </el-table-column>
        <el-table-column prop="Open_id" label="开课号"></el-table-column>
        <el-table-column prop="Open_name" label="开课名"></el-table-column>
        <el-table-column prop="credit" label="学分"></el-table-column>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button
              type="primary"
              icon="el-icon-edit"
              size="mini"
              @click="showEditDialog(scope.row.Open_id)"
            >
            </el-button>
            <el-button
              type="danger"
              icon="el-icon-delete"
              size="mini"
              @click="deleteOpen(scope.row.Open_id)"
            >
            </el-button>
          </template>
        </el-table-column>
      </el-table>
      <!-- 分页栏 -->
      <el-pagination
        class="pagination"
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :current-page="currentPage"
        :page-sizes="[5, 10, 15]"
        :page-size="pageSize"
        layout="total, sizes, prev, pager, next, jumper"
        :total="total"
      >
      </el-pagination>
    </el-card>
    <!-- 添加开课对话框 -->
    <el-dialog
      title="添加开课"
      :visible.sync="addDialogVisible"
      width="50%"
      @close="addDialogClosed"
    >
      <!-- 内容主题区域 -->
      <el-form
        :model="addForm"
        :rules="addFormRules"
        ref="addFormRef"
        label-width="90px"
      >
        <el-form-item label="开课号" prop="Open_id">
          <el-input
            v-model="addForm.Open_id"
            placeholder="请输入开课号"
            clearable
          ></el-input>
        </el-form-item>
        <el-form-item label="开课名" prop="Open_name">
          <el-input
            v-model="addForm.Open_name"
            placeholder="请输入开课名"
            clearable
          ></el-input>
        </el-form-item>
        <el-form-item label="学分" prop="credit">
          <el-input
            v-model.number="addForm.credit"
            placeholder="请输入学分"
            clearable
          ></el-input>
        </el-form-item>
      </el-form>
      <!-- 底部区域 -->
      <span slot="footer" class="dialog-footer">
        <el-button @click="addDialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="addOpen"> 确 定 </el-button>
      </span>
    </el-dialog>
    <!-- 修改开课对话框 -->
    <el-dialog
      title="修改开课信息"
      :visible.sync="editDialogVisible"
      width="50%"
      @close="editDialogClosed"
    >
      <!-- 内容主题区域 -->
      <el-form
        :model="editForm"
        :rules="editFormRules"
        ref="editFormRef"
        label-width="90px"
      >
        <el-form-item label="开课号" prop="Open_id">
          <el-input v-model="editForm.Open_id" disabled></el-input>
        </el-form-item>
        <el-form-item label="开课名" prop="Open_name">
          <el-input
            v-model.number="editForm.Open_name"
            placeholder="请输入开课名"
            clearable
          ></el-input>
        </el-form-item>
         <el-form-item label="学分" prop="credit">
          <el-input
            v-model.number="editForm.credit"
            placeholder="请输入学分"
            clearable
          ></el-input>
        </el-form-item>
      </el-form>
      <!-- 底部区域 -->
      <span slot="footer" class="dialog-footer">
        <el-button @click="editDialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="editOpen"> 确 定 </el-button>
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
          value: '开课号',
          label: '开课号',
        },
        {
          value: '开课名',
          label: '开课名',
        },
        {
          value: '学分',
          label: '学分',
        },
      ],
      selected: '开课号', // 搜索选择
      input: '', // 搜索输入框
      OpenList: [], // 开课列表
      OpenListShow: [], // 展示的开课列表
      total: 0, // 开课列表总数
      currentPage: 1, // 当前页面
      pageSize: 5, // 每页展示列表数
      // 控制添加对话框显示与隐藏
      addDialogVisible: false,
      // 添加开课的表单数据
      addForm: {
        Open_id: '',
        Open_name: '',
        credit: 0,
      },
      // 添加表单的验证规则
      addFormRules: {
        Open_id: [
          { required: true, message: '请输入开课号', trigger: 'blur' },
          {
            min: 2,
            max: 6,
            message: '开课名长度在2~6个数字之间',
            trigger: 'blur',
          },
        ],
        Open_name: [
          { required: true, message: '请输入开课名', trigger: 'blur' },
          {
            min: 3,
            max: 20,
            message: '开课名长度在3~20个字符之间',
            trigger: 'blur',
          },
        ],
        credit: [
          { required: true, message: '请输入学分', trigger: 'blur' },
          {
            type: 'number',
            message: '学分为数字',
            trigger: 'blur',
          },
        ],
      },
      // 控制修改对话框显示与隐藏
      editDialogVisible: false,
      // 查询到的开课信息
      editForm: {},
      // 修改表单的验证规则
      editFormRules: {
        Open_name: [
          { required: false, message: '请输入开课名', trigger: 'blur' },
          {
            min: 3,
            max: 20,
            message: '开课名长度在3~20个字符之间',
            trigger: 'blur',
          },
        ],
        credit: [
          { required: false, message: '请输入学分', trigger: 'blur' },
          {
            type: 'number',
            message: '学分为数字',
            trigger: 'blur',
          },
        ],
      },
    }
  },
  created() {
    this.getOpenList()
  },
  methods: {
    // 获取开课列表
    async getOpenList(search) {
      var query = {}
      if (search) {
        if (this.selected === '开课号') {
          query = { Open_id: this.input }
        } else if (this.selected === '开课名') {
          query = { Open_name: this.input }
        } else if (this.selected === '学分') {
          query = { credit: this.input }
        }
      }
      const { data: res } = await this.$http.get('admin/Open/search/', {
        params: query,
      })
      if (res.status !== 200) return this.$message.error('获取开课列表失败')
      this.OpenList = res.data.Opens
      this.total = res.data.total

      this.currentPage = 1
      var start = 0
      var end = start + this.pageSize
      this.OpenListShow = res.data.Opens.slice(start, end)
      console.log(res)
    },
    // 监听对话框关闭事件
    addDialogClosed() {
      // 重置表单
      this.$refs.addFormRef.resetFields()
    },
    // 添加开课
    addOpen() {
      this.$refs.addFormRef.validate(async (valid) => {
        if (!valid) return
        // 校验正确则发起请求
        const { data: res } = await this.$http.post('admin/Open/create/', [
          this.addForm,
        ])
        if (res.status === 200) this.$message.success('添加成功！')
        else this.$message.error('添加失败！\n' + res.detail[0])
        this.addDialogVisible = false
        // 重新获取开课列表
        this.getOpenList()
      })
    },
    // 根据开课号开课信息
    async showEditDialog(id) {
      console.log(id)
      this.editDialogVisible = true
      const { data: res } = await this.$http.get('admin/Open/search/', {
        params: { Open_id: id },
      })
      if (res.status !== 200) return this.$message.error('获取开课列表失败')
      this.editForm = res.data.Opens[0]
      //   console.log(res)
    },
    // 监听修改对话框的关闭事件
    editDialogClosed() {
      this.$refs.editFormRef.resetFields()
    },
    // 修改开课信息
    editOpen() {
      this.$refs.editFormRef.validate(async (valid) => {
        // console.log(valid)
        if (!valid) return
        // 校验正确则发起请求
        const { data: res } = await this.$http.put(
          'admin/Open/edit/' + this.editForm.Open_id,
          {
            Open_name: this.editForm.Open_name,
            credit: this.editForm.credit,
          }
        )
        if (res.status !== 200)
          this.$message.error('修改失败！\n' + res.detail[0])
        this.$message.success('更新成功！')
        this.editDialogVisible = false
        // 重新获取开课列表
        this.getOpenList()
      })
    },
    // 删除开课
    deleteOpen(id) {
      // 弹框提示
      this.$confirm('此操作将永久删除该开课, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning',
      })
        .then(async () => {
          // 确定删除
          const { data: res } = await this.$http.delete(
            'admin/Open/edit/' + id
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
          // 刷新开课列表
          this.getOpenList()
        })
        .catch(() => {
          this.$message({
            type: 'info',
            message: '已取消删除',
          })
        })
    },
    // 监听分页变化
    handleSizeChange(pageSize) {
      this.pageSize = pageSize
      let start = 0
      let end = start + pageSize
      this.OpenListShow = this.OpenList.slice(start, end)
    },
    // 监听当前页面变化
    handleCurrentChange(currentPage) {
      this.currentPage = currentPage
      let start = (currentPage - 1) * this.pageSize
      let end = start + this.pageSize
      this.OpenListShow = this.OpenList.slice(start, end)
    },
  },
}
</script>
<style lang="less" scoped>
.select {
  width: 120px;
}
.pagination {
  margin-top: 15px;
}
</style>