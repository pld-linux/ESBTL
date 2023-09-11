Summary:	Easy Structural Biology Template Library
Summary(pl.UTF-8):	Easy Structural Biology Template Library - łatwa w użyciu biblioteka szablonów do biologii strukturalnej
Name:		ESBTL
Version:	1.0
%define	subver	beta01
Release:	0.%{subver}.1
License:	GPL v3 with CGAL exception
Group:		Libraries
Source0:	https://downloads.sourceforge.net/esbtl/%{name}-%{version}-%{subver}.tar.bz2
# Source0-md5:	ba2868d3613b6e242f779e2dfd343193
URL:		https://esbtl.sourceforge.net/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C++ header-only library for easy structural biology computations and
geometric constructions.

%description -l pl.UTF-8
Łatwa w użyciu, czysto nagłówkowa biblioteka C++ do obliczeń i
konstrukcji geometrycznych dotyczących biologii strukturalnej.

%package devel
Summary:	Easy Structural Biology Template Library
Summary(pl.UTF-8):	Easy Structural Biology Template Library - łatwa w użyciu biblioteka szablonów do biologii strukturalnej
Group:		Development/Libraries
Requires:	boost-devel
Requires:	libstdc++-devel

%description devel
C++ header-only library for easy structural biology computations and
geometric constructions.

%description devel -l pl.UTF-8
Łatwa w użyciu, czysto nagłówkowa biblioteka C++ do obliczeń i
konstrukcji geometrycznych dotyczących biologii strukturalnej.

%prep
%setup -q -n %{name}-%{version}-%{subver}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}

cp -pr include/ESBTL $RPM_BUILD_ROOT%{_includedir}
%{__rm} $RPM_BUILD_ROOT%{_includedir}/ESBTL/Doxyfile

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc exception.txt
%{_includedir}/ESBTL
