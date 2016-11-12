require('es6-promise').polyfill();
var path = require('path');

module.exports = {
  entry: {
    sample_app: path.resolve(__dirname, "sample_app.jsx"),
  },
  output: {
    path: path.resolve(__dirname, "..", "sample_app", "static"),
    filename: "[name].js"
  },
  module: {
    preLoaders: [
      {
        test: /\.jsx?$/,
        exclude: /(node_modules|bower_components)/,
        loader: "eslint-loader"
      },
    ],
    loaders: [
      {
        test: /\.jsx?$/,
        exclude: /(node_modules|bower_components)/,
        loader: "babel",
        query: {
          presets: ["react", "es2015"]
        }
      },
      {
        test: /\.less$/,
        loader: "style!css!less"
      },
    ],
  },
  resolve: {
    extensions: ["", ".js", ".jsx"]
  },
};
