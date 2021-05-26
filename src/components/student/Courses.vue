<template>
  <div>
    <!-- 卡片视图 -->
    <el-card class="box-card">
      <!-- 学生课程查询视图 -->
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
          <el-button type="primary" icon="el-icon-search" @click="getScoreList()">查询课程</el-button>
        </el-form-item>
      </el-form>

      <!-- 列表区域 -->
      <el-table :data="scoreListShow" border stripe>
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
        <el-table-column prop="score" label="成绩"></el-table-column>
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
      scoreList: [], // 课程列表
      scoreListShow: [], // 展示的课程列表
      total: 0, // 课程列表总数
      currentPage: 1, // 当前页面
      pageSize: 5, // 每页展示列表数
    }
  },
  created() {
    this.getScoreList()
  },
  methods: {
    // 获取课程列表
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
      const { data: res } = await this.$http.get('student/score/search/', {
        params: query,
      })
      if (res.status !== 200) return this.$message.error('获取课程列表失败')
      this.scoreList = res.Scores
      this.total = res.total

      this.currentPage = 1
      var start = 0
      var end = start + this.pageSize
      this.scoreListShow = res.Scores.slice(start, end)
      // console.log(res)
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