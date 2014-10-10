%define upstream_name	 Imager
%define upstream_version 0.98

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	2

Summary:	Perl extension for generating 24 bit images

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/%{upstream_name}/%{upstream_name}-%{upstream_version}.tar.gz
Source100: %{name}.rpmlintrc

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
%make test

%install
%makeinstall_std

%clean 

%files
%doc README Changes
%{perl_vendorarch}/Imager.pm
%{perl_vendorarch}/Imager
%{perl_vendorarch}/auto/Imager
%{_mandir}/*/*



