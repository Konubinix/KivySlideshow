[app]

# title of the application
title = Slideshow

# package name
package.name = slideshow

# package domain (mostly used for android/ios package)
package.domain = org.kivy

# indicate where the source code is living
source.dir = .
source.include_exts = py,png,kv,json

# search the version information into the source code
version.regex = __version__ = '(.*)'
version.filename = %(source.dir)s/main.py

# (str) Supported orientation (one of landscape, portrait or all)
orientation = all

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# requirements of the app
requirements = pycrypto,pyasn1,twisted,kivy,plyer,rpyc
#,zmq,ipykernel

# android specific
# http://developer.android.com/reference/android/Manifest.permission.html
# # 13 error(s) found in the buildozer.spec
# [app] "android.permission" contain an unknown permission #ACCESS_NOTIFICATION_POLICY
# [app] "android.permission" contain an unknown permission #BIND_CARRIER_MESSAGING_SERVICE
# [app] "android.permission" contain an unknown permission #BIND_CARRIER_SERVICES
# [app] "android.permission" contain an unknown permission #BIND_CHOOSER_TARGET_SERVICE
# [app] "android.permission" contain an unknown permission #BIND_INCALL_SERVICE
# [app] "android.permission" contain an unknown permission #BIND_MIDI_DEVICE_SERVICE
# [app] "android.permission" contain an unknown permission #BIND_NFC_SERVICE
# [app] "android.permission" contain an unknown permission BIND_TELECOM_CONNECTION_SERVICE
# [app] "android.permission" contain an unknown permission GET_ACCOUNTS_PRIVILEGED
# [app] "android.permission" contain an unknown permission PACKAGE_USAGE_STATS
# [app] "android.permission" contain an unknown permission REQUEST_IGNORE_BATTERY_OPTIMIZATIONS
# [app] "android.permission" contain an unknown permission REQUEST_INSTALL_PACKAGES
# [app] "android.permission" contain an unknown permission USE_FINGERPRINT
# [app] "android.permission" contain an unknown permission BIND_DREAM_SERVICE
# [app] "android.permission" contain an unknown permission BIND_TV_INPUT
# [app] "android.permission" contain an unknown permission BIND_VOICE_INTERACTION
# [app] "android.permission" contain an unknown permission BODY_SENSORS
# [app] "android.permission" contain an unknown permission READ_VOICEMAIL
# [app] "android.permission" contain an unknown permission WRITE_VOICEMAIL
android.permissions = ACCESS_CHECKIN_PROPERTIES,
                    ACCESS_COARSE_LOCATION,
                    ACCESS_FINE_LOCATION,
                    ACCESS_LOCATION_EXTRA_COMMANDS,
                    ACCESS_NETWORK_STATE,
                    ACCESS_WIFI_STATE,
                    ACCOUNT_MANAGER,
                    ADD_VOICEMAIL,
                    BATTERY_STATS,
                    BIND_ACCESSIBILITY_SERVICE,
                    BIND_APPWIDGET,
                    BIND_DEVICE_ADMIN,
                    BIND_INPUT_METHOD,
                    BIND_NOTIFICATION_LISTENER_SERVICE,
                    BIND_PRINT_SERVICE,
                    BIND_REMOTEVIEWS,
                    BIND_TEXT_SERVICE,
                    BIND_VPN_SERVICE,
                    BIND_WALLPAPER,
                    BLUETOOTH,
                    BLUETOOTH_ADMIN,
                    BLUETOOTH_PRIVILEGED,
                    BROADCAST_PACKAGE_REMOVED,
                    BROADCAST_SMS,
                    BROADCAST_STICKY,
                    BROADCAST_WAP_PUSH,
                    CALL_PHONE,
                    CALL_PRIVILEGED,
                    CAMERA,
                    CAPTURE_AUDIO_OUTPUT,
                    CAPTURE_SECURE_VIDEO_OUTPUT,
                    CAPTURE_VIDEO_OUTPUT,
                    CHANGE_COMPONENT_ENABLED_STATE,
                    CHANGE_CONFIGURATION,
                    CHANGE_NETWORK_STATE,
                    CHANGE_WIFI_MULTICAST_STATE,
                    CHANGE_WIFI_STATE,
                    CLEAR_APP_CACHE,
                    CONTROL_LOCATION_UPDATES,
                    DELETE_CACHE_FILES,
                    DELETE_PACKAGES,
                    DIAGNOSTIC,
                    DISABLE_KEYGUARD,
                    DUMP,
                    EXPAND_STATUS_BAR,
                    FACTORY_TEST,
                    FLASHLIGHT,
                    GET_ACCOUNTS,
                    GET_PACKAGE_SIZE,
                    GET_TASKS,
                    GLOBAL_SEARCH,
                    INSTALL_LOCATION_PROVIDER,
                    INSTALL_PACKAGES,
                    INSTALL_SHORTCUT,
                    INTERNET,
                    KILL_BACKGROUND_PROCESSES,
                    LOCATION_HARDWARE,
                    MANAGE_DOCUMENTS,
                    MASTER_CLEAR,
                    MEDIA_CONTENT_CONTROL,
                    MODIFY_AUDIO_SETTINGS,
                    MODIFY_PHONE_STATE,
                    MOUNT_FORMAT_FILESYSTEMS,
                    MOUNT_UNMOUNT_FILESYSTEMS,
                    NFC,
                    PERSISTENT_ACTIVITY,
                    PROCESS_OUTGOING_CALLS,
                    READ_CALENDAR,
                    READ_CALL_LOG,
                    READ_CONTACTS,
                    READ_EXTERNAL_STORAGE,
                    READ_FRAME_BUFFER,
                    READ_INPUT_STATE,
                    READ_LOGS,
                    READ_PHONE_STATE,
                    READ_SMS,
                    READ_SYNC_SETTINGS,
                    READ_SYNC_STATS,
                    REBOOT,
                    RECEIVE_BOOT_COMPLETED,
                    RECEIVE_MMS,
                    RECEIVE_SMS,
                    RECEIVE_WAP_PUSH,
                    RECORD_AUDIO,
                    REORDER_TASKS,
                    RESTART_PACKAGES,
                    SEND_RESPOND_VIA_MESSAGE,
                    SEND_SMS,
                    SET_ALARM,
                    SET_ALWAYS_FINISH,
                    SET_ANIMATION_SCALE,
                    SET_DEBUG_APP,
                    SET_PREFERRED_APPLICATIONS,
                    SET_PROCESS_LIMIT,
                    SET_TIME,
                    SET_TIME_ZONE,
                    SET_WALLPAPER,
                    SET_WALLPAPER_HINTS,
                    SIGNAL_PERSISTENT_PROCESSES,
                    STATUS_BAR,
                    SYSTEM_ALERT_WINDOW,
                    TRANSMIT_IR,
                    UNINSTALL_SHORTCUT,
                    UPDATE_DEVICE_STATS,
                    USE_SIP,
                    VIBRATE,
                    WAKE_LOCK,
                    WRITE_APN_SETTINGS,
                    WRITE_CALENDAR,
                    WRITE_CALL_LOG,
                    WRITE_CONTACTS,
                    WRITE_EXTERNAL_STORAGE,
                    WRITE_GSERVICES,
                    WRITE_SECURE_SETTINGS,
                    WRITE_SETTINGS,
                    WRITE_SYNC_SETTINGS
android.wakelock = True
[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2
