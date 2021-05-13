<template>
  <div>
    <!-- 面包屑导航区域 -->
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/admin/home' }"
        >首页</el-breadcrumb-item
      >
      <el-breadcrumb-item>信息管理</el-breadcrumb-item>
      <el-breadcrumb-item>课程列表</el-breadcrumb-item>
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
              @click="getCourseList(true)"
            ></el-button>
            <el-button
              slot="append"
              icon="el-icon-refresh-right"
              @click="getCourseList(false)"
            ></el-button>
          </el-input>
        </el-col>
        <el-col :span="4">
          <el-button type="primary" @click="addDialogVisible = true">
            添加课程
          </el-button>
        </el-col>
      </el-row>
      <!-- 列表区域 -->
      <el-table :data="courseListShow" border stripe>
        <!-- 自定义索引 -->
        <el-table-column type="index"> </el-table-column>
        <el-table-column prop="course_id" label="课程号"></el-table-column>
        <el-table-column prop="course_name" label="课程名"></el-table-column>
        <el-table-column prop="credit" label="学分"></el-table-column>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button
              type="primary"
              icon="el-icon-edit"
              size="mini"
              @click="showEditDialog(scope.row.course_id)"
            >
            </el-button>
            <el-button
              type="danger"
              icon="el-icon-delete"
              size="mini"
              @click="deleteCourse(scope.row.course_id)"
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
    <!-- 添加课程对话框 -->
    <el-dialog
      title="添加课程"
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
        <el-form-item label="课程号" prop="course_id">
          <el-input
            v-model="addForm.course_id"
            placeholder="请输入课程号"
            clearable
          ></el-input>
        </el-form-item>
        <el-form-item label="课程名" prop="course_name">
          <el-input
            v-model="addForm.course_name"
            placeholder="请输入课程名"
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
        <el-button type="primary" @click="addCourse"> 确 定 </el-button>
      </span>
    </el-dialog>
    <!-- 修改课程对话框 -->
    <el-dialog
      title="修改课程信息"
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
        <el-form-item label="课程号" prop="course_id">
          <el-input v-model="editForm.course_id" disabled></el-input>
        </el-form-item>
        <el-form-item label="课程名" prop="course_name">
          <el-input
            v-model.number="editForm.course_name"
            placeholder="请输入课程名"
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
        <el-button type="primary" @click="editCourse"> 确 定 </el-button>
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
          value: '课程名',
          label: '课程名',
        },
        {
          value: '学分',
          label: '学分',
        },
      ],
      selected: '课程号', // 搜索选择
      input: '', // 搜索输入框
      courseList: [], // 课程列表
      courseListShow: [], // 展示的课程列表
      total: 0, // 课程列表总数
      currentPage: 1, // 当前页面
      pageSize: 5, // 每页展示列表数
      // 控制添加对话框显示与隐藏
      addDialogVisible: false,
      // 添加课程的表单数据
      addForm: {
        course_id: '',
        course_name: '',
        credit: 0,
      },
      // 添加表单的验证规则
      addFormRules: {
        course_id: [
          { required: true, message: '请输入课程号', trigger: 'blur' },
          {
            min: 2,
            max: 6,
            message: '课程号长度在2~6个数字之间',
            trigger: 'blur',
          },
        ],
        course_name: [
          { required: true, message: '请输入课程名', trigger: 'blur' },
          {
            min: 3,
            max: 20,
            message: '课程名长度在3~20个字符之间',
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
      // 查询到的课程信息
      editForm: {},
      // 修改表单的验证规则
      editFormRules: {
        course_name: [
          { required: false, message: '请输入课程名', trigger: 'blur' },
          {
            min: 3,
            max: 20,
            message: '课程名长度在3~20个字符之间',
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
    this.getCourseList()
  },
  methods: {
    // 获取课程列表
    async getCourseList(search) {
      var query = {}
      if (search) {
        if (this.selected === '课程号') {
          query = { course_id: this.input }
        } else if (this.selected === '课程名') {
          query = { course_name: this.input }
        } else if (this.selected === '学分') {
          query = { credit: this.input }
        }
      }
      const { data: res } = await this.$http.get('admin/course/search/', {
        params: query,
      })
      if (res.status !== 200) return this.$message.error('获取课程列表失败')
      this.courseList = res.data.Courses
      this.total = res.data.total

      this.currentPage = 1
      var start = 0
      var end = start + this.pageSize
      this.courseListShow = res.data.Courses.slice(start, end)
      console.log(res)
    },
    // 监听对话框关闭事件
    addDialogClosed() {
      // 重置表单
      this.$refs.addFormRef.resetFields()
    },
    // 添加课程
    addCourse() {
      this.$refs.addFormRef.validate(async (valid) => {
        if (!valid) return
        // 校验正确则发起请求
        const { data: res } = await this.$http.post('admin/course/create/', [
          this.addForm,
        ])
        if (res.status === 200) this.$message.success('添加成功！')
        else this.$message.error('添加失败！\n' + res.detail[0])
        this.addDialogVisible = false
        // 重新获取课程列表
        this.getCourseList()
      })
    },
    // 根据课程号课程信息
    async showEditDialog(id) {
      console.log(id)
      this.editDialogVisible = true
      const { data: res } = await this.$http.get('admin/course/search/', {
        params: { course_id: id },
      })
      if (res.status !== 200) return this.$message.error('获取课程列表失败')
      this.editForm = res.data.Courses[0]
      //   console.log(res)
    },
    // 监听修改对话框的关闭事件
    editDialogClosed() {
      this.$refs.editFormRef.resetFields()
    },
    // 修改课程信息
    editCourse() {
      this.$refs.editFormRef.validate(async (valid) => {
        // console.log(valid)
        if (!valid) return
        // 校验正确则发起请求
        const { data: res } = await this.$http.put(
          'admin/course/edit/' + this.editForm.course_id,
          {
            course_name: this.editForm.course_name,
            credit: this.editForm.credit,
          }
        )
        if (res.status !== 200)
          this.$message.error('修改失败！\n' + res.detail[0])
        this.$message.success('更新成功！')
        this.editDialogVisible = false
        // 重新获取课程列表
        this.getCourseList()
      })
    },
    // 删除课程
    deleteCourse(id) {
      // 弹框提示
      this.$confirm('此操作将永久删除该课程, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning',
      })
        .then(async () => {
          // 确定删除
          const { data: res } = await this.$http.delete(
            'admin/course/edit/' + id
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
          // 刷新课程列表
          this.getCourseList()
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
      this.courseListShow = this.courseList.slice(start, end)
    },
    // 监听当前页面变化
    handleCurrentChange(currentPage) {
      this.currentPage = currentPage
      let start = (currentPage - 1) * this.pageSize
      let end = start + this.pageSize
      this.courseListShow = this.courseList.slice(start, end)
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