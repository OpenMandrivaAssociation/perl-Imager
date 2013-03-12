%define upstream_name	 Imager
%define upstream_version 0.84

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	2

Summary:	Perl extension for generating 24 bit images
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Imager/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:  fontconfig-devel
BuildRequires:  jpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:	perl-devel
BuildRequires:  t1lib-devel
BuildRequires:  ungif-devel

%description
Imager is a module for creating and altering images. It can read and write
various image formats, draw primitive shapes like lines,and polygons, blend
multiple images together in various ways, scale, crop, render text and more.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
IM_SUPPRESS_PROMPT=1 %{__perl} Makefile.PL INSTALLDIRS=vendor
%make "CFLAGS=%{optflags}"

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorarch}/Imager.pm
%{perl_vendorarch}/Imager
%{perl_vendorarch}/auto/Imager
%{_mandir}/*/*


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.840.0-2
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Wed Jun 22 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.840.0-1
+ Revision: 686639
- update to new version 0.84

* Sun May 22 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.830.0-1
+ Revision: 677358
- update to new version 0.83

* Fri Mar 18 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.820.0-1
+ Revision: 646336
- update to new version 0.82

* Mon Feb 28 2011 Funda Wang <fwang@mandriva.org> 0.810.0-2
+ Revision: 640769
- rebuild to obsolete old packages

* Fri Feb 18 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.810.0-1
+ Revision: 638483
- update to new version 0.81

* Tue Feb 01 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.800.0-1
+ Revision: 634684
- update to new version 0.80

* Sat Dec 11 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.790.0-1mdv2011.0
+ Revision: 620578
- update to new version 0.79
- update to new version 0.78

* Sun Aug 15 2010 Jérôme Quelin <jquelin@mandriva.org> 0.770.0-1mdv2011.0
+ Revision: 569943
- update to 0.77

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.750.0-2mdv2011.0
+ Revision: 555961
- rebuild for perl 5.12

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.750.0-1mdv2011.0
+ Revision: 552368
- update to 0.75

* Mon Mar 15 2010 Jérôme Quelin <jquelin@mandriva.org> 0.730.0-1mdv2010.1
+ Revision: 519958
- update to 0.73

* Sat Jan 16 2010 Funda Wang <fwang@mandriva.org> 0.720.0-2mdv2010.1
+ Revision: 492265
- rebuild for new libjpeg v8

* Sat Dec 12 2009 Jérôme Quelin <jquelin@mandriva.org> 0.720.0-1mdv2010.1
+ Revision: 477622
- update to 0.72

* Tue Nov 17 2009 Jérôme Quelin <jquelin@mandriva.org> 0.710.0-1mdv2010.1
+ Revision: 466751
- update to 0.71

* Tue Sep 22 2009 Jérôme Quelin <jquelin@mandriva.org> 0.700.0-1mdv2010.0
+ Revision: 447134
- update to 0.70

* Wed Sep 09 2009 Jérôme Quelin <jquelin@mandriva.org> 0.690.0-1mdv2010.0
+ Revision: 435735
- update to 0.69

* Mon Sep 07 2009 Jérôme Quelin <jquelin@mandriva.org> 0.680.0-1mdv2010.0
+ Revision: 432821
- update to 0.68

* Sun Aug 23 2009 Funda Wang <fwang@mandriva.org> 0.670.0-3mdv2010.0
+ Revision: 419880
- rebuild for new libjpeg v7

* Mon Aug 03 2009 Jérôme Quelin <jquelin@mandriva.org> 0.670.0-1mdv2010.0
+ Revision: 407783
- rebuild using %%perl_convert_version

* Sun Dec 14 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.67-1mdv2009.1
+ Revision: 314247
- update to new version 0.67

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.65-2mdv2009.0
+ Revision: 268534
- rebuild early 2009.0 package (before pixel changes)

* Wed May 21 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.65-1mdv2009.0
+ Revision: 209674
- update to new version 0.65
- update to new version 0.64

* Tue Apr 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.63-1mdv2009.0
+ Revision: 193854
- update to new version 0.63

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 0.62-2mdv2008.1
+ Revision: 151418
- rebuild for perl-5.10.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Dec 11 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.62-1mdv2008.1
+ Revision: 117501
- update to new version 0.62

* Tue Nov 06 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.61-1mdv2008.1
+ Revision: 106567
- update to new version 0.61
- update to new version 0.61

* Sat Sep 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.60-1mdv2008.0
+ Revision: 77704
- update to new version 0.60

* Tue Jul 03 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.59-1mdv2008.0
+ Revision: 47660
- update to new version 0.59


* Fri Feb 16 2007 Olivier Thauvin <nanardon@mandriva.org> 0.55-2mdv2007.0
+ Revision: 122009
- add buildrequires to enable format support

* Thu Jan 04 2007 Olivier Thauvin <nanardon@mandriva.org> 0.55-1mdv2007.1
+ Revision: 103938
- 0.55

* Sat Dec 09 2006 Olivier Thauvin <nanardon@mandriva.org> 0.54-1mdv2007.1
+ Revision: 94360
- 0.54
- 0.53
- Import perl-Imager

* Fri Jun 02 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.51-1mdv2007.0
- New release 0.51

* Tue Apr 04 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.50-1mdk
- new version
- proper cflags
- repmbuildupdate aware
- fix directory ownership

* Wed Mar 08 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.49-1mdk
- 0.49

* Fri Feb 17 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.47-1mdk
- 0.47

* Tue Dec 20 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.46-1mdk
- 0.46

* Sat Jun 25 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.45-1mdk
- First Mandriva release

