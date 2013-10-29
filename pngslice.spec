Summary:	create ragged images in HTML
Summary(pl.UTF-8):	tworzenie podzielonych obrazków  HTML
Name:		pngslice
Version:	0.66
Release:	4
License:	GPL v2
Group:		Applications
Source0:	http://sview01.wiredworkplace.net/pub/jjg/code/%{name}.tar.gz
# Source0-md5:	816313410dee225f417765b1af0e6186
Patch0:		%{name}-DESTDIR.patch
URL:		http://sview01.wiredworkplace.net/pub/jjg/en/code/pngslice.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libpng-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The pngslice utility is a tool for creating ragged images in HTML:
Eric Meyer's ragged floats. The idea is to slice the image into thin
strips that are trimmed and stacked vertically. The program produces
the trimmed PNG slices and a fragment of HTML to include them.

%description -l pl.UTF-8
Narzędzie pngslice służy do tworzenia rozdzielonych obrazów w HTML,
tzw. podzielone obrazy Eric Meyer'a. W zamyśle chodzi tu o podzielenie
obrazka na nieduże paski, które są przycięte i nakładane pionowo.
Progam ten tworzy przycięte kawałki PNG oraz fragment kodu HTML do ich
złączenia.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/pngslice.1*
