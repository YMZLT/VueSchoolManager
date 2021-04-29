import Vue from 'vue'
import Router from 'vue-router'
import Login from './components/Login.vue'
import Home_admin from './components/admin/Home.vue'
import Welcome_admin from './components/student/Welcome.vue'
import Home_student from './components/student/Home.vue'
import Welcome_student from './components/student/Welcome.vue'
import Home_teacher from './components/teacher/Home.vue'
import Welcome_teacher from './components/teacher/Welcome.vue'

Vue.use(Router)

const router = new Router({
  routes: [
    // 重定向
    { path: '/', redirect: '/login' },
    { path: '/login', component: Login },
    {
      path: '/admin/home',
      component: Home_admin,
      redirect: '/admin/welcome',
      children: [
        { path: '/admin/welcome', component: Welcome_admin },
      ]
    },
    {
      path: '/student/home',
      component: Home_student,
      redirect: '/student/welcome',
      children: [
        { path: '/student/welcome', component: Welcome_student },
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