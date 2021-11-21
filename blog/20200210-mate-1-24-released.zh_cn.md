<!--
.. link:
.. description:
.. tags: Releases,发布
.. date: 2020-02-10 09:00:00
.. title: MATE 1.24 发布
.. slug: 2020-02-10-mate-1-24-released
.. author: Wolfgang Ulbrich
-->

经过大约一年的开发，MATE Desktop 团队终于发布了 MATE 1.24。非常感谢帮助实现这一目标的所有贡献者。

![MATE 关于对话框](/assets/img/blog/about-mate-1.24.zh_cn.png){ width=50% }

## MATE 1.24 的新特性

此版本包含许多新功能，Bug 修复和常规改进。 一些最重要的亮点包括：

* 我们再次这样做，一旦用户启动会话，MATE桌面环境将比以前更易于使用。 您要隐藏应用程序吗？ 现在，您可以设置要在启动时显示的应用程序。
* **Engrampa** 现在支持一些其它格式，并且其中一些密码和Unicode字符支持得到了修复。
* **MATE之眼** 现在支持[Wayland](https://wayland.freedesktop.org/)，并且增加了对嵌入式颜色配置文件的支持。
    *     * 缩略图生成器已在多处进行了修复。
    *     * 添加了对 webp 文件的支持。
* 窗口管理器 **marco** 进行了很多更改：
    * 我们带来了一堆过去的窗口装饰，以满足您的怀旧情怀。
    * 最后添加了不可见的调整大小边框。无需再为寻找不到边框而费劲了！
    * 所有窗口控件（最小、最大、关闭按钮）现在都以 HiDPI 呈现。
    * Alt+Tab 和工作区切换弹出窗口已_完全_重新设计。现在，它们以漂亮的OSD样式呈现，更具可配置性，并且可以响应键盘箭头。
    * 现在，使用键盘平铺窗口允许您循环浏览不同的窗口大小。您不再只受限于一半的屏幕。
* **系统监视器** 面板小程序现在支持 NVMe 驱动器。
* **计算器**现在支持使用“pi”或“π”。
    * **计算器** 现在支持使用“ pi”或“π”。
    * 一些支持预定义物理常数的修复程序。
* **控制中心**现在在HiDPI显示器上正确显示其图标。
* **控制中心** 现在可以在HiDPI显示屏上正确显示其图标。
* 添加了一个全新的 **时间和日期管理器** 应用程序。
* **首选应用程序**应用程序在可访问性方面得到了改进，并更好地支持与IM客户端的集成。
* 改进了 **首选应用程序** 应用程序，以提高可访问性，并更好地支持与IM客户端的集成。
* 说到图标，我们自己的主题中的network manager小程序图标已经完全重新设计，现在可以在HiDPI显示器上使用。
* 如果您是那种不喜欢在忙碌、演讲或观看电影时被打扰的人，您会很高兴知道**通知守护程序**现在支持请勿打扰模式。
* 如果您是那种在忙碌、演讲或看电影时不喜欢被打扰的人，您会很高兴知道 **通知守护程序** 现在支持了“请勿打扰” 模式。
    * 对 [Wayland](https//wayland.freedesktop.org/) 兼容性的支持已大为改善。
    * 状态图标（又称**通知区**，或**系统托盘**）支持HiDPI显示。
    * **万达鱼**改头换面，现在你可以尽情享受她的荣耀了。
    * **万达鱼** 得到了一个改造，现在你可以享受她完全的 HiDPI 支持。
    * 整个面板及其核心小程序的各种可访问性改进。
* 如果你的系统不支持[systemd](https://freedesktop.org/wiki/Software/systemd/)您可能有兴趣知道我们已经添加了对[elogind]的支持(https://github.com/elogind/elogind)到**伴侣屏幕保护程序**和**伴侣会话**。
* 我们还添加了一个全新的**MATE磁盘映像装入器**实用程序。
* **菜单编辑器Mozo**现在支持撤消和重做操作。
* **Pluma** 插件现已完全切换到 Python 3。
* **Pluma** 不再需要羡慕其他复杂编辑器的任何内容，因为它现在可以显示格式标记。
* i18n：所有应用已从 intltools 迁移到 gettext。



MATE Desktop 1.24 的组件可通过以下链接下载：

  * <https://pub.mate-desktop.org/releases/1.24/>

## 更多细节

这里有更多的细节

### atril
* 修复缩放时的高内存消耗
* 修复制作缩略图和注释文本时的内存泄漏
* Drag and Drop：在 drag-and-drop操作开始时重置 `pressed_button`动作
* 在菜单项上添加更多加速器
* 删除“synctex”库的内部版本，仅使用软件供应商提供的外部版本
* 修复希腊用户指南中阻止完成构建目标的错误
* Tiff后端：从TIFFREADRGBAIMAGEORIED解决故障
* Tiff后端：修复Tiff document.c中的缓冲区溢出
* Tiff backend: Fix a buffer overflow in tiff-document.c
* 迁移到Python3进行测试
* 需要GLib 2.54.0或更新版本
* 需要WebKitGTK-4.0 2.6.0或更新版本
* 需要Cairo 1.14.0或更新版本
* 放弃WebKitGTK-3.0支持
* i18n:从intltools迁移到gettext
* g10n：更新翻译

在完成更改日志<https://github.com/mate-desktop/atril/commits/master/>

### caja
* 准备好使用GCC10
* fm-properties: 删除mate桌面缩略图帮助器的使用
* 不要将文件名连字符
* 添加一个新的扩展接口：CajaWidgetViewProviderAPI
* 添加新对象：FmWidgetView
* 修复翻译人员报告的语法错误
* 修复了几个代码解析、Clang Static Analyzer、Cppcheck和GCC报告的弃用警告
* 修复在韩国地区移动文件时Caja崩溃的问题
* 使用“视图”选项卡中的“显示图标”选项
* 添加用于在列表视图中隐藏图标的配置选项
* 在几个菜单项上添加缺少的图标
* 在列表视图中显示缩略图
* 将更多图标渲染为cairo_曲面，以获得更好的HIDPI支持
* 重构自定义CSS加载到单独的函数中
* 添加对使用gla11y检查UI文件可访问性的支持
* 在图标视图标签上恢复透明背景
* 为文件的属性和 caja 的首选项窗口添加带有鼠标滚轮的滚动选项卡
* 桌面：默认情况下在桌面项目上强制没有边框
* 将 URL 前缀从 http 更改为 https
* caja-progress-info：向文件传输对话框添加工具提示
* 在文件传输操作对话框中为按钮添加可访问的名称
* eel：删除日期和时间功能
* caja-file：修复不完整的文件替换对话框
* caja-file-operations：添加带有误报警告的评论
* 修复多处内存泄漏
* i18n：允许翻译图形界面的更多元素
* i18n：从 intltools 迁移到 gettext
* g10n：更新翻译

在 <https://github.com/mate-desktop/caja/commits/master/> 完成更新日志

### caja-dropbox
* 使用 CAJA_EXTENSION_DIR_SYS 保存并显示系统 caja 扩展目录
* 显示 caja-extension-dir 的完整路径

在 <https://github.com/mate-desktop/caja-dropbox/commits/master/> 完成更新日志

### caja-extensions
* caja-wallpaper-extension：修复内存泄漏
* image-converter: 从头开始重写 caja-image-resize.ui 修复弃用
* 修复了 Clang Static Analyzer、Cppcheck 和 GCC 报告的几个代码分析、弃用警告
* 使用 gupnp 1.0 或 1.2 版构建。
* image-converter：不要在上下文菜单中使用不存在的图标
* ii18n 图像转换器：允许选择角度下拉列表的翻译
* i18n：从 intltools 迁移到 gettext
* g10n：更新翻译

在 <https://github.com/mate-desktop/caja-extensions/commits/master/> 完成更新日志

### engrampa
* 准备使用 gcc 10
* fr-command-rpm：使用 rpm 软件包附带的 rpm2cpio 二进制文件
* 将源 rpm 添加到支持的 MIME 类型
* 7z：不要设置工作目录，即使用临时目录
* 修复本地化的暂停 UI 逻辑
* Zstandard：更新 MIME 类型
* Ar：更新 MIME 类型并添加幻数
* LHA：修复互联网媒体类型
* dlg-package-installer：在错误对话框按钮中显示图标
* unace 2.5：不在文件列表中显示存档摘要
* java-utils：在读取包名之前删除空格
* 添加 zcompress 支持
* fr-command-unarchiver：必要时询问密码
* 修复了 Clang Static Analyzer、Cppcheck 和 GCC 报告的几个代码分析、弃用警告
* 修复多个内存泄漏
* 将手册升级到 docbook 5.0
* 支持 .udeb 包格式
* 在命令行上显示应用程序版本
* i18n：从 intltools 迁移到 gettext
* g10n：更新翻译

在 <https://github.com/mate-desktop/engrampa/commits/master/> 完成更新日志

### eom
* 为 webp 文件添加 eom-thumbnailer
* thumbnail:移除使用mate-desktop-thumbnail 帮助
* 启用 Wayland 支持
* EomPrintPreview：修复 HiDPI 显示器上的预览缩略图
* 修复了 Clang Static Analyzer、Cppcheck 和 GCC 报告的几个代码分析、弃用警告
* 允许使用 Alpha 通道对图像进行颜色校正
* 需要 GLib 2.52 或更新版本
* store：将当前目录下的任意图片文件添加到store
* 将手册升级到 docbook 5.0
* 使用持久页面设置
* i18n：从 intltools 迁移到 gettext
* g10n：更新翻译

在 <https://github.com/mate-desktop/eom/commits/master/> 完成更新日志

### libmatekbd
* 修复了 Clang Static Analyzer、Cppcheck 和 GCC 报告的几个代码分析、弃用警告
* 使用 UI gresources  文件
* i18n：从 intltools 迁移到 gettext
* g10n：更新翻译

在 <https://github.com/mate-desktop/libmatekbd/commits/master/> 完成更新日志

### libmatemixer
* 修复了 Clang Static Analyzer、Cppcheck 和 GCC 报告的几个代码分析、弃用警告
* i18n：从 intltools 迁移到 gettext
* g10n：更新翻译

在 <https://github.com/mate-desktop/libmatemixer/commits/master/> 完成更新日志

### libmateweather
* Locations：添加 Lleida – Alguaire 机场气象站
* 修复了 Clang Static Analyzer、Cppcheck 和 GCC 报告的几个代码分析、弃用警告
* locations:更改俄罗斯顿河畔罗斯托夫的气象站
* i18n：从 intltools 迁移到 gettext
* g10n：更新翻译

在 <https://github.com/mate-desktop/libmateweather/commits/master/> 完成更新日志

### marco
* 主题：修复所有主题的窗口控件 hidpi 渲染。
* tabpopup：完成返工
* window: 添加可选的尺寸
* 添加更多窗口装饰主题：添加 Atlanta、Esco、Gorilla、Motif、Raleigh
* 修复了 Clang Static Analyzer、Cppcheck 和 GCC 报告的几个代码分析、弃用警告
* 修复未使用合成时在 frame.c 中使用 RBGA 视觉的问题
* 修复了将窗口移动到边缘以与 CSD 客户端一起使用的问题。
* 添加对meson构建系统的支持
* 使 alt+tab 最大列数可配置并考虑窗口标签宽度
* 添加隐形边框
* 主题：从最大化平铺时修复窗口状态
* constraints：修复 meta_window_constrain() 中的内存泄漏
* alt+tab 弹出窗口：返工
* 允许在 alt+tab 弹出窗口中使用向上/向下箭头键
* 修复几个内存泄漏
* i18n：从 intltools 迁移到 gettext
* g10n：更新翻译

在 <https://github.com/mate-desktop/marco/commits/master/> 完成更新日志

### mate-applets
* 准备使用 gcc 10
* 使用 ${datadir}/dbus-1/system.d 作为默认的 D-Bus 配置目录
* 使 dbus 目录可配置
* 修复了 Clang Static Analyzer、Cppcheck 和 GCC 报告的几个代码分析、弃用警告
* 使 cpufreq 构建独立于内核头文件版本。
* geyes：避免内存泄漏
* multiload: 支持NVME 驱动
* 使命令小程序异步运行命令
* 在关于对话框中制作可翻译的文档
* 在关于对话框中制作可翻译的版权信息
* 确保关于对话框标题的正确翻译
* i18n：从 intltools 迁移到 gettext
* g10n：更新翻译

在 <https://github.com/mate-desktop/mate-applet/commits/master/> 完成更新日志

### 伴侣背景
* 启用对ninja构建系统的支持
* i18n：从 intltools 迁移到 gettext
* g10n：更新翻译

在 <https://github.com/mate-desktop/mate-backgrounds/commits/master/> 完成变更日志

### mate-calc

* 修复复数的科学表示
* 修复了 Clang Static Analyzer、Cppcheck 和 GCC 报告的几个代码分析、弃用警告
* mp-equation：更新物理常数中的值以与数学按钮中的工具提示值匹配
* 将单位工具提示添加到物理常数
* 不要专注于点击
* mp-equation：添加预定义的物理常数
* 将资源用于 UI 文件
* mp: 修正计算结果 ln (e ^ (i * π))
* 以科学记数法显示小数
* mate-calc：修复内存泄漏
* 除了“π”之外，添加对“pi”的支持
* i18n：从 intltools 迁移到 gettext
* g10n：更新翻译

在 <https://github.com/mate-desktop/mate-calc/commits/master/> 完成更新日志

### 共同的伴侣
* 更新 MATE_CXX_WARNINGS 宏
* 在 MATE_DEBUG_CHECK 中设置编译器调试标志
* 检查 AX_APPEND_FLAG 和 AX_CHECK_COMPILE_FLAG 是否可用
* 更新 mate-compiler-flags 宏

在 <https://github.com/mate-desktop/mate-common/commits/master/> 完成更新日志

### mate-control-center
* 在系统数据目录中搜索系统主题
* display: 启用帮助按钮
* 修复了 Clang Static Analyzer、Cppcheck 和 GCC 报告的几个代码分析、弃用警告
* HIDPI 显示器的几个图标修复
* 字体查看器：将字体/集合添加到支持的 mimetypes
* font-viewer：添加 font/ttf 和 font/otf mime 类型
* 在几个应用程序中修复内存泄漏
* 鼠标：添加对加速配置文件的支持
* at-properties：从 dbus-glib 迁移到 gdbus
* 支持 lightdm-gtk-greeter-settings 作为登录首选项程序
* 删除 libXxf86 依赖项
* 为 gla11y 使用 python3
* 在多个 capplets 中添加带有鼠标滚轮的滚动选项卡
* 添加对检查可访问性的支持 洋葱 使用 gla11y 的文件
* 添加新的时间管理应用程序
* 将即时通讯键绑定添加到 mate-keybinding-properties
* 默认应用程序：为默认信使应用程序添加小部件
* capplets：为 UI 文件使用 gresources
* 从 dbus-glib 迁移到 GDBus
* 使用系统数据目录定位键绑定
* 默认应用程序：改进 UI 可访问性
* i18n：从 intltools 迁移到 gettext
* g10n：更新翻译

在 <https://github.com/mate-desktop/mate-control-center/commits/master/> 完成变更日志

### mate-desktop
* Drop mate_desktop_thumbnail_scale_down_pixbuf()
* 将缩略图的大小增加到 256
* 修复了 Clang Static Analyzer、Cppcheck 和 GCC 报告的几个代码分析、弃用警告
* 将剩余的外围架构移至 mate-settings-daemon
* 模式：将鼠标模式移动到 mate-settings-daemon
* schemas：为默认信使定义架构
* 添加配对语言的测试代码。
* 添加对ninja构建系统的支持。
* 修复一些内存泄漏
* MateHSV 实现（GtkHSV fork）
* i18n：从 intltools 迁移到 gettext
* g10n：更新翻译

在 <https://github.com/mate-desktop/mate-desktop/commits/master/> 完成更新日志

### mate-icon-theme
* 为移动网络连接添加状态图标
* Rework volume-status 图标
* 添加 VPN 网络状态图标
* 更新网络状态图标
* 增加 dropbox-status 图标
* 增加 mate/256x256/actions/mail-send.png
* 修复 mate/22x22/devices/printer.png
* 将 22x22px 图标升级到 24x24px 将 1px 添加到边缘
* 使用径向渐变（模糊 13.9%，不透明度 73.4%）作为 MATE 标志阴影
* 添加缺少的首选项系统时间图标
* 在面板中以更好的对比度显示音量状态
* 从 paper-sheets.svg 生成 png mimetypes 图标 - Mate 主题
* 从源生成preferences-system-time.png
* 从源生成 png 图标 - Mate 主题、应用程序、类别和设备
* 更新 mate 主题的终端图标
* i18n：从 intltools 迁移到 gettext
* g10n：更新翻译

在 <https://github.com/mate-desktop/mate-icon-theme/commits/master/> 完成更新日志

### 配对指示器小程序
* 调整指示器图标的大小以适合面板
* i18n：从 intltools 迁移到 gettext
* g10n：更新翻译

在 <https://github.com/mate-desktop/mate-indicator-applet/commits/master/> 完成更新日志

### mate-media
* 修复了 Clang Static Analyzer、Cppcheck 和 GCC 报告的几个代码分析、弃用警告
* gvc 小程序：添加缺少的翻译 (i18n)
* 以与媒体键相同的可配置步骤滚动音量
* 使用鼠标滚轮添加滚动界面
* 允许禁用状态图标或面板小程序
* 为输出启用静音菜单项
* 添加一个新的真正的面板小程序
* i18n：从 intltools 迁移到 gettext
* g10n：更新翻译

在 <https://github.com/mate-desktop/mate-media/commits/master/> 完成更新日志

### mate-menus
* 安装 gir 文件时使用 datadir 和 libdir 变量
* i18n：从 intltools 迁移到 gettext
* g10n：更新翻译

在 <https://github.com/mate-desktop/mate-menus/commits/master/> 完成更新日志

### mate-netbook
* 修复了 Clang Static Analyzer、Cppcheck 和 GCC 报告的几个代码分析、弃用警告
* Fix several code analysis, deprecation warnings reported by Clang Static Analyzer, Cppcheck and GCC
* 让“show-home-title”功能再次发挥作用
* 更改窗口选择器小程序的首选项标签，并添加工具提示
* i18n：从 intltools 迁移到 gettext
* g10n：更新翻译

在 <https://github.com/mate-desktop/mate-netbook/commits/master/> 完成更新日志

### mate-notification-daemon
* 将 gresource 用于 mate-notification-properties.ui
* mate-notification-properties：添加免打扰功能
* i18n：从 intltools 迁移到 gettext
* g10n：更新翻译

在 <https://github.com/mate-desktop/mate-notification-daemon/commits/master/> 完成更新日志

### mate-panel
* 避免在面板顶层使用双 a11y 描述
* 时钟小程序：添加对 ATK 的调用以提供当前显示的时间
* clock applet: Add a call to ATK to provide the current displayed time
* fish：为 Wanda the Fish 使用更高分辨率的图像
* 修复了 Clang Static Analyzer、Cppcheck 和 GCC 报告的几个代码分析、弃用警告
* panel-toplevel：修复扩展垂直面板上的小程序放置
* [clock-applet] 添加鼠标滚轮滚动界面标签
* 对 Wayland 支持的更多改进
* 使系统托盘仅 X11
* 仅制作面板支柱 X11
* 准备好面板-多显示器 Wayland
* 准备好面板背景 Wayland
* 使面板背景监视器仅 X11
* 加载和存储小程序支持的平台
* panel-addto 支持禁用小程序
* 面板添加到 Wayland 支持
* 修复面板重置后重新加载默认布局
* 修复面板重置时的随机崩溃
* 窗口列表：悬停时显示窗口预览
* 修复面板小程序键盘焦点陷阱
* i18n：从 intltools 迁移到 gettext
* g10n：更新翻译

在 <https://github.com/mate-desktop/mate-panel/commits/master/> 完成变更日志

### mate-polkit
* 修复了 Clang Static Analyzer、Cppcheck 和 GCC 报告的几个代码分析、弃用警告
* 从 GSimpleAsyncResult 迁移到 GTask
* i18n：从 intltools 迁移到 gettext
* g10n：更新翻译

在 <https://github.com/mate-desktop/mate-polkit/commits/master/> 完成更新日志

### mate-power-manager
* 图标：添加更高分辨率的图标
* 修复了 Clang Static Analyzer、Cppcheck 和 GCC 报告的几个代码分析、弃用警告
* 需要 upower-0.99.8 或更新版本
* 使用 up_client_get_devices2()
* 为 ui 文件使用 gresources
* 使用鼠标滚轮添加滚动界面选项卡
* 添加 conf 选项以禁用低鼠标功率警告
* i18n：从 intltools 迁移到 gettext
* g10n：更新翻译

在 <https://github.com/mate-desktop/mate-power-manager/commits/master/> 完成变更日志

### mate-screensaver
* 修复了 Clang Static Analyzer、Cppcheck 和 GCC 报告的几个代码分析、弃用警告
* 确保在挂起时锁定并在恢复时解锁
* 为 ui 文件使用 gresources
* 删除 libXxf86 依赖项
* 添加 ELOGIND 支持
* g10n：更新翻译

在 <https://github.com/mate-desktop/mate-screensaver/commits/master/> 完成更新日志

### mate-sensors-applet
* i18n：从 intltools 迁移到 gettext
* g10n：更新翻译

在 <https://github.com/mate-desktop/mate-sensors-applet/commits/master/> 完成更新日志

### mate-session-manager
* 修复了 Clang Static Analyzer、Cppcheck 和 GCC 报告的几个代码分析、弃用警告
* 使用 gnome-keyring 3.34 修复超时
* 删除 GNOME_KEYRING_LIFETIME_FD
* 修复 mate-session-properties 垂直缩放
* test-inhibit: 迁移到 gdbus
* 添加显示隐藏复选框和 gsettings 标志。
* 在启动应用程序中隐藏 NoDisplay 应用程序
* 修复多个内存泄漏
* 添加硬件兼容性文件
* 修复无法检索 org.gnome.SessionManager.Renderer 属性
* 添加 mate_session_check_accelerated 帮助
* 添加 ELOGIND 支持
* i18n：从 intltools 迁移到 gettext
* g10n：更新翻译

在 <https://github.com/mate-desktop/mate-session-manager/commits/master/> 完成变更日志

### mate-settings-daemon
* 需要 DBUS 1.10.0 或更新版本
* 默认 DBUS_SYS_DIR 为 ${datadir}/dbus-1/system.d
* 修复了 Clang Static Analyzer、Cppcheck 和 GCC 报告的几个代码分析、弃用警告
* xrandr：为托盘小程序添加更大的图标尺寸
* 从启动应用程序 capplet 中隐藏 MATE 设置守护程序
* 从 mate-desktop 添加剩余的外围架构
* 鼠标：添加加速度配置文件
* 在 gschema 中将 media-keys volume-step 默认值从 6 更改为 5
* 插件：删除 libXxf86 依赖项
* 插件管理：代码优化
* media-keys：执行由架构定义的默认即时消息应用程序
* locate-pointer：尝试定位时不要抓住指针按钮
* i18n：从 intltools 迁移到 gettext
* g10n：更新翻译

在 <https://github.com/mate-desktop/mate-settings-daemon/commits/master/> 完成更新日志

### mate-system-monitor

* 修复了 Clang Static Analyzer、Cppcheck 和 GCC 报告的几个代码分析、弃用警告
* 需要 GLib 2.56.0 或更新版本
* 改进对 HiDPI 的支持
* 在使用和首选项部分添加磁盘 I/O 信息
* 修复一些内存泄漏
* 在进程信息上添加磁盘 IO
* 在系统选项卡上显示 GPU 信息
* 支持多达 32 个 CPU
* 显示 ZFS 中的可用磁盘空间
* 在系统选项卡中显示 OpenIndiana 版本和内核信息
* Show OpenIndiana release and kernel info in System tab
* 修复 openSUSE Tumbleweed 滚动发布信息
* i18n：从 intltools 迁移到 gettext
* g10n：更新翻译

在 <https://github.com/mate-desktop/mate-system-monitor/commits/master/> 完成变更日志

### mate-terminal
* 准备使用 gcc 10
* 修复多个内存泄漏
* 终端屏幕：修复关闭窗口时的警告
* 修复了 Clang Static Analyzer、Cppcheck 和 GCC 报告的几个代码分析、弃用警告
* 使“突出显示鼠标指针下的东西”可配置
* 如果关闭时有多个打开的选项卡，则显示确认对话框
* 将手册升级到 docbook 5.0
* i18n：从 intltools 迁移到 gettext
* g10n：更新翻译

在 <https://github.com/mate-desktop/mate-terminal/commits/master/> 完成更新日志

### mate-user-guide
* 更新报告错误部分
* 删除 custom-command-options 部分并解决语法问题
* 更新首选应用程序部分
* 用外部参照替换 docbook 链接并修复 linkend 属性（#30）
* 将手册升级到 docbook 5.0
* g10n：更新翻译

在 <https://github.com/mate-desktop/mate-user-guide/commits/master/> 完成变更日志

### mate-user-share
* 修复了 Clang Static Analyzer、Cppcheck 和 GCC 报告的几个代码分析、弃用警告
* 复 HTTPD 配置通知
* i18n：从 intltools 迁移到 gettext
* g10n：更新翻译

在 <https://github.com/mate-desktop/mate-user-share/commits/master/> 完成变更日志

### mate-utils
* 准备使用 gcc 10
* 将资源用于 UI 文件
* 修复了 Clang Static Analyzer、Cppcheck 和 GCC 报告的几个代码分析、弃用警告
* 添加 MATE Disk Image Mounter 实用程序
* logview：使用当前语言环境的首选日期和时间表示
* 使用鼠标滚轮添加滚动选项卡
* 使inkscape 和rsvg-convert 成为可选项
* 修复一些内存泄漏
* 从 svg 文件重新生成 png 图标
* 更新关于对话框中的文档
* i18n：从 intltools 迁移到 gettext
* g10n：更新翻译

在 <https://github.com/mate-desktop/mate-utils/commits/master/> 完成更新日志

### mozo
* 添加撤消和重做按钮
* 修复项目拖放创建副本，修复撤消，重做和刷新时崩溃
* 修复了 Clang Static Analyzer、Cppcheck 和 GCC 报告的几个代码分析、弃用警告
* 添加对meson构建系统的支持
* 修复创建新菜单和项目
* i18n：从 intltools 迁移到 gettext
* g10n：更新翻译

在 <https://github.com/mate-desktop/mozo/commits/master/> 完成更新日志

### pluma
* 添加显示不可打印字符（空格/制表符/换行符）的功能
* 修复了 Clang Static Analyzer、Cppcheck 和 GCC 报告的几个代码分析、弃用警告
* window：不要覆盖 GdkWindowState
* 修复一些内存泄漏
* 使用 GtkSourceView 3.22 修复构建
* 拼写检查插件：添加缺少的翻译 (i18n)
* 添加对使用 gla11y 检查 UI 文件的可访问性的支持
* 添加片段以切换评论/取消评论
* pluma-print-preview：修复警告：相同的表达式
* 切换到 Python 3
* 手册：更新如何从菜单中打开pluma
* 将手册升级到 docbook 5.0
* i18n：从 intltools 迁移到 gettext
* g10n：更新翻译

Complete changelog at <https://github.com/mate-desktop/pluma/commits/master/>

### python-caja
* 准备使用 gcc 10
* 放弃对 Python 2 的支持
* 添加对使用 Python 3.9 构建的支持
* i18n：从 intltools 迁移到 gettext
* g10n：更新翻译

在 <https://github.com/mate-desktop/python-caja/commits/master/> 完成更新日志
