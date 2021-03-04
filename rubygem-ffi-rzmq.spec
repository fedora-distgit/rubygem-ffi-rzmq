# Generated from ffi-rzmq-2.0.7.gem by gem2rpm -*- rpm-spec -*-
%global gem_name ffi-rzmq

Name: rubygem-%{gem_name}
Version: 2.0.7
Release: 1%{?dist}
Summary: This gem wraps the ZeroMQ (0mq) networking library using Ruby FFI (foreign function interface)
License: MIT
URL: http://github.com/chuckremes/ffi-rzmq
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(rspec) >= 3.7
BuildRequires: rubygem(ffi-rzmq-core)
BuildArch: noarch

%description
This gem wraps the ZeroMQ networking library using the ruby FFI (foreign
function interface). It's a pure ruby wrapper so this gem can be loaded
and run by any ruby runtime that supports FFI. That's all of the major ones -
MRI, Rubinius and JRuby.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
rspec -Ilib spec
popd

%files
%dir %{gem_instdir}
%{gem_instdir}/.bnsignore
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.travis.yml
%{gem_instdir}/ext
%{gem_libdir}
%{gem_instdir}/travis_build_script.sh
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/AUTHORS.txt
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/History.txt
%doc %{gem_instdir}/README.rdoc
%{gem_instdir}/Rakefile
%{gem_instdir}/examples
%{gem_instdir}/ffi-rzmq.gemspec
%{gem_instdir}/spec

%changelog
* Fri Nov 13 2020 Pavel Valena <pvalena@redhat.com> - 2.0.7-1
- Initial package
