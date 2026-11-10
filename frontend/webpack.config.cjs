
const path = require("path");
const webpack = require("webpack");
const HtmlWebpackPlugin = require("html-webpack-plugin");

module.exports = (env, argv) => {
  const isProduction = argv.mode === "production";

  const API_URL =
    process.env.REACT_APP_API_URL ||
    "http://127.0.0.1:8000";

  return {
    mode: isProduction ? "production" : "development",

    entry: path.resolve(__dirname, "src/index.js"),

    output: {
      path: path.resolve(__dirname, "dist"),
      filename: "bundle.js",
      publicPath: "/",
      clean: true,
    },

    devtool: isProduction ? false : "eval-source-map",

    module: {
      rules: [
        {
          test: /\.jsx?$/,
          exclude: /node_modules/,
          type: "javascript/auto",
          use: {
            loader: "babel-loader",
            options: {
              sourceType: "unambiguous",
              presets: [
                "@babel/preset-env",
                [
                  "@babel/preset-react",
                  {
                    runtime: "automatic",
                    development: false,
                  },
                ],
              ],
            },
          },
        },
        {
          test: /\.css$/,
          use: ["style-loader", "css-loader"],
        },
      ],
    },

    resolve: {
      extensions: [".js", ".jsx"],
    },

    plugins: [
      new webpack.DefinePlugin({
        "process.env.REACT_APP_API_URL": JSON.stringify(API_URL),
      }),

      new HtmlWebpackPlugin({
        template: path.resolve(__dirname, "public/index.html"),
        inject: "body",
      }),
    ],

    devServer: {
      port: 3000,
      open: true,
      hot: true,
      historyApiFallback: true,
      static: {
        directory: path.resolve(__dirname, "public"),
      },
    },
  };
};
