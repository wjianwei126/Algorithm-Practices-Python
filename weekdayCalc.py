

class Solution:
	def weekdayCalc(self, date, weekday):
		# first decide weekday(Mon, Tue, etc.) of the date
		if weekday == 0: return date
		if date >= 0:
			week = date % 7
		else:
			if (-date) % 7 != 0:
			    week = 7 - (-date) % 7
			else:
				week = 0
		if week != 0:
			if weekday > 0:
				if weekday%7 == 0:
					return date + weekday - week
				elif weekday%7 <= week:
					return date + 7 - week + weekday
				elif weekday%7 > week:
					return date - week + weekday
			elif weekday < 0:
				if (-weekday)%7 == 0:
					return date - week + weekday + 7
				elif (-weekday)%7 < week:
					return date + weekday
				elif (-weekday)%7 >= week:
					return date - week - (7 - (-weekday)%7) - 7 * ((-weekday) / 7)
					
		else:
			if weekday > 0:
				return date + weekday
			elif weekday <0:
				if (-weekday)%7 == 0:
					return date + weekday
				elif ((-weekday)%7 != 0):
					return date - (7 - (-weekday)%7) - 7 * ((-weekday) / 7)



if __name__ == "__main__":
	solu = Solution()
	'''
	print solu.weekdayCalc(11111,1)#11117
	print solu.weekdayCalc(11111,4)#11113	
	print solu.weekdayCalc(11111,7)#11116
	print solu.weekdayCalc(11111,2)#11118
	print solu.weekdayCalc(11111,-1)#11110
	print solu.weekdayCalc(11111,-4)#11106
	print solu.weekdayCalc(11111,-7)#11109
	print solu.weekdayCalc(11111,-2)#11104
	print solu.weekdayCalc(11111,8)#11124
	print solu.weekdayCalc(11111,11)#11120
	print solu.weekdayCalc(11111,14)#11123
	print solu.weekdayCalc(11111,9)#11125
	print solu.weekdayCalc(11111,-8)#11103
	print solu.weekdayCalc(11111,-11)#11099
	print solu.weekdayCalc(11111,-14)#11102
	print solu.weekdayCalc(11111,-9)#11097
	'''
	print solu.weekdayCalc(11116,-9)#11104
	print solu.weekdayCalc(11116,-17)#11098
	print solu.weekdayCalc(11116,-14)#11102
	print solu.weekdayCalc(11116,-7)#11109
	print solu.weekdayCalc(11116,2)#11118
	print solu.weekdayCalc(11116,13)#11129



