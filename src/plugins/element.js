import Vue from 'vue'
import { Button, Input, Message, Form, FormItem, 
    Container,Header,Aside,Main,
    Menu, Submenu, MenuItemGroup, MenuItem, Breadcrumb, BreadcrumbItem,
    Card, Row, Col, Table, TableColumn, Switch, Tooltip, Pagination, Select, Option, Dialog, MessageBox, Radio, RadioGroup, Upload, CheckboxGroup, Checkbox
} from 'element-ui'


Vue.use(Button)
Vue.use(Form)
Vue.use(FormItem)
Vue.use(Input)
Vue.use(Container)
Vue.use(Header)
Vue.use(Aside)
Vue.use(Main)
Vue.use(Menu)
Vue.use(Submenu)
Vue.use(MenuItemGroup)
Vue.use(MenuItem)
Vue.use(Breadcrumb)
Vue.use(BreadcrumbItem)
Vue.use(Card)
Vue.use(Row)
Vue.use(Col)
Vue.use(Table)
Vue.use(TableColumn)
Vue.use(Switch)
Vue.use(Tooltip)
Vue.use(Pagination)
Vue.use(Select)
Vue.use(Option)
Vue.use(Dialog)
Vue.use(Radio)
Vue.use(RadioGroup)
Vue.use(Upload)
Vue.use(Checkbox)
Vue.use(CheckboxGroup)
Vue.prototype.$message = Message
Vue.prototype.$confirm = MessageBox.confirm
