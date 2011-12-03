# Authority: dag
# Upstream: Dag Wieers <dag@wieers.com>

Summary: Versatile resource statistics tool
Name: dstat
Version: 0.7.0
Release: 1%{?dist}
License: GPLv2
Group: System Environment/Base
URL: http://dag.wieers.com/home-made/dstat/

Source: http://dag.wieers.com/home-made/dstat/dstat-%{version}.tar.bz2
Patch0: dstat-0.6.8-dbus.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root%(%{__id_u} -n)

BuildArch: noarch
BuildRequires: python
Requires: python

%description
Dstat is a versatile replacement for vmstat, iostat, netstat and ifstat.
Dstat overcomes some of their limitations and adds some extra features,
more counters and flexibility. Dstat is handy for monitoring systems
during performance tuning tests, benchmarks or troubleshooting.

Dstat allows you to view all of your system resources instantly, you
can eg. compare disk usage in combination with interrupts from your
IDE controller, or compare the network bandwidth numbers directly
with the disk throughput (in the same interval).

Dstat gives you detailed selective information in columns and clearly
indicates in what magnitude and unit the output is displayed. Less
confusion, less mistakes.

%prep
%setup -q
%patch0 -p1 -b .dbus

%build
# Make sure the docs are in unix format
%{__sed} -i 's/\r//' docs/*.html
# Remove the broken symlink
%{__rm} -rf examples/dstat.py
%{__chmod} a-x examples/*

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}
# Install the man page
cd docs
%{__make} install DESTDIR=%{buildroot}
# Plugins .py files are modules, not executable python
%{__chmod} a-x %{buildroot}/%{_datadir}/dstat/*.py
%{__chmod} a+x %{buildroot}/%{_datadir}/dstat/dstat.py

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%dir %{_datadir}/dstat
%doc AUTHORS ChangeLog COPYING README TODO docs/*.html docs/*.txt examples/
%{_mandir}/man1/dstat.1*
%{_bindir}/dstat
%{_datadir}/dstat/*.py*

%changelog
* Thu Dec 03 2009 Jan Zeleny <jzeleny@redhat.com> - 0.7.0-1
- rebased to 0.7.0

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Dec 23 2008 Zdenek Prikryl <zprikryl@redhat.com> - 0.6.9-3
- Fixed wrong total disk counts (#476935)

* Thu Dec 04 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.6.9-2
- Rebuild for Python 2.6

* Thu Dec 04 2008 Zdenek Prikryl <zprikryl@redhat.com> - 0.6.9-1
- Updated to 0.6.9
- Fixed dbus module patch again

* Mon Dec 01 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.6.8-2
- Rebuild for Python 2.6

* Tue Sep 16 2008 Zdenek Prikryl <zprikryl@redhat.com> - 0.6.8-1
- Updated to 0.6.8
- Fixed dbus module patch

* Fri Apr 25 2008 Radek Brich <rbrich@redhat.com> - 0.6.7-3
- fix dbus module (new dbus-python interface since FC4)

* Thu Mar 27 2008 Radek Brich <rbrich@redhat.com> - 0.6.7-2
- fixes for interrupt stats:
  * traceback when called with unknown name of interrupt (bz#439143)
  * allow '-I total' option (bz#439146)

* Wed Mar 19 2008 Radek Brich <rbrich@redhat.com> - 0.6.7-1
- Release 0.6.7
- Drop upstream patches

* Fri Jan 18 2008 Radek Brich <rbrich@redhat.com> - 0.6.6-3
- Fix --nocolor and --raw (upstream patches)
- Fix errors in man page

* Tue Sep 04 2007 Radek Brich <rbrich@redhat.com> - 0.6.6-2
- Updated license tag.
- Spec clean up.

* Tue May 01 2007 Scott Baker <scott@perturb.org> - 0.6.6-1
- Bumped to latest release

* Wed Apr 18 2007 Scott Baker <scott@perturb.org> - 0.6.5-1
- Bumped to latest release

* Tue Dec 12 2006 Scott Baker <scott@perturb.org> - 0.6.4-1
- Bumped to 0.6.4

* Fri Aug 11 2006 Scott Baker <scott@perturb.org> - 0.6.3-5
- Removed the execute permission from the examples directory
- Fixed the changelog to remove the replaceable %%clean

* Tue Jul 25 2006 Scott Baker <scott@perturb.org> - 0.6.3-4
- Removed some commeted lines in the .spec file that weren't needed
- Changed the permissions on the examples/* scripts
- Converted the HTML documentation to unix line endings
- Removed the erroneous commenting of the %%clean section of the .spec

* Fri Jul 21 2006 Scott Baker <scott@perturb.org> - 0.6.3-3
- Packaged for Fedora Extras.

* Mon Jun 26 2006 Dag Wieers <dag@wieers.com> - 0.6.3-1 - 4303+/dries
- Updated to release 0.6.3.

* Thu Mar 09 2006 Dag Wieers <dag@wieers.com> - 0.6.2-1
- Updated to release 0.6.2.

* Mon Sep 05 2005 Dag Wieers <dag@wieers.com> - 0.6.1-1
- Updated to release 0.6.1.

* Sun May 29 2005 Dag Wieers <dag@wieers.com> - 0.6.0-1
- Updated to release 0.6.0.

* Fri Apr 08 2005 Dag Wieers <dag@wieers.com> - 0.5.10-1
- Updated to release 0.5.10.

* Mon Mar 28 2005 Dag Wieers <dag@wieers.com> - 0.5.9-1
- Updated to release 0.5.9.

* Tue Mar 15 2005 Dag Wieers <dag@wieers.com> - 0.5.8-1
- Updated to release 0.5.8.

* Fri Dec 31 2004 Dag Wieers <dag@wieers.com> - 0.5.7-1
- Updated to release 0.5.7.

* Mon Dec 20 2004 Dag Wieers <dag@wieers.com> - 0.5.6-1
- Updated to release 0.5.6.

* Thu Dec 02 2004 Dag Wieers <dag@wieers.com> - 0.5.5-1
- Updated to release 0.5.5.

* Thu Nov 25 2004 Dag Wieers <dag@wieers.com> - 0.5.4-1
- Updated to release 0.5.4.
- Use dstat15 if distribution uses python 1.5.

* Sun Nov 21 2004 Dag Wieers <dag@wieers.com> - 0.5.3-1
- Updated to release 0.5.3.

* Sat Nov 13 2004 Dag Wieers <dag@wieers.com> - 0.5.2-1
- Updated to release 0.5.2.

* Thu Nov 11 2004 Dag Wieers <dag@wieers.com> - 0.5.1-1
- Updated to release 0.5.1.

* Tue Oct 26 2004 Dag Wieers <dag@wieers.com> - 0.4-1
- Initial package. (using DAR)
