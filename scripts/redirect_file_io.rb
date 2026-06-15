# frozen_string_literal: true

# Atomic replace for redirect list edits (crash-safe on POSIX).
module RedirectFileIO
  module_function

  def atomic_write!(path, content)
    path = File.expand_path(path)
    dir = File.dirname(path)
    base = File.basename(path)
    tmp = File.join(dir, ".#{base}.tmp.#{Process.pid}")
    File.binwrite(tmp, content)
    File.rename(tmp, path)
  rescue StandardError
    File.unlink(tmp) if tmp && File.file?(tmp)
    raise
  end
end
