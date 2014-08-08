%define major 5
%define libname %mklibname KF5UnitConversion %{major}
%define devname %mklibname KF5UnitConversion -d
%define debug_package %{nil}

Name: kunitconversion
Version: 5.1.0
Release: 1
Source0: http://ftp5.gwdg.de/pub/linux/kde/stable/frameworks/%{version}/%{name}-%{version}.tar.xz
Summary: The KDE Frameworks 5 unit conversion library
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt5Xml)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5Config) kconfig
BuildRequires: qmake5
BuildRequires: extra-cmake-modules5
Requires: %{libname} = %{EVRD}

%description
KUnitConversion is an abstraction to unit conversion.

%package -n %{libname}
Summary: The KDE Frameworks 5 unit conversion library
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
KUnitConversion is an abstraction to unit conversion.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/KDE and Qt
Requires: %{libname} = %{EVRD}

%description -n %{devname}
KUnitConversion is an abstraction to unit conversion.

%prep
%setup -q
%cmake

%build
%make -C build

%install
%makeinstall_std -C build
mkdir -p %{buildroot}%{_libdir}/qt5
mv %{buildroot}%{_prefix}/mkspecs %{buildroot}%{_libdir}/qt5
%find_lang %{name}%{major}

%files -f %{name}%{major}.lang

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5UnitConversion
%{_libdir}/qt5/mkspecs/modules/*
