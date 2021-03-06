%{!?python3_sitelib: %define python3_sitelib %(python3 -c "from distutils.sysconfig import get_python_lib;print(get_python_lib())")}

Name:           python3-M2Crypto
Version:        0.30.1
Release:        4%{?dist}
Summary:        Crypto and SSL toolkit for Python
Group:          Development/Languages/Python
License:        MIT
URL:            https://pypi.python.org/pypi/M2Crypto/0.26.0
Source0:        https://pypi.python.org/packages/11/29/0b075f51c38df4649a24ecff9ead1ffc57b164710821048e3d997f1363b9/M2Crypto-%{version}.tar.gz
Vendor:         VMware, Inc.
Distribution:   Photon
%define sha1    M2Crypto=8e2eb23196afbac08ad566ecb3378de9f35c5f12
Patch0:         fix_test_public_encrypt.patch
BuildRequires:  openssl
BuildRequires:  openssl-devel
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-typing
BuildRequires:  python3-xml
Requires:       python3-typing
Requires:       python3

%description
M2Crypto is a crypto and SSL toolkit for Python featuring the following:

RSA, DSA, DH, HMACs, message digests, symmetric ciphers (including
AES). SSL functionality to implement clients and servers. HTTPS
extensions to Python's httplib, urllib, and xmlrpclib. Unforgeable
HMAC'ing AuthCookies for web session management. FTP/TLS client and
server. S/MIME. ZServerSSL: A HTTPS server for Zope. ZSmime: An S/MIME
messenger for Zope.

%prep
%setup -q -n M2Crypto-%{version}
%patch0 -p1

%build
CFLAGS="%{optflags}" python3 setup.py build

%install
rm -rf %{buildroot}
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}

%check
python3 setup.py test

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{python3_sitelib}/*

%changelog
*   Tue Jun 16 2020 Tapas Kundu <tkundu@vmware.com> 0.30.1-4
-   Mass removal python2
*   Mon Oct 07 2019 Shreyas B. <shreyasb@vmware.com> 0.30.1-3
-   Fixed makecheck errors.
*   Mon Dec 03 2018 Ashwin H <ashwinh@vmware.com> 0.30.1-2
-   Add %check
*   Sun Sep 09 2018 Tapas Kundu <tkundu@vmware.com> 0.30.1-1
-   Update to version 0.30.1
*   Fri Oct 13 2017 Alexey Makhalov <amakhalov@vmware.com> 0.26.0-2
-   Remove BuildArch
*   Fri Jul 14 2017 Kumar Kaushik <kaushikk@vmware.com> 0.26.0-1
-   Initial packaging
