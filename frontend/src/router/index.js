import { createRouter, createWebHistory } from 'vue-router';
import card_parks from '../views/card_parks.vue';
import card_hotel from '../views/card_hotel.vue';
import card_theater from '../views/card_theater.vue';
import card_rest from '../views/card_rest.vue';

import card_catalog_theater_wrapper from '../views/card_catalog_theater_wrapper.vue';
import card_catalog_hotel_wrapper from '../views/card_catalog_hotel_wrapper.vue'
import card_catalog_rest_wrapper from '../views/card_catalog_rest_wrapper.vue'

import card_catalog_parks_wrapper from '../views/card_catalog_parks_wrapper.vue'
import main_page from '../views/main_page.vue';





const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/card_catalog_theater_wrapper',
      name: 'card_catalog_theater_wrapper',
      component: card_catalog_theater_wrapper,
          // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      // component: () => import('../components/card_catalog_wrapper.vue')
    },  {
      path:"/card_catalog_hotel_wrapper",
      name:'card_catalog_hotel_wrapper',
      component:card_catalog_hotel_wrapper,
    },
  
    
   
    {
      path:'/card_catalog_rest_wrapper',
      name:'card_catalog_rest_wrapper',
      component:card_catalog_rest_wrapper,
    },
    {
      path: '/card_catalog_parks_wrapper',
      name: 'card_catalog_parks_wrapper',
      component: card_catalog_parks_wrapper,
          // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      // component: () => import('../components/card_catalog_wrapper.vue')
    },
    
  
   {
    path:'/card_parks',
    name:'card_parks',
    component:card_parks,
    // component: () => import('../components/header_page.vue')

   },
   {
    path:'/',
    name:'main_page',
    component:main_page
   },
   {
    path:'/card_rest',
    name:'card_rest',
    component:card_rest
   },
   {
    path:'/card_hotel',
    name:'card_hotel',
    component:card_hotel
   },
   {
    path:'/card_theater',
    name:'card_theater',
    component:card_theater
   },
   


  
  ]
})

export default router
