import {SidebarConfig4Multiple} from "vuepress/config";

import ideaSideBar from "./sidebars/ideaSideBar";
import osSideBar from "./sidebars/osSideBar";
import cnSideBar from "./sidebars/cnSideBar";
import lcSideBar from "./sidebars/lcSideBar";
import dsSideBar from "./sidebars/dsSideBar";
import pythonerSideBar from "./sidebars/pythonerSideBar";

// @ts-ignore
export default {
    "/蓝莓随便扯/": ideaSideBar,
    "/操作系统/": osSideBar,
    "/计算机网络/": cnSideBar,
    "/力扣刷题/": lcSideBar,
    "/分布式系统/": dsSideBar,
    "/Pythoner/": pythonerSideBar,
    // 降级，默认根据文章标题渲染侧边栏
    "/": "auto",
} as SidebarConfig4Multiple;
