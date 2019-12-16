Summary: nethserver-rainloop  is a module for rainloop
%define name nethserver-rainloop
Name: %{name}
%define version 0.1.1
%define release 1
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
Requires: rainloop
Requires: nethserver-mail-server
Requires: nethserver-mysql
BuildRequires: nethserver-devtools
BuildArch: noarch

%description

Simple, modern & fast web-based email client


%changelog
* Sat Dec 15 2018 stephane de Labrusse <stephdl@de-labrusse.fr>
- Force SMTP authentification

* Sun May 13 2018 stephane de Labrusse <stephdl@de-labrusse.fr>
- initial

%prep
%setup

%build
%{makedocs}
perl createlinks
sed -i 's/_RELEASE_/%{version}/' %{name}.json

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)

mkdir -p %{buildroot}/usr/share/cockpit/%{name}/
mkdir -p %{buildroot}/usr/share/cockpit/nethserver/applications/
mkdir -p %{buildroot}/usr/libexec/nethserver/api/%{name}/
cp -a manifest.json %{buildroot}/usr/share/cockpit/%{name}/
cp -a logo.png %{buildroot}/usr/share/cockpit/%{name}/
cp -a %{name}.json %{buildroot}/usr/share/cockpit/nethserver/applications/
cp -a api/* %{buildroot}/usr/libexec/nethserver/api/%{name}/


rm -f %{name}-%{version}-%{release}-filelist
%{genfilelist} $RPM_BUILD_ROOT \
> %{name}-%{version}-%{release}-filelist

%post
%postun

%clean 
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
%dir %{_nseventsdir}/%{name}-update
%doc COPYING
%config(noreplace) %{_datadir}/rainloop/data/_data_/_default_/configs/application.ini
