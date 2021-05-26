import Vue from 'vue'
import Router from 'vue-router'
import Login from './components/Login.vue'
// 管理员页面
import Home_admin from './components/admin/Home.vue'
import Welcome_admin from './components/admin/Welcome.vue'
import Admins from './components/admin/Admins.vue'
import Students from './components/admin/Students.vue'
import Teachers from './components/admin/Teachers.vue'
import Colleges from './components/admin/Colleges.vue'
import Courses from './components/admin/Courses.vue'
import Opens from './components/admin/Opens.vue'
import Selections from './components/admin/Selections.vue'
import AddSelection from './components/admin/AddSelection.vue'
import Scores from './components/admin/Scores.vue'
import ScoresAnalysis from './components/admin/ScoresAnalysis.vue'

// 学生页面
import Home_student from './components/student/Home.vue'
import Welcome_student from './components/student/Welcome.vue'
import Courses_Info from './components/student/Courses.vue'
import Select from './components/student/Select.vue'
import Analysis from './components/student/Analysis.vue'


// 教师页面
import Home_teacher from './components/teacher/Home.vue'
import Welcome_teacher from './components/teacher/Welcome.vue'

Vue.use(Router)

const router = new Router({
  routes: [
    // 重定向
    { path: '/', redirect: '/login' },
    { path: '/login', component: Login },

    // 管理员页面路由
    { path: '/admin', redirect: '/admin/home' },
    {
      path: '/admin/home',
      component: Home_admin,
      redirect: '/admin/welcome',
      children: [
        { path: '/admin/welcome', component: Welcome_admin },
        { path: '/admin/admins', component: Admins },
        { path: '/admin/students', component: Students },
        { path: '/admin/teachers', component: Teachers },
        { path: '/admin/colleges', component: Colleges },
        { path: '/admin/courses', component: Courses },
        { path: '/admin/opens', component: Opens },
        { path: '/admin/selections', component: Selections },
        { path: '/admin/addSelection', component: AddSelection },
        { path: '/admin/scores', component: Scores },
        { path: '/admin/scoresAnalysis', component: ScoresAnalysis },
      ]
    },
    
    {
      path: '/student/home',
      component: Home_student,
      redirect: '/student/welcome',
      children: [
        { path: '/student/welcome', component: Welcome_student },
        { path: '/student/courses', component: Courses_Info },
        { path: '/student/select', component: Select },
        { path: '/student/Analysis', component: Analysis },
      ]
    },
    {
      path: '/teacher/home',
      component: Home_teacher,
      redirect: '/teacher/welcome',
      children: [
        { path: '/teacher/welcome', component: Welcome_teacher },
      ]
    },
  ]
})

// 挂载路由导航守卫
router.beforeEach((to, from, next) => {
  // to:将要访问的路径
  // from:跳转来的路径
  // next:放行函数 next()放行  next('/login') 强制跳转
  if (to.path === '/login') return next();
  // 获取token
  const tokenStr = window.sessionStorage.getItem('token');
  if (!tokenStr) return next('/login');
  next()
})
export default router