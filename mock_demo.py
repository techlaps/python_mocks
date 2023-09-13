from unittest.mock import Mock

mock = Mock()

import json
data = json.dumps({"a": 1})

json = mock
print(json)
print(dir(json))


print(mock)