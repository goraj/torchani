import torchani  # noqa: F401
import sphinx_rtd_theme

project = 'TorchANI'
copyright = '2018, Roitberg Group'
author = 'Xiang Gao'

version = '0.1'
release = '0.1alpha'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx_gallery.gen_gallery',
]

templates_path = ['_templates']
html_static_path = ['_static']

source_suffix = '.rst'
master_doc = 'index'
pygments_style = 'sphinx'
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
htmlhelp_basename = 'TorchANIdoc'

sphinx_gallery_conf = {
     'examples_dirs': '../examples',
     'gallery_dirs': 'examples',
     'filename_pattern': r'.*\.py'
}

intersphinx_mapping = {
    'python': ('https://docs.python.org/', None),
    'numpy': ('http://docs.scipy.org/doc/numpy/', None),
    'torch': ('https://pytorch.org/docs/master/', None),
    'ignite': ('https://pytorch.org/ignite/', None),
}

latex_documents = [
    (master_doc, 'TorchANI.tex', 'TorchANI Documentation',
     'Xiang Gao', 'manual'),
]

man_pages = [
    (master_doc, 'torchani', 'TorchANI Documentation',
     [author], 1)
]

texinfo_documents = [
    (master_doc, 'TorchANI', 'TorchANI Documentation',
     author, 'TorchANI', 'One line description of project.',
     'Miscellaneous'),
]
