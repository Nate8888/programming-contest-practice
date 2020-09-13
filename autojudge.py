filename = input().rstrip()
extensions = [".c", ".cpp", ".java", ".py"]
name_given = input().rstrip().split(".")

return_code, time_limit, time_elapsed = input().rstrip().split(" ")

amt_lines_correct = int(input().rstrip())
correct_lines = []
for x in range(amt_lines_correct):
	correct_lines.append(input())

amt_lines_prob = int(input().rstrip())
prob_lines = []

for x in range(amt_lines_prob):
	prob_lines.append(input())

printed = 0

if len(name_given) == 2:
	if filename != name_given[0]:
		print("Compile Error")
		printed = 1
	else:
		if return_code != "0":
			print("Run-Time Error")
			printed = 1
		else:
			if int(time_elapsed) > int(time_limit):
				print("Time Limit Exceeded")
				printed = 1
			else:
				if amt_lines_correct != amt_lines_prob:
					print("Wrong Answer")
					printed = 1
				else:
					for i in range(len(correct_lines)):
						if correct_lines[i] != prob_lines[i]:
							print("Wrong Answer")
							printed = 1
							break
					if not printed:
						print("Correct")
else:
	print("Compile Error")
