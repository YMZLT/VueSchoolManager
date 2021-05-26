<template>
    <div>
        <!-- 导航-->
        <el-breadcrumb separator="/">
            <el-breadcrumb-item :to="{ path: '/teacher/welcome' }">首页</el-breadcrumb-item>
            <el-breadcrumb-item>教学相关</el-breadcrumb-item>
            <el-breadcrumb-item>课程简介及教学大纲</el-breadcrumb-item>
        </el-breadcrumb>
        <el-card>
            <!-- 搜索与添加区域 v-model提供数据绑定功能-->
            <el-row :gutter="20">
                <el-col :span="16">
                    <el-input :placeholder="'请输入'+selected"
                              prefix-icon="el-icon-search"
                              v-model="input"
                              clearable
                              @clear="getcourseName"
                              >
                        <el-select v-model="selected"
                                   slot="prepend"
                                   placeholder="请选择"
                                   class="select">
                            <el-option v-for="item in options"
                                       :key="item.value"
                                       :label="item.label"
                                       :value="item.value">
                            </el-option>
                        </el-select>
                        <el-button  @click="getcourseName" slot="append">
                            搜索
                        </el-button>
                    </el-input>
                </el-col>

            </el-row>
            <!--课程列表区域-->
            <el-table :data="courselistShow" border stripe>
                <el-table-column type="index" label="#"></el-table-column>
                <el-table-column label="课程号" prop="course.course_id"  align="center"></el-table-column>
                <el-table-column label="课程名称" prop="course.course_name"  align="center"></el-table-column>
                <el-table-column label="教师号" prop="teacher.user.user_id"  align="center"></el-table-column>
                <el-table-column label="教师名" prop="teacher.user.user_name"  align="center"></el-table-column>
                <!--通过作用域插槽-->
                <el-table-column label="编辑" align="center">
                    <template>
                        <!--上传按钮-->
                        <el-upload class="upload-teachingschedule"
                                   action="http://127.0.0.1:8001/teacher/save_pdf/"
                                   :on-preview="handlePreview"
                                   :on-remove="handleRemove"
                                   :before-remove="beforeRemove"
                                   multiple
                                   :limit="3"
                                   :on-exceed="handleExceed">
                            <el-button slot="trigger" size="mini" type="text">点击此处上传教学大纲</el-button>
                        </el-upload>
                        <!--修改按钮
    <el-button type="primary" icon="el-icon-edit" size="mini">修改</el-button>
    删除按钮
                        <el-button type="danger" icon="el-icon-delete" size="mini">删除</el-button>-->
                    </template>
                </el-table-column>
  
            </el-table>
            <!--页码栏-->
            <el-pagination @size-change="handleSizeChange"
                           @current-change="handleCurrentChange"
                           :current-page="currentPage"
                           :page-sizes="[1, 2, 3, 5]"
                           :page-size="pageSize"
                           layout="total, sizes, prev, pager, next, jumper"
                           :total="total">
            </el-pagination>
        </el-card>

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
                        value: '学期',
                        label: '学期',
                    },
                    {
                        value: '教师号',
                        label: '教师号',
                    }
                ],
                selected: '', // 搜索选择
                input: '',
                //获取课程列表
                //query: {
                //    course_id: '',
                   // course_name: ''
                    //teacher: ''
               // },
                courselist: [],
                total: 0, // 院系列表总数
                currentPage: 1, // 当前页面
                pageSize: 3, // 每页展示列表数
            }
        },
        created() {
            this.getcourseName()
        },
        methods: {
            async getcourseName(select) {
                var query = {}
                if (select) {
                    if (this.selected === '课程号') {
                        query = { course_id: this.input }
                    } else if (this.selected === '学期') {
                        query = { semester: this.input }
                    } else if (this.selected === '教师号')
                        query = {teacher: this.input}

                }
                else
                    query = {}
                const { data: res } = await this.$http.get('teacher/open/search/', { params: query })
                if (res.status !== 200) return this.$message.error('获取课程列表失败')
                this.courselist = res.data.Opens
                this.total = res.data.total
                this.currentPage = 1
                var start = 0
                var end = start + this.pageSize
                this.courselistShow = res.data.Opens.slice(start, end)
                console.log(res)
            },
            //教学大纲上传
            handleRemove(file, fileList) {
                console.log(file, fileList);
            },
            handlePreview(file) {
                console.log(file);
            },
            handleExceed(files, fileList) {
                this.$message.warning(`当前限制选择 3 个文件，本次选择了 ${files.length} 个文件，共选择了 ${files.length + fileList.length} 个文件`);
            },
            beforeRemove(file, fileList) {
                return this.$confirm(`确定移除 ${file.name}？`);
            },
            handleSizeChange(pageSize) {
                console.log(pageSize)
                this.pageSize = pageSize
                let start = 0
                let end = start + pageSize
                this.courselistShow = this.courselist.slice(start, end)
            },
            // 监听当前页面变化
            handleCurrentChange(currentPage) {
                this.currentPage = currentPage
                let start = (currentPage - 1) * this.pageSize
                let end = start + this.pageSize
                this.courselistShow = this.courselist.slice(start, end)
            },
        }

    }
</script>

<style lang="less" scoped>
    .demo-input-label {
        display: inline-block;
        width: 130px;
    }
    .select{
        width:120px
    }
</style>