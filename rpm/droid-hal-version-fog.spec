%define device fog
%define vendor xiaomi

%define vendor_pretty Xiaomi
%define device_pretty Redmi 10C

%define rpm_vendor xiaomi

%define have_vibrator_native 1

BuildRequires: droid-hal-%{device}
BuildRequires: droid-hal-%{device}-img-boot
BuildRequires: droid-hal-%{device}-img-recovery
BuildRequires: droid-hal-%{device}-kernel
BuildRequires: droid-hal-%{device}-tools
BuildRequires: droid-hal-%{device}-vendor_boot

BuildRequires: droid-config-%{rpm_device}
BuildRequires: droid-config-%{rpm_device}-bluez5
BuildRequires: droid-config-%{rpm_device}-flashing
BuildRequires: droid-config-%{rpm_device}-preinit-plugin
BuildRequires: droid-config-%{rpm_device}-pulseaudio-settings
BuildRequires: droid-config-%{rpm_device}-sailfish

%include droid-hal-version/droid-hal-version.inc
