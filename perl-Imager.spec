%define upstream_name	 Imager
%define upstream_version 0.73

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Perl extension for generating 24 bit images
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Imager/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:  fontconfig-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:	perl-devel
BuildRequires:  t1lib-devel
BuildRequires:  ungif-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

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
