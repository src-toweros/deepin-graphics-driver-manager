%bcond_with check
%global debug_package   %{nil}
%global _unpackaged_files_terminate_build 0 
Name:          deepin-graphics-driver-manager
Version:       5.0.0
Release:       1
Summary:       deepin driver manager.

License:       GPLv3
URL:           https://uos-packages.deepin.com/uos/pool/main/d/deepin-graphics-driver-manager/
Source0:       %{name}-%{version}.orig.tar.xz

BuildRequires: cmake
BuildRequires: qt5-qtbase-devel
BuildRequires: dtkwidget-devel
BuildRequires: deepin-gettext-tools
BuildRequires: freeglut
BuildRequires: freeglut-devel
BuildRequires: pciutils
BuildRequires: pciutils-devel

%description
deepin driver manager.

%prep
%setup

%build
export PATH=$PATH:/usr/lib64/qt5/bin
cmake .
make

%install
%make_install
mkdir -p %{?buildroot}%{_libdir}
mv %{?buildroot}/usr/lib/* %{?buildroot}%{_libdir}/
rm -rf  %{?buildroot}%{_libdir}/%{name}/debug/


%files
/lib/systemd/system/driver-installer.service
%{_bindir}/%{name}
%{_libdir}/*
%{_datadir}/*
%doc README.md


%changelog
* Thu Jul 30 2020 openEuler Buildteam <buildteam@openeuler.org> - 5.0.0-1
- Package init
