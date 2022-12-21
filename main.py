class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def sum(self, vector1, vector2):
        return Vector(vector1.x + vector2.x, vector1.y + vector2.y, vector1.z + vector2.z)

    def subtract(self, vector1, vector2):
        return Vector(vector1.x - vector2.x, vector1.y - vector2.y, vector1.z - vector2.z)

    def scalar_multiply(self, vector1, vector2):
        return vector1.x * vector2.x + vector1.y * vector2.y + vector1.z * vector2.z

    def multiply_by_scalar(self, vector, scalar):
        return Vector(vector.x * scalar, vector.y * scalar, vector.z * scalar)


def input_value():
    return int(input('Введите число: '))


def main():
    question = input('Чтобы начать, нажмите +: ')
    while question == '+':

        try:
            print('Введите координаты первого вектора')
            vector1 = Vector(input_value(), input_value(), input_value())
            print('Введите координаты второго вектора')
            vector2 = Vector(input_value(), input_value(), input_value())
            operation = input('Что выполняем?: ')

            if operation == '+':
                vector3 = vector1.sum(vector1, vector2)
                print(f'Result of sum:\nX: {vector3.x}; Y: {vector3.y}; Z: {vector3.z}')
            elif operation == '-':
                vector3 = vector1.subtract(vector1, vector2)
                print(f'Result of subtraction:\nX: {vector3.x}; Y: {vector3.y}; Z: {vector3.z}')
            elif operation == '*':
                print(f'Result of scalar multiplication: {vector1.scalar_multiply(vector1, vector2)}')
            elif operation == '*scalar':
                scalar = int(input('Input a scalar value: '))
                vector3 = vector1.multiply_by_scalar(vector1, scalar)
                vector4 = vector2.multiply_by_scalar(vector2, scalar)
                print(f'Result of vector1\'s multiplication by a scalar:\nX: {vector3.x}; Y: {vector3.y}; Z: {vector3.z}')
                print(f'Result of vector2\'s multiplication by a scalar:\nX: {vector4.x}; Y: {vector4.y}; Z: {vector4.z}')
            else:
                print('Ошибка')

        except ValueError:
            print('Ошибка')

        question = input('Хотите продолжить: ')

    else:
        print('Возвращайтесь снова:)')


main()

