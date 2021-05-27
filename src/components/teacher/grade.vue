<template>
  <div>
    <!-- 导航-->
    <el-breadcrumb separator="/">
      <el-breadcrumb-item :to="{ path: '/teacher/welcome' }"
        >首页</el-breadcrumb-item
      >
      <el-breadcrumb-item>教学相关</el-breadcrumb-item>
      <el-breadcrumb-item>成绩录入</el-breadcrumb-item>
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
      </el-row>
      <!--课程列表区域-->
      <div id="printMe" ref="printContent">
        <!-- <el-table-column
            :label="
              this.input2 +
              '   学期   ' +
              this.studentlist[0].open.course.course_name +
              '   课程   学生成绩登记表'
            "
            align="center"
          >
          </el-table-column> -->
        <el-table :data="studentlistShow" border stripe>
          <el-table-column type="index" align="center"></el-table-column>
          <el-table-column
            label="学号"
            prop="student.user.user_id"
            width="120px"
            align="center"
          ></el-table-column>
          <el-table-column
            label="姓名"
            prop="student.user.user_name"
            width="100px"
            align="center"
          ></el-table-column>
          <el-table-column
            label="课程号"
            prop="open.course.course_id"
            width="100px"
            align="center"
          ></el-table-column>
          <el-table-column
            label="课程名"
            prop="open.course.course_name"
            width="150px"
            align="center"
          ></el-table-column>
          <el-table-column
            label="学期"
            prop="open.semester"
            width="100px"
            align="center"
          ></el-table-column>
          <el-table-column label="成绩" align="center">
            <template slot-scope="scope">
              <el-button
                type="text"
                icon="el-icon-circle-plus-outline"
                size="medium"
                @click="showAddDialog(scope.row.student.user.user_id)"
                >录入</el-button
              >
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
    <!--新录入学生成绩表单-->
    <el-dialog
      title="学生成绩登记"
      :visible.sync="addDialogVisible"
      width="50%"
      @close="addDialogClosed"
    >
      <!-- 表单布局 -->
      <el-form
        :model="addForm"
        :rules="addFormRules"
        ref="addFormRef"
        labei-position="right"
        label-width="68px"
      >
        <el-row>
          <el-col span="12">
            <el-form-item label="学号" prop="user_id">
              <el-input v-model="addForm.user_id" disabled></el-input>
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="姓名" prop="user_name">
              <el-input v-model="addForm.user_name" disabled></el-input>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="12">
            <el-form-item label="课程号" prop="course_id">
              <el-input v-model="addForm.course_id" disabled></el-input>
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="课程名" prop="course_name">
              <el-input v-model="addForm.course_name" disabled></el-input>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="15">
            <el-form-item label="成绩" prop="score">
              <el-input
                v-model.number="addForm.score"
                placeholder="请输入学生成绩"
                clearable
              ></el-input>
            </el-form-item>
          </el-col>
        </el-row>
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
      input1: '',
      input2: '',
      studentlist: [],
      studentlistShow: [],
      total: 0, // 列表总数
      currentPage: 1, // 当前页面
      pageSize: 3, // 每页展示列表数
      checkList: [],
      // 控制添加对话框显示与隐藏
      addDialogVisible: false,
      // 添加课程的表单数据
      addForm: {
        user_id: '',
        user_name: '',
        course_id: '',
        course_name: '',
        score: '',
      },
      // 添加表单的验证规则
      addFormRules: {
        score: [
          { required: true, message: '成绩不能为空', trigger: 'blur' },
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
      this.studentlist = res.data.Scores
      this.total = res.data.total
      this.currentPage = 1
      var start = 0
      var end = start + this.pageSize
      this.studentlistShow = res.data.Scores.slice(start, end)
      console.log(res)
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
    // 监听对话框关闭事件
    addDialogClosed() {
      // 重置表单
      this.$refs.addFormRef.resetFields()
    },
    // 载入学生信息
    async showAddDialog(id) {
      console.log(id) //get每行的学生学号
      this.addDialogVisible = true
      const { data: res } = await this.$http.get('teacher/score/search/', {
        params: { student: id, teacher: sessionStorage.getItem('user') },
      })
      if (res.status !== 200) return this.$message.error('获取学生列表失败')
      console.log(res.data)

      this.addForm.user_id = res.data.Scores[0].student.user.user_id
      this.addForm.user_name = res.data.Scores[0].student.user.user_name
      this.addForm.course_id = res.data.Scores[0].open.course.course_id
      this.addForm.course_name = res.data.Scores[0].open.course.course_name
      //   console.log(res)
    },
    // 录入成绩
    addScore() {
      this.$refs.addFormRef.validate(async (valid) => {
        if (!valid) return
        // 校验正确则发起请求
        const { data: res } = await this.$http.put(
          'teacher/score/edit/?student=' + this.addForm.user_id,
          {
            score: this.addForm.score,
          }
        )
        if (res.status === 200) this.$message.success('添加成功！')
        else this.$message.error('添加失败！\n' + res.detail[0])
        this.addDialogVisible = false
        // 重新获取课程列表
        this.getstudent()
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