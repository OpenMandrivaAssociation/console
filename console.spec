Name:           console
Version:        42.beta
Release:        1
Summary:        A simple user-friendly terminal emulator for the GNOME desktop
License:        GPL-3.0
URL:            https://gitlab.gnome.org/GNOME/console
Source:         https://gitlab.gnome.org/GNOME/console/-/archive/%{version}/console-%{version}.tar.bz2

BuildRequires:  appstream-utils
BuildRequires:  desktop-file-utils
BuildRequires:  libxml2-utils
BuildRequires:  meson >= 0.59.0
BuildRequires:  sassc
BuildRequires:  pkgconfig(gio-2.0) >= 2.66
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.24
#BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libhandy-1) >= 1.5
BuildRequires:  pkgconfig(vte-2.91) >= 0.67
BuildRequires:  pkgconfig(libgtop-2.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(libnautilus-extension)
BuildRequires:  pkgconfig(gio-unix-2.0)

%description
A simple user-friendly terminal emulator for the GNOME desktop.

%lang_package

%package -n nautilus-extension-console
Summary:        Nautilus Extension to open Console in Folders
Supplements:    (nautilus and %{name})

%description -n nautilus-extension-console
This is a nautilus extension that allows you to open a terminal in
arbitrary folders.

%prep
%autosetup -p1

%build
%meson \
	-D tests=true \
	-D nautilus=enabled
%meson_build

%install
%meson_install
%find_lang kgx %{?no_lang_C} %{name}.lang


%files -f %{name}.lang
%license COPYING
%doc README.md
%{_bindir}/kgx
%{_datadir}/applications/org.gnome.Console.desktop
%{_datadir}/dbus-1/services/org.gnome.Console.service
%{_datadir}/glib-2.0/schemas/org.gnome.Console.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Console.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Console-symbolic.svg
%{_datadir}/metainfo/org.gnome.Console.metainfo.xml

%files -n nautilus-extension-console
%{_libdir}/nautilus/extensions-3.0/libkgx-nautilus.so

