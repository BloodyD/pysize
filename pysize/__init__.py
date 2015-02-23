def ensure_is_size(func):
  def wrapper(self, other):
    if isinstance(other, SIZE):
      return func(self, other)
    elif isinstance(other, (float, int, long)):
      return func(self, SIZE(int(other)))
    else:
      raise ValueError("%s should be int, float, or SIZE instance, but was %s!"%(str(other), str(type(other))))
  return wrapper

class SIZE(object):
  BYTE = 1
  KB = BYTE * 1024
  MB = KB * 1024
  GB = MB * 1024

  UNITS_NAMES = {
    BYTE: "B",
    KB: "KB",
    MB: "MB",
    GB: "GB",
  }

  def __init__(self, value, unit = BYTE):
    super(SIZE, self).__init__()
    self._bytes = value * unit

    rest = self._bytes
    self.__gb = rest / SIZE.GB
    rest = max(0, rest - (self.__gb * SIZE.GB))
    self.__mb = rest / SIZE.MB
    rest = max(0, rest - (self.__mb * SIZE.MB))
    self.__kb = rest / SIZE.KB
    self.__b = max(0, rest - (self.__kb * SIZE.KB))

  def display_with_unit(self, value, unit = BYTE):
    if value: return "%d%s" %(value, SIZE.name(unit))
    else: return ""

  def display(self):
    return " ".join([val for val in map(
      self.display_with_unit,
      [self.__gb, self.__mb, self.__kb, self.__b],
      [SIZE.GB, SIZE.MB, SIZE.KB, SIZE.BYTE]) if val != ""])

  @staticmethod
  def name(unit): return SIZE.UNITS_NAMES.get(unit, "Unknown")

  def __str__(self): return self.display()

  def __repr__(self): return str(self)

  @ensure_is_size
  def __add__(self, other):
    return SIZE(int(self._bytes + other._bytes))

  @ensure_is_size
  def __sub__(self, other):
    return SIZE(int(self._bytes - other._bytes))

  @ensure_is_size
  def __mul__(self, other):
    return SIZE(int(self._bytes * other._bytes))

  @ensure_is_size
  def __div__(self, other):
    return SIZE(int(self._bytes / other._bytes))

  @ensure_is_size
  def __cmp__(self, other):
    return cmp(self._bytes, other._bytes)

  def __int__(self):
    return self._bytes

