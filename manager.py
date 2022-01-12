class Manager:
    def __init__(self, _class):
        self._class = _class

    def search(self, **kwargs):
        results = list()
        for key, value in kwargs.items():
            if key.endswith('__min'):
                key = key[:-5]
                compare_key = 'min'
            elif key.endswith('__max'):
                key = key[:-5]
                compare_key = 'max'
            else:
                compare_key = 'equal'

            for obj in self._class.objects_list:
                if hasattr(obj, key):
                    if compare_key == 'min':
                        result = getattr(obj, key) >= value
                    elif compare_key == 'max':
                        result = getattr(obj, key) <= value
                    else:
                        result = getattr(obj, key) == value
                    if result:
                        results.append(obj)
        return results

    def get(self, **kwargs):
        for key, value in kwargs.items():
            for obj in self._class.objects_list:
                if hasattr(obj, key) and getattr(obj, key) == value:
                    return obj
