[app]

# (str) Title of your application
title = My Kivy Application

# (str) Package name
package.name = mykivyapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,json

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let empty to exclude nothing)
#source.exclude_exts = spec

# (list) List of directories to exclude (let empty to exclude nothing)
#source.exclude_dirs = tests, bin

# (list) List of exclusions using pattern matching
#source.exclude_patterns = license,images/originals/*

# (str) Application versioning (method 1)
version = 0.1

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,hostpython3

# (str) Custom source folders for requirements
# Custom architectures/packages can be added here
#requirements.source.kivy = ../../kivy

# (str) Supported orientation (landscape, portrait, all)
orientation = portrait

# (list) List of service to declare
#services = NAME:ENTRYPOINT_TO_PYTHON,VIP:BIN_TO_PY


# =============================================================================
# iOS specific sections
# =============================================================================

# (str) Interactive environments
# ios.kivy_ios_dir = ../kivy-ios
# ios.kivy_ios_url = https://github.com
# ios.kivy_ios_branch = master

# (str) Name of the Xcode project (default to title if not set)
#ios.project_name = MyKivyApp

# (str) Development Team ID (10-character string from your Apple Developer Account)
#ios.dev_id = DEVID12345

# (str) Bundle Identifier (default to domain.name)
#ios.bundle_identifier = org.test.mykivyapp

# (str) Codesign identity (Use "iPhone Developer" for debug, "iPhone Distribution" for release)
ios.codesign.identity = "iPhone Developer"

# (str) Path to the provisioning profile (Alternatively handled by Github Secrets)
#ios.codesign.development = "path/to/development.mobileprovision"
#ios.codesign.allowed_to_sign_in_parallel = false

# (list) List of frameworks to link against
#ios.frameworks = SystemConfiguration,Security

# (list) iOS additional libraries to link with
#ios.libs = libsqlite3

# (str) Path to a custom plist file
#ios.plist = path/to/custom.plist

# (str) iOS codesigning deployment target (Minimum iOS version)
ios.ios_deploy_target = 13.0

# (str) Target architectures (arm64 is mandatory for physical iOS devices)
ios.archs = arm64

# (bool) If true, the xcode project will be open after the build
ios.manifest.launch_app = false

# (str) Icon of the application (must be a png format)
icon.filename = %(source.dir)s/icon.png

# (str) Presplash screen of the application
presplash.filename = %(source.dir)s/presplash.png


# =============================================================================
# Buildozer settings
# =============================================================================

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (default))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = false, 1 = true)
warn_on_root = 1

# (str) Path to build directory (where build outputs go)
build_dir = ./.buildozer

# (str) Path to store layout/cached dependencies
bin_dir = ./bin


# =============================================================================
# Advanced target control
# =============================================================================

# (str) Target platform (Must be set to ios for your GitHub action workflow)
platform = ios

# (str) Name of the production artifact
# release_artifact = %(title)s-%(version)s.ipa
