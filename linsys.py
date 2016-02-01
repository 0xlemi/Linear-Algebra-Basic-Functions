from decimal import Decimal, getcontext
from copy import deepcopy

from vector import Vector
from plane import Plane

getcontext().prec = 30


class LinearSystem(object):

    ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG = 'All planes in the system should live in the same dimension'
    NO_SOLUTIONS_MSG = 'No solutions'
    INF_SOLUTIONS_MSG = 'Infinitely many solutions'
    SOME_VALUES_ARE_ZERO_MSG = 'Some of the values provided are zero'

    def __init__(self, planes):
        try:
            d = planes[0].dimension
            for p in planes:
                assert p.dimension == d

            self.planes = planes
            self.dimension = d

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)


    def swap_rows(self, row1, row2):
        row1_content = self.planes[row1]
        row2_content = self.planes[row2]
        self.planes[row2] = row1_content
        self.planes[row1] = row2_content
        pass

    def multiply_coefficient_and_row(self, coefficient, row):
        normal_vector_multiplied = self.planes[row].normal_vector.times_scalar(coefficient)
        constant_term_multiplied = self.planes[row].constant_term * coefficient
        self.planes[row] = Plane(normal_vector_multiplied.coordinates, constant_term_multiplied)
        pass


    def add_multiple_times_row_to_row(self, coefficient, row_to_add, row_to_be_added_to):
        # get the plain to add
        n1 = self.planes[row_to_add].normal_vector
        k1 = self.planes[row_to_add].constant_term
        # get the plane to be added
        n2 = self.planes[row_to_be_added_to].normal_vector
        k2 = self.planes[row_to_be_added_to].constant_term
        # convine the rows
        n = n1.times_scalar(coefficient).plus(n2)
        k = (k1 * coefficient) + k2
        # replace plane
        self.planes[row_to_be_added_to] = Plane(n.coordinates, k)
        pass


    def indices_of_first_nonzero_terms_in_each_row(self):
        num_equations = len(self)
        num_variables = self.dimension

        indices = [-1] * num_equations

        for i,p in enumerate(self.planes):
            try:
                indices[i] = p.first_nonzero_index(p.normal_vector.coordinates)
            except Exception as e:
                if str(e) == Plane.NO_NONZERO_ELTS_FOUND_MSG:
                    continue
                else:
                    raise e

        return indices


    def __len__(self):
        return len(self.planes)


    def __getitem__(self, i):
        return self.planes[i]


    def __setitem__(self, i, x):
        try:
            assert x.dimension == self.dimension
            self.planes[i] = x

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)

    def compute_triangular_form(self):
        system = deepcopy(self)
        
        num_equations = len(system)
        num_variables = system.dimension

        j = 0
        for i in range(num_equations):
            while j < num_variables:
                c = MyDecimal(system[i].normal_vector.coordinates[j])
                if c.is_near_zero():
                    swap_succeeded = system.swap_with_row_below_for_nonzero_coefficient_if_able(i, j)
                    if not swap_succeeded:
                        j += 1
                        continue
                system.clear_coefficients_below(i, j)
                j += 1
                break


        return system

    def swap_with_row_below_for_nonzero_coefficient_if_able(self, row, col):
        num_equations = len(self)
        for k in range(row+1, num_equations):
            coefficient = MyDecimal(self[k].normal_vector.coordinates[col])
            if not coefficient.is_near_zero():
                self.swap_rows(row,k)
                return True
        return False

    def clear_coefficients_below(self, row, col):
        num_equations = len(self)
        beta = MyDecimal(self[row].normal_vector.coordinates[col])
        for k in range(row+1, num_equations):
            n = self[k].normal_vector.coordinates
            gamma = n[col]
            alpha = -gamma/beta
            self.add_multiple_times_row_to_row(alpha,row,k)

    def __order_equations__(self):
        planes_sorted = []
        for (indices,plane) in sorted(zip(self.indices_of_first_nonzero_terms_in_each_row(), self.planes)):
            planes_sorted.append(plane)
        self.planes = planes_sorted


    def __are_different_symbol__(self, x, y):
        if(x == 0 or y == 0):
            raise Exception(self.SOME_VALUES_ARE_ZERO_MSG)
        if(x < 0 ):
            if (y > 0):
                return True
            return False
        else:
            if(y < 0):
                return True
            return False


    def __str__(self):
        ret = 'Linear System:\n'
        temp = ['Equation {}: {}'.format(i+1,p) for i,p in enumerate(self.planes)]
        ret += '\n'.join(temp)
        return ret


class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps

