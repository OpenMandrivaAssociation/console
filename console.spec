Name:           console
Version:        48.0.1
Release:        1
Summary:        A simple user-friendly terminal emulator for the GNOME desktop
License:        GPL-3.0
URL:            https://gitlab.gnome.org/GNOME/console
#Source:         https://gitlab.gnome.org/GNOME/console/-/archive/%{version}/console-%{version}.tar.bz2
Source0:	https://download.gnome.org/sources/gnome-console/46/gnome-console-%{version}.tar.xz

BuildRequires:  appstream-util
BuildRequires:  desktop-file-utils
BuildRequires:  libxml2-utils
BuildRequires:  meson >= 0.59.0
BuildRequires:	gettext
BuildRequires:  pkgconfig(gio-2.0) >= 2.66
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(vte-2.91-gtk4)
BuildRequires:  pkgconfig(libgtop-2.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:	pkgconfig(libpcre2-8)

Provides:	gnome-console
Obsoletes: nautilus-extension-console < 43.0

%description
A simple user-friendly terminal emulator for the GNOME desktop.

%lang_package


%prep
%autosetup -n gnome-console-%{version} -p1
sed -i "s/'werror=true'/'werror=false'/g" meson.build

%build
%meson \
	-D tests=false \
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


