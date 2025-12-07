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

BuildRequires: droid-config-%{device}
BuildRequires: droid-config-%{device}-bluez5
BuildRequires: droid-config-%{device}-flashing
BuildRequires: droid-config-%{device}-preinit-plugin
BuildRequires: droid-config-%{device}-pulseaudio-settings
BuildRequires: droid-config-%{device}-sailfish

%include droid-hal-version/droid-hal-version.inc
