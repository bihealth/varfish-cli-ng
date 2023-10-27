# varfish-cli-ng

## Developer Documentation

### Development Setup

Preqrequisites:

- install pyenv
- install Java SDK >=17
- install [Smithy CLI](https://smithy.io/2.0/guides/smithy-cli/cli_installation.html)

Then, first install Python 3.11 and 3.9.
Python 3.9 is only used for building the smithy generator code itself.
Python 3.11 is the actual prerequisite for the built code.

```
pyenv install 3.9
pyenv install 3.11
pyenv global 3.11 3.9
pyenv local 3.11 3.9
pip install black
```

Now, clone the `smithy-python` repository and build all components:

```
git clone git@github.com:smithy-lang/smithy-python.git
cd smithy-python
make install-components
```

Now you can clone this repository and build the code etc.

```
git clone git@github.com:bihealth/varfish-cli-ng.git
cd varfish-cli-ng
```

### GitHub Project Management with Terraform

```
export GITHUB_OWNER=bihealth
export GITHUB_TOKEN=ghp_<thetoken>

cd utils/terraform
terraform init
terraform import github_repository.varfish-cli-ng varfish-cli-ng
terraform validate
terraform fmt
terraform plan
terraform apply
```
