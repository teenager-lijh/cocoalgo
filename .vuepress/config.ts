import { defineConfig } from "vuepress/config";
import navbar from "./navbar";
import sidebar from "./sidebar";
import footer from "./footer";
import extraSideBar from "./extraSideBar";

const author = "蓝莓";
const domain = "https://blueberry-universe.cn";
const tags = ["编程", "计算机", "分布式系统"];

export default defineConfig({
  title: "酷酷的算法",
  description: "我想帮助 1666 个学习计算机的小伙伴变得更好!",
  head: [
    // 站点图标
    ["link", { rel: "icon", href: "/logo.jpg" }],
    // SEO
    [
      "meta",
      {
        name: "keywords",
        content:
          "酷酷的算法, 计算机, 操作系统, 计算机网络, 蓝莓随便扯, Pythoner, 力扣刷题",
      },
    ],
    // 百度统计
    [
      "script",
      {},
      `
        var _hmt = _hmt || [];
        (function() {
          var hm = document.createElement("script");
          hm.src = "https://hm.baidu.com/hm.js?2675818a983a3131404cee835018f016";
          var s = document.getElementsByTagName("script")[0]; 
          s.parentNode.insertBefore(hm, s);
        })();
      `,
    ],
  ],
  // permalink: "/:slug",

  // 监听文件变化，热更新
  extraWatchFiles: [".vuepress/*.ts", ".vuepress/sidebars/*.ts"],
  markdown: {
    // 开启代码块的行号
    lineNumbers: true,
    // 支持 4 级以上的标题渲染
    extractHeaders: ["h2", "h3", "h4", "h5", "h6"],
  },
  // @ts-ignore
  plugins: [
    ["@vuepress/back-to-top"],
    // Google 分析
    [
      "@vuepress/google-analytics",
      {
        ga: "GTM-WVS9HM6W", // 补充自己的谷歌分析 ID，比如 UA-00000000-0
      },
    ],
    ["@vuepress/medium-zoom"],
    // https://github.com/lorisleiva/vuepress-plugin-seo
    [
      "seo",
      {
        siteTitle: (_, $site) => $site.title,
        title: ($page) => $page.title,
        description: ($page) =>
          $page.frontmatter.description || $page.description,
        author: (_, $site) => $site.themeConfig.author || author,
        tags: ($page) => $page.frontmatter.tags || tags,
        type: ($page) => "article",
        url: (_, $site, path) =>
          ($site.themeConfig.domain || domain || "") + path,
        image: ($page, $site) =>
          $page.frontmatter.image &&
          (($site.themeConfig.domain &&
            !$page.frontmatter.image.startsWith("http")) ||
            "") + $page.frontmatter.image,
        publishedAt: ($page) =>
          $page.frontmatter.date && new Date($page.frontmatter.date),
        modifiedAt: ($page) => $page.lastUpdated && new Date($page.lastUpdated),
      },
    ],
    // https://github.com/ekoeryanto/vuepress-plugin-sitemap
    [
      "sitemap",
      {
        hostname: domain,
      },
    ],
    // https://github.com/IOriens/vuepress-plugin-baidu-autopush
    ["vuepress-plugin-baidu-autopush"],
    // https://github.com/zq99299/vuepress-plugin/tree/master/vuepress-plugin-tags
    ["vuepress-plugin-tags"],
    // https://github.com/znicholasbrown/vuepress-plugin-code-copy
    [
      "vuepress-plugin-code-copy",
      {
        successText: "代码已复制",
      },
    ],
    // https://github.com/webmasterish/vuepress-plugin-feed
    [
      "feed",
      {
        canonical_base: domain,
        count: 10000,
        // 需要自动推送的文档目录
        posts_directories: [],
      },
    ],
    // https://github.com/tolking/vuepress-plugin-img-lazy
    ["img-lazy"],
  ],
  // 主题配置
  themeConfig: {
    logo: "/logo.jpg",
    nav: navbar,
    sidebar,
    lastUpdated: "最近更新",

    // GitHub 仓库位置
    repo: "teenager-lijh/cocoalgo",
    docsBranch: "main",

    // 编辑链接
    editLinks: true,
    editLinkText: "完善页面",

    // @ts-ignore
    // 底部版权信息
    footer,
    // 额外右侧边栏
    extraSideBar,
  },
});
