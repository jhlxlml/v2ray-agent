# 伪装站 ZIP 静态审计

安装与更换只部署脚本内的 Welcome 或 Field Notes 页面。这两页只有 HTML 和内联 CSS。历史 ZIP 无自动部署入口。

逐条读取 ZIP 中央目录并扫描 HTML、JS、CSS、JSON、XML、SVG、文本和映射。检查绝对路径、父目录、反斜杠、大小写碰撞、符号链接、嵌套压缩扩展与魔数，以及单文件 16 MiB、合计 64 MiB 的阈值。九个 ZIP 均通过结构检查。未运行归档内的任何代码。下面的域名清单包括注释、链接和可能的运行时请求。

## html1.zip

引导页和本地脚本。抽样定位的页面跳转指向站内 index.html，外部字体或图片引用按清单复核。旧打包 JS 留待专项审阅。

125 个条目，展开 3,551,453 字节，最大单条 418,163 字节。
SHA-256 `a226ca42b854e3cd3585d57bfb9f8c6f09d4d195dbe5fbf41c5358cd7540631b`。

外部域名候选

daneden.me, github.com, opensource.org, www.idangero.us

完整条目清单

```text
check
css/
__MACOSX/._css
css/animate.css
__MACOSX/css/._animate.css
css/common.css
__MACOSX/css/._common.css
css/swiper.min.css
__MACOSX/css/._swiper.min.css
css/iconfont_loading.css
__MACOSX/css/._iconfont_loading.css
css/iconfont.css
__MACOSX/css/._iconfont.css
guide1.html
__MACOSX/._guide1.html
guide2.html
__MACOSX/._guide2.html
guide3.html
__MACOSX/._guide3.html
img/
__MACOSX/._img
img/guide/
__MACOSX/img/._guide
img/link/
__MACOSX/img/._link
img/index/
__MACOSX/img/._index
img/guide/14_2.png
__MACOSX/img/guide/._14_2.png
img/guide/14_3.png
__MACOSX/img/guide/._14_3.png
img/guide/8_1.png
__MACOSX/img/guide/._8_1.png
img/guide/16_1.png
__MACOSX/img/guide/._16_1.png
img/guide/14_1.png
__MACOSX/img/guide/._14_1.png
img/guide/14_4.png
__MACOSX/img/guide/._14_4.png
img/guide/14_5.png
__MACOSX/img/guide/._14_5.png
img/guide/10_1.png
__MACOSX/img/guide/._10_1.png
img/guide/12_1.png
__MACOSX/img/guide/._12_1.png
img/guide/index_bg.jpg
__MACOSX/img/guide/._index_bg.jpg
img/guide/8.png
__MACOSX/img/guide/._8.png
img/guide/9.png
__MACOSX/img/guide/._9.png
img/guide/15_1.png
__MACOSX/img/guide/._15_1.png
img/guide/14.png
__MACOSX/img/guide/._14.png
img/guide/15.png
__MACOSX/img/guide/._15.png
img/guide/16.png
__MACOSX/img/guide/._16.png
img/guide/9_1.png
__MACOSX/img/guide/._9_1.png
img/guide/12.png
__MACOSX/img/guide/._12.png
img/guide/13.png
__MACOSX/img/guide/._13.png
img/guide/11.png
__MACOSX/img/guide/._11.png
img/guide/11_1.png
__MACOSX/img/guide/._11_1.png
img/guide/10.png
__MACOSX/img/guide/._10.png
img/guide/3_1.png
__MACOSX/img/guide/._3_1.png
img/guide/1_1.png
__MACOSX/img/guide/._1_1.png
img/guide/5_1.png
__MACOSX/img/guide/._5_1.png
img/guide/7_1.png
__MACOSX/img/guide/._7_1.png
img/guide/4.png
__MACOSX/img/guide/._4.png
img/guide/5.png
__MACOSX/img/guide/._5.png
img/guide/2_1.png
__MACOSX/img/guide/._2_1.png
img/guide/text4.png
__MACOSX/img/guide/._text4.png
img/guide/7.png
__MACOSX/img/guide/._7.png
img/guide/6.png
__MACOSX/img/guide/._6.png
img/guide/text5.png
__MACOSX/img/guide/._text5.png
img/guide/text1.png
__MACOSX/img/guide/._text1.png
img/guide/2.png
__MACOSX/img/guide/._2.png
img/guide/4_2.png
__MACOSX/img/guide/._4_2.png
img/guide/6_1.png
__MACOSX/img/guide/._6_1.png
img/guide/3.png
__MACOSX/img/guide/._3.png
img/guide/text2.png
__MACOSX/img/guide/._text2.png
img/guide/1.png
__MACOSX/img/guide/._1.png
img/guide/4_1.png
__MACOSX/img/guide/._4_1.png
img/guide/text3.png
__MACOSX/img/guide/._text3.png
img/link/bg1.jpg
__MACOSX/img/link/._bg1.jpg
img/link/bg2.jpg
__MACOSX/img/link/._bg2.jpg
img/index/loading.gif
__MACOSX/img/index/._loading.gif
index.html
__MACOSX/._index.html
js/
__MACOSX/._js
js/swiper.min.js
__MACOSX/js/._swiper.min.js
js/jquery.min.js
__MACOSX/js/._jquery.min.js
```

