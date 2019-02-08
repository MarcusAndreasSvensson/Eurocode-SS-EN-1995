import threading


def calc_square(number, iter):
	for _ in range(iter):
		print('Square:' , number * number)

def calc_quad(number, iter):
	for _ in range(iter):
		print('Quad:' , number * number * number * number)


if __name__ == "__main__":
	number = 7
	thread1 = threading.Thread(target=calc_quad, args=(number, 100000))
	thread2 = thread1
# Will execute both in parallel
	thread1.start()
	thread2.start()
# Joins threads back to the parent process, which is this
	# program
	thread1.join()
	thread2.join()
# This program reduces the time of execution by running tasks in              parallel