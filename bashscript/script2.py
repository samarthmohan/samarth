def payout(hours,taxrate,hourlyrate):
	pay_pretax=hourlyrate*hours
	pay_posttax=pay_pretax*(1-taxrate)
	return pay_posttax
pay_fulltime = payout(40,.22,24)

print pay_fulltime