## html2.zip

多页面模板。HTML 有外部百度链接，含旧 jQuery、Bootstrap、Swiper 与 CSS sourcemap。旧 jQuery 包中出现 iframe 字符串，需结合行为审阅。

176 个条目，展开 4,216,828 字节，最大单条 906,068 字节。
SHA-256 `42e9f76fdf8df0af7a07dc1408a1e3caac7db6691f3ff49aabe38913eb0bbb75`。

外部域名候选

a11yproject.com, blog.alexmaccaw.com, bugs.webkit.org, daneden.me, developer.mozilla.org, getbootstrap.com, github.com, nicolasgallagher.com, opensource.org, timkadlec.com, www.baidu.com, www.idangero.us, www.modernizr.com, www.superslide2.com, www.w3.org, www.xrcgteam.com

完整条目清单

```text
about.html
check
contract.html
css/
__MACOSX/._css
css/bootstrap.min.css
__MACOSX/css/._bootstrap.min.css
css/animate.min.css
__MACOSX/css/._animate.min.css
css/bootstrap.css
__MACOSX/css/._bootstrap.css
css/bootstrap.css.map
__MACOSX/css/._bootstrap.css.map
css/bootstrap.min.css.map
__MACOSX/css/._bootstrap.min.css.map
css/bootstrap-theme.css.map
__MACOSX/css/._bootstrap-theme.css.map
css/bootstrap-theme.min.css.map
__MACOSX/css/._bootstrap-theme.min.css.map
css/swiper.min.css
__MACOSX/css/._swiper.min.css
css/style.css
__MACOSX/css/._style.css
css/bootstrap-theme.css
__MACOSX/css/._bootstrap-theme.css
css/bootstrap-theme.min.css
__MACOSX/css/._bootstrap-theme.min.css
en_about.html
en_contract.html
en_index.html
en_recruit.html
en_worksShow.html
fonts/
__MACOSX/._fonts
fonts/glyphicons-halflings-regular.woff
__MACOSX/fonts/._glyphicons-halflings-regular.woff
fonts/glyphicons-halflings-regular.eot
__MACOSX/fonts/._glyphicons-halflings-regular.eot
fonts/glyphicons-halflings-regular.woff2
__MACOSX/fonts/._glyphicons-halflings-regular.woff2
fonts/glyphicons-halflings-regular.ttf
__MACOSX/fonts/._glyphicons-halflings-regular.ttf
fonts/glyphicons-halflings-regular.svg
__MACOSX/fonts/._glyphicons-halflings-regular.svg
img/
__MACOSX/._img
img/email.png
__MACOSX/img/._email.png
img/yuan.png
__MACOSX/img/._yuan.png
img/about_03.jpg
__MACOSX/img/._about_03.jpg
img/about_02.jpg
__MACOSX/img/._about_02.jpg
img/tel.png
__MACOSX/img/._tel.png
img/right_arrow1.png
__MACOSX/img/._right_arrow1.png
img/about_01.jpg
__MACOSX/img/._about_01.jpg
img/hezuo.png
__MACOSX/img/._hezuo.png
img/about_05.jpg
__MACOSX/img/._about_05.jpg
img/about_10.jpg
__MACOSX/img/._about_10.jpg
img/about_04.jpg
__MACOSX/img/._about_04.jpg
img/slider-right-arrow.png
__MACOSX/img/._slider-right-arrow.png
img/slider-left-arrow1.png
__MACOSX/img/._slider-left-arrow1.png
img/about_06.jpg
__MACOSX/img/._about_06.jpg
img/left_arrow.png
__MACOSX/img/._left_arrow.png
img/about_07.jpg
__MACOSX/img/._about_07.jpg
img/addr-bg.png
__MACOSX/img/._addr-bg.png
img/banner.png
__MACOSX/img/._banner.png
img/cha.png
__MACOSX/img/._cha.png
img/lunbo6.png
__MACOSX/img/._lunbo6.png
img/blank.png
__MACOSX/img/._blank.png
img/right_arrow.png
__MACOSX/img/._right_arrow.png
img/work_img3.png
__MACOSX/img/._work_img3.png
img/doimg_2.png
__MACOSX/img/._doimg_2.png
img/doimg_3.png
__MACOSX/img/._doimg_3.png
img/work_img2.png
__MACOSX/img/._work_img2.png
img/map.png
__MACOSX/img/._map.png
img/lunbo5.png
__MACOSX/img/._lunbo5.png
img/banner1.png
__MACOSX/img/._banner1.png
img/foot_logo.png
__MACOSX/img/._foot_logo.png
img/doimg_1.png
__MACOSX/img/._doimg_1.png
img/work_img1.png
__MACOSX/img/._work_img1.png
img/lunbo4.png
__MACOSX/img/._lunbo4.png
img/work_img5.png
__MACOSX/img/._work_img5.png
img/doimg_4.png
__MACOSX/img/._doimg_4.png
img/doimg_5.png
__MACOSX/img/._doimg_5.png
img/work_img4.png
__MACOSX/img/._work_img4.png
img/loading.gif
__MACOSX/img/._loading.gif
img/lunbo1.png
__MACOSX/img/._lunbo1.png
img/lunbo3.png
__MACOSX/img/._lunbo3.png
img/left_arrow1.png
__MACOSX/img/._left_arrow1.png
img/work_img6.png
__MACOSX/img/._work_img6.png
img/doimg_6.png
__MACOSX/img/._doimg_6.png
img/gai.png
__MACOSX/img/._gai.png
img/slider-right-arrow1.png
__MACOSX/img/._slider-right-arrow1.png
img/lunbo2.png
__MACOSX/img/._lunbo2.png
img/dingwei.png
__MACOSX/img/._dingwei.png
img/logo.png
__MACOSX/img/._logo.png
img/addr.png
__MACOSX/img/._addr.png
img/btns.png
__MACOSX/img/._btns.png
img/about_09.jpg
__MACOSX/img/._about_09.jpg
img/about_08.jpg
__MACOSX/img/._about_08.jpg
img/map1.png
__MACOSX/img/._map1.png
img/slider-left-arrow.png
__MACOSX/img/._slider-left-arrow.png
index.html
__MACOSX/._index.html
js/
__MACOSX/._js
js/npm.js
__MACOSX/js/._npm.js
js/swiper.min.js
__MACOSX/js/._swiper.min.js
js/bootstrap.js
__MACOSX/js/._bootstrap.js
js/wow.min.js
__MACOSX/js/._wow.min.js
js/numberAdd.js
__MACOSX/js/._numberAdd.js
js/jquery.min.js
__MACOSX/js/._jquery.min.js
js/bootstrap.min.js
__MACOSX/js/._bootstrap.min.js
js/jquery.SuperSlide.2.1.js
__MACOSX/js/._jquery.SuperSlide.2.1.js
recruit.html
worksShow.html
```

