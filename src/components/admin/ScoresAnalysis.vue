<template>
  <div>
    <!-- 面包屑导航区域 -->
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/admin/home' }"
        >首页</el-breadcrumb-item
      >
      <el-breadcrumb-item>教务管理</el-breadcrumb-item>
      <el-breadcrumb-item>成绩分析</el-breadcrumb-item>
    </el-breadcrumb>
    <!-- 学生成绩查询区域 -->
    <el-card>
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
        <!-- <el-form-item label="课程号">
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
        </el-form-item> -->
        <el-form-item>
          <el-button type="primary" icon="el-icon-search" @click="refresh"
            >查询结果</el-button
          >
        </el-form-item>
      </el-form>
      <!-- 列表区域 -->
      <el-table :data="analysisListShow" border stripe>
        <!-- 自定义索引 -->
        <!-- <el-table-column type="index"> </el-table-column> -->
        <el-table-column prop="course_id" label="课程号"></el-table-column>
        <el-table-column prop="course_name" label="课程名"></el-table-column>
        <el-table-column prop="teacher_id" label="教师号"></el-table-column>
        <el-table-column prop="user_name" label="教师名"></el-table-column>
        <!-- <el-table-column prop="credit" label="学分"></el-table-column> -->
        <!-- <el-table-column prop="course_time" label="上课时间"></el-table-column> -->
        <el-table-column prop="student_num" label="学生人数"></el-table-column>
        <el-table-column prop="pass_num" label="及格人数"></el-table-column>
        <el-table-column prop="pass_rate" label="及格率"></el-table-column>
        <el-table-column prop="score_avg" label="平均分"></el-table-column>
        <el-table-column prop="score_min" label="最低分"></el-table-column>
        <el-table-column prop="score_max" label="最高分"></el-table-column>
        <el-table-column prop="difficulty" label="难度系数"></el-table-column>
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
    <el-card class="card_box">
      <div id="main" style="width: 1200px; height: 550px"></div>
    </el-card>
    <el-card class="card_box">
      <div id="chart_dificulty" style="width: 1200px; height: 550px"></div>
    </el-card>
    <el-card class="card_box">
      <div id="chart_distribution" style="width: 1200px; height: 550px"></div>
    </el-card>
  </div>
