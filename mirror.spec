%define name mirror
%define version 2.9
%define release 14

Name: %name
Version: %version
Release: %release
Summary: Perl program to mirror FTP sites
License: BSD style
Group: Networking/File transfer
Source:  ftp://sunsite.org.uk/packages/mirror/%{name}.tar.bz2  
URL: https://sunsite.doc.ic.ac.uk/packages/%{name}/
Patch: %{name}-%{version}-mandrake.patch.bz2
Patch1: %{name}-no-directory-goback.patch.bz2
Patch2: %{name}-ftp.pl_wupatch.patch.bz2
Patch3: %{name}-deldir.patch.bz2
BuildRequires: patch, coreutils
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
%patch3 -p0 -b .dd

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

mv $RPM_BUILD_ROOT/%{_mandir}/man1/mm.1 $RPM_BUILD_ROOT/%{_mandir}/man1/mm-mirror.1

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
%{_mandir}/man1/mm-mirror.1*
%doc README.txt *.html CHANGES*
%doc %{name}.nightly support/cyber-patches support/lstest.pl


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 2.9-13mdv2011.0
+ Revision: 620365
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 2.9-12mdv2010.0
+ Revision: 430050
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 2.9-11mdv2009.0
+ Revision: 252543
- rebuild

* Thu Jan 03 2008 Olivier Blin <oblin@mandriva.com> 2.9-9mdv2008.1
+ Revision: 140954
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 22 2007 Bruno Cornec <bcornec@mandriva.org> 2.9-9mdv2008.0
+ Revision: 92289
- Adds SOURCES/mirror-deldir.patch.bz2 to fix bug #33248
  (Cf: http://qa.mandriva.com/show_bug.cgi?id=33248)

* Thu Aug 23 2007 Thierry Vignaud <tv@mandriva.org> 2.9-8mdv2008.0
+ Revision: 70133
- fileutils, sh-utils & textutils have been obsoleted by coreutils a long time ago

* Mon May 07 2007 Lenny Cartier <lenny@mandriva.org> 2.9-7mdv2008.0
+ Revision: 23987
- Fixed manpage naming (Bug #19040)
- Import mirror



* Tue Jan 03 2006 Lenny Cartier <lenny@mandriva.com> 2.9-6mdk
- rebuild

* Tue Nov 09 2004 Lenny Cartier <lenny@mandrakesoft.com> 2.9-5mdk
- rebuild

* Tue Oct 07 2003 Lenny Cartier <lenny@mandrakesoft.com> 2.9-4mdk
- from Bruno Cornec <bruno@HyPer-Linux.org> :
	- Fix path to perl script functions in first patch file

* Thu Oct 02 2003 Lenny Cartier <lenny@mandrakesoft.com> 2.9-3mdk
- disable wrong requires

* Thu Sep 18 2003 Lenny Cartier <lenny@mandrakesoft.com> 2.9-2mdk
- from Bruno Cornec <bruno@HyPer-Linux.org> :
	- Corrections for rpmlint -i
	- Now creates /etc/mirror.conf

* Fri Aug 15 2003 Bruno Cornec <bruno@HyPer-Linux.org> 2.9-1mdk
- Creation of first MDK package
- based on Connectiva spec file from Ricardo Erbano <erbano@conectiva.com>