## html3.zip

个人博客。contact.html 加载 Google Maps 并嵌入示例 API key，google_map.js 存在 HTTP 地理编码调用。含模板外链。

84 个条目，展开 2,247,753 字节，最大单条 566,607 字节。
SHA-256 `3e8e4835c54e9c3ca4d771db4c2256d5af9dde3d2d19bd2f41364afc9079d75e`。

外部域名候选

daneden.me, developers.google.com, getbootstrap.com, github.com, gsgd.co.uk, maps.googleapis.com, modernizr.com, opensource.org, www.baidu.com, www.gnu.org, www.w3.org, www.woothemes.com

完整条目清单

```text
about.html
blog.html
check
contact.html
css/
__MACOSX/._css
css/flexslider.css
__MACOSX/css/._flexslider.css
css/bootstrap.css
__MACOSX/css/._bootstrap.css
css/animate.css
__MACOSX/css/._animate.css
css/icomoon.css
__MACOSX/css/._icomoon.css
css/style.css
__MACOSX/css/._style.css
fonts/
__MACOSX/._fonts
fonts/bootstrap/
__MACOSX/fonts/._bootstrap
fonts/icomoon/
__MACOSX/fonts/._icomoon
fonts/bootstrap/glyphicons-halflings-regular.woff
__MACOSX/fonts/bootstrap/._glyphicons-halflings-regular.woff
fonts/bootstrap/glyphicons-halflings-regular.eot
__MACOSX/fonts/bootstrap/._glyphicons-halflings-regular.eot
fonts/bootstrap/glyphicons-halflings-regular.woff2
__MACOSX/fonts/bootstrap/._glyphicons-halflings-regular.woff2
fonts/bootstrap/glyphicons-halflings-regular.ttf
__MACOSX/fonts/bootstrap/._glyphicons-halflings-regular.ttf
fonts/bootstrap/glyphicons-halflings-regular.svg
__MACOSX/fonts/bootstrap/._glyphicons-halflings-regular.svg
fonts/icomoon/icomoon.ttf
__MACOSX/fonts/icomoon/._icomoon.ttf
fonts/icomoon/icomoon.woff
__MACOSX/fonts/icomoon/._icomoon.woff
fonts/icomoon/icomoon.eot
__MACOSX/fonts/icomoon/._icomoon.eot
fonts/icomoon/icomoon.svg
__MACOSX/fonts/icomoon/._icomoon.svg
images/
__MACOSX/._images
images/img_bg_1.jpg
__MACOSX/images/._img_bg_1.jpg
images/img_bg_3.jpg
__MACOSX/images/._img_bg_3.jpg
images/img_bg_2.jpg
__MACOSX/images/._img_bg_2.jpg
images/img-3.jpg
__MACOSX/images/._img-3.jpg
images/img-2.jpg
__MACOSX/images/._img-2.jpg
images/img-1.jpg
__MACOSX/images/._img-1.jpg
images/img-5.jpg
__MACOSX/images/._img-5.jpg
images/img-4.jpg
__MACOSX/images/._img-4.jpg
images/img-6.jpg
__MACOSX/images/._img-6.jpg
images/loc.png
__MACOSX/images/._loc.png
index.html
js/
__MACOSX/._js
js/respond.min.js
__MACOSX/js/._respond.min.js
js/modernizr-2.6.2.min.js
__MACOSX/js/._modernizr-2.6.2.min.js
js/jquery.easing.1.3.js
__MACOSX/js/._jquery.easing.1.3.js
js/jquery.min.js
__MACOSX/js/._jquery.min.js
js/main.js
__MACOSX/js/._main.js
js/bootstrap.min.js
__MACOSX/js/._bootstrap.min.js
js/jquery.flexslider-min.js
__MACOSX/js/._jquery.flexslider-min.js
js/google_map.js
__MACOSX/js/._google_map.js
js/jquery.waypoints.min.js
__MACOSX/js/._jquery.waypoints.min.js
portfolio.html
```

