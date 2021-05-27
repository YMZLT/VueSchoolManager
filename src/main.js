import Vue from 'vue'
import App from './App.vue'
import router from './router'
import './plugins/element.js'
// 导入全局样式表
import './assets/css/global.css'

import axios from 'axios'
import Print from './utils/vue-print-nb/src'
Vue.use(Print)
// 配置请求的根路径
axios.defaults.baseURL = 'http://127.0.0.1:8001/'
// axios.defaults.baseURL = 'http://127.0.0.1:8888/api/private/v1/'
// 请求拦截器
axios.interceptors.request.use(config=>{
  // console.log(config)
  config.headers.authorization = 'jwt '+window.sessionStorage.getItem('token')
  return config
})
// 挂载到vue
Vue.prototype.$http = axios


Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
