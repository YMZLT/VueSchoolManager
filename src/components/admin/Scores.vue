<template>
  <div>
    <!-- 面包屑导航区域 -->
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/admin/home' }"
        >首页</el-breadcrumb-item
      >
      <el-breadcrumb-item>教务管理</el-breadcrumb-item>
      <el-breadcrumb-item>成绩管理</el-breadcrumb-item>
    </el-breadcrumb>
    <!-- 卡片视图 -->
    <el-card class="box-card">
      <!-- 学生选课结果查询视图 -->
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
          <el-button type="primary" icon="el-icon-search" @click="getScoreList()">查询成绩</el-button>
        </el-form-item>
      </el-form>

      <!-- 列表区域 -->
      <el-table :data="scoreListShow" border stripe>
        <!-- 自定义索引 -->
        <el-table-column type="index"> </el-table-column>
        <el-table-column
          prop="student.user.user_id"
          label="学号"
        ></el-table-column>
        <el-table-column
          prop="student.user.user_name"
          label="姓名"
        ></el-table-column>
        <el-table-column prop="open.id" label="开课号"></el-table-column>
        <el-table-column
          prop="open.course.course_id"
          label="课程号"
        ></el-table-column>
        <el-table-column
          prop="open.course.course_name"
          label="课程名"
        ></el-table-column>
        <el-table-column
          prop="open.course_time"
          label="上课时间"
        ></el-table-column>
        <el-table-column
          prop="open.course.credit"
          label="学分"
        ></el-table-column>
        <el-table-column
          prop="open.teacher.user.user_id"
          label="教师号"
        ></el-table-column>
        <el-table-column
          prop="open.teacher.user.user_name"
          label="教师名"
        ></el-table-column>
        <el-table-column prop="score" label="成绩"></el-table-column>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button
              type="primary"
              icon="el-icon-edit"
              size="mini"
              @click="showEditDialog(scope.row)"
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
    <!-- 修改成绩对话框 -->
    <el-dialog
      title="修改开课信息"
      :visible.sync="editDialogVisible"
      width="50%"
      @close="editDialogClosed"
    >
      <!-- 内容主题区域 -->
      <el-form
        label-position="left"
        :model="editForm"
        :rules="editFormRules"
        ref="editFormRef"
        label-width="90px"
      >
        <el-form-item label="学号">
          <el-input v-model="editForm.student" disabled></el-input>
        </el-form-item>
        <el-form-item label="开课号">
          <el-input v-model="editForm.open" disabled></el-input>
        </el-form-item>
        <el-form-item label="课程号">
          <el-input v-model="editForm.course" disabled></el-input>
        </el-form-item>
        <el-form-item label="教师号">
          <el-input v-model="editForm.teacher" disabled></el-input>
        </el-form-item>
        <el-form-item label="学期">
          <el-input v-model="editForm.semester" disabled></el-input>
        </el-form-item>
        <el-form-item label="成绩">
          <el-input v-model.number="editForm.score"></el-input>
        </el-form-item>
      </el-form>
      <!-- 底部区域 -->
      <span slot="footer" class="dialog-footer">
        <el-button @click="editDialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="editScore"> 确 定 </el-button>
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
      scoreList: [], // 选课列表
      scoreListShow: [], // 展示的选课列表
      total: 0, // 选课列表总数
      currentPage: 1, // 当前页面
      pageSize: 5, // 每页展示列表数
      // 控制修改对话框显示与隐藏
      editDialogVisible: false,
      // 修改选课的表单数据
      editForm: {
        student: '',
        teacher: '',
        course: '',
        semester: '',
        score: 0.0,
      },
      // 修改表单的验证规则
      editFormRules: {
        score: [
          { required: true, message: '请输入成绩', trigger: 'blur' },
          {
            type: 'number',
            message: '成绩为数字',
            trigger: 'blur',
          },
        ],
      },
    }
  },
  created() {
    this.getScoreList()
  },
  methods: {
    // 获取选课列表
    async getScoreList() {
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

      const { data: res } = await this.$http.get('admin/score/search_detail/', {
        params: query,
      })
      if (res.status !== 200) return this.$message.error('获取选课列表失败')
      this.scoreList = res.data.Scores
      this.total = res.data.total

      this.currentPage = 1
      var start = 0
      var end = start + this.pageSize
      this.scoreListShow = res.data.Scores.slice(start, end)
      // console.log(res)
    },
    // 根据开课号查询开课信息
    async showEditDialog(row) {
      // console.log(row.open.id)
      this.editDialogVisible = true
      // const { data: res } = await this.$http.get('admin/score/search_detail/', {
      //   params: { student: row.student.user.user_id, open: row.open.id },
      // })
      // if (res.status !== 200) return this.$message.error('获取开课信息失败')
      this.editForm.student = row.student.user.user_id
      this.editForm.open = row.open.id
      this.editForm.teacher = row.open.teacher.user.user_id
      this.editForm.semester = row.open.semester
      this.editForm.course = row.open.course.course_id
      this.editForm.score = row.score
      // console.log(res)
    },
    // 监听修改对话框的关闭事件
    editDialogClosed() {
      this.$refs.editFormRef.resetFields()
    },
    // 修改开课信息
    async editScore() {
      this.$refs.editFormRef.validate(async (valid) => {
        // console.log(valid)
        if (!valid) return
        // 校验正确则发起请求
        console.log(this.editForm)
        const { data: res } = await this.$http.put(
          `admin/score/edit/?student=${this.editForm.student}&open=${this.editForm.open}`,
          {
            score: this.editForm.score,
          }
        )
        if (res.status !== 200)
          this.$message.error('修改失败！\n' + res.detail[0])
        this.$message.success('更新成功！')
        console.log(res)
        this.editDialogVisible = false
        // 重新获取开课列表
        this.getScoreList()
      })
    },
    // 删除选课
    deleteScore(row) {
      // 弹框提示
      this.$confirm('此操作将永久删除该选课, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning',
      })
        .then(async () => {
          // 确定删除
          const { data: res } = await this.$http.delete('admin/score/delete/', {
            params: {
              student: row.student.user.user_id,
              open: row.open.id,
            },
          })
          if (res.status != 200)
            return this.$message({
              type: 'error',
              message: '删除失败!',
            })

          this.$message({
            type: 'success',
            message: '删除成功!',
          })
          // 刷新选课列表
          this.getScoreList()
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
      this.scoreListShow = this.scoreList.slice(start, end)
    },
    // 监听当前页面变化
    handleCurrentChange(currentPage) {
      this.currentPage = currentPage
      let start = (currentPage - 1) * this.pageSize
      let end = start + this.pageSize
      this.scoreListShow = this.scoreList.slice(start, end)
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
.text {
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>