## html4.zip

企业站。含 SWF、FLA、PSD、Thumbs.db 和 macOS 元数据；Flash 页面引用 Macromedia，contact 页有第三方站点引用。Flash 与打包脚本未执行或动态验证。

287 个条目，展开 47,231,290 字节，最大单条 10,189,040 字节。
SHA-256 `6e17ee5a6d8db1e266139694dfacb11ea379dbbfbf2342f3024fd8cd709f0156`。

外部域名候选

blog.deconcept.com, download.macromedia.com, www.baidu.com, www.macromedia.com, www.opensource.org, www.w3.org, www.wzgeili.com, x1989.com

完整条目清单

```text
about.html
check
contact.html
css/
__MACOSX/._css
css/style.css
__MACOSX/css/._style.css
en/
__MACOSX/._en
en/sc.html
__MACOSX/en/._sc.html
en/kh.html
__MACOSX/en/._kh.html
en/index.html
__MACOSX/en/._index.html
en/product.html
__MACOSX/en/._product.html
en/about.html
__MACOSX/en/._about.html
en/css/
__MACOSX/en/._css
en/contact.html
__MACOSX/en/._contact.html
en/images/
__MACOSX/en/._images
en/js/
__MACOSX/en/._js
en/sitemap.html
__MACOSX/en/._sitemap.html
en/kshop16.xml
__MACOSX/en/._kshop16.xml
en/news.html
__MACOSX/en/._news.html
en/img/
__MACOSX/en/._img
en/news-detail.html
__MACOSX/en/._news-detail.html
en/search.html
__MACOSX/en/._search.html
en/product-detail.html
__MACOSX/en/._product-detail.html
en/swf/
__MACOSX/en/._swf
en/css/style.css
__MACOSX/en/css/._style.css
en/images/gobtn.gif
__MACOSX/en/images/._gobtn.gif
en/images/Thumbs.db
__MACOSX/en/images/._Thumbs.db
en/images/logo.gif
__MACOSX/en/images/._logo.gif
en/images/asda1.gif
__MACOSX/en/images/._asda1.gif
en/images/gybtn.gif
__MACOSX/en/images/._gybtn.gif
en/images/1251.jpg
__MACOSX/en/images/._1251.jpg
en/images/map.jpg
__MACOSX/en/images/._map.jpg
en/images/gypic.jpg
__MACOSX/en/images/._gypic.jpg
en/images/line-x.gif
__MACOSX/en/images/._line-x.gif
en/images/pic-repeat-x.png
__MACOSX/en/images/._pic-repeat-x.png
en/images/cert-icon.gif
__MACOSX/en/images/._cert-icon.gif
en/images/topbg.png
__MACOSX/en/images/._topbg.png
en/images/1236a.jpg
__MACOSX/en/images/._1236a.jpg
en/images/12367.jpg
__MACOSX/en/images/._12367.jpg
en/images/search-repeat-x.png
__MACOSX/en/images/._search-repeat-x.png
en/images/132167.jpg
__MACOSX/en/images/._132167.jpg
en/images/titicon.gif
__MACOSX/en/images/._titicon.gif
en/images/navbg.gif
__MACOSX/en/images/._navbg.gif
en/images/repeat-x-bottom.gif
__MACOSX/en/images/._repeat-x-bottom.gif
en/images/aboutbtn.jpg
__MACOSX/en/images/._aboutbtn.jpg
en/images/verline.jpg
__MACOSX/en/images/._verline.jpg
en/images/nav.swf
__MACOSX/en/images/._nav.swf
en/images/video-icon.gif
__MACOSX/en/images/._video-icon.gif
en/images/culture-icon.gif
__MACOSX/en/images/._culture-icon.gif
en/images/technology-icon.gif
__MACOSX/en/images/._technology-icon.gif
en/images/onlinebg.png
__MACOSX/en/images/._onlinebg.png
en/images/repeat-x.png
__MACOSX/en/images/._repeat-x.png
en/images/12316.jpg
__MACOSX/en/images/._12316.jpg
en/images/25pic.jpg
__MACOSX/en/images/._25pic.jpg
en/images/1216.jpg
__MACOSX/en/images/._1216.jpg
en/images/geili-icon.gif
__MACOSX/en/images/._geili-icon.gif
en/js/swfobject.js
__MACOSX/en/js/._swfobject.js
en/js/jquery.plugins.js
__MACOSX/en/js/._jquery.plugins.js
en/js/jquery.Xslider.js
__MACOSX/en/js/._jquery.Xslider.js
en/js/jquery.js
__MACOSX/en/js/._jquery.js
en/img/Thumbs.db
__MACOSX/en/img/._Thumbs.db
en/img/img8.jpg
__MACOSX/en/img/._img8.jpg
en/img/img5.jpg
__MACOSX/en/img/._img5.jpg
en/img/img4.jpg
__MACOSX/en/img/._img4.jpg
en/img/img6.jpg
__MACOSX/en/img/._img6.jpg
en/img/img7.jpg
__MACOSX/en/img/._img7.jpg
en/img/img3.jpg
__MACOSX/en/img/._img3.jpg
en/img/img2.jpg
__MACOSX/en/img/._img2.jpg
en/img/img1.jpg
__MACOSX/en/img/._img1.jpg
en/swf/nav.swf
__MACOSX/en/swf/._nav.swf
en/swf/nav.fla
__MACOSX/en/swf/._nav.fla
images/
__MACOSX/._images
images/gobtn.gif
__MACOSX/images/._gobtn.gif
images/Thumbs.db
__MACOSX/images/._Thumbs.db
images/logo.gif
__MACOSX/images/._logo.gif
images/asda1.gif
__MACOSX/images/._asda1.gif
images/gybtn.gif
__MACOSX/images/._gybtn.gif
images/1251.jpg
__MACOSX/images/._1251.jpg
images/map.jpg
__MACOSX/images/._map.jpg
images/gypic.jpg
__MACOSX/images/._gypic.jpg
images/line-x.gif
__MACOSX/images/._line-x.gif
images/pic-repeat-x.png
__MACOSX/images/._pic-repeat-x.png
images/cert-icon.gif
__MACOSX/images/._cert-icon.gif
images/topbg.png
__MACOSX/images/._topbg.png
images/1236a.jpg
__MACOSX/images/._1236a.jpg
images/12367.jpg
__MACOSX/images/._12367.jpg
images/search-repeat-x.png
__MACOSX/images/._search-repeat-x.png
images/132167.jpg
__MACOSX/images/._132167.jpg
images/titicon.gif
__MACOSX/images/._titicon.gif
images/navbg.gif
__MACOSX/images/._navbg.gif
images/repeat-x-bottom.gif
__MACOSX/images/._repeat-x-bottom.gif
images/aboutbtn.jpg
__MACOSX/images/._aboutbtn.jpg
images/verline.jpg
__MACOSX/images/._verline.jpg
images/nav.swf
__MACOSX/images/._nav.swf
images/video-icon.gif
__MACOSX/images/._video-icon.gif
images/culture-icon.gif
__MACOSX/images/._culture-icon.gif
images/technology-icon.gif
__MACOSX/images/._technology-icon.gif
images/onlinebg.png
__MACOSX/images/._onlinebg.png
images/repeat-x.png
__MACOSX/images/._repeat-x.png
images/12316.jpg
__MACOSX/images/._12316.jpg
images/25pic.jpg
__MACOSX/images/._25pic.jpg
images/1216.jpg
__MACOSX/images/._1216.jpg
images/geili-icon.gif
__MACOSX/images/._geili-icon.gif
img/
__MACOSX/._img
img/Thumbs.db
__MACOSX/img/._Thumbs.db
img/kshop16.xml
__MACOSX/img/._kshop16.xml
img/img8.jpg
__MACOSX/img/._img8.jpg
img/img5.jpg
__MACOSX/img/._img5.jpg
img/img4.jpg
__MACOSX/img/._img4.jpg
img/img6.jpg
__MACOSX/img/._img6.jpg
img/img7.jpg
__MACOSX/img/._img7.jpg
img/img3.jpg
__MACOSX/img/._img3.jpg
img/img2.jpg
__MACOSX/img/._img2.jpg
img/img1.jpg
__MACOSX/img/._img1.jpg
img/pro.psd
__MACOSX/img/._pro.psd
img/nav/
__MACOSX/img/._nav
img/nav/pro05.jpg
__MACOSX/img/nav/._pro05.jpg
img/nav/Thumbs.db
__MACOSX/img/nav/._Thumbs.db
img/nav/pro04.jpg
__MACOSX/img/nav/._pro04.jpg
img/nav/pro06.jpg
__MACOSX/img/nav/._pro06.jpg
img/nav/pro07.jpg
__MACOSX/img/nav/._pro07.jpg
img/nav/pro03.jpg
__MACOSX/img/nav/._pro03.jpg
img/nav/pro02.jpg
__MACOSX/img/nav/._pro02.jpg
img/nav/pro01.jpg
__MACOSX/img/nav/._pro01.jpg
img/nav/nav.fla
__MACOSX/img/nav/._nav.fla
img/nav/pro08.jpg
__MACOSX/img/nav/._pro08.jpg
index.html
__MACOSX/._index.html
js/
__MACOSX/._js
js/swfobject.js
__MACOSX/js/._swfobject.js
js/jquery.plugins.js
__MACOSX/js/._jquery.plugins.js
js/jquery.Xslider.js
__MACOSX/js/._jquery.Xslider.js
js/jquery.js
__MACOSX/js/._jquery.js
kh.html
kshop16.xml
__MACOSX/._kshop16.xml
news-detail.html
news.html
product-detail.html
product.html
psd/
__MACOSX/._psd
psd/Product.psd
__MACOSX/psd/._Product.psd
psd/index.psd
__MACOSX/psd/._index.psd
psd/news.psd
__MACOSX/psd/._news.psd
psd/about us.psd
__MACOSX/psd/._about us.psd
psd/gy.psd
__MACOSX/psd/._gy.psd
sc.html
search.html
sitemap.html
swf/
__MACOSX/._swf
swf/nav.swf
__MACOSX/swf/._nav.swf
swf/nav.fla
__MACOSX/swf/._nav.fla
```

