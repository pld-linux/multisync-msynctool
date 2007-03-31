%define		_realname	msynctool
Summary:	OpenSync data synchronization command line programs
Summary(pl.UTF-8):	Programy działające z linii poleceń do synchronizacji danych OpenSync
Name:		multisync-msynctool
Version:	0.22
Release:	1
License:	GPL
Group:		Applications
Source0:	http://www.opensync.org/attachment/wiki/download/%{_realname}-%{version}.tar.bz2?format=raw
# Source0-md5:	3ddc55209e682a8b99a47cf3d0053dbf
URL:		http://opensync.org/
BuildRequires:	libopensync-devel >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenSync is a synchronization framework that is platform and distribution
independent.

It consists of several plugins that can be used to connect to devices,
a powerful sync-engine and the framework itself.

This package contains command line program to use OpenSync framework.

%description -l pl.UTF-8
OpenSync to niezależny od platformy i dystrybucji szkielet do
synchronizacji danych.

Składa się z różnych wtyczek, których można używać do łączenia z
urządzeniami, potężnego silnika synchronizacji oraz samego szkieletu.

Ten pakiet zawiera działający z linii poleceń program do korzystania
ze szkieletu OpenSync.

%prep
%setup -q -n %{_realname}-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1*
