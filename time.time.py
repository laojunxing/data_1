#!/usr/bin/python
import time
print ("time.time(): %f " %  time.time()) #获取到的是从1970-1-1 00:00:00 到现在的秒数（小数位还有6位）。
print (time.localtime( time.time() )) #sec -- 转换为time.struct_time类型的对象的秒数。
# 0  tm_year（年）	 比如2011
# 1	 tm_mon（月）	 1 - 12
# 2	 tm_mday（日）	 1 - 31
# 3	 tm_hour（时）	 0 - 23
# 4	 tm_min（分）	 0 - 59
# 5	 tm_sec（秒）	 0 - 61
# 6	 tm_wday（weekday）	 0 - 6（0表示周日）
# 7	 tm_yday（一年中的第几天）	 1 - 366
# 8	 tm_isdst（是否是夏令时）	 默认为-1
print (time.asctime( time.localtime(time.time()) ))
#接受时间元组并返回一个可读的形式为"Thu Jan 28 13:40:37 2021的24个字符的字符串。