## html5.zip

音乐解锁。已移除 index.html 的 _paq 跟踪初始化、远程统计 JS 与无脚本像素。主包和 Web Worker 内仍存在 stats.ixarea.com 的 /apis 常量，service worker 有外部引用。保留隔离，不推断这些功能端点的实际传输内容。

31 个条目，展开 12,631,600 字节，最大单条 4,194,304 字节。
SHA-256 `bdf764f4ef8de2670bab8027ea32c79b7da2a29241a6f605248b4712dfe9ba27`。

外部域名候选

element.eleme.io, example.com, feross.org, github.com, goo.gl, musicbrainz.org, registry.npmjs.org, stats.ixarea.com, storage.googleapis.com, www.firefox.com.cn, www.google.cn, www.microsoft.com, www.w3.org

完整条目清单

```text
03ab1ccebc1df96da5ee.worker.js
bf3c651698974db01293.worker.js
check
css/
css/chunk-vendors.8cf7dd44.css
css/app.893c7cfa.css
favicon.ico
fonts/
fonts/element-icons.535877f5.woff
fonts/element-icons.732389de.ttf
img/
img/icons/
img/icons/favicon-16x16.png
img/icons/safari-pinned-tab.svg
img/icons/android-chrome-192x192.png
img/icons/apple-touch-icon-152x152.png
img/icons/android-chrome-512x512.png
img/icons/msapplication-icon-144x144.png
img/icons/favicon-32x32.png
index.html
js/
js/app.319aaba4.js
js/app-legacy.0329a78a.js
js/chunk-vendors.56f18896.js
js/chunk-vendors-legacy.e0e5c135.js
manifest.json
precache-manifest.6854feef646b0f61d7911d9c92d80120.js
precache-manifest.e6b4c091ed2e059e54023b499b398e01.js
service-worker.js
static/
static/kgm.mask
```

