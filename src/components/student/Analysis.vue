<template>
  <div>
    <el-card class="card_box">
      <div id="main" style="width: 1200px; height: 550px"></div>
    </el-card>
  </div>
</template>
<script>
// 1.导入echarts
import * as echarts from 'echarts'

export default {
  data() {
    return {
      avgScoreList: [],
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
      this.drawChart()
    },
    // 获取统计数据
    async getData() {
      const { data: res } = await this.$http.get('student/analysis/')
      if (res.status !== 200) return this.$message.error('获取数据失败')
      console.log(res)
      this.avgScoreList = res.data
    },
    // 成绩分布图
    drawChart() {
      var myChart = echarts.init(document.getElementById('main'))
      var colors = ['#5470C6', '#91CC75', '#EE6666']
      var option = {
        title: {
          text: '平均成绩变化情况',
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
            data: this.avgScoreList.semester,
          },
        ],
        yAxis: [
          {
            type: 'value',
            name: '分数',
            min: 0,
            max: 100,
            position: 'left',
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
            type: 'line',
            name: '平均成绩',
            data: this.avgScoreList.avg_score,
          },
        ],
      }
      // 5.使用刚指定的配置项和数据显示图表。
      myChart.setOption(option)
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