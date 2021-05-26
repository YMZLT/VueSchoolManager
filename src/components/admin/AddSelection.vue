<template>
  <div>
    <!-- 面包屑导航区域 -->
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/admin/home' }"
        >首页</el-breadcrumb-item
      >
      <el-breadcrumb-item>教务管理</el-breadcrumb-item>
      <el-breadcrumb-item>添加选课</el-breadcrumb-item>
    </el-breadcrumb>
    <!-- 卡片视图 -->
    <el-card class="box-card">
      <!-- 查询区域 -->
      <el-form :inline="true">
        <el-form-item label="学年">
          <el-input
            placeholder="请输入学年"
            v-model="searchQuery.semester_year"
          ></el-input>
        </el-form-item>
        <el-form-item label="学期">
          <el-select
            placeholder="请选择学期"
            v-model="searchQuery.semester_season"
          >
            <el-option
              v-for="item in semesterMap"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            >
            </el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="课程号">
          <el-input
            placeholder="请输入课程号"
            v-model="searchQuery.course"
          ></el-input>
        </el-form-item>
        <el-form-item label="教师号">
          <el-input
            placeholder="请输入教师号"
            v-model="searchQuery.teacher"
          ></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" icon="el-icon-search" @click="getOpenList()"
            >查询课程</el-button
          >
        </el-form-item>
      </el-form>
      <!-- 列表区域 -->
      <el-table :data="OpenListShow" border stripe>
        <!-- 自定义索引 -->
        <el-table-column type="index"> </el-table-column>
        <!-- <el-table-column prop="id" label="选课号"></el-table-column> -->
        <el-table-column
          prop="course.course_id"
          label="课程号"
        ></el-table-column>
        <el-table-column
          prop="course.course_name"
          label="课程名"
        ></el-table-column>
        <el-table-column prop="course.credit" label="学分"></el-table-column>
        <el-table-column
          prop="teacher.user.user_id"
          label="教师号"
        ></el-table-column>
        <el-table-column
          prop="teacher.user.user_name"
          label="教师名"
        ></el-table-column>
        <el-table-column prop="semester" label="学期"></el-table-column>
        <el-table-column prop="course_time" label="上课时间"></el-table-column>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button
              type="primary"
              icon="el-icon-circle-plus-outline"
              size="mini"
              @click="showAddDialog(scope.row)"
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
    <!-- 添加选课对话框 -->
    <el-dialog
      title="添加选课"
      :visible.sync="addDialogVisible"
      width="50%"
      @close="addDialogClosed"
    >
      <!-- 内容主题区域 -->
      <el-form
        label-position="left"
        :model="addForm"
        :rules="addFormRules"
        ref="addFormRef"
        label-width="90px"
      >
        <el-form-item label="课程号" prop="course">
          <el-input v-model="addForm.course" disabled></el-input>
        </el-form-item>
        <el-form-item label="教师号" prop="teacher">
          <el-input v-model="addForm.teacher" disabled></el-input>
        </el-form-item>
        <el-form-item label="学期" prop="semester">
          <el-input v-model="addForm.semester" disabled></el-input>
        </el-form-item>
        <el-form-item label="上课时间" prop="course_time">
          <el-input v-model="addForm.course_time" disabled></el-input>
        </el-form-item>
        <el-form-item label="学号" prop="student">
          <el-input v-model="addForm.student"></el-input>
        </el-form-item>
      </el-form>
      <!-- 底部区域 -->
      <span slot="footer" class="dialog-footer">
        <el-button @click="addDialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="addScore"> 确 定 </el-button>
      </span>
    </el-dialog>
  </div>
</template>
<script>
export default {
  data() {
    return {
      semesterMap: [
        { value: '01', label: '春季' },
        { value: '02', label: '夏季' },
        { value: '03', label: '秋季' },
        { value: '04', label: '冬季' },
      ],
      searchQuery: {
        semester_year: '2020',
        semester_season: '01',
        course: '',
        teacher: '',
      },
      OpenList: [], // 选课列表
      OpenListShow: [], // 展示的选课列表
      total: 0, // 选课列表总数
      currentPage: 1, // 当前页面
      pageSize: 5, // 每页展示列表数
      // 控制添加对话框显示与隐藏
      addDialogVisible: false,
      // 添加选课的表单数据
      addForm: {},
      // 添加表单的验证规则
      addFormRules: {
        student: [
          { required: true, message: '请输入学号', trigger: 'blur' },
          {
            min: 8,
            max: 8,
            message: '学号长度为8个字符',
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
    // 获取选课列表
    async getOpenList() {
      var query = {}
      if (this.searchQuery.course != '') {
        query.course = this.searchQuery.course
      }
      if (this.searchQuery.teacher != '') {
        query.teacher = this.searchQuery.teacher
      }
      if (
        this.searchQuery.semester_year != '' &&
        this.searchQuery.semester_season != ''
      ) {
        query.semester =
          this.searchQuery.semester_year + this.searchQuery.semester_season
      }
      const { data: res } = await this.$http.get('admin/open/search_detail/', {
        params: query,
      })
      //   console.log(res)
      if (res.status !== 200) return this.$message.error('获取选课列表失败')
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
    // 根据选课号查询选课信息
    async showAddDialog(row) {
      //   console.log(row)
      this.addDialogVisible = true
      const { data: res } = await this.$http.get('admin/open/search/', {
        params: {
          course: row.course.course_id,
          teacher: row.teacher.user.user_id,
        },
      })
      if (res.status !== 200) return this.$message.error('获取开课信息失败')
      this.addForm = res.data.Opens[0]
      //   console.log(res)
    },
    // 添加选课
    addScore() {
      this.$refs.addFormRef.validate(async (valid) => {
        if (!valid) return
        // 校验正确则发起请求
        const { data: res } = await this.$http.post('admin/score/create/', [
          { open: this.addForm.id, student: this.addForm.student },
        ])
        if (res.status === 200) this.$message.success('添加成功！')
        else this.$message.error('添加失败！\n' +'已选过该课程')
        this.addDialogVisible = false
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