
class Config:
  """docstring for Config"""
  def __init__(self):
    self.seo_url="<%=config.seo_url%>"
    self.version="<%=config.version%>"
    self.controller_folder="<%=config.controller_folder%>"
    self.asenzor_host="<%=config.asenzor_host%>"
    self.apps="<%=config.apps%>"
    self.base_url="<%=config.base_url%>"
    self.default_app="<%=config.default_app%>"

window.config=Config()