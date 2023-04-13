import {createStore} from 'vuex'
import axios from 'axios';
const store=createStore({
  state:{
    top_3_products:[],
    hotels:[],
    rests:[],
    theaters:[],
    parks:[],
  },
  mutations:{
    SET_TOP_3_PRODUCTS_TO_STATE:(state,top_3_products)=>{
   state.top_3_products=top_3_products;
  
    },




    SET_CARD_HOTEL_PRODUCTS_TO_STATE:(state,hotels)=>{
    state.hotels=hotels;
    },
    SET_CARD_THEATER_PRODUCTS_TO_STATE:(state,theaters)=>{
      state.theaters=theaters;
    },
    SET_CARD_REST_PRODUCTS_TO_STATE:(state,rests)=>{
      state.rests=rests;
    },
    SET_CARD_PARK_PRODUCTS_TO_STATE:(state,parks)=>{
      state.parks=parks;
    },
  },







  actions:{
    async GET_PRODUCTS_FROM_API({commit}){
      try {
        const top_3_products = await axios("  http://localhost:3000/hotels", {
          method: "GET"
        });
        commit('SET_TOP_3_PRODUCTS_TO_STATE', top_3_products.data);
        return top_3_products;
      }
       catch (error) {
        console.log(error);
        return error;
      }
    },



    async GET_PRODUCTS_HOTEL_FROM_API({commit}){
      try{
      const hotels = await axios ("http://localhost:3000/hotels",{
        method:"GET"
      });
      commit('SET_CARD_HOTEL_PRODUCTS_TO_STATE',hotels.data);
      return hotels;
    }
    catch (error){
      console.log(error);
      return error;
    }
  },

  async GET_PRODUCTS_THEATER_FROM_API({commit}){
    try{
    const theaters = await axios ("http://localhost:5000/theaters",{
      method:"GET"
    });
    commit('SET_CARD_THEATER_PRODUCTS_TO_STATE',theaters.data);
    return theaters;
  }
  catch (error){
    console.log(error);
    return error;
  }
},


async GET_PRODUCTS_REST_FROM_API({commit}){
  try{
  const rests = await axios (" http://localhost:6000/rests",{
    method:"GET"
  });
  commit('SET_CARD_REST_PRODUCTS_TO_STATE',rests.data);
  return rests;
}
catch (error){
  console.log(error);
  return error;
}
},

async GET_PRODUCTS_PARK_FROM_API({commit}){
  try{
  const parks = await axios ("http://localhost:7000/parks",{
    method:"GET"
  });
  commit('SET_CARD_REST_PRODUCTS_TO_STATE',parks.data);
  return parks;
}
catch (error){
  console.log(error);
  return error;
}
},





  },







  getters:{
    TOP_3_PRODUCTS(state){
      return state.top_3_products;
    },
  HOTELS(state){
       return state.hotels;
  },
  THEATERS(state){
    return state.theaters;
},
  RESTS(state){
  return state.rests;
},
PARKS(state){
  return state.parks;
},


  }


})
export default store;