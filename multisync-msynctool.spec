%define		_realname	msynctool
Summary:	OpenSync data synchronization command line programs
Summary(pl):	Programy lini poleceñ do synchronizacji danych OpenSync
Name:		multisync-msynctool
Version:	0.19
Release:	0.1
License:	GPL
Group:		Applications
Source0:	%{_realname}-%{version}.tar.gz
# Source0-md5:	5c7728254f2d634051af603e7d467832
#Source0:	http://www.opensync.org/attachment/wiki/download/%{_realname}-%{version}.tar.gz?format=raw
URL:		http://opensync.org/
BuildRequires:	libopensync-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenSync is a synchronization framework that is platform and distribution
independent.

It consists of several plugins that can be used to connect to devices,
a powerful sync-engine and the framework itself.

This package contains command line program to use OpenSync framework.

%description -l pl
OpenSync to niezale¿ny od platformy i dystrybucji szkielet do
synchronizacji danych.

Sk³ada siê z ró¿nych wtyczek, których mo¿na u¿ywaæ do ³±czenia z
urz±dzeniami, potê¿nego silnika synchronizacji oraz samego szkieletu.

Ten pakiet zawiera program linii komend do korzystania
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
