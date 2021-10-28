import Vue from 'vue'
import Vuetify from 'vuetify/lib'

Vue.use(Vuetify)

const vuetify = new Vuetify({
  theme: { 
    dark: true,
      themes: {
        light: {
          primary: '#EBEBEB',
          secondary: '#D8D4D8',
          accent: '#9A69A4',
          error: '#FF5252',
          info: '#2196F3',
          success: '#4CAF50',
          warning: '#FFC107',
        },
        dark: {
          primary: '#1F1F1F',
          secondary: '#2A2D32',
          accent: '#6F9BD9',
          error: '#FF5252',
          info: '#2196F3',
          success: '#4CAF50',
          warning: '#FFC107',
        }
      }
    }
  })
  
  export default vuetify