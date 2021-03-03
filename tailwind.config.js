module.exports = {
  purge: [
    'flaskr/templates/*.html',
    'flaskr/templates/**/*.html',
    'flaskr/static/js/*.js',
  ],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      colors: {
        beige: '#f5d7b2',
      },
      fontFamily: {
        aurore: ['La Belle Aurore', 'cursive'],
        josefin: ['Josefin Sans', 'sans-serif'],
      },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
}