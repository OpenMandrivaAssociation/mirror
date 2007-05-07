%define name mirror
%define version 2.9
%define release %mkrel 6

Name: %name
Version: %version
Release: %release
Summary: Perl program to mirror FTP sites
License: BSD style
Group: Networking/File transfer
Source:  ftp://sunsite.org.uk/packages/mirror/%{name}.tar.bz2  
URL: http://sunsite.doc.ic.ac.uk/packages/%{name}/
Patch: %{name}-%{version}-mandrake.patch.bz2
Patch1: %{name}-no-directory-goback.patch.bz2
Patch2: %{name}-ftp.pl_wupatch.patch.bz2
BuildRequires: patch, fileutils
Requires: perl, perl-base
BuildArchitectures: noarch
BuildRoot: %{_tmppath}/%{name}-%buildoot

%description
Perl program to mirror FTP sites.

%prep

%setup -q -c

%patch -p1 -b .mdk
%patch1 -p1 -b .sec
%patch2 -p0 -b .wu

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{name}
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1
make "PLDIR=$RPM_BUILD_ROOT//%{_datadir}/%{name}" "BINDIR=$RPM_BUILD_ROOT/%{_bindir}" "MANDIR=$RPM_BUILD_ROOT/%{_mandir}/man1" install

install -m 644 %{name}.defaults $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}.conf
install -m 644 %{name}.defaults $RPM_BUILD_ROOT/%{_datadir}/%{name}

ln -sf %{name}.pl $RPM_BUILD_ROOT/%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_bindir}/do_unlinks.pl
%{_bindir}/%{name}
%{_bindir}/%{name}.pl
%{_bindir}/mm.pl
%{_bindir}/pkgs_to_mmin.pl
%defattr(0644,root,root,0755)
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/mm.1*
%doc README.txt *.html CHANGES*
%doc %{name}.nightly support/cyber-patches support/lstest.pl
