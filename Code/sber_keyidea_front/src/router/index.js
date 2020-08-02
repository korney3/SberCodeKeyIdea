import Vue from 'vue'
import Router from 'vue-router'
import stat from '@/pages/stat'
import teams from '@/pages/teams'
import trends from '@/pages/trends'
import dashboard from '@/pages/dashboard'
import test from '@/pages/test'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      component: test
    },
    {
      path: '/stat',
      component: stat
    },
    {
      path: '/teams',
      component: teams
    },
    {
      path: '/trends',
      component: trends
    },
    {
      path: '/dashboard',
      component: dashboard
    },
    {
      path: '/test',
      component: test
    }
  ]
})
