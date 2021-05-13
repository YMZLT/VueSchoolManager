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
        <!-- <el-table-column prop="id" label="开课号"></el-table-column> -->
        <el-table-column prop="course" label="课程号"></el-table-column>
        <el-table-column prop="teacher" label="教师号"></el-table-column>
        <el-table-column prop="semaster" label="学期"></el-table-column>
        <el-table-column prop="course_time" label="上课时间"></el-table-column>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button
              type="primary"
              icon="el-icon-edit"
              size="mini"
              @click="showEditDialog(scope.row)"
            >
            </el-button>
            <el-button
              type="danger"
              icon="el-icon-delete"
              size="mini"
              @click="deleteOpen(scope.row)"
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
        <el-form-item label="课程号" prop="course">
          <el-input
            v-model="addForm.course"
            placeholder="请输入课程号"
            clearable
          ></el-input>
        </el-form-item>
        <el-form-item label="教师号" prop="teacher">
          <el-input
            v-model="addForm.teacher"
            placeholder="请输入教师号"
            clearable
          ></el-input>
        </el-form-item>
        <el-form-item label="学期" prop="semaster">
          <el-input
            v-model="addForm.semaster"
            placeholder="请输入学期"
            clearable
          ></el-input>
        </el-form-item>
        <el-form-item label="上课时间" prop="course_time">
          <el-input
            v-model="addForm.course_time"
            placeholder="请输入上课时间"
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
        <el-form-item label="课程号" prop="course">
          <el-input v-model="editForm.course" disabled></el-input>
        </el-form-item>
        <el-form-item label="教师号" prop="teacher">
          <el-input
            v-model="editForm.teacher"
            placeholder="请输入教师号"
            disabled
          ></el-input>
        </el-form-item>
        <el-form-item label="学期" prop="semaster">
          <el-input
            v-model="editForm.semaster"
            placeholder="请输入学期"
            clearable
          ></el-input>
        </el-form-item>
        <el-form-item label="上课时间" prop="course_time">
          <el-input
            v-model="editForm.course_time"
            placeholder="请输入上课时间"
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
          value: '课程号',
          label: '课程号',
        },
        {
          value: '教师号',
          label: '教师号',
        },
        {
          value: '学期',
          label: '学期',
        },
        {
          value: '上课时间',
          label: '上课时间',
        },
      ],
      selected: '课程号', // 搜索选择
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
        course: '',
        teacher: '',
        semaster: '',
        course_time: '',
      },
      // 添加表单的验证规则
      addFormRules: {
        course: [
          { required: true, message: '请输入课程号', trigger: 'blur' },
          {
            min: 2,
            max: 6,
            message: '课程号长度在2~6个数字之间',
            trigger: 'blur',
          },
        ],
        teacher: [
          { required: true, message: '请输入教师号', trigger: 'blur' },
          {
            min: 4,
            max: 4,
            message: '工号长度为4个字符',
            trigger: 'blur',
          },
        ],
        semaster: [{ required: true, message: '请输入学期', trigger: 'blur' }],
        course_time: [
          { required: true, message: '请输入上课时间', trigger: 'blur' },
        ],
      },
      // 控制修改对话框显示与隐藏
      editDialogVisible: false,
      // 查询到的开课信息
      editForm: {
        semaster: '',
        course_time: '',
      },
      // 修改表单的验证规则
      editFormRules: {
        semaster: [{ required: false, message: '请输入学期', trigger: 'blur' }],
        course_time: [
          { required: false, message: '请输入上课时间', trigger: 'blur' },
        ],
      },
      // 学期转换
      semesterMap: ['春', '夏', '秋', '冬'],
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
        if (this.selected === '课程号') {
          query = { course: this.input }
        } else if (this.selected === '教师号') {
          query = { teacher: this.input }
        } else if (this.selected === '学期') {
          query = { semaster: this.input }
        } else if (this.selected === '上课时间') {
          query = { course_time: this.input }
        }
      }
      const { data: res } = await this.$http.get('admin/open/search/', {
        params: query,
      })
      console.log(res)
      if (res.status !== 200) return this.$message.error('获取开课列表失败')
      await res.data.Opens.forEach((element) => {
        var str = element.semaster
        var year = str.slice(0, 4)
        var sem = this.semesterMap[Number(str.slice(5)) - 1]
        element.semaster = year + '年' + sem + '季学期'
      })
      this.OpenList = res.data.Opens
      this.total = res.data.total
      this.currentPage = 1
      var start = 0
      var end = start + this.pageSize
      this.OpenListShow = res.data.Opens.slice(start, end)
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
        const { data: res } = await this.$http.post('admin/open/create/', [
          this.addForm,
        ])
        if (res.status === 200) this.$message.success('添加成功！')
        else this.$message.error('添加失败！\n' + res.detail[0])
        this.addDialogVisible = false
        // 重新获取开课列表
        this.getOpenList()
      })
    },
    // 根据开课号查询开课信息
    async showEditDialog(row) {
      console.log(row)
      this.editDialogVisible = true
      const { data: res } = await this.$http.get('admin/open/search/', {
        params: { course: row.course, teacher: row.teacher },
      })
      if (res.status !== 200) return this.$message.error('获取开课信息失败')
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
          'admin/open/edit/' + this.editForm.id,
          {
            course_time: this.editForm.course_time,
            semaster: this.editForm.semaster,
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
    deleteOpen(row) {
      // 弹框提示
      this.$confirm('此操作将永久删除该开课, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning',
      })
        .then(async () => {
          // 确定删除
          const { data: res } = await this.$http.delete('admin/open/edit/' + row.id)
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