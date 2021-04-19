from typing import Optional, Union, Callable, Type
import inspect

import bailong_core

class BaiLongException(Exception):
	...


def impl(obj: Union[Callable, Type]) -> Callable:
	src = inspect.getsource(obj)
	ret = bailong_core.load(src)
	return ret
	# return None


bailong_core.init(
	exc=BaiLongException
	# ...
	)