</template>
<script>
// 1.导入echarts
import * as echarts from 'echarts'

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
        semester_season: '02',
        course: '',
        teacher: '',
      },
      distribution: [],
      analysisList: [],
      analysisListShow: [],
      total: 0, // 列表总数
      currentPage: 1, // 当前页面
      pageSize: 5, // 每页展示列表数
    }
  },
  created() {},
  // 此时页面上的元素渲染完毕
  mounted() {
    this.refresh()
  },
  methods: {
    // 更新
    async refresh() {
      await this.getData()
      this.drawChart_1()
      this.drawChart_2()
      this.drawChart_3()
    },
    // 获取统计数据
    async getData() {
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
      const { data: res } = await this.$http.get(
        'admin/score/analysis/' + query.semester,
        {
          params: query,
        }
      )
      if (res.status !== 200) return this.$message.error('获取数据失败')
      console.log(res)
      res.basicData.forEach((element) => {
        element.pass_rate = element.pass_rate * 100
      })
      this.analysisList = res.basicData
      this.distribution = res.distribution.data
      this.distribution.unshift(res.distribution.columns)
      console.log(this.distribution)
      this.total = res.basicData.length

      this.currentPage = 1
      var start = 0
      var end = start + this.pageSize
      this.analysisListShow = res.basicData.slice(start, end)
    },
    // 绘制分析图
    drawChart_1() {
      // console.log(Number(this.searchQuery.semester_season))
      var season = this.semesterMap[
        Number(this.searchQuery.semester_season) - 1
      ].label
      // 3.基于准备好的dom，初始化echarts实例
      var myChart = echarts.init(document.getElementById('main'))
      var colors = ['#5470C6', '#91CC75', '#EE6666']
      // 4.指定图表的配置项和数据
      var option = {
        dataset: {
          // 用 dimensions 指定了维度的顺序。直角坐标系中，
          // 默认把第一个维度映射到 X 轴上，第二个维度映射到 Y 轴上。
          dimensions: ['course_id', 'score_avg', 'score_max', 'score_min'],
          source: this.analysisList,
        },
        title: {
          text: '平均分、最低分、最高分分布',
          subtext: `${this.searchQuery.semester_year}学年${season}学期`,
          x: 'center',
        },

        tooltip: {
          trigger: 'axis',
        },
        legend: {
          data: ['score_avg', 'score_max', 'score_min'],
          orient: 'vertical',
          x: 'right',
          y: 'center',
          formatter: function (name) {
            let myMap = new Map()
            myMap.set('score_avg', '平均分')
            myMap.set('score_max', '最高分')
            myMap.set('score_min', '最低分')
            return myMap.get(name)
          },
        },
        toolbox: {
          show: true,
          feature: {
            magicType: { show: true, type: ['line', 'bar'] },
            restore: { show: true },
            saveAsImage: { show: true },
          },
        },
        calculable: true,
        // 横轴
        xAxis: [
          {
            type: 'category',
            name: '课程号',
          },
        ],
        yAxis: [
          {
            type: 'value',
            name: '分数',
            axisLine: {
              show: true,
              lineStyle: {
                color: colors[0],
              },
            },
          },
        ],
        series: [
          {
            type: 'bar',
          },
          {
            type: 'bar',
          },
          {
            type: 'bar',
          },
        ],
      }
      // 5.使用刚指定的配置项和数据显示图表。
      myChart.setOption(option)
    },
    drawChart_2() {
      // console.log(Number(this.searchQuery.semester_season))
      var season = this.semesterMap[
        Number(this.searchQuery.semester_season) - 1
      ].label
      // 3.基于准备好的dom，初始化echarts实例
      var myChart = echarts.init(document.getElementById('chart_dificulty'))
      var colors = ['#5470C6', '#91CC75', '#EE6666']
      // 4.指定图表的配置项和数据
      var option = {
        dataset: {
          // 用 dimensions 指定了维度的顺序。直角坐标系中，
          // 默认把第一个维度映射到 X 轴上，第二个维度映射到 Y 轴上。
          dimensions: [
            'course_id',
            'student_num',
            'pass_num',
            'pass_rate',
            'difficulty',
          ],
          source: this.analysisList,
        },
        title: {
          text: '难度系数与及格关联情况',
          subtext: `${this.searchQuery.semester_year}学年${season}学期`,
          x: 'center',
        },
        tooltip: {
          trigger: 'axis',
        },
        legend: {
          top: '12%',
          data: ['student_num', 'pass_num', 'pass_rate', 'difficulty'],
          formatter: function (name) {
            let myMap = new Map()
            myMap.set('pass_num', '及格人数')
            myMap.set('student_num', '总人数')
            myMap.set('pass_rate', '及格率')
            myMap.set('difficulty', '难度系数')
            return myMap.get(name)
          },
        },
        toolbox: {
          show: true,
          feature: {
            magicType: { show: true, type: ['line', 'bar'] },
            restore: { show: true },
            saveAsImage: { show: true },
          },
        },
        calculable: true,
        // 横轴
        xAxis: [
          {
            type: 'category',
            name: '课程号',
          },
        ],
        yAxis: [
          {
            type: 'value',
            name: '人数',
            min: 0,
            max: 20,
            offset: 80,
            position: 'right',
            axisLine: {
              show: true,
              lineStyle: {
                color: colors[0],
              },
            },
          },
          {
            type: 'value',
            name: '难度系数',
            min: 0,
            max: 1,
            position: 'left',
            offset: 80,
            axisLine: {
              show: true,
              lineStyle: {
                color: colors[1],
              },
            },
          },
          {
            type: 'value',
            name: '通过率',
            min: 0,
            max: 100,
            position: 'left',
            offset: 0,
            axisLine: {
              show: true,
              lineStyle: {
                color: colors[2],
              },
            },
            axisLabel: {
              formatter: '{value} %',
            },
          },
        ],
        series: [
          {
            type: 'bar',
          },
          {
            type: 'bar',
          },
          {
            type: 'line',
            yAxisIndex: 2,
          },
          {
            type: 'line',
            yAxisIndex: 1,
          },
        ],
      }
      // 5.使用刚指定的配置项和数据显示图表。
      myChart.setOption(option)
    },
    // 成绩分布图
    drawChart_3() {
      var season = this.semesterMap[
        Number(this.searchQuery.semester_season) - 1
      ].label
      var myChart = echarts.init(document.getElementById('chart_distribution'))
      var series = []
      for (let i = 0; i < this.distribution.length-1; i++) {
        series.push({
          type: 'line',
          seriesLayoutBy: 'row',
        })
      }
      var colors = ['#5470C6', '#91CC75', '#EE6666']
      var option = {
        dataset: {
          source: this.distribution,
        },
        title: {
          text: '成绩分布情况',
          subtext: `${this.searchQuery.semester_year}学年${season}学期`,
          x: 'center',
        },
        tooltip: {
          trigger: 'axis',
        },
        legend: {
          orient: 'vertical',
          x: 'right',
          y: 'center',
        },
        toolbox: {
          show: true,
          feature: {
            magicType: { show: true, type: ['line', 'bar'] },
            restore: { show: true },
            saveAsImage: { show: true },
          },
        },
        calculable: true,
        // 横轴
        xAxis: [
          {
            type: 'category',
            // data: ['class_A', 'class_B', 'class_C', 'class_D', 'class_E'],
            // formatter: function (name) {
            //   let myMap = new Map()
            //   myMap.set('class_A', '90~100')
            //   myMap.set('class_B', '80~90')
            //   myMap.set('class_C', '70~80')
            //   myMap.set('class_D', '60~70')
            //   myMap.set('class_E', '0~60')
            //   return myMap.get(name)
            // },
          },
        ],
        yAxis: [
          {
            type: 'value',
            name: '人数',
            min: 0,
            max: 20,
            position: 'left',
            axisLine: {
              show: true,
              lineStyle: {
                color: colors[0],
              },
            },
          },
        ],
        series: series,
      }
      // 5.使用刚指定的配置项和数据显示图表。
      myChart.setOption(option)
    },
    // 监听分页变化
    handleSizeChange(pageSize) {
      this.pageSize = pageSize
      let start = 0
      let end = start + pageSize
      this.analysisListShow = this.analysisList.slice(start, end)
    },
    // 监听当前页面变化
    handleCurrentChange(currentPage) {
      this.currentPage = currentPage
      let start = (currentPage - 1) * this.pageSize
      let end = start + this.pageSize
      this.analysisListShow = this.analysisList.slice(start, end)
    },
  },
}
</script>
<style lang="less" scoped>
.card_box {
  margin-top: 20px;
}
.pagination {
  margin-top: 15px;
}
</style>