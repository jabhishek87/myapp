var config = {
   entry: './src/app.js',

   output: {
    path: __dirname + "/src/",
    filename: "app.min.js"
  },

   devServer: {
      inline: true,
      port: 7777
   },

   module: {
      loaders: [
         {
            test: /\.jsx?$/,
            exclude: /node_modules/,
            loader: 'babel',

            query: {
               presets: ['es2015', 'react']
            }
         }
      ]
   }
}

module.exports = config;