## html6.zip

Mikutap。依赖 fonts.loli.net、cdnjs.loli.net，含外部站点链接、Dockerfile、打包脚本和 JSON 数据。未运行 Dockerfile 或 Web 脚本。

45 个条目，展开 369,539 字节，最大单条 203,378 字节。
SHA-256 `d06c145330f46587a6f8c91c0ba7acdf3a3224bf028d87726f31e88162ee725a`。

外部域名候选

aidn.jp, apis.google.com, cdnjs.loli.net, connect.facebook.net, ec.crypton.co.jp, exittunes.com, fonts.loli.net, github.com, hfiprogramming.github.io, i.loli.net, line.me, patatap.com, platform.twitter.com, plus.google.com, translate.google.com, twitter.com, www.facebook.com, www.v2ex.com, yuilibrary.com

完整条目清单

```text
check
css/
__MACOSX/._css
css/mikutap.css
__MACOSX/css/._mikutap.css
data/
__MACOSX/._data
data/track/
__MACOSX/data/._track
data/main/
__MACOSX/data/._main
data/track/track.json
__MACOSX/data/track/._track.json
data/main/main.json
__MACOSX/data/main/._main.json
Dockerfile
__MACOSX/._Dockerfile
icon.png
__MACOSX/._icon.png
index.html
__MACOSX/._index.html
js/
__MACOSX/._js
js/mikutap.min.js
__MACOSX/js/._mikutap.min.js
README.md
__MACOSX/._README.md
shared/
__MACOSX/._shared
shared/sp/
__MACOSX/shared/._sp
shared/css/
__MACOSX/shared/._css
shared/js/
__MACOSX/shared/._js
shared/sp/css/
__MACOSX/shared/sp/._css
shared/css/common-1.css
__MACOSX/shared/css/._common-1.css
shared/css/index-1.css
__MACOSX/shared/css/._index-1.css
shared/js/common-2.min.js
__MACOSX/shared/js/._common-2.min.js
shared/sp/css/common.css
__MACOSX/shared/sp/css/._common.css
```

## html7.zip

企业站。HTML 含百度模板外链，包含旧 jQuery、PNG 兼容脚本和 Thumbs.db。

