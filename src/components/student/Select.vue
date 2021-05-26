<template>
  <div>
    <el-card class="box-card-head">
      <el-form :inline="true">
        <el-form-item label="学年">
          <el-input
            placeholder="请输入学年"
            v-model="searchQuery.semester_year"
            disabled
          ></el-input>
        </el-form-item>
        <el-form-item label="学期">
          <el-select
            placeholder="请选择学期"
            v-model="searchQuery.semester_season"
            disabled
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
      </el-form>
    </el-card>
    <!-- 查询开课 -->
    <el-card class="box-card">
      <!-- 查询区域 -->
      <el-form :inline="true">
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
              @click="addScore(scope.row)"
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
    <!-- 已选选列表 -->
    <el-card class="box-card">
      <div><h1>已选课程</h1></div>
      <!-- 列表区域 -->
      <el-table :data="SelectListShow" border stripe>
        <!-- 自定义索引 -->
        <el-table-column type="index"> </el-table-column>
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
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button
              type="danger"
              icon="el-icon-delete"
              size="mini"
              @click="deleteScore(scope.row)"
            >
            </el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-card>
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
        semester_year: '2021',
        semester_season: '01',
        course: '',
        teacher: '',
      },
      OpenList: [], // 选课列表
      OpenListShow: [], // 展示的选课列表
      total: 0, // 选课列表总数
      currentPage: 1, // 当前页面
      pageSize: 5, // 每页展示列表数

      SelectListShow: [], // 已选课程
    }
  },
  created() {
    this.getOpenList()
    this.getSelectCourseList()
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
      const { data: res } = await this.$http.get('student/open/search/', {
        params: query,
      })
      //   console.log(res)
      if (res.status !== 200) return this.$message.error('获取开课列表失败')
      this.OpenList = res.Opens
      this.total = res.total
      this.currentPage = 1
      var start = 0
      var end = start + this.pageSize
      this.OpenListShow = res.Opens.slice(start, end)
    },
    // 获取已选列表
    async getSelectCourseList() {
      var query = {}
      if (
        this.searchQuery.semester_year != '' &&
        this.searchQuery.semester_season != ''
      ) {
        query.semester =
          this.searchQuery.semester_year + this.searchQuery.semester_season
      }
      const { data: res } = await this.$http.get('student/score/search/', {
        params: query,
      })
      console.log(res)
      if (res.status !== 200) return this.$message.error('获取选课列表失败')
      this.SelectListShow = res.Scores
      this.total = res.total
    },
    // 添加选课
    async addScore(row) {
      // console.log(row)
      const { data: res } = await this.$http.post(
        'student/score/create/?open=' + row.id
      )
      if (res.status === 200) this.$message.success('添加成功！')
      else this.$message.error('添加失败！\n' + '已选过该课程')
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
          console.log('确定')
          // 确定删除
          const { data: res } = await this.$http.delete('student/score/delete/', {
            params: {
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
          this.getSelectCourseList()
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
.box-card {
  margin-top: 10px;
}
.select {
  width: 120px;
}
.pagination {
  margin-top: 15px;
}
</style>