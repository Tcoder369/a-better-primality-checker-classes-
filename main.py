print(
    'this is a primality checker. it checks if your number is prime or not\n')
print('please put in only natural numbers\n')
print('putting in letters will result in an error\n')
print(
    'putting in math expressions like 5+8 or 5^4 will also result inan error\n'
)
print('putting in symbols of any kind will also result in an error\n')


class Number:
    def __init__(self, number):
        self.primality = False
        self.number = number

    def find_if_prime(self):
        if self.number == 1 or self.number == 2:
            return str(self.number) + ' is prime' + '\n'
        elif self.number <= 0:
            return 'please insert a posotive integer (no zero or negetives)\n'
        else:
            for i in range(2, int(self.number)):
                if int(self.number) % i == 0:
                    self.primality = False
                    broken_at = i
                    break
                else:
                    self.primality = True
            if self.primality == True:
                return str(self.number) + ' is prime' + '\n'
            else:
                return str(self.number) + ' is not prime, it is divisible by ' + str(
                    broken_at) + '\n'


while True:

    numberr = Number(int(input()))
    print(numberr.find_if_prime())