123 个条目，展开 1,196,336 字节，最大单条 174,717 字节。
SHA-256 `bf0d0e7cc1ecbf9663d326603e9262c7f30c9fcc939c1ace8522b05c92cb376a`。

外部域名候选

dillerdesign.com, gsgd.co.uk, jquery.com, jquery.org, msdn.microsoft.com, sizzlejs.com, thiagosf.net, www.baidu.com, www.dillerdesign.com, www.thanatopsic.org, www.w3.org

完整条目清单

```text
check
cp_cp.html
cp.html
gs.html
images/
__MACOSX/._images
images/lianx.png
__MACOSX/images/._lianx.png
images/left_lx_bg.jpg
__MACOSX/images/._left_lx_bg.jpg
images/rexian.png
__MACOSX/images/._rexian.png
images/Thumbs.db
__MACOSX/images/._Thumbs.db
images/new_title.jpg
__MACOSX/images/._new_title.jpg
images/cp_1.jpg
__MACOSX/images/._cp_1.jpg
images/nav_bj.jpg
__MACOSX/images/._nav_bj.jpg
images/on.png
__MACOSX/images/._on.png
images/gs_t.jpg
__MACOSX/images/._gs_t.jpg
images/cp_3.jpg
__MACOSX/images/._cp_3.jpg
images/cp_2.jpg
__MACOSX/images/._cp_2.jpg
images/cp_title_bg.jpg
__MACOSX/images/._cp_title_bg.jpg
images/nav_n_bj.jpg
__MACOSX/images/._nav_n_bj.jpg
images/QQµê¬σ¢╛20070101064743.png
__MACOSX/images/._QQµê¬σ¢╛20070101064743.png
images/off.png
__MACOSX/images/._off.png
images/cp_5.jpg
__MACOSX/images/._cp_5.jpg
images/cp_4.jpg
__MACOSX/images/._cp_4.jpg
images/banner.jpg
__MACOSX/images/._banner.jpg
images/banner2.jpg
__MACOSX/images/._banner2.jpg
images/wl_13.jpg
__MACOSX/images/._wl_13.jpg
images/banner3.jpg
__MACOSX/images/._banner3.jpg
images/QQµê¬σ¢╛20070101064321.png
__MACOSX/images/._QQµê¬σ¢╛20070101064321.png
images/xw_13.jpg
__MACOSX/images/._xw_13.jpg
images/zakladka.png
__MACOSX/images/._zakladka.png
images/QQµê¬σ¢╛20070101065021.png
__MACOSX/images/._QQµê¬σ¢╛20070101065021.png
images/zx_13.jpg
__MACOSX/images/._zx_13.jpg
images/jishu.png
__MACOSX/images/._jishu.png
images/new_li.jpg
__MACOSX/images/._new_li.jpg
images/zaix.png
__MACOSX/images/._zaix.png
images/logo.png
__MACOSX/images/._logo.png
images/cp_title.jpg
__MACOSX/images/._cp_title.jpg
images/cp_cp.png
__MACOSX/images/._cp_cp.png
images/footer_bg.jpg
__MACOSX/images/._footer_bg.jpg
images/nav_li.jpg
__MACOSX/images/._nav_li.jpg
images/more.jpg
__MACOSX/images/._more.jpg
images/left_title_2.jpg
__MACOSX/images/._left_title_2.jpg
images/wangl.png
__MACOSX/images/._wangl.png
images/gs_title.jpg
__MACOSX/images/._gs_title.jpg
images/QQµê¬σ¢╛20070101064833.png
__MACOSX/images/._QQµê¬σ¢╛20070101064833.png
images/left_title_1.jpg
__MACOSX/images/._left_title_1.jpg
index.html
__MACOSX/._index.html
jishu.html
js/
__MACOSX/._js
js/index.js
__MACOSX/js/._index.js
js/jquery.easing.1.3.js
__MACOSX/js/._jquery.easing.1.3.js
js/menu_min.js
__MACOSX/js/._menu_min.js
js/jquery.min.js
__MACOSX/js/._jquery.min.js
js/jquery-1.4.2.min.js
__MACOSX/js/._jquery-1.4.2.min.js
js/jquery-1.6.3.min.js
__MACOSX/js/._jquery-1.6.3.min.js
js/PNG.js
__MACOSX/js/._PNG.js
js/jquery.skitter.min.js
__MACOSX/js/._jquery.skitter.min.js
js/1.js
__MACOSX/js/._1.js
js/jquery-1.8.2.min.js
__MACOSX/js/._jquery-1.8.2.min.js
lianx.html
new.html
style/
__MACOSX/._style
style/menu-css.css
__MACOSX/style/._menu-css.css
style/css.css
__MACOSX/style/._css.css
style/style.css
__MACOSX/style/._style.css
wangluo.html
zaixian.html
```

## html8.zip

个人博客。页面请求 Google Fonts，有旧 jQuery 与弹窗插件。iframe 字符串出现在插件代码中，需结合行为审阅。

99 个条目，展开 3,223,437 字节，最大单条 516,367 字节。
SHA-256 `01b510bd8efe94ecc9b6c585c87261f849a8ed91f1323e8e1764b6c596de8e68`。

