%define device pipa
%define vendor xiaomi

%define vendor_pretty Xiaomi
%define device_pretty Pad 6

BuildRequires: droid-hal-%{device}
BuildRequires: droid-hal-%{device}-img-boot
BuildRequires: droid-hal-%{device}-img-recovery
BuildRequires: droid-hal-%{device}-kernel
BuildRequires: droid-hal-%{device}-tools
BuildRequires: droid-hal-%{device}-vendor_boot

%include droid-hal-version/droid-hal-version.inc
