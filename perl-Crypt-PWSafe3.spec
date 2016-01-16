#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Crypt
%define		pnam	PWSafe3
%include	/usr/lib/rpm/macros.perl
Summary:	Crypt::PWSafe3 - Read and write Passwordsafe v3 files
Name:		perl-Crypt-PWSafe3
Version:	1.21
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Crypt/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4f770e04dee6b423281bafdf7a8b0f49
URL:		http://search.cpan.org/dist/Crypt-PWSafe3/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Crypt::CBC) >= 2.3
BuildRequires:	perl(Crypt::ECB) >= 1.45
BuildRequires:	perl(Crypt::Random) >= 1.25
BuildRequires:	perl(Crypt::Twofish) >= 2.14
BuildRequires:	perl(Data::UUID) >= 1.217
BuildRequires:	perl(Digest::HMAC) >= 1
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt::PWSafe3 provides read and write access to password database
files created by Password Safe V3 (and up) available at
http://passwordsafe.sf.net.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a sample $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README
%{perl_vendorlib}/Crypt/*.pm
%{perl_vendorlib}/Crypt/PWSafe3
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
