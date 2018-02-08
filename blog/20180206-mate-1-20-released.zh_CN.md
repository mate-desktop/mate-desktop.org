<!--
.. link:
.. description:
.. tags: Releases,发布
.. date: 2018-02-07 09:00:00
.. title: MATE 1.20 发布
.. slug: 2018-02-07-mate-1-20-released
.. author: Martin Wimpress
-->

经过将近 11 个月的开发，MATE Desktop 团队很高兴能在此发布 MATE Desktop 1.20。
我们非常感激每一个 MATE 贡献者为这个版本付出的辛勤劳动。

![about](/assets/img/blog/about-mate-1.20.zh_CN.png)

## MATE 1.20 的新特性

本次更新的主要任务在于通过现代化老旧代码来提高 MATE Desktop 的稳定性。与此同时
我们还改进了 MATE 的窗口管理器 (Marco) 并添加了 HiDPI 支持。除此之外，我们还
修复了相当数量的已知问题。

MATE Desktop 1.20 包含如下主要更改：

  * **MATE Desktop 1.20 支持 HiDPI 显示器，且支持动态探测和缩放。**
    * 与此同时，提交 Qt 应用程序的 HiDPI 设置信息到桌面环境以改善基于多个图形库的应用程序之
    间的外观统一。
    * HiDPI 开关直接触发动态界面缩放和大小调整，无需重新登录。
  * **Marco（在可用时）新增 [DRI3 及 XPresent](https：//lwn.net/Articles/569701/) 支持。**
     * 使用 Marco 时的游戏性能明显提高。
  * Marco 新增 **¼ 平铺支持**，方向键现在可用于控制 <kbd>Alt</kbd> + <kbd>tab</kbd>
    窗口切换，并且新增了用于移动窗口到其他显示屏。
  * 新增 **全局菜单支持**，可配合 [vala-panel-appmenu](https：//github.com/rilian-la-te/vala-panel-appmenu)
    一类的服务使用。
  * MATE 面板的 [状态通知项 (SNI)](https：//www.freedesktop.org/wiki/Specifications/StatusNotifierItem/) 支持大大增强。
  * **书签栏现在支持 GTK+3 位置。**
  * MATE 终端新增背景图像支持、Solarised 主题及用于切换标签页的组合键。
  * **Atril，MATE 的默认文档阅读器已完全整修**，该程序的许多方面都得到了相当的改善。
    * 大幅度改善了无障碍支持，尤其对于视力受损的用户。
    * 新增光标导航支持。
  * **移除了 MATE 小挂件中的“投资”挂件。**
    * 由雅虎 (Yahoo) 提供的 API 已不再受到维护，且没有任何功能均等的替代品。
  * 面板小挂件现在通过显示单位来正确调整大小，与此同时许多图表现已支持动态缩放。
  * **MATE 主题得到了大量改进**，并已完全支持 GTK+ 3.22 新增的组件和样式类型。
  * Engrampa，MATE 默认归档管理器的加密 7z 归档支持得到增强。
  * MATE 传感器挂件（终于）添加了 udisks2 支持。
  * MATE 屏幕保护程序新增 OpenBSD 认证支持，Atril 中的 minizip 也新增了许多 BSD 变种的
    支持。
  * 翻译已更新。 *感谢各位翻译贡献者！*
  * 发行版维护者请注意，我们提高了 GTK+3 和 GLib 版本要求。
    * MATE Desktop 现在需要 GTK 3.22 和 GLib 2.50 的更新版本才能构建。
  * 你可能会在变更日志里面看到有关 Wayland 的信息，不过不要激动：这些改动可能跟你想的不太一样 `：-)`

MATE Desktop 的大量组件现可通过如下链接下载：

  * <http：//pub.mate-desktop.org/releases/1.20/>

## 变更日志

如下是各个组件的详细更改记录。

### mate-desktop 1.20.0

  * 在 gsettings 里面添加窗口缩放系数设置
  * 移除多余的 GLib 最低版本检查
  * 删除 < gtk+-3.22 的东西并且升级 gtk+ 的最低要求
  * schema：移除 can-change-accels 键, 因为在 GTK+3 下无效
  * 实现 WidthOfScreen 和 HeightOfScreen
  * 删除 `MateAboutDialog`
  * mate-about：删除 libunique 的残余引用
  * mate-about：改为使用 `GtkAboutDialog`
  * gtk 3.22：避免使用过时的 `gdk_screen_get_monitor` 函数：
  * 避免使用过时的 `gdk_screen_get_width/height`
  * mate-desktop-item：mate-about：避免使用过时的 `gtk_show_uri`
  * mate-about：避免使用过时的 `gtk_show_uri`
  * 避免使用过时的 `gdk_screen_get_n_monitors`
  * 避免使用过时的 `gdk_screen_make_display_name`
  * 避免使用过时的 `gdk_screen_get_number`
  * 修正了 `man mate-about` 里面一些不准确的信息
  * 修复 `mate-colorsel.c` 中损坏的备用光标
  * mate-colorsel：不使用过时的 `GTK_STOCK_COLOR_PICKER`
  * 添加全局菜单支持
  * 更新翻译

### mate-user-guide 1.20.0

  * 更新翻译

### libmatekbd 1.20.0

  * 删除 < gtk+-3.22 的东西并且升级 gtk+ 的最低要求
  * 实现 WidthOfScreen 和 HeightOfScreen
  * matekbd-status：修复在创建状态栏图标时的 Gdk-CRITICAL 警告
  * gtk 3.22：避免使用过时的 `gdk_screen_get_monitor` functions：
  * 避免使用过时的 `gdk_screen_get_width/height`
  * 避免使用过时的 `gdk_screen_get_number`
  * matekbd-indicator：不要展开
  * matekbd-indicator：不使用过时的 `gdk_cairo_create`
  * 修正 GtkIconInfo 的奇怪行为
  * matekbd-indicator：不使用过时的 GtkAlignment
  * keyboard-drawing：set css name matekbd-keyboard-drawing
  * Slightly increase the font size for the key labels
  * matekbd-keyboard-drawing：不要取消双重缓冲
  * matekbd-keyboard-drawing：处理 `XkbGetKeyboard()` 失败的情况
  * matekbd-keyboard-drawing：Prevent gtk+ keynav from taking focus away
  * fix some introspection warnings
  * show-layout.ui：不使用过时的组件
  * UI：expand kbdraw vertical
  * 更新翻译

### libmateweather 1.20.0

  * locations：Add Radom, Poland
  * Locations：add Zhukovsky airport (Moscow, Russia)
  * Locations：fix Sheremetyevo airport name (Moscow, Russia)
  * Add timeout, actully invalidate session in weather_info_abort
  * Start reducing weather spam by creating intial cut of `weather_info_equal()`
    function that will help apps determine if two WeatherInfo instances are 'the same'
    enough to not bother with a notification
  * remove warning on unused bsun by actually testing value
  * Fix `soup_session_async_new()` deprecation warning
  * Add missing Polish cities with airports
  * Fix Novosibirsk timezone
  * Add Ceiba in Puerto Rico
  * 文档：移除远古的 MateConf 说明以及其他的一些东西
  * 更新哈萨克斯坦的城市列表 (Kazakhstan).
  * 检查 `$GIO_REQUIRED` 变量的值
  * 更新翻译

### mate-icon-theme 1.20.0

  * 替换掉了一些损坏了的标志
  * 更新翻译

### caja 1.20.0

  * 不在 GTK+ 3.14 上使用 CSS
  * Fix tasklist icon change when opening new tab
  * Include local files with "" instead of <>
  * `search_dispose` and `search_finilize` can't be run after search finished
  * add missing window icon to About dialog for extensions
  * move libegg to the top srcdir and drop some leftovers
  * 实现 WidthOfScreen 和 HeightOfScreen
  * caja-places-sidebar：fix refusal to unmount when sidebar is wide
  * caja-places-sidebar：disable overlay scrollbar
  * 修正：wrong behavior with key "enter" while renaming files in list view
  * open folder in new window：<kbd>ctrl</kbd> + <kbd>shift</kbd> + <kbd>w</kbd>
  * zoom-control：change zoom with mousewheel scroll over button
  * View -> Visible Columns：fix vertical expand of dialog content
  * reword Size on Disk column description a bit
  * 修正：wrong <Shift+Del> behavior while renaming files
  * icon-dnd：remove hardcoded highlight frame
  * 修正：在加载背景图片时导致的高 CPU 占用
  * list view：fix large icon margins on zooming out
  * make sure scaling the desktop wallpaper works in all monitors
  * remove weird +x attribute from a source file
  * gtk 3.22：避免使用过时的 `gdk_screen_get_monitor` 函数：
  * Adds columns autosizing
  * Refresh all rows on zoom change
  * Forces widget redraw on zoom
  * pathbar：enable mousewheel scrolling like it was with GTK+2
  * libcaja-private：remove wrong link from internal README
  * private：Ensure we allow launching .desktop files from trusted symlinks
  * 修正：Scaling the desktop wallpaper doesn't work
  * open-with-dialog：set max-char-width for a label
  * Fix "Open With" dialog "Open" button's text misaligned
  * 避免使用过时的 `gdk_screen_width/height`
  * 避免使用过时的 `gdk_screen_get_width/height`
  * 避免使用过时的 `gdk_screen_make_display_name`
  * libegg：替换过时的 `gtk_drag_begin`
  * eggsmclient：fix a build warning because of -Wcomment
  * 不使用过时的 `gtk_show_uri`
  * 避免使用过时的 `gdk_screen_get_number`
  * Fix browsing/autorun media on insertion
  * fix vertical Compact View scrolling in `fm_icon_view_scroll_event()`
  * property-browser：add style class frame to scrolledwindows"
  * Fix off-by-one error in `caja-pathbar.c`
  * added feature：present the size on disk of files as we present the size of the file.
  * restore DBus interface initialization
  * CSS：在 Load a different caja-desktop.css with GTK 3.14
  * Use gtk+-3 bookmarks location
  * Open With dialog：force icon size
  * file：make `caja_file_get_gicon` return custom icons too
  * Expand grid width to canvas
  * 使用 `atk_component_get_extents` 替换 `atk_component_get_position`
  * don't parse .hidden files manually - GIO does it since 2.36
  * 不要检查 `MATE22_USER_DIR` 这一不存在的环境变量
  * 不要检查 `~/.mate2` 这一不存在的目录
  * eel-accessibility：remove unused code and outdated comments
  * show correct right-click menu after making selection
  * eel：Queue resizes on the canvas as elements change visibility
  * Add size_request to IconContainer to work around unncecessary relayouting
  * IconCanvasItem：fix overlapping filenames on hover
  * eel：remove unneeded #include with condition
  * eel：remove some unused code from eel-gdk-pixbuf-extensions
  * 修复构建警告 (此处不需要常量，no const needed there)
  * 修复使用 gcc 4.9.2 导致的问题 (似乎这个版本的编译器默认使用c89)
  * 搜索：添加标签支持 (xattr：：xdg.tags).
  * Fix broken rename in list view by selectin file name cell.
  * property-browser：add style class frame to scrolledwindows
  * caja-application.c：修复未经初始化的值的问题
  * 更新翻译

### mate-polkit 1.20.0

  * 删除 polkitgtkmate 库和文档
  * 修复 statusnotifier 图标的隐藏/再显示问题
  * status-icon：不使用原版图标
  * polkitmateauthenticationdialog：避免使用过时的 GtkAlignment
  * polkitmateauthenticationdialog：替换掉过时的 GTK_STOCK
  * 更新翻译

### marco 1.20.0

  * 构建：移除不再需要的 pangoxft 依赖
  * Small bugfix for the move_to_X keybinds
  * 修复在不同大小的显示器上的显示问题
  * Restructured monitor keybinds and adjust `save_rect`
  * Implemented simple shourtcuts to move window to another monitor
  * schema：更正手误
  * compositor：don't try to paint window that is not viewable
  * Fix wrong result in `meta_window_titlebar_is_onscreen()` for windows without a frame
  * Add support for gtk3 `_GTK_SHOW_WINDOW_MENU` event
  * More elegant solution for handling new move-to-workspace keybinds
  * Implemented a setting to disable top tiling
  * Implemented tabpopup when moving window to different workspace
  * keybindings.c：修复编译器警告：
  * Reset tile_resized to false when fullscreening
  * Fixes windows not going to `save_rect` when unmaximimizing
  * Allow horizontal and vertical resizing when corner tiled
  * Fixes window getting reset to saved_rect when untiling from corner
  * Added keybindings for corner tiling
  * Implemented simple corner tiling by mouse drag
  * 实现 WidthOfScreen 和 HeightOfScreen
  * XFIXES regions are leaked during paint_windows
  * Add stricter logic for running without XPresent support
  * 使 XPresent 成为可选依赖
  * 添加一些来自 xfwm4 的变化
  * Cancel present_pending flag when erroring out
  * XPresent 拓展支持
  * Store a window flag when user resizes from tiled
  * Allow tiled windows to be resized horizontally
  * gtk 3.22：避免使用过时的 `gdk_screen_get_monitor` functions：
  * 避免使用过时的 `gdk_screen_width/height`
  * 避免使用过时的 `gdk_screen_get_width`
  * display：不使用过时的 `GDK_DEVICE_MANAGER`
  * tools：remove marco-mag and marco-grayscaletools
  * Fix synthetic keybinding/button-grab window
  * Forces a window scale of 1 for the window manager, instead of using the default or user configured scale.
  * 避免使用过时的 `gdk_display_get_screen`
  * 避免使用过时的 `gdk_screen_get_number`
  * Alt/tab - define arrow keycode + numpad arrows
  * Allow use of arrows while in <kbd>Alt</kbd> + <kbd>Tab</kbd> popup
  * ui：Fix invalid object construction in frames
  * README：更正 GSettings 键的名称
  * keybindings：从 “当前工作区 (current workspace)” 删除大写字母
  * 为重命名当前工作区添加了热键
  * 不再使用过时的 API
  * 更新翻译

### mate-settings-daemon 1.20.0

  * HiDPI：Load xsettings during initialization phase
  * Add HiDPI configuration in XSettings
  * Add support for HiDPI displays
  * plugins：`G_GNUC_UNUSED` in unused but needed variables
  * xsettings：drop CanChangeAccels which won't work with GTK+3
  * msd-datetime-mechanism.c：Fix build warnings：
  * msd-mpris-manager.c：修复编译器警告：
  * configure.ac：删除 `GLIB_VERSION_MAX_ALLOWED`
  * 更新翻译

### mate-session-manager 1.20.0

  * gsm-manager.c：修复编译器警告：
  * 在显示“注销”或者“关机”对话框时不失去焦点
  * add style class `logout-dialog`
  * 避免使用过时的 `gdk_screen_make_display_name`
  * 不使用过时的 `gtk_show_uri`
  * 避免使用过时的 `gdk_screen_get_number`
  * systemd user-session needs to be updated to get all user-defined enviroment when the session starts.
  * dbus needs to be updated to get all user-defined environment when the session starts.
  * 更新翻译

### mate-menus 1.20.0

  * 更新 gio 版本到 2.50.0
  * make mate-applications-merged symlink
  * 更新翻译

### mate-panel 1.20.0

  * Support panel auto-scaling for HiDPI displays
  * bump minimum required libwnck version to 3.4.6
  * status-notifier：don't crash if tooltip has wrong type
  * status-notifier：don't crash if menu layout has wrong type
  * Fix rendering of radio buttons in status notifier
  * panel-run-dialog：fix segfault when program list is enabled
  * get focus when displaying "applet broken" dialog
  * Update workspace switcher properties dialog
  * 简化代码
  * rework the process of cancelling the background change operation
  * status-notifier：properly handle the NULL case for items
  * status-notifier：handle wrong-size icons called by path
  * status-notifier：load icons specified by path
  * Fix failures to load icons when the application calls for a path and not an icon name
  * 修复编译器警告：`toplevel_configure_event` defined but not used
  * 修复编译器警告：`GLIB_VERSION_MIN_REQUIRED` redefined
  * status-notifier：fix failure to show icon for missing icon
  * 实现 WidthOfScreen 和 HeightOfScreen
  * panel-toplevel：Remove pointer boundary check in `panel_toplevel_queue_auto_hide()`
  * remove ancient gnome-panel leftovers
  * Keep the right icons on bottom still displaying right when the resolution change larger
  * wncklet：disconnect signals by data on destroy
  * clock：disconnect one more signal handler on destroy
  * panel-applet-frame-dbus-c：comment out newly unused variable
  * Clock：don't check variables that can never be < 0 for < 0
  * panel-applet-frame-dbus.c：comment out never used code block
  * panel-toplevel：remove duplicate break statement
  * status-notifier：remove duplicate check found by cppcheck
  * status-notifier：hide mate-polkit icon if passive
  * Apply position fix on popup to GTK 3.20 and earlier
  * GTK 3.22 status notifier：reposition menu when size changes
  * GTK 3.22/status-notifer Fix menu position if size changed since last shown
  * Stop panel collapse left on adding certain out-of-process applets
  * make file/folder launchers work again
  * panel-context-menu：Add confirmation dialog to panel reset option
  * Add option to context menu to reset the panel
  * clock：disconnect signal handlers on destroy
  * Fix crashes on moving/removing applets with glib 2.53.4 or later
  * gtk 3.22：避免使用过时的 `gdk_screen_get_monitor` functions：
  * Add a gsettings key to enable/disable SNI Support
  * wncklet：stop segfaults, warnings on removing in-process switcher, window-list
  * fish：fix adding back after removal
  * Fish：stop all warnings on removing when built in-process
  * Clock：fix removal warnings when in-process applet removed
  * clock：stop segfault on removing applet when built in-process
  * libmate-panel-applet：fix typos in id->factory_id rename
  * libmate-panel-applet：Only declare `_panel_applet_shlib_factory()` when needed
  * libmate-panel-applet：fix error in unregistering dbus object
  * libmate-panel-applet：fix build warning
  * libmate-panel-applet：fix introspection
  * libmate-panel-applet：unown bus name and unregister dbus object
  * libmate-panel-applet GTK 3.14/3.16：fix custom bg w alpha
  * libmate-panel-applet：include dummy variable in factory for certian applets
  * libmate-panel-applet：fix bg rendering for in-process applets
  * libpanel-applet/panel-applet.h：Rename id to `factory_id` for factory
  * limatepanel-applet：add panel-applet-private.h
  * don't use GtkPlug/GtkSocket for in process applets
  * make it possible to get applet widget
  * libpanel-applet：add `panel_applet_factory_get_applet_widget`
  * libpanel-applet：return process type and applet uid
  * libpanel-applet：store factories in hash table
  * libpanel-applet：delay GtkPlug creation
  * libpanel-applet：add process type to private data
  * libpanel-applet：Remove `out_process` from `panel_applet_factory_main()`
  * 避免使用过时的 `gdk_screen_get_width/height`
  * 避免使用过时的 `gdk_screen_get_n_monitors`
  * fish：fix applet opening as thin line when built in-process
  * Forces a window scale of 1 for the panel, instead of using the default or user configured scale.
  * 避免使用过时的 `gdk_screen_make_display_name`
  * 避免使用过时的 `gdk_display_get_screen`
  * 不使用过时的 `gtk_show_uri`
  * 避免使用过时的 `gdk_screen_get_number`
  * fix applet crashes on transparent user-set panel bg
  * system tray：fix hidden icons on image/transparent color BG
  * Fix GTK theme image bg support on vertical panel
  * Make panel image background in GTK theme work again
  * clock：fix hovering over timezone text, causes panel to scale beyond screen limit
  * GTK 3.18+ fix transparent default panel bg
  * menu：restore focus after drag-n-dropping menuitem outside
  * menu：restore focus after closing popup menu of a menuitem
  * 修正：menubar/menu-button can't launch mozo
  * menu：remove incorrect code from the popup menu of a menuitem
  * status notifier：follow same menu theme as rest of panel
  * fix moving applets between panels
  * menu：fix crash when some .desktop file has empty Icon field
  * clock：properly handle visibility of edit button
  * clock：drop deprecated `gtk_size_group_set_ignore_hidden`
  * clock：move GtkButton in another horizontal GtkBox parent
  * clock.c：drop deprecated `gtk_size_group_set_ignore_hidden`
  * localized application's name and description
  * menu-button：disconnect from GSettings when applet is removed
  * action-button：disconnect from GSettings when applet is removed
  * remove a needless glib check
  * status-notifier：fix crash on unknown signal name
  * use GTK+3 bookmarks location for Places menu
  * doc：remove some references to nonexistent stuff
  * fix build with gcc 4.9.2 (looks like it's in c89 mode by default)
  * Run dialog：Add option to reverse history view
  * Run dialog：Fix wrong history len with max size 1
  * Run dialog：Allow changing history size
  * doc：drop ancient MateConf references
  * Run dialog：Fix wrong history order
  * status-notifier：Do not hide passive items
  * panel-menu-bar：fix build warning and some spacing
  * properly fit expanded panel to smaller screen size
  * system-tray：Properly propagate orientation changes
  * notification-area：Fix item orientation
  * workspace switcher：handle `GDK_SCROLL_SMOOTH` and fix build warning
  * Reenable workspace switcher wrapping
  * pre-bump version
  * status-notifier：Fix handling of icon-padding style property
  * Simplify panel description shown when switching panels with the WM
  * status-notifier：Plug a memory leak
  * remove deprecated `sys/timeb.h` header, as nothing uses it
  * status-notifier-watcher：Allow re-registration of registered items
  * setup custom icon
  * status-notifier：Plug a memory leak
  * notification area：Fix memory leak sorting items
  * 更新翻译

### mate-backgrounds 1.20.0

   * 删除 gnome 的上古遗留
   * 更新翻译

### mate-themes 3.22.8 to 3.22.15

  * Submarine themes：remove a box-shadow at engrampa toolbar
  * submarine themes：remove padding from caja-sidebar treeview
  * all themes caja：remove right-border from scrolledwindow.frame
  * Menta metacity themes：remove left/right-border for maximised windows
  * BlackMATE：write the border on scrollbar trough
  * all themes：remove right-border from scrolledwindow.frame
  * submarine themes：fix fg color of button.suggested-action in headerbars
  * BlackMATE：Workaround for Yelp/Lireoffice/Firefox scrollbar issue
  * Revert "Gtk+-3.20 all themes：fix redraw issue with yelp"
  * TOK/TG：sliders：keep the original size
  * Gtk+-3.20 submarine：reduce border radius for treeview.selected/hover in sidebars
  * Gtk+-3.20 submarine：set font color for spinbutton entry
  * Gtk+-3.20 submarine themes：fix a jumpin button in headerbar of gitg
  * Gtk+-3.20 submarine themes：setup dnd for caja-icon-view
  * Gtk+-3.20 T. themes：fix double border in mate-volume-control notebook
  * Gtk+-3.20 Submarine themes：fix focus state of pluma-statusbar-button
  * Gtk+-3.20 Most themes：style menuitem accelerator hover
  * All themes：change syntax for loading panel-grid image for mate-1.20
  * Gtk+-3.20 submarine themes：set top borderradius for .titlebar > headerbar
  * Gtk+-3.20 Most Themes：fix padding of primary/secondary image in GtkEntry
  * Gtk+-3.20 TRAD themes：fix color of grey-out arrows in menus
  * TOK/TG：add menuitem radio mixed
  * TOK/TG menuitems：checkboxes and radio buttons redesigned
  * Gtk+-3.20 most themes：fix GtkScale slider mouse-selection if slider is out of range
  * Gtk+-3.20 all themes：fix redraw issue with yelp
  * Gtk+-3.20 GreenLaguna：some menu fixes
  * Gtk+-3.20 Menta themes：add transition effect for menu arrows
  * Gtk+-3.20 Menta themes：drop settings for firefox menus
  * Gtk+-3.20 submarine themes：drop transition effect from labels
  * Add index.theme file for gtk+ High Contrast theme
  * Gtk+-3.20 Most themes：setup border for clockmap in clock applet
  * Gtk+-3.20 Submarine themes：some fixes for clock applet
  * Gtk+-3.20 BlackMate：some panel clock fixes
  * TOK/TG：caja：solid color to the notebook header border
  * Gtk+-3.20 Menta themes：use a hardcoded bg color for tooltips
  * BlackMATE：CSD apps-match noncomposited headerbar to square window border
  * BlackMATE：more CSD app fixes
  * BlackMATE fixes for CSD apps
  * Gtk+-3.20 Menta themes：change colors for panel applet buttons
  * Gtk+-3.20 Menta themes：change transition timining for menubar menuitem
  * Gtk+-3.20 Menta themes：use normal menubar menuitems styling for the panel
  * Gtk+-3.20 Menta themes：remove transition effect from menuitems
  * TOK/TG：mate-terminal：solid color to the notebook header border
  * Gtk+-3.20 BlackMATE：fix fontcolor in url bar of google chrome
  * Gtk+-3.20 BlackMATE：change menuitem accelerator font color
  * TOK/TG：xfce4-terminal：solid color to the notebook header border
  * TOK/TG：Remove gradient from notebook header
  * cursor：add color-picker to make file
  * Gtk+-3.20 Submarine themes：improve pluma sidebar
  * Gtk+-3.20 submarine themes：fix fg color in pluma error dialogs
  * BlackMATE：fully style noncomposited m-s-d OSD
  * BlackMATE：support new msd-osd-window-solid style class for non-composited OSD case
  * BlackMATE：make caja renaming labels more readable
  * ContrastHighInverse：Fix Caja rename labels when theme actually applied
  * cursor：add color-picker cursor image
  * GTK+-3.20 submarine themes：improve mate- and mintmenu
  * Gtk+-3.20 menta themes：fixes for mate- and mint-menu
  * Gtk+-3.20 Traditional themes：improve some dialog windows
  * Traditional themes：don't draw a bg for mate-indicator-applet
  * Gtk+-3.20 most themes：fix bg color in list-view of caja inactive-pane
  * Gtk+-3.20 all themes：add new css name matekbd-keyboard-drawing
  * metacity submarine themes：fix innerborder if metacity or compiz WM is used
  * TOK/TG：xfce4-terminal：gradient color to the notebook header border
  * TOK/TG：make padding in notebook tabs 2 pixels bigger
  * menta-fix "{{" typo breaking gtk-widgets.css file
  * All themes：修正：print dialog paper depictions not appearing correctly
  * Gtk+-3.20 Menta themes：don't make any different between backdrop and normal state
  * Gtk+-3.20 most themes：mate-panel hide button modification
  * TOK/TG：caja：set gradient color to the notebook header border
  * Gtk+-3.20 submarine themes：mate-panel hide button modifications
  * TOK/TG：Fixes borders in xfce4-terminal tabs and probably more applications
  * Gtk+-3.20 all themes：improvements for mate-menu
  * Gtk+-3.20 all themes：better way to style keyboard layouts
  * TOK/TG：mate-terminal：set gradient color to the notebook header border
  * Gtk+-3.20 Traditional：set color to the notebook header border in mate-terminal
  * Gtk+-3.20 Menta themes：sort mate-applications.css
  * Menta themes：set color to the notebook header border
  * TOK/TG：New colors in panel grid
  * Gtk+-3.20 all themes：style mate-keyboard-layout-viewer
  * Traditional themes - use applet handles from Menta
  * TOK/TG：mate-terminal：use border in header tab instead notebook
  * Gtk+-3.20 ContrastHighInverse：add missing assets to avoid a runtime warning
  * Menta themes：eliminate wrong border-color for lockscreen
  * Gtk+-3.20 submarine：eliminate wrong border-color for lockscreen
  * GreenLaguna：correct notebook tab borders in mate-terminal
  * Submarine themes：correct notebook tab borders in mate-terminal
  * Gtk+-3.20 Menta themes：correct notebook header borders in mate-terminal
  * Traditional themes：drop some lines in mate-terminal for a better look
  * Gtk+-3.20 Most themes：don't use a border for terminal notebook
  * Traditional themes：print dialog improvements
  * Traditional themes：set notebook borders for pavu-control (better fix)
  * Traditional themes：set notebook borders for pavu-control
  * Gtk+-3.20 GreenLaguna：style scrollbar junction
  * Gtk+-3.20：add an annoying wildcard for firefox
  * Gtk+-3.20 GreenLaguna：some border fixes for caja sidebar
  * Gtk+-3.20 GreenLaguna：change border color of GtkSwitch
  * Gtk+-3.20 GreenLaguna：change border-color for scrollbars
  * GTK+-3.20 GreenLaguna：change insensitive_bg_color
  * Gtk+-3.20 GreenLaguna：improve notebooks
  * Traditional themes：drop the two useless lines in the notebooks
  * Gtk+-3.20 GreenLaguna：re-work  borders of frame and other improvements
  * GreenLaguna metacity：increase border size
  * Submarine metacity：increase border size
  * Gtk+-3.20 Submarine：set color for dim-labels at list rows
  * Traditional themes：set more border colors in checked notebook tabs
  * Gtk+-3.20 submarine themes set a padding on statusbars
  * Gtk+-3.20：fix jumping button in mate-font-viewer toolbar
  * Gtk+-3.20 submarine themes：improve headerbars and popover menus
  * Gtk+-3.20 submarine themes：set a padding for gedit statusbar
  * Gtk+-3.20 Menta themes：add missing border-image for button.fat：checked in filezilla and atril
  * Gtk+-3.20 Menta themes：some notebook improvements
  * Fixed URL colors for Firefox search suggestions
  * Gtk+-3.20 Menta themes：re-work borders for frames and other improvements (mega commit)
  * Traditional themes：make padding in notebook tabs smaller
  * Gtk+-3.20 submarine themes：several improvements
  * Gtk+-3.22 Submarine themes：some notebook improvements
  * Gtk+-3.22 Submarine themes：re-work borders for frames
  * Gtk+-3.20 Submarine themes：fix previous commit for rubberband
  * Gtk+-3.20 submarine themes：fix rubberband for mate-screenshot
  * Gtk+-3.20 submarine themes：fix toolbar label color
  * Traditional themes：use gradient color on active tabs
  * Gtk+-2.0 Greenlaguna：use hardcoded hex colors in gtkrc
  * Gtk+-2.0 most themes：use a oneliner for color definitions in gtkrc
  * Traditional themes：add a border-image for some applets
  * Gtk+-3.20 Traditional themes：use a border for the whole GtkInfobar
  * Gtk+-3.20 Traditional themes：workaround, fix some borders in firefox
  * Gtk+-3.20 Traditional themes：fix jumping combobox button
  * Gtk+-3.20 most themes：fix sidebar of GtkAssistant
  * Gtk+-3.20 Submarine themes：fix sidebar of GtkAssistant
  * Gtk+-3 all themes：don't set NaTrayApplet-icon-size

### mate-notification-daemon 1.20.0

  * 实现 WidthOfScreen 和 HeightOfScreen
  * gtk 3.22：避免使用过时的 `gdk_screen_get_monitor` functions：
  * 避免使用过时的 `gdk_screen_get_width/height`
  * 避免使用过时的 `gdk_screen_get_n_monitors`
  * Fixes high cpu usage with large timeouts
  * unescape URI-encode paths for icon files
  * 更新翻译

### mate-control-center 1.20.0

  * Scale font DPI for HiDPI displays
  * 添加对高解析度 (HiDPI) 显示器的支持
  * theme-installer.c：在 `mate_theme_install_real` 里面没有 `g_object_unref`
  * theme-util.c：fix reinstalling the deleted theme can cause failure
  * Support the theme compression package for installing XZ format
  * 删除未使用的变量
  * eggcellrendererkeys.c：Fix build warnings：
  * remove some leftovers related to MacOS support
  * theme-thumbnail.c：Fix build warnings with `write` and `pipe`：
  * libslab：store search entry widget as `GtkEntry`
  * libslab：fix search icon misaligned
  * 更新翻译

### mate-screensaver 1.20.0

  * Add HiDPI support for lock screen
  * gs-lock-plug.c：修复编译器警告：
  * 实现 WidthOfScreen 和 HeightOfScreen
  * restore the correct mate-screensaver-command manpage
  * fix loop initial declarations
  * 修正：idle slider display in all languages
  * drop glib required max version
  * 避免使用过时的 `gdk_screen_get_width/height`
  * 不使用过时的 `gtk_show_uri`
  * 使用 `bsd_auth(3)` 实现 OpenBSD 的验证机制
  * Bug 修正：`g_get_real_name` will never return NULL pointer
  * lock-dialog UI：避免使用过时的 widgets
  * Bug 修正：screensaver and lock screen not correctly displayed in configurations with overlapping monitor geometries
  * [GTK+3.20] Switch to GdkSeat
  * Set input purpose for the password entry widget
  * copy theme dialog：fix build warning about wrong variable type
  * 更新翻译

### mate-media 1.20.0

  * gvc-applet：don't try to increase refcount of a NULL object
  * gvc-combo-box：fix signal arguments
  * applet：restore icon for "Sound Preferences" menu item
  * 避免使用过时的 `gdk_screen_get_height`
  * applet：use GdkSeat with GTK+ >= 3.20
  * applet：make keyboard work in popup
  * gtk 3.22：避免使用过时的 `gdk_screen_get_monitor`... functions：
  * refresh tray icon on icon theme change
  * mixer-dialog：remove style class .frame from a scrolledwindow
  * volume-control-dialog：避免使用过时的 GtkAlignment
  * applet：show volume in popup even when muted
  * applet：improve volume increments
  * enable deprecation warnings by default
  * 更新翻译

### mate-power-manager 1.20.0

  * 避免使用过时的 GtkStock
  * inhibit：fix error that spammed logs from previous commit
  * inhibit applet：修复图标渲染问题
  * 实现 WidthOfScreen 和 HeightOfScreen
  * 修正注释中的拼写错误
  * 修正拼写错误
  * gtk 3.22：避免使用过时的 `gdk_screen_get_monitor` 函数
  * 不在收到未知的 DBus 信号时中止程序
  * 避免使用过时的 `gdk_screen_get_width/height`
  * 避免使用过时的 `gdk_display_get_screen`
  * 不使用过时的 `gtk_show_uri`
  * 在图标主题发生变化时刷新托盘图标
  * 检查 `$XPROTO_REQUIRED` 变量的值
  * statistics UI：add style class mpm-statistics
  * 更新翻译

### mate-system-monitor 1.20.0

  * procman.cpp：修复编译器警告：argument 1 null where non-null expected
  * sysinfo.cpp：修复编译器警告：this ‘if’ clause does not guard...
  * proctable.cpp：修复编译器警告：this ‘else’ clause does not guard...
  * Fix system logo alignment
  * 实现 WidthOfScreen 和 HeightOfScreen
  * process table：make search case-insensitive
  * sysinfo：disable focus in all labels
  * 避免使用过时的 `gdk_screen_width/height`
  * sysinfo：避免使用过时的 GtkAlignment
  * 更新翻译

### atril 1.20.0

  * build：remove pre-GTK+3 option
  * epub：make minizip support more BSD variants
  * previewer：add style class atril-previewer-window
  * 实现 WidthOfScreen 和 HeightOfScreen
  * shell：show caret navigation in menu
  * ev-link-accessible：Improve efficiency of methods to get start and end indices
  * Expose form fields as AtkObject children of the page
  * Expose images as AtkObject children of the page
  * Expose links as AtkObject children of the page
  * ev-view-accessible：Add a method to determine if a given doc rect is showing
  * ev-page-cache：Add method to check if a given page has been cached
  * libview：Update the caret cursor when jumping to a find result
  * libview：Update `ATK_STATE_SHOWING` when the visible page range changes
  * libview：Implement AtkComponent for pages
  * libview：Fix shift+click text selection
  * a11y：ensure text cached when you request an EvPageAccessible
  * a11y：managing atk states on EvPageAccessible
  * a11y：add if applies ATK_RELATION_FLOWS_TO/FROM on EvPageAccessible
  * a11y：move AtkHyperText implementation from EvViewAccessible to EvPageAccessible
  * a11y：move AtkText implementation from EvViewAccessible to EvPageAccessible
  * a11y：expose EvPageAccessible as children of EvViewAccessible
  * a11y：new EvPageAccessible
  * libview：Fix some broken aspects EvViewAccessible text support
  * libview：Take caret navigation into account when getting AtkHyperlink indices
  * a11y：cleaning implementation for `atk_text_get_caret_offset`
  * a11y：fixing implementation for `atk_text_set_caret_offset`
  * view：set_caret_cursor_position should emit "cursor-moved" if applies
  * Remove support for deprecated `atk_text_get_text_{before,after}_offset()`
  * a11y：implement AtkDocument on EvViewAccessible
  * a11y：with caret navigation enabled, accessibility current page is cursor page
  * ev-view-accessible：call `document_changed_cb` when setting the model
  * Some text fixes for caret message area
  * ev-view-accessible：Fix a crash in `ev_view_accessible_get_link`
  * ev-view-accessible：Clear the cached data when the current page
  * shell：remove `view_actions_focus_out_cb`
  * shell：Remove `ev_window_set_view_accels_sensitivity`
  * shell：forward accels to the focused widget
  * Use a global array for view accel action
  * fix crash when selecting text in djvu documents
  * shell：fix stock item for message area
  * 文档：libview：Re-add type builtins section
  * Fix crashes of epub documents with caret-navigation
  * Store the caret cursor position in document metadata
  * libview：Add `ev_view_set_caret_cursor_position`
  * libview：Update the current page also when pending scroll is to find a location
  * libview：Do not schedule a redraw when enabling/disabling caret navigation
  * libview：Stop caret cursor blinking when cursor is not in a visible page
  * shell：Enable/disable the caret navigation with F7
  * libview：Add `ev_view_supports_caret_navigation()`
  * ev-link-accesible：Return the index/offset after the last character in the link
  * help：Remove references to removed selection mode
  * libview：Fix selections starting/ending in page margins
  * libview：Reduce the pages to scan for selections
  * libview：Remove unused rectangle selection mode
  * libview：Rework ev_view_accessible_get_selection
  * libview：do not redraw the whole view when caret cursor moves
  * libview：Update the cursor area after positioning the cursor when moving between lines
  * ev-view-accessible：Fix `ev_view_accesssible_get_n_selections`
  * ev-view-accessibl：Fix get_caret_offset when the caret navigation is enabled
  * libview：Use error bell and return early when moving between lines fails
  * libview：do not schedule a resize in `ensure_rectangle_is_visible`
  * libview：Stop the cursor blink when there are selections active
  * libview：Deprecate ev_view_scroll in favor of `g_signal_emit_by_name`
  * ev-window：Use g_signal_emit_by name instead of `ev_view_scroll`
  * previewer：Remove scroll accelerators
  * ev-window：Remove scroll accelerators
  * libview：Add more scroll key bindings to EvView
  * libview：Fix second parameter type of scroll signal for h, j, k and l bindings
  * libview：Use merge_selection_region passing NULL to clear the selections
  * ev-pixbuf-cache：Clear the selection region also when clearing the job selection
  * ev-pixbuf-cache：fix the condition for when a new selection is needed
  * ev-view-accessible：Rewrite get_run_attributes to return the text attributes from the document
  * pdf：Implement `ev_document_text_get_text_attrs()`
  * libview：Get text attributes from backend and save them in page cache
  * libdocument：Add `ev_document_text_get_text_attrs()`
  * libview：Emit the AtkText text-caret-moved and text-selection-changed signals
  * libview：clear the selection when cursor is moved
  * libview：Do not show the caret cursor when there are active selections
  * libview：Return NULL instead of empty regions from the pixbuf cache
  * libview：Don't draw the caret cursor when the view is not focused
  * libview：Fix moving caret cursor between lines in multicolumn documents
  * libview：Pre-cache some prev/next pages to the current page range.
  * ev-pixbuf-cache：schedule prev or next jobs first depending on the scroll direction
  * ev-pixbuf-cache：Schedule jobs to render previous pages in inverse order
  * libview：Added 'cursor-moved' signal to notify when the caret cursor has been moved.
  * libview：Avoid unnecessary region copies when selecting text
  * libview：Use a larger damage area to redraw selections
  * libview：Don't queue a redraw when damaged region hasn't changed
  * libview：Invalidate union of old and new selection
  * libview：Move the caret cursor when clicking outside a selection
  * libview：Remove unused in_selection member from SelectionInfo struct
  * libview：Keep the offset inside a line when moving the caret between lines
  * libview：Position the caret cursor at beginning/end of the line
  * libview：Do not schedule a redraw when selecting all text
  * libview：Use prepend + reverse instead of append to create selections  list
  * libview：Use GSlice to allocate EvViewSelection
  * libview：Text selection using the caret cursor.
  * libview：Update the caret cursor after selecting text with the mouse
  * libview：Take page border into account when computing selections
  * libview：Fix a crash when selecting more than one page
  * libview：Make sure the cursor blinks after moving it by a click
  * libview：merge `get_caret_cursor_rect_from_offset` and `get_caret_cursor_area`
  * libview：Notify about caret navigation errors using the error bell.
  * libview：Do not redraw after a click if cursor position hasn't changed
  * libview：Use GtkBindings for caret navigation
  * libview：Rename EvView：：binding-activated signal as EvView：：scroll
  * libview：Position the caret cursor by clicking
  * libview：Use `EvPixbufCache` to find selection region
  * libview：Split `ev_pixbuf_cache_get_selection_surface` into two functions
  * libview：Draw selection highlight from region
  * libview：Fix the damage area used to redraw the caret cursor
  * libview：Actually update the page when moving the care from a different page
  * libview：Avoid to update the current page and scroll to the cursor position, if the caret cursor was not updated
  * libview：Make caret cursor blink
  * libview：Use logical attributes instead text layout to move the caret cursor
  * libview：Add a way to get the text logical attributes from the page cache
  * libview：Initial implementation of caret navigation
  * libview：Refactor code for drawing page and selection surfaces
  * shell：disable `ViewDualOddLeft` in menus for epubs
  * libview：only access the relevant page cache for the height request
  * Activate shortcut keys for dual and continuous layout
  * ev-view：Forward key events to the focused form field
  * Add shortcut keys for fit-page and fit-width options
  * shell：Do not open single page pdfs in dual mode by default
  * libview：Don't update current_page to negative number
  * libview：Make page layout a mode
  * libview：Add new zoom mode that optimizes for readability
  * Rename Fit Page Width as Fit Width
  * Rename Best Fit mode as Fit Page
  * Move dual page with odd pages left to the view menu
  * libview：drop deprecated usage of gtk_container_set_resize_mode
  * shell：Check if doc implements Annotations interface before cast
  * Refreshing annotations' sidebar upon deletion
  * libdocument：Make `ev_mapping_list_remove` void
  * page-cache：Add flags parameter to `ev_page_cache_mark_dirty()`
  * pdf：Reset the annotation mapping when there are no more annotations
  * Add an option to remove annotations to the view popup menu
  * libview：add ev_view_remove_annotation
  * pdf：Implement remove_annotation virtual func
  * libdocument：add ev_mapping_list_remove
  * libdocument：Add remove_annotation to DocumentAnnotations.
  * pdf：Make annotation names unique
  * pdf：Add support for adding other types of annotations
  * libview：Rename ev_view_set_focused_element and make it public internally
  * Change the opacity of the annotation window
  * Change color of annotation window
  * libview：Grab focus for form fields and links on mouse press
  * libdocument：Added `ev_mapping_list_get`
  * pdf：Add activation link for Fields that have it.
  * libview：Handle activation link of a Form Field  if present
  * libdocument：Add activation_link to EvFormField struct
  * ev-properties-licence：不使用过时的 GtkAlignment
  * libview：：避免使用过时的 gtk_adjustment_changed
  * ev-job-find：mark two methods as skip
  * ev-jobs：have `ev_job_failed_from_error` shadow `ev_job_failed`
  * libview：add missing transfer and element-type annotations
  * ev-mapping-list：make a boxed type
  * libdocument：add missing transfer and element-type annotations
  * gtk 3.22：避免使用过时的 gdk_screen_get_monitor... functions：
  * avoid `gdk_screen_get_primary_monitor/gdk_screen_get_monitor_scale_factor`
  * ev-document-misc.c：避免使用过时的 `gdk_screen_get_width/height_mm`
  * dvi：Mitigate command injection attacks by quoting filename
  * mdvi-lib：Fix compilation warning (const-correctness)
  * libmisc：set width chars for page label
  * libview：Scroll small pages in non-continuous mode
  * libview：Enable `GDK_SMOOTH_SCROLL` events for view
  * libview：Ctrl+mouse wheel zoom should be pointer-centered, not window-centered
  * ev-view：Add pan gesture to switch page
  * ev-view：explicitly require a `GtkScrolledWindow` as the parent widget
  * ev-view：Add pinch/zoom gesture to handle document zooming
  * sidebar-thumbnails：fix unwanted move to start after fullscreen
  * sidebar-thumbnails：preload one extra visible range while scrolling
  * sidebar-thumbnails：keep thumbnails already rendered
  * sidebar-thumbnails：fix clunky scrolling
  * annotations-sidebar：Clean up the styling
  * ev-annotation-window：Fix setting the color of the window border
  * libview：fix annotation window focus change after creation
  * libview：Fix focus on ev_annotation_window
  * libview：Don't change the font color of the annotation window
  * shell：Use GdkRGBA for annotations
  * libdocument：Add EvAnnotation API using GdkRGBA
  * libdocument：Use the new deprecation macros
  * Add deprecation macros
  * fix runtime warnings caused by previous HDPI commit
  * Take monitor scale factor into account when calculating zoom.
  * Add hi-dpi support for main view.
  * shell：Ditch gimpcellrenderertoggle
  * sidebar-layers：Make it actually usable and fix a runtime warning
  * libview：setting annotation window icons sizes
  * libview：save changes to a dropdown in an embedded form
  * libdocument：adjust rendering of shadow for active and inactive pages
  * 避免使用过时的 `gdk_screen_make_display_name`
  * ev-window：remove deprecated `GtkToolbar-shadow-type`
  * annotation-properties-dialog：don't use a headerbar
  * 避免使用过时的 `gdk_display_get_screen` and `gdk_display_get_n_screens`
  * ev-window：不使用过时的 `gtk_show_uri`
  * 避免使用过时的 `gdk_screen_get_number`
  * build：properly clean the generated .caja-extension file
  * build：require cairo >= 1.10.0 and drop some old code
  * shell：remove unused code from utils
  * ev-view：避免使用过时的 `gtk_drag_begin`
  * egg-editable-toolbar：避免使用过时的 `gtk_drag_begin`
  * message-area：replace some `GtkStock` deprecations
  * ev-sidebar：避免使用过时的 `GTK_STOCK_CLOSE` icon
  * password-view：replace some `GtkStock` deprecations
  * password-view：不使用过时的 `GtkAlignment`
  * toolbar-editor：不使用过时的 `GtkAlignment`
  * 更新翻译

### caja-extensions 1.20.0

  * xattr-tags：use better English in extension description
  * po：add missing translatable strings from xattrs extension
  * xattr-tags：fix extension description
  * open-terminal：don't use excessive string duplication
  * 避免使用过时的 `gdk_screen_make_display_name`
  * sendto burn：避免使用过时的 `gtk_show_uri`
  * xattr-tags：remove hack, it's not needed now
  * xattr-tags：fix typo causing undefined reference
  * fix the `libcaja_gksu_la_LDFLAGS` variable declaration
  * xattr-tags：add missing newline to startup message
  * xattr-tags：unescaping stored attributes.
  * 更新翻译

### engrampa 1.20.0

  * build：use `PKG_CONFIG` to fix cross-build
  * Add our copyright to About dialog and Caja extension
  * 7z：修正：rename files with password without the list encrypted
  * 7z：修正：delete/rename files/folders with the list encrypted
  * 避免使用过时的 `gdk_screen_make_display_name`
  * 不使用过时的 `gtk_show_uri`
  * 使用更常用的 gtk+ 函数
  * 避免使用过时的 `gdk_screen_get_number`
  * Add the button "Show the Files and Quit" in the progress dialog
  * 修正：create zip files in "maximum" compression level
  * 修正：Browsing history not correct
  * hide folders in "View All Files"
  * 修正：Wrong behavior of Skip button in Replace file dialog
  * UI files：避免使用过时的函数
  * gtk-utils：remove some `GTK_STOCK` deprecations
  * gtk-utils：避免使用过时的 gtk_icon_size_lookup_for_settings
  * fr-window：fix some `GTK_STOCK` deprecations
  * add style class frame to scrolledwindows
  * fr-window：避免使用过时的 `GtkMisc` and `GtkAlignment`
  * dlg-add-folder：避免使用过时的 `gtk_alignment_new()`
  * build：use variable instead of hardcoded file name when cleaning
  * 更新翻译

### eom 1.20.0

  * drop CSS for GTK+ 3.18
  * egg-editable-toolbar.c/egg-toolbars-model.c：删除未使用的变量
  * print-preview：replace custom code with GDK function call
  * gtk 3.22：避免使用过时的 `gdk_screen_get_monitor` functions：
  * 不使用过时的 `gtk_show_uri`
  * 避免使用过时的 `gdk_screen_get_number`
  * fix warning on closing empty window with multiple eom windows
  * EomThumbView：Replace deprecated `gtk_menu_popup` function
  * multiple-save-as-dialog.ui：避免使用过时的 widgets
  * error-message：replace usage of GtkStock
  * A bunch of instrospection warning fixes
  * EomScrollView：fix override_background deprecated call
  * EomPropertiesDialog：Fix deprecation warnings
  * EomThumbNav：Fix deprecated function warning
  * EomScrollView：Replace deprecated `gtk_menu_popup` function
  * EomScrollView：Switch from GtkDeviceManager to GdkSeat
  * fix typo in function annotation
  * use different css files for < gtk+=3.20
  * EomWindow：Set file open dialog transient for its parent window
  * settings：use rgb color definition as defaults
  * UI：avoid using deprecaded widgets
  * EomCloseConfirmationDialog：set max width chars for primary label
  * EomCloseConfirmationDialog：Fix size request for the image list
  * Printing paper orientation should default based on image dimensions
  * Avoid recompressing JPEGs as PNG when printing
  * EomFileChooser：Use MateThumbnailFactory to create preview image
  * EomPropertiesDialog：Allow RGBA for transparent background color
  * preferences-ui：drop usage of `MateColorButton`
  * EomScrollView：Switch to `GdkRGBA` for background and transparent colors
  * EomPrintPreview：Avoid unnecessary color parsing
  * Fix a few GtkStock deprecations
  * EomCloseConfirmationDialog：replace deprecated `GTK_STOCK_DIALOG_WARNING`
  * toolbar-editor：避免使用过时的 GtkAlignment
  * Bring eom-image.c's SVG handling up to date, properly recognize svgz filetypes
  * eom_uri_converter：GList leak fix
  * 更新翻译

### mate-applets 1.20.0

  * multiload：使用用户定义的阈值缩放网络图表
  * multiload：修复空格/缩进符混用
  * multiload：修复空格数量
  * multiload：移除不必要的空格
  * weather：修复打开首选项对话框时可能发生的崩溃
  * 移除“投资”挂件及所有 Python 依赖
  * 修复构建警告：忽略 `fgets` 的返回值
  * command：提高间隔调整区间
  * 实现 WidthOfScreen 和 HeightOfScreen
  * build：找不到 gtksourceview 时显示此包名
  * Cpufreq：根据最新数值更新工具提示
  * Cpufreq：修复一个构建警告
  * Cpufreq：阻止数值变化时移动单位文字标签
  * 修复绘制时的约数错误
  * cpufreq：修复频率/单位/百分比标签的最大宽度计算
  * stickynotes：修复文字选中
  * cpufreq：在样式更改（例如字体大小）时刷新挂件大小
  * 动态识别 GSettings 更改
  * 用于调整已挂载卷的显示颜色的 GSettings 键值
  * cpufreq：修复挂件随机隐藏的问题
  * 为已挂载的卷使用不同的图标
  * gtk 3.22：避免使用过时的 `gdk_screen_get_monitor` 函数
  * 修复构建时的 misleading_indentation 及 maybe-uninitialized 警告
  * 避免使用过时的 `gdk_screen_width/height`
  * 避免使用过时的 `gdk_screen_get_width/height`
  * 所有挂件：不使用过时的 `gtk_show_uri`
  * 新增“数字”主题
  * drivemount：修复构建警告
  * cpufreq-prefs：不使用过时的 `gtk_show_uri`
  * 提高 libmateweather 版本要求到 1.19.1
  * weather：一旦位置改变，中止一切未完成的天气更新
  * weather：添加在上次天气数值一致时不通知天气信息的逻辑
  （使用 `weather_info_equal()` 探测）
  * 避免使用过时的 `gdk_screen_get_number`
  * drivemount：在列表为空时显示 media-floppy 图标
  * stickynotes：改写上一个提交信息且不要泄漏目录名称
  * stickynotes：为 `stickynotes-applet.xml` 按需创建上级目录
  * 基于负载均衡自动缩放负载图表
  * trashapplet：删除死代码
  * cpufreq：为所有 CPU 核心设置频率
  * 修正 GError 的内存泄漏
  * 修复“命令”挂件中的崩溃
  * 更新翻译

### mate-calc 1.20.0

  * 为首选项对话框中的关闭按钮添加图标
  * 避免使用过时的 GtkStock
  * 添加缺失的关于对话框窗口图标
  * math-window：不使用过时的 `gtk_show_uri`
  * 更新翻译

### mate-icon-theme-faenza 1.20.0

  * 根据原项目的变更将许可证调整为 GPL3
  * 修复暗色主题下的 MATE 图标

### mate-indicator-applet 1.20.0

  * 支持基于 Ayatana Indicator 及 Ubuntu Indicator 构建
  * 更新翻译

### mate-netbook 1.20.0

  * 实现 WidthOfScreen 和 HeightOfScreen
  * 窗口选择器：在析构函数中解除信号处理器
  * 窗口选择器：在首选项对话框增加图标
  * 窗口选择器：在设置对话框中禁用按钮的纵向放大
  * 窗口选择器：为关于对话框新增任务栏图标
  * maximus：不要在出现无效窗口 ID 时崩溃
  * 更新翻译

### mate-sensors-applet 1.20.0

  * build：使用 udisks2 插件
  * 移除过时的 udisks 插件
  * udisks 插件：修复 GValue 变量的内存管理
  * 移除过时的 eee 插件
  * 修复已删除硬盘的弹出消息
  * ibm-acpi.c：修复编译器警告：
  * eee-plugin.c：修复编译器警告：
  * active-sensor.c：修复编译器警告：
  * sensors-applet.c：修复编译器警告：
  * 清理代码缩进
  * 清理项目
  * 阻止挂件在数值改变时四处移动
  * 修复传感器的保存顺序
  * 更新隐藏的温度单位
  * 移除重复代码
  * sensor-applet.c：替换过时的 GtkMisc
  * sensor-applet.c：避免使用过时的 `GTK_STOCK_MISSING_IMAGE`
  * sensor-config-dialog：避免使用过时的 GtkAlignment
  * sensor-config-dialog：不使用过时的 GtkColorButton
  * prefs-dialog：向 scrolledwindow 添加了样式类框架
  * prefs-dialog：避免使用过时的 GtkAlignment
  * prefs-dialog：避免使用过时的 `GTK_VBUTTON_BOX`, `GTK_TYPE_{H,V}BOX`
  * 为 `sensor_applet` 使用 `GTK_ALIGN_CENTER`
  * 更新翻译

### mate-terminal 1.20.0

  * 要求 VTE 0.46
  * screen：不再设置 `TERM` 和 `COLORTERM` 环境变量
  * schema：修正一些键值的简介和详细描述
  * 从“查找”键盘快捷键删除“…”
  * profile-editor：正确初始化第一个调色板颜色
  * terminal-screen.c：删除未使用的变量
  * 修正构建警告：忽略 `chdir` 的返回值,
  * 在标签上按下鼠标中键：向 gsettings 添加了键值以启用此功能
  * 统一化一些文件中的缩进
  * 修正处理 DBus 方法调用时可能产生的崩溃问题
  * 拼写：删除终端中 Ctrl 生成的空白
  * 添加来自 GNOME 终端的 Solarised 主题
  * 实现 WidthOfScreen 和 HeightOfScreen
  * 添加 <kbd>ctrl</kbd> + <kbd>tab</kbd> 及 <kbd>ctrl</kbd> +
  <kbd>shift</kbd> + <kbd>tab</kbd> 作为切换标签页的组合键
  * 允许重新映射“搜索”快捷键
  * 支持 VTE3 背景图片
  * find-dialog.ui：修复键盘选择
  * 避免使用过时的 `vte_terminal_search_get_gregex`
  * 添加 "全选" 动作的热键t：<kbd>control</kbd> + <kbd>shift</kbd> + <kbd>A<kbd>
  * gtk 3.22：避免使用过时的 `gdk_screen_get_monitor` 函数
  * 避免使用过时的 `gdk_screen_get_width/height`
  * 避免使用过时的 `gdk_screen_make_display_name`
  * terminal-util：avoid `deprecated gtk_show_uri`
  * 避免使用过时的 `gdk_display_get_screen`
  * 避免使用过时的 `gdk_screen_get_number`
  * 修正：双击右键导致 Xorg 崩溃
  * 更新翻译

### mate-user-share 1.20.0

  * 构建：使用正确的宏以避免交叉编译的问题
  * 不使用过时的 `gtk_show_uri`
  * 更新翻译

### mate-utils 1.20.0

  * 添加对高解析度 (HiDPI) 显示器的截图支持
  * mate-screenshot：添加“新建”按钮
  * screenshot-save.c：修正由 `pipe` `write` 和 `read` 导致的警告：
  * 添加样式类 logview-window
  * 更新翻译
  * 实现 WidthOfScreen 和 HeightOfScreen
  * baobab：使鼠标滚轮能在图表上控制缩放
  * screenshot：移除一些死代码
  * screenshot：不要获取窗口标题，因为之后不会用到
  * baobab/logview/dictionary：向“关于”菜单添加我们的版权信息
  * baobab：为远程连接对话框设置临时父窗体
  * baobab：不要在 .ui 文件中使设置对话框可见
  * baobab：为“关于”对话框设置父窗口
  * 避免使用过时的 `gdk_screen_get_active_window`
  * gtk 3.22：避免使用过时的 `gdk_screen_get_monitor` 函数
  * 避免使用过时的 `gdk_screen_width/height`
  * 避免使用过时的 `gdk_screen_get_width/height`
  * screenshot：避免使用过时的 GdkDevice 对象
  * dictionary：避免使用过时的 GdkDevice 对象
  * 避免使用过时的 `gdk_screen_get_n_monitors`
  * 避免使用过时的 `gdk_screen_make_display_name`
  * gdict-applet：不使用过时的 `gtk_show_uri`
  * 不使用过时的 `gtk_show_uri`
  * 避免使用过时的 `gdk_screen_get_number`
  * searchtool 及 logview：避免使用过时的 GtkAlignment
  * mate-screenshot：修复在保存区域截图时的“忙”光标
  * screenshot：不翻译文件名中的时间戳
  * mate-dictionary：包含正确的头文件以避免构建失败
  * 更新翻译

### mozo 1.20.0

  * 更新翻译

### pluma 1.20.0

  * 把 `peas_engine_enable_loader` 放在正确的位置
  * 修正：修复最近使用的文件列表
  * 删除未使用的变量
  * pluma-spell-checker-language.c：修复编译器警告：
  * pluma.c：修复编译器警告：
  * pluma-document.c：修复编译器警告：
  * pluma-window：将 GtkRecentData 分配在栈上而不是堆上
  * WidthOfScreen 及 HeightOfScreen 实现
  * 修正带有反向引用的正则表达式替换操作（例如：`"\0"`）
  * pluma-view.c：减少一个静态变量来实现同样的功能
  * 确保 Pluma 于同一工作区下的窗口中打开
  * 修正：Pluma 在按下 [右 + 中] 键及 <kbd>ctrl</kbd> + <kbd>+</kbd> /
  <kbd>ctrl</kbd> + <kbd>-</kbd>（数字小键盘）时未预期地关闭标签页
  * 添加 gsettings 键值：在文件存在更改时显示保存提示框
  * 修正：使用 [右 + 中] 键及 <kbd>ctrl</kbd> + <kbd>+</kbd> /
  <kbd>ctrl</kbd> + <kbd>-</kbd> 调整字体大小时行为不正确
  * 不要在文档没有更改时提示保存
  * 添加 gsettings 键值以使用侧边栏隐藏/显示（默认）标签页
  * 在使用侧边栏时隐藏标签页
  * gtk 3.22：避免使用过时的 `gdk_screen_get_monitor` 函数
  * 避免使用过时的 `gdk_screen_get_width/height`
  * 避免使用过时的 `gdk_screen_make_display_name`
  * pluma-help：不再使用 `deprecated gtk_show_uri`
  * filebrowser：不再使用 `deprecated gtk_show_uri`
  * 避免使用过时的 `gdk_display_get_screen` 及 `gdk_screen_get_number`
  * 添加保存文档外部更改的功能
  * 禁用文档无更改时保存的功能
  * print-preferences UI：替换一些基本的过时函数
  * encoding-dialog UI：替换一些基本的过时函数
  * preferences-dialog UI：替换一些基本的过时函数
  * pluma-panel：移除过时的 GtkImage 类型
  * plumal-panel：移除一些过时的 GtkStock 函数
  * search-dialogs：修复 -Wpointer-compare 警告
  * tag-list-plugin：避免使用过时的 GtkStock
  * file-browser-widget：移除一个过时的 GtkStock 函数
  * configure：删除 `GLIB_VERSION_MAX_ALLOWED`
  * File browser：不再使用 GIOScheduler（已过时）
  * file-browser-view：修复一些构建警告
  * pluma-view：避免使用过时的 GtkStock 函数
  * pluma-tab：替换了一些 GtkStock 图标
  * pluma-notebook：不使用过时的 `gdk_cursor_new`
  * progress-message-area：移除一个过时的 GtkStock 函数
  * io-error-message-dialog：修复一些 GtkStock 过时警告
  * 修正：Pluma 在按下中键时未预期地退出
  * pluma-notebook.c：修复构建警告
  * 在最近使用的标签页右侧双击以新建标签页
  * 支持新的 GTK+ 书签文件位置
  * 文档：Pluma 现在使用编码组合框而不是选项菜单
  * 移除对 PlumaStatus 的引用
  * 文档：删除一些对不存在对象的引用
  * filebrowser：不要解析 .hidden 隐藏文件 - GIO 从 2.36 就这么做了
  * 关闭确认框：启用文本选择 + 禁用所有标签的焦点
  * 关闭确认框：设置标签组件的最大宽度
  * 修正代码注释中的拼写错误
  * 修正在 Wayland 下运行的问题
  * modelines：修复在有多个 Pluma 窗口的情况下，关闭一个窗口会导致随机崩溃的问题
  * 更新翻译

### python-caja 1.20.0

  * 更新翻译
