%define name webcam_server
%define version 0.40
%define release %mkrel 9
%define url http://donn.dyndns.org/portalofnnod

Summary: A server to stream webcam video or snapshots
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{url}/%{name}-%{version}.tar.bz2
Source1: %name.bz2
License: GPL
Group: System/Kernel and hardware
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: jpeg-devel
Prefix: /usr
URL: https://donn.dyndns.org/portalofnnod/

%description
webcam_server  is  a  server  daemon that can stream frames
from any video4linux device to remote clients running the 
provided applet or single frame snapshots running a web browser.
Client applets provided in /usr/share/doc/webcam_server-%{version}/client

%prep
%setup -q

%build
%configure 
# --prefix=/usr --mandir=/usr/share/man
%make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%_sysconfdir/rc.d/init.d
#mkdir -p $RPM_BUILD_ROOT/%{bindir}
#mkdir -p $RPM_BUILD_ROOT/%{mandir}/man1
#mkdir -p $RPM_BUILD_ROOT/%{bindir}/share/%{name}-%{version}/client
#for i in src/client/*; do
#         install -m644 $i $RPM_BUILD_ROOT/%{_datadir}/%{name}-%{version}/client/
# done
		 
bzcat %{SOURCE1} > $RPM_BUILD_ROOT/%_sysconfdir/rc.d/init.d/webcam_server
chmod 755 $RPM_BUILD_ROOT/%_sysconfdir/rc.d/init.d/webcam_server
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc src/client/*
%{_bindir}/*
%{_mandir}/man1/*
%attr(-,root,root) %config %_sysconfdir/rc.d/init.d/webcam_server
#%attr(-,root,root) /%{bindir}/share/%{name}-%{version}/client/*

