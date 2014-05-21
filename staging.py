import os
import glob

class file:
  def __init__(self, filepath):
    self.filepath = filepath
    self.extension = os.path.splitext(filepath)[1].replace(".", "")

  def get_thumbnail(self):
    return self.filepath

  def load_image(self):
    f = open(self.filepath)
    contents = f.read()
    f.close()
    return { 'content': contents, 'filetype': self.extension }

  def load_pdf(self):
    self.filepath

class staging:
  def __init__(self, path):
    self.path = path

  def list_files(self):
    return glob.glob(self.path + "/*")

  def get_staging_files(self):
    return map(self.staging_file_from_path, self.list_files())

  def staging_file_from_path(self, path):
    return file.staging_file(path)

