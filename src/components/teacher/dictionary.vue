<template>
  <div>
    <!-- 导航-->
    <el-breadcrumb separator="/">
      <el-breadcrumb-item :to="{ path: '/teacher/welcome' }"
        >首页</el-breadcrumb-item
      >
      <el-breadcrumb-item>教学相关</el-breadcrumb-item>
      <el-breadcrumb-item>学生名单</el-breadcrumb-item>
    </el-breadcrumb>
    <el-card>
      <!-- 搜索与添加区域 v-model提供数据绑定功能-->
      <el-row :gutter="20">
        <el-col :span="7">
          <el-input
            placeholder="请输入课程号"
            prefix-icon="el-icon-search"
            v-model="input1"
            clearable
            @clear="getstudent"
          >
          </el-input>
        </el-col>
        <el-col :span="7">
          <el-input
            placeholder="请输入学期"
            prefix-icon="el-icon-search"
            v-model="input2"
            clearable
            @clear="getstudent"
          >
          </el-input>
        </el-col>
        <el-col :span="4">
          <el-button @click="getstudent" type="primary"> 搜索 </el-button>
        </el-col>
        <el-col :span="4">
          <el-button type="text" @click="toImg">转至打印页</el-button>
        </el-col>
      </el-row>
      <!--课程列表区域-->
      <div id="printMe" ref="printContent">
        <!-- <el-table><el-table-column :label="this.input2 +'学期'+this.studentlist[0].open.course.course_name +'课程学生名单'" align="center">
          </el-table-column></el-table> -->
        <el-table :data="studentlistShow" border stripe>
          <el-table-column type="index" align="center"></el-table-column>
          <el-table-column
            label="学号"
            prop="student.user.user_id"
            width="100px"
            align="center"
          ></el-table-column>
          <el-table-column
            label="姓名"
            prop="student.user.user_name"
            width="110px"
            align="center"
          ></el-table-column>
          <el-table-column
            label="课程号"
            prop="open.course.course_id"
            width="90px"
            align="center"
          ></el-table-column>
          <el-table-column
            label="课程名"
            prop="open.course.course_name"
            width="150px"
            align="center"
          ></el-table-column>
          <el-table-column
            label="上课时间"
            prop="open.course_time"
            width="120px"
            align="center"
          ></el-table-column>
          <el-table-column label="出勤" align="center">
            <template>
              <el-checkbox-group v-model="checkList">
                <el-checkbox label="1"></el-checkbox>
                <el-checkbox label="2"></el-checkbox>
                <el-checkbox label="3"></el-checkbox>
                <el-checkbox label="4"></el-checkbox>
                <el-checkbox label="5"></el-checkbox>
                <el-checkbox label="6"></el-checkbox>
                <el-checkbox label="7"></el-checkbox>
                <el-checkbox label="8"></el-checkbox>
                <el-checkbox label="9"></el-checkbox>
                <el-checkbox label="10"></el-checkbox>
              </el-checkbox-group>
            </template>
          </el-table-column>
        </el-table>
      </div>

      <!--页码栏-->
      <el-pagination
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :current-page="currentPage"
        :page-sizes="[1, 2, 3, 5]"
        :page-size="pageSize"
        layout="total, sizes, prev, pager, next, jumper"
        :total="total"
      >
      </el-pagination>
    </el-card>
  </div>
</template>

<script>
import html2canvas from 'html2canvas'
import printJS from 'print-js'
export default {
  data() {
    return {
      input1: '',
      input2: '',
      studentlist: [],
      studentlistShow: [],
      total: 0, // 列表总数
      currentPage: 1, // 当前页面
      pageSize: 3, // 每页展示列表数
      checkList: [],
    }
  },
  created() {
    this.getstudent()
  },
  methods: {
    async getstudent() {
      var query = {
        teacher: sessionStorage.getItem('user'),
      }
      if (this.input1) {
        query.course = this.input1
      }
      if (this.input2) {
        query.semester = this.input2
      }
      const { data: res } = await this.$http.get('teacher/score/search/', {
        params: query,
      })
      if (res.status !== 200) return this.$message.error('获取学生列表失败')
    //   console.log(res)
      this.studentlist = res.data.Scores
      this.total = res.data.total
      this.currentPage = 1
      var start = 0
      var end = start + this.pageSize
      this.studentlistShow = res.data.Scores.slice(start, end)
      //   console.log(res.data.Scores[0].open.course.course_name)
    },

    handleSizeChange(pageSize) {
      console.log(pageSize)
      this.pageSize = pageSize
      let start = 0
      let end = start + pageSize
      this.studentlistShow = this.studentlist.slice(start, end)
    },
    // 监听当前页面变化
    handleCurrentChange(currentPage) {
      this.currentPage = currentPage
      let start = (currentPage - 1) * this.pageSize
      let end = start + this.pageSize
      this.studentlistShow = this.studentlist.slice(start, end)
    },
    //转至打印页
    toImg() {
      html2canvas(this.$refs.printContent, {
        backgroundColor: null,
        useCORS: true,
        windowHeight: document.body.scrollHeight,
      }).then((canvas) => {
        // let url = canvas.toDataURL('image/jpeg', 1.0)
        const url = canvas.toDataURL()
        this.img = url
        printJS({
          printable: url,
          type: 'image',
          documentTitle: '打印图片',
        })
        // console.log(url)
      })
    },
  },
}
</script>

<style lang="less" scoped>
.demo-input-label {
  display: inline-block;
  width: 130px;
}

.select {
  width: 120px;
}
</style>