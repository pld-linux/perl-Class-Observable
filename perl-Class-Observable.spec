#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	Class
%define	pnam	Observable
Summary:	Class::Observable - Allow other classes and objects to respond to events in yours
Summary(pl):	Modu³ Class::Observable - pozwalaj±cy innym klasom odpowiadaæ na zdarzenia
Name:		perl-Class-Observable
Version:	0.03
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	161bab9d9b70ba9eae53012d1101b043
BuildRequires:	perl-devel >= 5.6
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-Class-ISA >= 0.32
BuildRequires:	perl-Test-Simple >= 0.40
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
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

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
