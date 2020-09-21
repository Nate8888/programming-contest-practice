amt = input().rstrip().split(":")

total_seconds_hours = int(amt[0])*60*60 + int(amt[1]) * 60

total_seconds_input = int(amt[0]) * 60 + int(amt[1])

extra_seconds = total_seconds_hours - total_seconds_input

amt_hours = extra_seconds//3600

extra_seconds = extra_seconds - amt_hours*3600
amt_mins = extra_seconds//60
extra_seconds = extra_seconds - amt_mins*60
amt_secs = extra_seconds

h_res = str(amt_hours).zfill(2)
m_res = str(amt_mins).zfill(2)
s_res = str(amt_secs).zfill(2)

print("{}:{}:{}".format(h_res,m_res, s_res))