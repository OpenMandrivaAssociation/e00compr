Name:		e00compr
Version:	1.0.1
Release:	%mkrel 2
Summary:	Tools to Read/Write Compressed E00 Files
License:	BSD-like
Source:		http://avce00.maptools.org/dl/%{name}-%{version}.tar.bz2
URL:		http://avce00.maptools.org/e00compr
Group:		Sciences/Geosciences
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
E00Compr is an Open Source (i.e. Free!) ANSI-C library to compress and
uncompress Arc/Info Export (E00) files.

For those who do not need a library but simply want to convert some files, the
package includes the "E00CONV" conversion program that allows you to convert a
E00 file to and from any compression level (NONE, PARTIAL or FULL). 

%package -n %{name}-devel
License:	BSD-like
Group:		Sciences/Geosciences
Summary:	A Library to Read/Write Compressed E00 Files

%description -n %{name}-devel
E00Compr is an Open Source (i.e. Free!) ANSI-C library to compress and
uncompress Arc/Info Export (E00) files.

The C library can be easily plugged into existing E00 translators to add
support for compressed E00 files simply by replacing the existing translator's
read/write function by the E00ReadNextLine() and E00WriteNextLine() functions
provided by the library. See the library documentation for all the details.

This package includes the development files (headers and static library)
for developing applications which use the e00 library.

%prep
%setup -q


%build
#configure
%make

%install
rm -Rf %{buildroot}
install -d %{buildroot}/{%{_includedir},%{_bindir},%{_libdir}}
install -m644 *.h %{buildroot}/%{_includedir}
install *.a %{buildroot}/%{_libdir}
install e00conv %{buildroot}/%{_bindir}

%clean
rm -Rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/e00conv

%files -n %{name}-devel
%{_includedir}/*.h
%{_libdir}/e00compr.a



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-2mdv2011.0
+ Revision: 617940
- the mass rebuild of 2010.0 packages

* Thu Aug 20 2009 Buchan Milne <bgmilne@mandriva.org> 1.0.1-1mdv2010.0
+ Revision: 418563
- update to new version 1.0.1

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.0.0-5mdv2009.0
+ Revision: 244600
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.0.0-3mdv2008.1
+ Revision: 140723
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import e00compr


* Wed Sep 06 2006 Buchan Milne <bgmilne@mandriva.org> 1.0.0-3mdv2007.0
- fix perms of headers
- clean buildroot

* Thu Feb 16 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.0.0-2mdk
- Fix Group ( Tks PierreLag)

* Sun Jan 01 2006 Buchan Milne <bgmilne@mandriva.org> 1.0.0-1
- initial Mandriva package
