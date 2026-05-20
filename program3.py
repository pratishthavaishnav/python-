#wap to calculate the largest digit of a number
number = 12683
largest = number % 10
nextNum = number // 10
nextCheck = nextNum % 10
largest = largest if (largest > nextCheck) else nextCheck

nextNum = nextNum // 10
nextCheck = nextNum % 10
largest = largest if (largest > nextCheck) else nextCheck

nextNum = nextNum // 10
nextCheck = nextNum % 10
largest = largest if (largest > nextCheck) else nextCheck

nextNum = nextNum // 10
nextCheck = nextNum % 10
largest = largest if (largest > nextCheck) else nextCheck

nextNum = nextNum // 10
nextCheck = nextNum % 10
largest = largest if (largest > nextCheck) else nextCheck

print("largest digit of the number is :", largest)
