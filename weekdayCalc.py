#日期计算，输入给你一个date和一个weekday。
#date是从1984年1月1日（星期天）以来的天数，weekday是代表下一个或者上一个weekday（比如7代表下一个星期天，-7代表上一个）。
#要根据这两个输入，输出对应到weekday的总天数，即是在date上计算出相应的推移量。
#比如11111（这是个星期二）和2，就输出11111，如果是-2，就输出11104，
#如果是-7，就输出11109，如果是7，就输出11116，以此类推。
#做好if else检查就可以，直接date % 7 然后开始一路判断，先有9个基本test case，过了之后还有11个隐藏的test case（我这里fail了不少，所以我猜date有可能是负数之类的）


class Solution:
	def weekdayCalc(self, date, weekday):
		# first decide weekday(Mon, Tue, etc.) of the date
		
		if date >= 0:
			week = date % 7
		else:
			if (-date) % 7 != 0:
			    week = 7 - (-date) % 7
			else:
				week = 0
		if week != 0:
			if weekday > 0 and weekday >= week:
				return date + weekday - week
			elif weekday > 0 and weekday < week:	
				return date + 7 + weekday - week
			elif weekday < 0 and (weekday + week <= 0):
				return date - week -7 - weekday
			elif weekday < 0 and (weekday + week > 0):
				return date - weekday - week
		else:
			if weekday > 0 and weekday != 7:
				return date + weekday
			elif weekday == 7:
				return date
			elif weekday < 0 and weekday != -7:
				return date - 7 - weekday
			elif weekday == -7:
				return date - 7

if __name__ == "__main__":
	solu = Solution()
	print solu.weekdayCalc(-23,-6)

