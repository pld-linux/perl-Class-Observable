#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%include	/usr/lib/rpm/macros.perl
%define	pdir	Class
%define	pnam	Observable
Summary:	Class::Observable - Allow other classes and objects to respond to events in yours
Summary(pl):	Modu³ Class::Observable - pozwalaj±cy innym klasom odpowiadaæ na zdarzenia
Name:		perl-Class-Observable
Version:	1.02
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	792de9e203bda8940d30caca3fb97d60
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Class-ISA >= 0.32
BuildRequires:	perl-Test-Simple >= 0.40
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
If you have ever used Java, you may have run across the
java.util.Observable class and the java.util.Observer interface. Using
them, you can decouple an object from the one or more objects that
wish to be notified whenever particular events occur.

%description -l pl
Znaj±cy Javê byæ mo¿e spotkali siê z klas± java.util.Observable i
interfejsem java.util.Observer. Przy ich u¿yciu mo¿na zrezygnowaæ z
³±czenia z jednym lub wiêcej obiektów, które maj± byæ powiadamiane o
wyst±pieniu okre¶lonych zdarzeñ.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
