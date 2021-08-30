<!--
.. link:
.. description:
.. tags: Releases
.. date: 2021-08-10 09:00:00
.. title: MATE 1.26 released
.. slug: 2021-08-08-mate-1-26-released
.. author: Johannes Unruh
-->

This release might have taken a little longer than usual but now after 18 month of development we are very pleased to release MATE 1.26. A big thank you to all contributors who helped to make this happen.

![MATE About dialog](/assets/img/blog/about-mate-1.26.ja.png)

## What's new in MATE 1.26

The theme for this release has been adding new functionality to the MATE Desktop while maintaining the look and feel that we all know and love. While all the added features are surely quite exciting we also did not forget to do tons of bugfixing, modernising the code base and optimizing the performance.

The headline changes in MATE Desktop 1.26 are:

* We added [Wayland](https://wayland.freedesktop.org/) support for Atril, System Monitor, Pluma, Terminal and other components of the Desktop. Furthermore Calculator and Terminal can now be built with [Meson](https://mesonbuild.com/).
* **Pluma** was subject to massive improvements.
    * There is a **new mini map** which gives you instant overview over the content.
    * The **new grid background pattern** turns Pluma into a writing pad.
    * The sort plugin now supports undo actions.
    * We added a show/hide line-numbers shortcut, namely <kbd>Ctrl</kbd> + <kbd>Y</kbd>.
    * The preferences dialog needed a redesign to catch up with all the new features.
* Together with the brand new **Pluma Plugins** our text editor **can be turned into a feature-rich IDE** with support for *Bracket completion*, *Comment/Uncomment code*, *Built-in terminal* and *Word completion*.
* The **Control Center** features an improved Windows preferences dialog with more options. In the Display dialog we added an option for display scaling.
* Notifications became even more useful as they gained support for hyperlinks. And we finally **added a Do not Disturb applet**.
* Speaking of applets, the Window List applet has a new option to disable mouse scrolling. The optional window thumbnails are now **crisp and clear as they are rendered as cairo surfaces**.
* The Netspeed applet shows more information by default and gained [netlink](https://www.man7.org/linux/man-pages/man7/netlink.7.html) support.
* The **Calculator** was ported to the [GNU MPFR](https://www.mpfr.org/)/[MPC](http://www.multiprecision.org/mpc) library which means more precision, faster computation and additional functions (e.g. Riemann zeta function, Gauss error function).
    * We finally **added a history to show recent computations**.
    * Calculator is now resizeable when the history is activated.
    * Vastly improved integer factorization speed.
    * Much faster modular arithmetic evaluation (modular exponentiation ability).
* In the file manager **Caja** you can select **a new Bookmarks sidebar**. Caja gained **support for formatting drives** from the context menu. The **Caja Actions** extension which allows you to add arbitrary programs to be launched through the context menu is now part of the Desktop.
* Scrolling through large documents in **Atril** is a lot faster now since a slow linear search has been replaced by a binary tree search. The document viewer's **memory footprint got even smaller** as a EvWebView is now only created if needed.
* The window manager **Marco** now restores minimized windows to its original position more reliable.
* **Engrampa** got support for Electronic Publication (EPUB) and ARC archives. In addition it can now open encrypted RAR archives.
* The **Power Manager** has a new option to enable keyboard dimming and has been ported to [libsecret](https://wiki.gnome.org/Projects/Libsecret).
* Most About dialogs have been updated with nicer descriptions. Because small things matter `:-)`.
* We fixed a lot of bugs, some memory leaks and modernised the codebase of almost all of the Desktop components.
* There is a new [Wiki](https://wiki.mate-desktop.org/) which makes it easier for new contributors to join our project. We urgently need motivated people so do not hesitate to [contact us](https://wiki.mate-desktop.org/introduction/contributing/) or [start contributing](https://wiki.mate-desktop.org/introduction/contributing/).
* Translations are updated. Thank you to our team of translators!

The various components of MATE Desktop 1.26 are available for download here:

  * <https://pub.mate-desktop.org/releases/1.26/>


## More details

Here are the gory details.

### atril
* Completely rewritten Help (make sure to visit the new synctex section if you write a lot of TeX files)
* ev-window.c: Only create a EvWebView if needed
* ev-sidebar-links: Optimize reverse link lookup for a page (the very slow linear search for links in the sidebar has been replaced by a search in a specalized binary tree)
* Add Wayland support
* Make sure attachments window fills entire sidebar
* Make synctex optional
* Fix segfault on empty navMap
* Fix several code analysis, deprecation warnings reported by Clang Static Analyzer, Cppcheck and GCC
* build: Add option to disable Native Language Support (NLS) (`--disable-nls`)
* g10n: Update the translations

Complete changelog at <https://github.com/mate-desktop/atril/commits/master/>

### caja
* You can now add information of the creation time in the list columns
* Add a setting to block lock icons position on the desktop
* Improved filesystem check on Drag and Drop
* You can now format drive in caja
* fm-properties-window: Make the location of system folders portable
* Middle-clicking the reload button duplicates tab
* Create links by default on dnd from Web Browsers
* Add a "Bookmarks" sidebar to Caja
* Support an explicit `--select` command line option
* Confirm before deleting during an undo operation
* Fix several code analysis, deprecation warnings reported by Clang Static Analyzer, Cppcheck and GCC
* Fix several memory leaks
* build: Add option to disable Native Language Support (NLS) (`--disable-nls`)
* g10n: Update the translations

Complete changelog at <https://github.com/mate-desktop/caja/commits/master/>

### caja-actions
* Makes its first appearance in this release
* i18n: Migrate from intltools to gettext
* Fix several code analysis, deprecation warnings reported by Clang Static Analyzer, Cppcheck and GCC
* g10n: Update the translations

### caja-dropbox
* Add i18n support
* g10n: Update the translations

Complete changelog at <https://github.com/mate-desktop/caja-dropbox/commits/master/>

### caja-extensions
* gksu: do not run the command on a new thread
* Require gtk+ 3.22 in glade files
* sendto: Fix evolution command for sending an email
* image-converter: rewrite caja-image-rotate.ui from scratch
* Fix several memory leaks
* build: Add option to disable Native Language Support (NLS) (`--disable-nls`)
* g10n: Update the translations

Complete changelog at <https://github.com/mate-desktop/caja-extensions/commits/master/>

### engrampa
* rar 6.00: Fix listing archive content with encrypted file list
* Add Electronic Publication (EPUB) support
* Add ARC archive support
* Fix several code analysis, deprecation warnings reported by Clang Static Analyzer, Cppcheck and GCC
* Fix several memory leaks
* build: Add option to disable Native Language Support (NLS) (`--disable-nls`)
* g10n: Update the translations

Complete changelog at <https://github.com/mate-desktop/engrampa/commits/master/>

### eom
* Upgrade ui files
* Ensure scrollbar moves when dragged to move image
* Add tab scrolling support for dialog windows
* Fix several code analysis, deprecation warnings reported by Clang Static Analyzer, Cppcheck and GCC
* build: Add option to disable Native Language Support (NLS) (`--disable-nls`)
* g10n: Update the translations

Complete changelog at <https://github.com/mate-desktop/eom/commits/master/>

### libmatekbd
* Reduce the font size of the key names on keyboard layout display
* g10n: Update the translations

Complete changelog at <https://github.com/mate-desktop/libmatekbd/commits/master/>

### libmatemixer
* alsa: Add udev support
* g10n: Update the translations

Complete changelog at <https://github.com/mate-desktop/libmatemixer/commits/master/>

### libmateweather
* Drop Berlin Tegel
* Add 2 brazil cities
* Update cities in Thailand
* g10n: Update the translations

Complete changelog at <https://github.com/mate-desktop/libmateweather/commits/master/>

### marco
* window: Add support for _GNOME_WM_STRUT_AREA
* screen: Add support for _GTK_WORKAREAS_Dn
* window: Do not render shadows on left/right tiled windows
* iconcache: Use GDesktopAppInfo to find correct application icons
* window: Track window rectangle before corner tiling
* window: Track window rectangle before tiling
* Added VI keys (hjkl) for moving and resizing windows
* window: Expand tile size cycling support
* In the pop-up workspace switcher, show the selected workspace
* Improve meson build script
* Fix several code analysis, deprecation warnings reported by Clang Static Analyzer, Cppcheck and GCC
* g10n: Update the translations

Complete changelog at <https://github.com/mate-desktop/marco/commits/master/>

### mate-applets
* netspeed: Allow to select an interface which is down
* netspeed: Show all ipv6 addresses in device details dialog
* netspeed: Show all IP addresses on tooltip if enabled
* multiload: Use bit rate in netload graph
* multiload: Increase refresh rate range setting
* battstat: Rewrite preference dialog from scratch
* multiload: Display the percentage used accurately on tooltip
* netspeed: Use IEC units for transfer rates
* netspeed: Add netlink support
* Fix several code analysis, deprecation warnings reported by Clang Static Analyzer, Cppcheck and GCC
* Fix several memory leaks
* g10n: Update the translations

Complete changelog at <https://github.com/mate-desktop/mate-applets/commits/master/>

### mate-backgrounds
* New 'Something slowly gets clear' elephants wallpaper
* g10n: Update the translations

Complete changelog at <https://github.com/mate-desktop/mate-backgrounds/commits/master/>

### mate-calc
* Port to GNU MPFR/MPC Library
* Add an optional history to show recent calculations
* With keyboard shortcuts to navigate through history (Alt+Up)/(Alt+Down)
* Make Calculator resizeable when history is activated
* Show exponents in prime factorization
* Vastly improve prime factorization speed
* To factorize integers bigger than 2^64 the Miller-Rabin primality test and Pollard's rho algorithm are used
* Much faster modular arithmetic evaluation (modular exponentiation ability)
* Add riemann zeta function, gauss error function, factorial function for real numbers
* Add meson build support
* Fix several code analysis, deprecation warnings reported by Clang Static Analyzer, Cppcheck and GCC
* Fix several memory leaks
* g10n: Update the translations

Complete changelog at <https://github.com/mate-desktop/mate-calc/commits/master/>

### mate-common
* g10n: Update the translations

Complete changelog at <https://github.com/mate-desktop/mate-common/commits/master/>

### mate-control-center
* windows-applet: New Show window border in Alt-Tab and Allow top tiling (Window-Snapping) option
* windows-applet: New compositing manager tab
* windows-applet: New titlebar layout option "left (with menu)" and "right" (without menu)
* Windows with client site decorations now respect the titlebar layout
* Fix preview in add wallpaper dialog
* Add file chooser options in the appearance dialogs interface section (the file chooser is the window that opens when opening or saving a file)
* Migrate some components from dbus-glib to GDBus
* Support tab-scrolling for the window and appearance dialog
* The Display applet gained an option for display scaling
* build: Add option to disable Native Language Support (NLS) (`--disable-nls`)
* Fix several code analysis, deprecation warnings reported by Clang Static Analyzer, Cppcheck and GCC
* Fix several memory leaks
* g10n: Update the translations

Complete changelog at <https://github.com/mate-desktop/mate-control-center/commits/master/>

### mate-desktop
* a11y-keyboard: Add capslock-beep-enable gsetting
* Set range for thumbnail cache maximum-age
* Remove GTimeVal deprecation warning for GLib 2.61.2+
* Fix several code analysis, deprecation warnings reported by Clang Static Analyzer, Cppcheck and GCC
* g10n: Update the translations

Complete changelog at <https://github.com/mate-desktop/mate-desktop/commits/master/>

### mate-icon-theme
* Remove the execution bit from some png files
* g10n: Update the translations

Complete changelog at <https://github.com/mate-desktop/mate-icon-theme/commits/master/>

### mate-indicator-applet
* applet-main: Replace GtkStock icon
* g10n: Update the translations

Complete changelog at <https://github.com/mate-desktop/mate-indicator-applet/commits/master/>

### mate-media
* Replace mute/unmute checkmenuitem with imagemenuitem
* panel-applet: Ensure speaker can be shown alongside or above mic
* Fix several code analysis, deprecation warnings reported by Clang Static Analyzer, Cppcheck and GCC
* g10n: Update the translations

Complete changelog at <https://github.com/mate-desktop/mate-media/commits/master/>

### mate-menus
* Add collection menu item
* build: Add option to disable Native Language Support (NLS) (`--disable-nls`)
* g10n: Update the translations

Complete changelog at <https://github.com/mate-desktop/mate-menus/commits/master/>

### mate-netbook
* mate-window: Replace GtkStock icons
* mate-maximus-autostart.desktop: Remove the deprecated Encoding key
* g10n: Update the translations

Complete changelog at <https://github.com/mate-desktop/mate-netbook/commits/master/>

### mate-notification-daemon
* Add Do Not Disturb Applet
* Add initial Wayland backend
* Add support for hyperlinks in the body of a notification
* Rewrite mate-notification-properties.ui from scratch
* Fix several code analysis, deprecation warnings reported by Clang Static Analyzer, Cppcheck and GCC
* Fix several memory leaks
* build: Add option to disable Native Language Support (NLS) (`--disable-nls`)
* g10n: Update the translations

Complete changelog at <https://github.com/mate-desktop/mate-notification-daemon/commits/master/>

### mate-panel
* workspace-switcher: Support xmonad WM
* Make Recent Documents list in Places menu of configurable length
* Add window list disable mouse scrolling option
* Add text label display support for notification area
* window-list: Render thumbnails as cairo surfaces
* Drop background compositing
* Window list Wayland support
* Redesign preferences dialog for window-list applet
* Fix adding applications launchers to panel when using the Add to Panel dialog
* Fix several code analysis, deprecation warnings reported by Clang Static Analyzer, Cppcheck and GCC
* Fix several memory leaks
* g10n: Update the translations

Complete changelog at <https://github.com/mate-desktop/mate-panel/commits/master/>

### mate-polkit
* g10n: Update the translations

Complete changelog at <https://github.com/mate-desktop/mate-polkit/commits/master/>

### mate-power-manager
* mate-power-preferences: Add option to enable keyboard dimming
* Switch default from libgnome-keyring to libsecret
* brightness applet: Prevent sliding from bogging down the UI
* Port from EggDebug to the built-in GLib logging framework
* Rewrite gpm-prefs.ui from scratch
* Remove the CPU wakeups feature
* Add some missing SVG files
* Fix several code analysis, deprecation warnings reported by Clang Static Analyzer, Cppcheck and GCC
* Fix several memory leaks
* g10n: Update the translations

Complete changelog at <https://github.com/mate-desktop/mate-power-manager/commits/master/>

### mate-screensaver
* Allow change of time and date formats on lock screen
* Add Show/Hide password emblem in password entry
* mate-screensaver-preferences: Show lock image preview on file chooser
* Fix several code analysis, deprecation warnings reported by Clang Static Analyzer, Cppcheck and GCC
* Fix several memory leaks
* g10n: Update the translations

Complete changelog at <https://github.com/mate-desktop/mate-screensaver/commits/master/>

### mate-sensors-applet
* Drop aticonfig plugin
* sonypi-plugin.c: Make sonypi plugin portable to GNU/Hurd
* libsensors-plugin: Port to GRegex
* g10n: Update the translations

Complete changelog at <https://github.com/mate-desktop/mate-sensors-applet/commits/master/>

### mate-session-manager
* Follow freedesktop guidelines to disable autorun using Hidden key
* Support xscreensaver when mate-screensaver is not available
* Add tab scrolling support for GTK3
* Accept Desktop Entry Specification v1.1
* Fix several code analysis, deprecation warnings reported by Clang Static Analyzer, Cppcheck and GCC
* Fix a memory leak
* build: Add option to disable Native Language Support (NLS) (`--disable-nls`)
* g10n: Update the translations

Complete changelog at <https://github.com/mate-desktop/mate-session-manager/commits/master/>

### mate-settings-daemon
* xsettings: Improve Qt HiDPI environment settings
* a11y-keyboard: Add support for togglekeys-backend setting
* Add option --without-libatspi and assorted status line
* a11y-keyboard: Add support for ringing the bell when CapsLock is active
* Fix several code analysis, deprecation warnings reported by Clang Static Analyzer, Cppcheck and GCC
* Fix two memory leaks
* g10n: Update the translations

Complete changelog at <https://github.com/mate-desktop/mate-settings-daemon/commits/master/>

### mate-system-monitor
* Add Wayland support
* Port to GtkApplication
* pretty-table: Prefer GIO to get application icons
* Added support for actions on multiple processes
* Fix several code analysis, deprecation warnings reported by Clang Static Analyzer, Cppcheck and GCC
* g10n: Update the translations

Complete changelog at <https://github.com/mate-desktop/mate-system-monitor/commits/master/>

### mate-terminal
* Fix desktop file validation warning
* Add meson build system
* Add tab scrolling support for GTK3
* Add Wayland support
* Fix searching in terminal window
* Add icons to "open tab" and "close window/tab"
* Prevent crash on bad term spawn due to redundant frees
* Fix several code analysis, deprecation warnings reported by Clang Static Analyzer, Cppcheck and GCC
* g10n: Update the translations

Complete changelog at <https://github.com/mate-desktop/mate-terminal/commits/master/>

### mate-user-guide
* Remove the execution bit from some Italian figures
* build: Add option to disable Native Language Support (NLS) (`--disable-nls`)
* g10n: Update the translations

Complete changelog at <https://github.com/mate-desktop/mate-user-guide/commits/master/>

### mate-user-share
* Use MATE_COMPILE_WARNINGS from mate-common
* g10n: Update the translations

Complete changelog at <https://github.com/mate-desktop/mate-user-share/commits/master/>

### mate-utils
* mate-screenshot: Fix the order of the buttons at the bottom
* mate-screenshot: Do not use stock icons in mate-screenshot.ui
* logview: Rewrite logview-filter.ui from scratch
* gsearchtool: Add copy path menu item to popup menu
* Fix several code analysis, deprecation warnings reported by Clang Static Analyzer, Cppcheck and GCC
* build: Add option to disable Native Language Support (NLS) (`--disable-nls`)
* g10n: Update the translations

Complete changelog at <https://github.com/mate-desktop/mate-utils/commits/master/>

### mozo
* Rewrite mozo.ui from scratch
* Fix a strange behavior when editing the collection directory
* g10n: Update the translations

Complete changelog at <https://github.com/mate-desktop/mozo/commits/master/>

### pluma
* Port sort plugin to the new GtkSourceView api.
* Port plugins to use the window-construct property.
* build: Port to gtksourceview-4
* Introduce PlumaWindowActivatable, PlumaAppActivatable, PlumaViewActivatable
* Add show/hide line-numbers shortcut (Ctrl+Y)
* Redesign Pluma Preferences Dialog
* Remove pluma-marshal.
* Add optional grid background pattern
* Remove changecase plugin. Functionality is provided by GtkSourceView.
* Add overview map
* Port to a new pluma-settings class
* Add support for wayland
* Add tab scrolling support for GTK3
* pluma.c: Set PlumaWindow size-request (min-size) to 250x250
* Fix several code analysis, deprecation warnings reported by Clang Static Analyzer, Cppcheck and GCC
* g10n: Update the translations

Complete changelog at <https://github.com/mate-desktop/pluma/commits/master/>

### pluma-plugins
* Makes its first appearance in this release
* The package contains the following additional plugins
    * bookmarks - *Easy document navigation with bookmarks.*
    * bracketcompletion - *Automatically adds closing brackets.*
    * codecomment - *Comment and uncomment blocks of code.*
    * smartspaces - *Forget you’re not using tabulations.*
    * synctex - *SyncTeX synchronization of TeX files and PDF output.*
    * terminal - *Embed a terminal in the bottom pane.*
    * wordcompletion - *Word completion using the completion framework.*
    * sourcecodebrowser - *View and navigate functions, variables and namespaces.*

### python-caja
* Fix memory leak reported by scan-build
* g10n: Update the translations

Complete changelog at <https://github.com/mate-desktop/python-caja/commits/master/>
