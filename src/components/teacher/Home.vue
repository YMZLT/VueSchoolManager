<template>
  <el-container class="home_container">
    <!-- 头部区域 -->
    <el-header>
      <div>
        <img src="../../assets/logo_Shu.png" alt="" />
        <span>上海大学教务管理系统教师端</span>
      </div>
      <el-button type="info" @click="logout">退出</el-button>
    </el-header>
    <!-- 主体区域 -->
    <el-container>
      <!-- 侧边栏 -->
      <el-aside :width="isCollapse ? '64px' : '200px'">
        <div class="toggle-button" @click="toggleCollapse">|||</div>
        <el-menu
          background-color="#043454"
          text-color="#fff"
          unique-opened
          :collapse="isCollapse"
          :collapse-transition="false"
          router
          :default-active="activePath"
          active-text-color="#409BFF"
                 >
          <!-- 一级菜单 -->
          <el-submenu
            :index="item.id + ''"
            v-for="item in menuList"
            :key="item.id"
          >
            <!-- 一级菜单模板 -->
            <template slot="title">
              <!-- 图标 -->
              <i class="el-icon-setting"></i>
              <!-- 文本 -->
              <span>{{ item.authName }}</span>
            </template>

            <!-- 二级菜单 -->
            <el-menu-item
              :index="'/teacher/'+subItem.path"
              v-for="subItem in item.children"
              :key="subItem.id" 
              @click ="saveNavState('/teacher/'+subItem.path)"
            >
              <template slot="title">
                <i class="el-icon-menu"></i>
                <span>{{ subItem.authName }}</span>
              </template>    
            </el-menu-item>
          </el-submenu>
        </el-menu>
      </el-aside>
      <!-- 右侧主体 -->
      <el-main>
        <!-- 路由占位符 -->
        <router-view></router-view>
      </el-main>
    </el-container>
  </el-container>
</template>


<script>
export default {
  data() {
    return {
      // 左侧菜单数据
        menuList: [
            {
                //id: 1,
                authName: '教学相关',
                path: '',
                children: [
                    {
                        //id: 2,
                        authName: '课程教学大纲',
                        path: 'teachingschedule/',
                        
                    },
                    {
                      //  id: 2,
                        authName: '学生名单',
                        path: 'dictionary/',
                        children: [
                        ],
                    },
                    {
                       // id: 2,
                        authName: '成绩录入',
                        path: 'grade/',
                        children: [
                        ],
                    },
                    {
                       // id: 2,
                        authName: '课程班级成绩查询',
                        path: 'select/',
                        children: [
                        ],
                    },
                   /* {
                       // id: 2,
                        authName: '教学情况总结表',
                        path: null,
                        children: [
                        ],
                    },*/

                ],
            },
           /* {
               // id: 3,
                authName: '教学质量评估',
                path: '',
                children: [
                    {
                        //id: 2,
                        authName: '课堂教学质量评估',
                        path: '',

                    },
                    {
                       // id: 2,
                        authName:'历史授课清单及评教',
                        path: '',
                        children: [
                        ],
                    },

                ],
            },*/

      ],
      // 菜单图标
      iconsObj: {
        1: 'el-icon-menu',
        2: 'el-icon-date',
        3: 'el-icon-reading',
        4: 'el-icon-s-order',
        5: 'el-icon-s-data',
      },
      // 是否折叠导航菜单栏
      isCollapse: false,
      // 右侧目录栏被激活的链接地址
      activePath: '',
    }
  },
  created() {[[]]
    // this.getMenuList()
    this.activePath = window.sessionStorage.getItem('activePath')
  },
  methods: {
    // 退出登录
    logout() {
      window.sessionStorage.clear()
      this.$router.push('/login')
    },
    // 菜单折叠与展开
    toggleCollapse() {
      this.isCollapse = !this.isCollapse
    },
    // 保存链接的激活状态到sessionstorage 
    saveNavState(activePath) {
      window.sessionStorage.setItem('activePath', activePath)
      this.activePath = activePath
    },
  },
}
</script>


<style lang="less" scoped>
.el-header {
  background-color: #043454;
  display: flex;
  justify-content: space-between;
  padding-left: 0;
  align-items: center; //退出图标居中
  color: #eceff1;
  font-size: 20px;
 > div {
    display: flex;
    align-items: center;
    height:auto;
    span {
      margin-left: 15px;
      font-size:20px;
    }
    img {
      height: 50px;
      width: 50px;
    }

  }
}
.el-aside {
  background-color: #043454;
  > div{
           font-size:15px;
       }
  .el-menu {
    border-right: none;
  }
}
.el-main {
  background-color: #eceff1;
}
.home_container {
  height: 100%;
}
.toggle-button {
  background-color: #4a6886;
  font-size: 10px;
  line-height: 24px;
  color: #fff;
  text-align: center;
  letter-spacing: 0.2em;
}
</style>