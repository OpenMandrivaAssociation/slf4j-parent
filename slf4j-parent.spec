Name:		slf4j-parent
Version:	1.7.36
Release:	1
Summary:	Parent POM for SLF4J
Group:		Development/Java
License:	MIT
URL:		https://www.slf4j.org/
Source0:	https://repo1.maven.org/maven2/org/slf4j/slf4j-parent/%{version}/slf4j-parent-%{version}.pom
Source1:	https://raw.githubusercontent.com/qos-ch/slf4j/v_1.7.36/LICENSE.txt
BuildArch:	noarch
BuildRequires:	python
# Literal, so the first rpmbuild -bs records them before sysjar is installed.
BuildRequires:	maven
BuildRequires:	java-current-devel
BuildSystem:	maven
BuildOption:	-N validate

%description
Parent POM for SLF4J 1.7.36. jcl-over-slf4j inherits its slf4j-api
version from this POM.

%prep
cp -p %{SOURCE0} pom.xml
cp -p %{SOURCE1} LICENSE
# Modules would publish the SLF4J jars, which already have their own packages.
# The direct dependency is test-scoped JUnit.
python - <<'PY'
import re
from pathlib import Path
path = Path("pom.xml")
text = path.read_text()
text = re.sub(r"\n  <modules>.*?</modules>", "", text, count=1, flags=re.S)
text = re.sub(r"\n  <dependencies>.*?</dependencies>", "", text, count=1, flags=re.S)
path.write_text(text)
PY

%files -f .mfiles
%doc LICENSE
