%define module	Imager
%define name	perl-%{module}
%define version	0.63
%define	release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Perl extension for generating 24 bit images
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/Imager/%{module}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:  libpng-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libtiff-devel
BuildRequires:  fontconfig-devel
BuildRequires:  t1lib-devel
BuildRequires:  ungif-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Imager is a module for creating and altering images. It can read and write
various image formats, draw primitive shapes like lines,and polygons, blend
multiple images together in various ways, scale, crop, render text and more.

%prep
%setup -q -n %{module}-%{version}

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


