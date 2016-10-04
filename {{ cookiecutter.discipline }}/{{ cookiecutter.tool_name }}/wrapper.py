__author__ = "{{ cookiecutter.full_name }}"
__copyright__ = "Copyright {% now 'local', '%Y' %}, {{ cookiecutter.full_name }}"
__email__ = "{{ cookiecutter.email }}"
__license__ = "{{ cookiecutter.license }}"


from snakemake.shell import shell

# Placeholder for optional parameters
{% if cookiecutter.use_extra_params -%}
extra = snakemake.params.get("extra", "")
{%- endif %}
# Run log
{% if cookiecutter.use_logging -%}
log = snakemake.log_fmt_shell()
{%- endif %}

# Executed shell command
shell()
