#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%include	/usr/lib/rpm/macros.perl
%define	pdir	Class
%define	pnam	Observable
Summary:	Class::Observable - allow other classes and objects to respond to events in yours
Summary(pl):	Class::Observable - umo�liwienie innym klasom odpowiadania na zdarzenia
Name:		perl-Class-Observable
Version:	1.04
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a4fe8e71f0082e51d5d97da865b6a708
BuildRequires:	perl-devel >= 1:5.8.0
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
Znaj�cy Jav� by� mo�e spotkali si� z klas� java.util.Observable i
interfejsem java.util.Observer. Przy ich u�yciu mo�na zrezygnowa� z
��czenia z jednym lub wi�cej obiekt�w, kt�re maj� by� powiadamiane o
wyst�pieniu okre�lonych zdarze�.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
