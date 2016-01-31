import math
from decimal import Decimal, getcontext

getcontext().prec = 30

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def plus(self,v):
        result = []
        for v1, v2 in zip(self.coordinates, v.coordinates):
            result.append(v1+Decimal(v2))
        return Vector(result)

    def minus(self,v):
        result = []
        for v1, v2 in zip(self.coordinates, v.coordinates):
            result.append(v1-Decimal(v2));
        return Vector(result)

    def times_scalar(self, c):
        result = []
        for v in self.coordinates:
            result.append(Decimal(c)*v)
        return Vector(result)

    def magnitude(self):
        sum_of_squares = 0;
        for v in self.coordinates:
            sum_of_squares += (Decimal(v) ** Decimal('2.0'))
        return Decimal(math.sqrt(sum_of_squares))

    def unit_vector(self):
        try:
            return self.times_scalar(Decimal('1.0')/self.magnitude())
        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector')

    def dot_product(self, v):
        multiplication = []
        for v1, v2 in zip(self.coordinates, v.coordinates):
            multiplication.append(v1*Decimal(v2))
        return sum(multiplication)

    def angle_between_vectors(self, v, radians=True):
        try:
            result = math.acos(self.dot_product(v)/(self.magnitude()*v.magnitude()))
            if(radians):
                return result
            return ((180 * result)/math.pi)
        except Exception as e:
            raise e

    def is_parallel(self, v, tolerance=1e-10):
        if ((self.dot_product(self) < tolerance) or (v.dot_product(v) < tolerance)):
            return True
        result = True
        for v1, v2 in zip(self.unit_vector().coordinates, v.unit_vector().coordinates):
            result = result and (abs(round(v1, 10)) == abs(round(v2, 10)));
        return result

    def is_orthogonal(self, v, tolerance=1e-10):
        return abs(self.dot_product(v)) < tolerance

    # def get_ortogonal(self):


    def get_component(self, basis):
        u = basis.unit_vector()
        return self.dot_product(u)

    def get_parallel_projection(self, basis):
        try:
            u = basis.unit_vector()
            return u.times_scalar(self.get_component(basis))
        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception(self.NO_UNIQUE_PARALLEL_COMPONENT_MSG)
            else:
                raise e

    def get_orthogonal_projection(self, basis):
        try:
            perpendicular_projection = self.get_perpendicular_projection(basis)
            return self.minus(perpendicular_projection)
        except Exception as e:
            if str(e) == self.NO_UNIQUE_PARALLEL_COMPONENT_MSG:
                raise Exception(self.NO_UNIQUE_ORTHOGONAL_COMPONENT_MSG)
            else:
                raise e

    def cross_product(self, v):
        try:
            if (self.dimension == 3 and v.dimension == 3):
                x1, y1, z1 = self.coordinates
                x2, y2, z2 = v.coordinates
                x = ((y1*z2) - (y2*z1))
                y = ((x1*z2) - (x2*z1)) * -1
                z = ((x1*y2) - (x2*y1))
                cross_product = Vector([x,y,z])
                # Verifing that the answer is really ortogonal
                if(self.is_orthogonal(cross_product) and v.is_orthogonal(cross_product)):
                    return Vector([x,y,z])
                raise Exception(self.RESULT_WAS_NOT_ORTOGONAL_AFTER_OPERATION_MSG)
            raise Exception(self.CROSS_PRODUCT_OPERATION_ONLY_FOR_3D_VECTORS_MSG)
        except Exception as e:
            raise e

    def area_of_parallelogram_spanned(self, v):
        return self.cross_product(v).magnitude()

    def area_of_triangle_spanned(self, v):
        return self.cross_product(v).magnitude()/2

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates
