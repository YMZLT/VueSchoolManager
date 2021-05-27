<template>
  <el-container class="home_container">
    <!-- 头部区域-->
    <el-header>
      <div>
        <img src="../../assets/system.png" alt="" />
        <span>上海大学教务管理系统学生端</span>
      </div>
      <el-button type="info" @click="logout">退出</el-button>
    </el-header>
    <!-- 主体区域 -->
    <el-container>
      <!-- 侧边栏 -->
      <el-aside :width="isCollapse ? '64px' : '200px'">
        <div class="toggle-button" @click="toggleCollapse">|||</div>
        <el-menu
          background-color="#2b4b6b"
          text-color="#fff"
          :collapse="isCollapse"
          :collapse-transition="false"
          router
          :default-active="activePath"
        >
          <!-- 一级菜单 -->
          <el-menu-item
            :index="'/' + item.path"
            v-for="item in menuList"
            :key="item.id"
            @click="saveNavState('/' + item.path)"
          >
            <!-- 一级菜单模板 -->
            <template slot="title">
              <!-- 图标 -->
              <i :class="iconsObj[item.id]"></i>
              <!-- 文本 -->
              <span>{{ item.authName }}</span>
            </template>
          </el-menu-item>
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
          id: 0,
          authName: '首页',
          path: 'student/home',
        },
        {
          id: 1,
          authName: '课程信息',
          path: 'student/courses',
        },
        {
          id: 2,
          authName: '选课信息',
          path: 'student/select',
        },
        {
          id: 3,
          authName: '成绩分析',
          path: 'student/Analysis',
        },
      ],
      // 菜单图标
      iconsObj: {
        0: 'el-icon-s-custom',
        1: 'el-icon-s-custom',
        2: 'el-icon-s-promotion',
        3: 'el-icon-s-goods',
        4: 'el-icon-s-order',
        5: 'el-icon-s-data',
      },
      // 是否折叠导航菜单栏
      isCollapse: false,
      // 被激活的链接地址
      activePath: '',
    }
  },
  created() {
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
    // 保存链接的激活状态
    saveNavState(activePath) {
      window.sessionStorage.setItem('activePath', activePath)
      this.activePath = activePath
    },
  },
}
</script>


<style lang="less" scoped>
.el-header {
  background-color: #2b4b6b;
  display: flex;
  justify-content: space-between;
  padding-left: 0;
  align-items: center;
  color: #eceff1;
  font-size: 20px;
  > div {
    display: flex;
    align-items: center;
    span {
      margin-left: 15px;
    }
    img {
      height: 50px;
      width: 50px;
    }
  }
}
.el-aside {
  background-color: #2b4b6b;
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