%define	version 3.2.0
%define release %mkrel 5

%define major 2
%define libname %mklibname otr %{major}
%define libnamedev %mklibname -d otr

Summary:	Off-The-Record Messaging library and toolkit
Name:		libotr
Version:	%{version}
Release:	%{release}
License:	LGPL/GPL
Group:		Networking/Instant messaging
URL:		http://www.cypherpunks.ca/otr/
Source0:	http://www.cypherpunks.ca/otr/%{name}-%{version}.tar.gz
Source1:	http://www.cypherpunks.ca/otr/%{name}-%{version}.tar.gz.asc
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	libgcrypt-devel >= 1.2.0

%description
%{name} is a library and toolkit which implements Off-the-Record (OTR)
Messaging.

OTR allows you to have private conversations over IM by providing:
 - Encryption
   - No one else can read your instant messages.
 - Authentication
   - You are assured the correspondent is who you think it is.
 - Deniability
   - The messages you send do _not_ have digital signatures that are
     checkable by a third party.  Anyone can forge messages after a
     conversation to make them look like they came from you.  However,
     _during_ a conversation, your correspondent is assured the messages
     he sees are authentic and unmodified.
 - Perfect forward secrecy
   - If you lose control of your private keys, no previous conversation
     is compromised.

%package	-n %{libname}
Summary:	Off-The-Record Messaging library and toolkit
Group:		Networking/Instant messaging
License:	LGPL
Provides:	%{name} = %{version}-%{release}

%description	-n %{libname}
%{name} is a library and toolkit which implements Off-the-Record (OTR)
Messaging.

OTR allows you to have private conversations over IM by providing:
 - Encryption
   - No one else can read your instant messages.
 - Authentication
   - You are assured the correspondent is who you think it is.
 - Deniability
   - The messages you send do _not_ have digital signatures that are
     checkable by a third party.  Anyone can forge messages after a
     conversation to make them look like they came from you.  However,
     _during_ a conversation, your correspondent is assured the messages
     he sees are authentic and unmodified.
 - Perfect forward secrecy
   - If you lose control of your private keys, no previous conversation
     is compromised.

%package	-n %{libnamedev}
Summary:	Development related files of %{name}
Group:		Networking/Instant messaging
License:	LGPL
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}
Obsoletes: %mklibname -d otr 2

%description	-n %{libnamedev}
%{name} is a library and toolkit which implements Off-the-Record (OTR)
Messaging. This package contains development related files of %{name}.

%package	utils
Summary:	Helper utilities of %{name}
Group:		Networking/Instant messaging
License:	GPL
Requires:	%{libname} = %{version}

%description	utils
%{name} is a library and toolkit which implements Off-the-Record (OTR)
Messaging. This package contains various helper utilities from %{name}.

%prep
%setup -q

%build
%configure2_5x --with-pic
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS
%{_libdir}/lib*.so.%{major}*

%files -n %{libnamedev}
%defattr(-,root,root)
%doc ChangeLog INSTALL Protocol-v2.html NEWS README
%{_datadir}/aclocal/*.m4
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/lib*.a
%{_libdir}/lib*.la
%{_libdir}/pkgconfig/*.pc

%files utils
%defattr(-,root,root)
%doc AUTHORS
%{_bindir}/*
%{_mandir}/man?/*