外部域名候选

bas2k.ru, bit.ly, code.google.com, dimsemenov.com, fonts.googleapis.com, getbootstrap.com, github.com, maps.google, masonry.desandro.com, player.vimeo.com, www.baidu.com, www.opensource.org, www.w3.org, www.youtube.com

完整条目清单

```text
check
css/
__MACOSX/._css
css/bootstrap.min.css
__MACOSX/css/._bootstrap.min.css
css/magnific-popup.css
__MACOSX/css/._magnific-popup.css
css/owl.theme.css
__MACOSX/css/._owl.theme.css
css/responsive.css
__MACOSX/css/._responsive.css
css/style.css
__MACOSX/css/._style.css
css/normalize.css
__MACOSX/css/._normalize.css
css/owl.carousel.css
__MACOSX/css/._owl.carousel.css
fonts/
__MACOSX/._fonts
fonts/Glyphter.svg
__MACOSX/fonts/._Glyphter.svg
fonts/Glyphter.woff
__MACOSX/fonts/._Glyphter.woff
fonts/Glyphter.ttf
__MACOSX/fonts/._Glyphter.ttf
fonts/Glyphter.eot
__MACOSX/fonts/._Glyphter.eot
images/
__MACOSX/._images
images/favicon.ico
__MACOSX/images/._favicon.ico
images/logo-big.png
__MACOSX/images/._logo-big.png
images/testimonial-bg.jpg
__MACOSX/images/._testimonial-bg.jpg
images/hero1.jpeg
__MACOSX/images/._hero1.jpeg
images/reza.jpg
__MACOSX/images/._reza.jpg
images/loader.gif
__MACOSX/images/._loader.gif
images/bw-5.png
__MACOSX/images/._bw-5.png
images/blog-6.jpg
__MACOSX/images/._blog-6.jpg
images/bw-4.png
__MACOSX/images/._bw-4.png
images/bw-6.png
__MACOSX/images/._bw-6.png
images/blog-5.jpg
__MACOSX/images/._blog-5.jpg
images/blog-4.jpg
__MACOSX/images/._blog-4.jpg
images/logo.png
__MACOSX/images/._logo.png
images/bw-3.png
__MACOSX/images/._bw-3.png
images/blog-1.png
__MACOSX/images/._blog-1.png
images/bw-2.png
__MACOSX/images/._bw-2.png
images/blog-3.jpg
__MACOSX/images/._blog-3.jpg
images/blog-2.jpg
__MACOSX/images/._blog-2.jpg
images/bw-1.png
__MACOSX/images/._bw-1.png
images/logo-bottom.png
__MACOSX/images/._logo-bottom.png
images/signature.png
__MACOSX/images/._signature.png
index.html
__MACOSX/._index.html
js/
__MACOSX/._js
js/jquery.appear.js
__MACOSX/js/._jquery.appear.js
js/jquery.magnific-popup.min.js
__MACOSX/js/._jquery.magnific-popup.min.js
js/classie.js
__MACOSX/js/._classie.js
js/typed.js
__MACOSX/js/._typed.js
js/masonry.pkgd.min.js
__MACOSX/js/._masonry.pkgd.min.js
js/jquery-1.9.1.min.js
__MACOSX/js/._jquery-1.9.1.min.js
js/masonry.js
__MACOSX/js/._masonry.js
js/main.js
__MACOSX/js/._main.js
js/owl.carousel.min.js
__MACOSX/js/._owl.carousel.min.js
js/bootstrap.min.js
__MACOSX/js/._bootstrap.min.js
js/html5shiv.min.js
__MACOSX/js/._html5shiv.min.js
js/smooth-scroll.min.js
__MACOSX/js/._smooth-scroll.min.js
```

## html9.zip

404 页面。index.html 含三秒倒计时及自动跳转百度，旧 CSS 存在 IE expression/eval。旧资源保持隔离。

29 个条目，展开 186,535 字节，最大单条 94,846 字节。
SHA-256 `eb7eb42a7c07c3bfd71c97d6b309fadf22924195e2b84b2ce420766a5c7162ff`。

外部域名候选

meyerweb.com, www.baidu.com, www.w3.org

完整条目清单

```text
404/
__MACOSX/._404
404/css/
__MACOSX/404/._css
404/images/
__MACOSX/404/._images
404/css/public.css
__MACOSX/404/css/._public.css
404/css/404.css
__MACOSX/404/css/._404.css
404/css/index.css
__MACOSX/404/css/._index.css
404/images/yun1.png
__MACOSX/404/images/._yun1.png
404/images/yun0.png
__MACOSX/404/images/._yun0.png
404/images/yun2.png
__MACOSX/404/images/._yun2.png
404/images/bird.png
__MACOSX/404/images/._bird.png
404/images/san.png
__MACOSX/404/images/._san.png
check
index.html
__MACOSX/._index.html
js/
__MACOSX/._js
js/jquery-1.7.2.min.js
__MACOSX/js/._jquery-1.7.2.min.js
```
